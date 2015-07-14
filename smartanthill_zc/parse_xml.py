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


from xml.etree import ElementTree

from smartanthill_zc import bodypart, builtin
from smartanthill_zc.encode import get_encoding_min_max, Encoding

try:
    from xml.etree.ElementTree import ParseError
except ImportError:
    from xml.parsers.expat import ExpatError as ParseError


def parse_test_xml_body_parts(compiler, data):
    '''
    Parse string containing test xml bodyparts declarations
    Returns a BodypartManagerNode with all the parsed bodyparts
    Used only for creation of test bodyparts
    '''

    manager = bodypart.create_body_parts_manager(compiler, compiler.BUILTIN)

    try:
        root = ElementTree.fromstring(data)
        # python 2.6
        for current in root.getiterator('smartanthill_zc.test'):
            for plugin in current.getiterator('plugin'):
                _make_plugin(compiler, manager, plugin)
    except ParseError:  # TODO improve
        compiler.report_error(compiler.BUILTIN, "Error parsing xml")
        compiler.raise_error()

    compiler.check_stage('test_xml_bodyparts')

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
                et, "Unexpected child tag '%s'" % current.tag)
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


def _make_plugin(compiler, manager, et):
    '''
    Creates a BodyPartDeclNode from an xml <test.plugin>
    '''

    assert et.tag == 'plugin'

    plugin = compiler.init_node(bodypart.PluginDeclNode(), et)

    tags = _get_tags(compiler, et,
                     ['command', 'reply', 'bodyparts'], [])

    for current in tags['bodyparts']:
        assert current.tag == 'bodypart'
        bp = _make_bodypart(compiler, current)
        bp.ref_plugin = plugin
        manager.child_body_part_list.add_declaration(bp)

    # build parameter list from <command>
    pl = compiler.init_node(builtin.ParameterListNode(), et)

    for current in tags['command']:

        assert current.tag == 'field'

        att = _get_attributes(compiler, current,
                              ['name', 'type'], ['min', 'max'])

        field = _make_command_field_type(compiler, manager, et, att)

        manager.child_type_list.add_declaration(field)

        pl.add_parameter(
            compiler.init_node(builtin.ParameterDeclNode(field.txt_name), et))

    plugin.set_parameter_list(pl)

    # build reply type <reply>
    if len(tags['reply']) == 0:
        plugin.txt_type_name = manager.child_empty_reply_type.txt_name
    else:
        reply_name = manager.get_unique_type_name('_zc_reply_')
        plugin.txt_type_name = reply_name

        reply = compiler.init_node(
            bodypart.MessageTypeDeclNode(reply_name), tags['reply'])

        for current in tags['reply']:

            if current.tag != 'field':
                compiler.report_error(
                    current, "Unexpected child tag '%s'" % current.tag)
                compiler.raise_error()

            field = _make_reply_field(compiler, manager, current)

            reply.add_element(field)

        manager.child_type_list.add_declaration(reply)

    manager.child_plugin_list.add_declaration(plugin)


def _make_bodypart(compiler, et):

    att = _get_attributes(compiler, et, ['name', 'id'], [])

    bp = compiler.init_node(bodypart.BodyPartDeclNode(), et)

    bp.txt_name = att['name']
    bp.bodypart_id = long(att['id'])

    return bp


def _make_reply_field(compiler, manager, et):
    '''
    Creates a MemberDeclNode from an xml <field>
    '''

    att = _get_attributes(compiler, et,
                          ['name', 'type'], ['min', 'max'])

    factory = manager.child_field_type_factory
    field = _make_field_type(compiler, manager, et, att)

    factory.add_field_type(compiler, field, et)
