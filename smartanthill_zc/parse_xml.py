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


def create_bodyparts(compiler, bodyparts):
    '''
    Returns a BodyPartsManagerNode populated with all created plugins
    and bodyparts
    '''

    manager = bodypart.create_body_parts_manager(compiler, compiler.BUILTIN)

    plugins = {}
    for current in bodyparts:
        z_plugin = current.plugin
        if z_plugin not in plugins:
            plugins[z_plugin] = _make_plugin(compiler, manager,
                                             compiler.BUILTIN,
                                             z_plugin.get_request_fields(),
                                             z_plugin.get_response_fields())

        _make_bodypart(compiler, manager, compiler.BUILTIN,
                       current.get_name(), current.get_id(), plugins[z_plugin])

    compiler.check_stage('bodyparts')

    return manager


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
                _make_test_plugin(compiler, manager, plugin)
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


def _make_test_plugin(compiler, manager, et):
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

    plugin = _make_plugin(compiler, manager, et, command_fields, reply_fields)

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
    field = compiler.init_node(builtin.FieldTypeDeclNode(field_name), ctx)

    encoding, min_v, max_v = _get_enconding_min_max(compiler, ctx, att)

    field.encoding = encoding
    field.min_value = min_v
    field.max_value = max_v
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


def _get_enconding_min_max(compiler, ctx, att):
    '''
    Process common encoding with min and max values
    '''
    t = ''.join(att['type'].split())  # to remove whites

    encoding = None
    max_bytes = 0

    if t == 'encoded-signed-int[max=2]' or t == 'encoded-int[max=2]':
        encoding = Encoding.SIGNED_INT
        max_bytes = 2
    elif t == 'encoded-unsigned-int[max=2]':
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
                    ctx, "Declared min (%s) is lower that type min (%s)"
                    % (min_value, encoding.min_value))
                min_value = encoding.min_value

    except:
        compiler.report_error(ctx, "Bad min '%s'" % att['min'])

    try:
        if 'max' in att:
            max_value = long(att['max'])
            if max_value > encoding.max_value:
                compiler.report_error(
                    ctx, "Declared max (%s) is grater than type min (%s)"
                    % (max_value, encoding.max_value))
                max_value = encoding.max_value
    except:
        compiler.report_error(ctx, "Bad max '%s'" % att['max'])

    return (encoding, min_value, max_value)


def _make_command_parameters(compiler, manager, ctx, fields):
    '''
    Created a new FieldTypeDeclNode from data in att dictionary
    '''
    pl = compiler.init_node(builtin.ParameterListNode(), ctx)

    for current in fields:
        field = _make_command_field_type(compiler, manager, ctx, current)

        manager.child_type_list.add_declaration(field)

        pl.add_parameter(
            compiler.init_node(builtin.ParameterDeclNode(field.txt_name), ctx))

    return pl


def _make_command_field_type(compiler, manager, ctx, att):
    '''
    Created a new FieldTypeDeclNode from data in att dictionary
    '''

    field_name = manager.get_unique_type_name('_zc_command_field_')
    field = compiler.init_node(
        bodypart.CommandFieldTypeDeclNode(field_name), ctx)

    encoding, min_v, max_v = _get_enconding_min_max(compiler, ctx, att)

    field.encoding = encoding
    field.min_value = min_v
    field.max_value = max_v

    return field
