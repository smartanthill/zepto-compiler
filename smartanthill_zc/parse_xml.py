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


import re
from xml.etree import ElementTree

from smartanthill_zc import bodypart, node
from smartanthill_zc.encode import Encoding


try:
    from xml.etree.ElementTree import ParseError
except ImportError:
    from xml.parsers.expat import ExpatError as ParseError


def create_bodyparts(compiler, bodyparts, ctx):
    '''
    Returns a BodyPartsManagerNode populated with all created plugins
    and bodyparts
    '''

    manager = bodypart.create_body_parts_manager(compiler, ctx)

    plugins = {}
    for current in bodyparts:
        z_plugin = current.plugin
        if z_plugin not in plugins:
            plugins[z_plugin] = _make_plugin(compiler, manager, ctx,
                                             z_plugin.get_request_fields(),
                                             z_plugin.get_response_fields())

        _make_bodypart(compiler, manager, ctx,
                       current.get_name(), current.get_id(), plugins[z_plugin])

    compiler.check_stage('bodypart')

    return manager


def parse_test_xml_body_parts(compiler, data, ctx):
    '''
    Parse string containing test xml bodyparts declarations
    Returns a BodypartManagerNode with all the parsed bodyparts
    Used only for creation of test bodyparts
    '''

    manager = bodypart.create_body_parts_manager(compiler, ctx)

    try:
        root = ElementTree.fromstring(data)
        # python 2.6
        for current in root.getiterator('smartanthill_zc.test'):
            for plugin in current.getiterator('plugin'):
                _make_test_plugin(compiler, manager, plugin, ctx)
    except ParseError:  # TODO improve
        compiler.report_error(ctx, "Error parsing xml")
        compiler.raise_error()

    compiler.check_stage('test_bodypart')

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


def _make_test_plugin(compiler, manager, et, ctx):
    '''
    Creates a BodyPartDeclNode from an xml <test.plugin>
    '''

    tags = _get_tags(compiler, et,
                     ['command', 'reply', 'bodyparts'], [])

    # build plugin

    command_fields = []
    for current in tags['command']:
        command_fields.append(current.attrib)

    reply_fields = []
    for current in tags['reply']:
        reply_fields.append(current.attrib)

    plugin = _make_plugin(compiler, manager, ctx, command_fields, reply_fields)

    for current in tags['bodyparts']:
        assert current.tag == 'bodypart'
        att = _get_attributes(compiler, current, ['name', 'id'], [])
        _make_bodypart(
            compiler, manager, current, att['name'], long(att['id']), plugin)


def _make_plugin(compiler, manager, ctx, command_fields, reply_fields):
    '''
    Creates a PluginDeclNode
    '''

    plugin = compiler.init_node(bodypart.PluginDeclNode(), ctx)

    # build parameter

    pl = _make_command_parameters(compiler, manager, ctx, command_fields)
    plugin.set_parameter_list(pl)

    reply = _make_reply_message_type(compiler, manager, ctx, reply_fields)
    plugin.txt_type_name = reply.txt_name

    manager.child_plugin_list.add_declaration(plugin)

    return plugin


def _make_bodypart(compiler, manager, ctx, name, bodypart_id, plugin):

    bp = compiler.init_node(bodypart.BodyPartDeclNode(), ctx)

    bp.txt_name = name
    bp.bodypart_id = bodypart_id
    bp.ref_plugin = plugin

    manager.child_body_part_list.add_declaration(bp)

    return bp


def _make_reply_message_type(compiler, manager, ctx, fields):
    '''
    Creates a MessageTypeDeclNode from a map of fields
    '''
    if len(fields) == 0:
        return manager.child_empty_reply_type

    reply_name = manager.get_unique_type_name('_zc_reply_')

    reply = compiler.init_node(
        bodypart.MessageTypeDeclNode(reply_name), ctx)

    for current in fields:

        field = _make_reply_member(compiler, manager, ctx, current)

        reply.add_element(field)

    manager.child_type_list.add_declaration(reply)

    return reply


def _make_reply_member(compiler, manager, ctx, att):
    '''
    Creates a MemberDeclNode from an xml <field>
    '''

    field = _make_reply_field_type(compiler, manager, ctx, att)

    manager.child_field_type_factory.add_field_type(compiler, field, ctx)

    member = compiler.init_node(bodypart.MemberDeclNode(att['name']), ctx)
    member.ref_field_type = field

    return member