#    manager.child_type_list.add_declaration(field)

    member = compiler.init_node(bodypart.MemberDeclNode(att['name']), et)
    member.ref_field_type = field

    tags = _get_tags(compiler, et, [], ['meaning'])
    if 'meaning' in tags:
        m = tags['meaning']
        meaning_att = _get_attributes(compiler, m, ['type'], [])
        if meaning_att['type'] != 'float':
            compiler.report_error(
                m, "Unsuported meaning type '%s'" % meaning_att['type'])
            compiler.raise_error()

        meaning_conv = _get_tags(
            compiler, m, [], ['linear-conversion'])

        if 'linear-conversion' in meaning_conv:
            conv = _get_attributes(compiler, meaning_conv['linear-conversion'],
                                   ['input-point0', 'output-point0',
                                    'input-point1', 'output-point1'], [])

            meaning = bodypart.LinearConvertionFloat()
            meaning.set_points(
                conv['input-point0'], conv['output-point0'],
                conv['input-point1'], conv['output-point1'])
            field.meaning = meaning
        else:
            # create convertion 1 to 1
            meaning = bodypart.LinearConvertionFloat()
            meaning.set_points('0', '0.', '1', '1.')
            field.meaning = meaning

    return member


def _make_field_type(compiler, manager, et, att):
    '''
    Created a new FieldTypeDeclNode from data in att dictionary
    '''
    t = ''.join(att['type'].split())  # to remove whites

    field_name = manager.get_unique_type_name('_zc_reply_field_')
    field = compiler.init_node(builtin.FieldTypeDeclNode(field_name), et)

    encoding = None
    max_bytes = 0
    if (t == 'encoded-signed-int[max=2]' or
            t == 'encoded-signed-int<max=2>'):
        encoding = Encoding.SIGNED_INT
        max_bytes = 2
    elif (t == 'encoded-unsigned-int[max=2]' or
          t == 'encoded-unsigned-int<max=2>'):
        encoding = Encoding.UNSIGNED_INT
        max_bytes = 2
    else:
        assert False

    min_value, max_value = get_encoding_min_max(encoding, max_bytes)
    try:
        if 'min' in att:
            min_value = long(att['min'])
            if min_value < encoding.min_value:
                compiler.report_error(
                    et, "Declared min (%s) is lower that type min (%s)"
                    % (min_value, encoding.min_value))
                min_value = encoding.min_value

    except:
        compiler.report_error(et, "Bad min '%s'" % att['min'])

    try:
        if 'max' in att:
            max_value = long(att['max'])
            if max_value > encoding.max_value:
                compiler.report_error(
                    et, "Declared max (%s) is grater than type min (%s)"
                    % (max_value, encoding.max_value))
                max_value = encoding.max_value
    except:
        compiler.report_error(et, "Bad max '%s'" % att['max'])

    field.encoding = encoding
    field.min_value = min_value
    field.max_value = max_value

    return field


def _make_command_field_type(compiler, manager, et, att):
    '''
    Created a new FieldTypeDeclNode from data in att dictionary
    '''
    t = ''.join(att['type'].split())  # to remove whites

    field_name = manager.get_unique_type_name('_zc_command_field_')
    field = compiler.init_node(
        bodypart.CommandFieldTypeDeclNode(field_name), et)

    encoding = None
    max_bytes = 0
    if (t == 'encoded-signed-int[max=2]' or
            t == 'encoded-signed-int<max=2>'):
        encoding = Encoding.SIGNED_INT
        max_bytes = 2
    elif (t == 'encoded-unsigned-int[max=2]' or
          t == 'encoded-unsigned-int<max=2>'):
        encoding = Encoding.UNSIGNED_INT
        max_bytes = 2
    else:
        compiler.report_error(et, "Unknown type '%s'" % t)
        compiler.raise_error()

    min_value, max_value = get_encoding_min_max(encoding, max_bytes)
    try:
        if 'min' in att:
            min_value = long(att['min'])
            if min_value < encoding.min_value:
                compiler.report_error(
                    et, "Declared min (%s) is lower that type min (%s)"
                    % (min_value, encoding.min_value))
                min_value = encoding.min_value

    except:
        compiler.report_error(et, "Bad min '%s'" % att['min'])

    try:
        if 'max' in att:
            max_value = long(att['max'])
            if max_value > encoding.max_value:
                compiler.report_error(
                    et, "Declared max (%s) is grater than type max (%s)"
                    % (max_value, encoding.max_value))
                max_value = encoding.max_value
    except:
        compiler.report_error(et, "Bad max '%s'" % att['max'])

    field.encoding = encoding
    field.min_value = min_value
    field.max_value = max_value

    return field
