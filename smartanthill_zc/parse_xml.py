# Copyright (C) 2015 OLogN Technologies AG
#
# This source file is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import xml.etree.ElementTree as ET

from smartanthill_zc.builtin import ParameterListNode
from smartanthill_zc.bodypart import (BodyPartDeclNode, MemberDeclNode,
    MessageTypeDeclNode, create_body_parts_manager)


def parse_xml_body_parts(compiler, data):
    '''
    Parse unicode string containing xml bodyparts declarations
    Returns a BodypartManagerNode with all the parsed bodyparts
    '''
    manager = create_body_parts_manager(compiler, compiler.BUILTIN)

    try:
        root = ET.fromstring(data)
        for current in root.iter('smartanthill.plugin'):
            _make_bodypart(compiler, manager, current)
    except ET.ParseError:  # TODO improve
        compiler.report_error(compiler.BUILTIN, "Error parsing xml")
        compiler.raise_error()

    compiler.check_stage('xml_bodyparts')

    return manager


def check_reserved_name(compiler, et, name):
    '''
    Returns the text of a parser token, checking for reserved names,
    and non-ascii characters
    TODO better check and error report for non-ascii
    '''

    if name.startswith('_zc_'):
        compiler.report_error(et, "Name '%s' and all names starting with "
                              "'_zc_' are reserved" % name)


def _get_attributes(compiler, et, req_names, opt_names):
    '''
    Returns a dictionary from xml attributes,
    it checks that all names in req_names are found,
    that no duplicate name is found,
    and that no unexpected name is found
    '''

    for name in et.attrib:
        if name not in req_names and name not in opt_names:
            compiler.report_error(et, "Unexpected attribute '%s'" % name)
        else:
            check_reserved_name(compiler, et, et.attrib[name])

    ok = True
    for current in req_names:
        if current not in et.attrib:
            compiler.report_error(
                et, "Missing required attribute '%s'" % current)
            ok = False

    if not ok:
        compiler.raise_error()

    return et.attrib


def _get_tags(compiler, et, req_names, opt_names):
    '''
    Returns a dictionary from xml tags,
    it checks that all names in req_names are found,
    that no duplicate name is found,
    and that no unexpected name is found
    '''
    result = {}

    for current in et:
        check_reserved_name(compiler, current, current.tag)

        if current.tag not in req_names and current.tag not in opt_names:
            compiler.report_error(
                current, "Unexpected child tag '%s'" % current.tag)
        else:
            result[current.tag] = current

    ok = True
    for current in req_names:
        if current not in result:
            compiler.report_error(
                et, "Missing required child tag '%s'" % current)
            ok = False

    if not ok:
        compiler.raise_error()

    return result


def _make_bodypart(compiler, manager, et):
    '''
    Creates a BodyPartDeclNode from an xml <smartanthill.plugin>
    '''

    assert et.tag == 'smartanthill.plugin'

    bodypart = compiler.init_node(BodyPartDeclNode(), et)
    att = _get_attributes(compiler, et,
                          ['name', 'id', 'version'], [])

    if att['version'] != '1.0':
        compiler.report_error(et, "Unidentified version number '%s'" %
                              att['version'])

    bodypart.txt_name = att['name']
    try:
        bodypart.bodypart_id = long(att['id'])
    except:
        compiler.report_error(et, "Bad id '%s'" % att['id'])

    tags = _get_tags(compiler, et,
                     ['command', 'reply'],
                     ['description', 'peripheral'])

    # build parameter list from <command>
    pl = compiler.init_node(ParameterListNode(), et)
    bodypart.set_parameter_list(pl)

    # build reply type <reply>
    if len(tags['reply']) == 0:
        compiler.report_error(tags['reply'], "Empty 'reply' not allowed")
        compiler.raise_error()

    reply_name = '_zc_reply_type_' + att['name']
    reply = compiler.init_node(
        MessageTypeDeclNode(reply_name), tags['reply'])

    for current in tags['reply']:

        if current.tag != 'field':
            compiler.report_error(
                current, "Unexpected child tag '%s'" % current.tag)
            compiler.raise_error()

        field = _make_field(compiler, manager, current)

        reply.add_element(field)

    bodypart.set_reply_type(reply)

    manager.child_body_part_list.add_declaration(bodypart)


def _make_field(compiler, manager, et):
    '''
    Creates a MemberDeclNode from an xml <field>
    '''

    att = _get_attributes(compiler, et,
                          ['name', 'type'], ['min', 'max'])

    field = manager.child_field_type_factory.create_field_type(
        compiler, et, att)

    member = compiler.init_node(MemberDeclNode(att['name']), et)
    member.ref_field_type = field

    # TODO handle <meaning>

    return member