def _make_reply_field_type(compiler, manager, ctx, att):
    '''
    Created a new FieldTypeDeclNode from data in att dictionary
    '''

    field_name = manager.get_unique_type_name('_zc_reply_field_')
    field = compiler.init_node(bodypart.FieldTypeDeclNode(field_name), ctx)

    field.encoding = get_enconding_helper(compiler, ctx, att)
    field.meaning = _make_meaning(compiler, ctx, att)

    return field


def _make_meaning(compiler, ctx, att):
    '''
    Created a new field meaning from data in att dictionary
    '''
    if 'meaning' in att:
        if att['meaning'] != 'float':
            compiler.report_error(
                ctx, "Unsuported meaning '%s'" % att['meaning'])
            compiler.raise_error()

        if 'conversion' in att:
            if att['conversion'] == 'linear-conversion':

                meaning = bodypart.LinearConvertionFloat()
                meaning.set_points(
                    att['input-point0'], att['output-point0'],
                    att['input-point1'], att['output-point1'])
                return meaning
            else:
                compiler.report_error(
                    ctx, "Unsuported conversion '%s'" % att['conversion'])
                compiler.raise_error()
    return None


def get_enconding_helper(compiler, ctx, att):
    '''
    Process common encoding with min and max values
    '''

    match = re.match(r'encoded\-(int|uint)\[max\=(\d)\]', att['type'])
    if match is None:
        compiler.report_error(ctx, "Unsuported type '%s'" % att['type'])
        compiler.raise_error()

    max_bytes = int(match.group(2))
    if max_bytes < 1 or max_bytes > 8:
        compiler.report_error(ctx, "Unsuported type max bytes %d" % max_bytes)
        compiler.raise_error()

    encoding = None

    if match.group(1) == 'int':
        encoding = Encoding.SIGNED_INT
    elif match.group(1) == 'uint':
        encoding = Encoding.UNSIGNED_INT
    else:
        assert False

    type_min, type_max = encoding.get_min_max(max_bytes)

    checker = _get_value_checker(compiler, ctx, att, type_min, type_max)
    return bodypart.EncodingHelper(encoding, checker)


def _get_value_checker(compiler, ctx, att, type_min, type_max):
    '''
    Process min and max values, or discrete value set
    '''

    if '_values' in att and att['_values'] is not None:
        s = []
        try:
            for each in att['_values']:
                v = long(each['value'])

                if v >= type_min and v <= type_max:
                    s.append(v)
                else:
                    compiler.report_error(
                        ctx,
                        "Discrete value %d is outside range [%d,%d]" %
                        (v, type_min, type_max))
        except:
            compiler.report_error(ctx, "Bad value set")

        return bodypart.DiscreteSetChecker(s)

    else:
        min_value = type_min
        max_value = type_max
        try:
            if 'min' in att and att['min'] is not None:
                min_value = long(att['min'])
                if min_value < type_min or min_value > type_max:
                    compiler.report_error(ctx, "Bad min %d" % min_value)
                    min_value = type_min

        except:
            compiler.report_error(ctx, "Bad min '%s'" % att['min'])

        try:
            if 'max' in att and att['max'] is not None:
                max_value = long(att['max'])
                if max_value > type_max or max_value < type_min:
                    compiler.report_error(ctx, "Bad max %d" % max_value)
                    max_value = type_max
        except:
            compiler.report_error(ctx, "Bad max '%s'" % att['max'])

        if min_value > max_value:
            compiler.report_error(ctx, "Bad min %d max %d" % (min_value,
                                                              max_value))
            max_value = type_max
            min_value = type_min

        return bodypart.RangeChecker(min_value, max_value)


def _make_command_parameters(compiler, manager, ctx, fields):
    '''
    Created a new FieldTypeDeclNode from data in att dictionary
    '''
    pl = compiler.init_node(node.ParameterListNode(), ctx)

    for current in fields:
        field = _make_command_field_type(compiler, manager, ctx, current)

        manager.child_type_list.add_declaration(field)

        pl.add_parameter(
            compiler.init_node(node.ParameterDeclNode(field.txt_name), ctx))

    return pl


def _make_command_field_type(compiler, manager, ctx, att):
    '''
    Created a new FieldTypeDeclNode from data in att dictionary
    '''

    field_name = manager.get_unique_type_name('_zc_command_field_')
    field = compiler.init_node(
        bodypart.CommandFieldTypeDeclNode(field_name), ctx)

    field.encoding = get_enconding_helper(compiler, ctx, att)

    return field
