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

from os.path import dirname
from xml.etree import ElementTree

from smartanthill_zc import parse_xml, parse_js, builtin, visitor,\
    vm, writer, op_node, encode
from smartanthill_zc.compiler import Compiler, Ctx, process_syntax_tree
from smartanthill_zc.root import RootNode


class ZeptoPlugin(object):

    def __init__(self, manifest_path):
        self.xml = ElementTree.parse(manifest_path).getroot()
        self._source_dir = dirname(manifest_path)

    def get_source_dir(self):
        return self._source_dir

    def get_id(self):
        return self.xml.get("id")

    def get_name(self):
        return self.xml.get("name")

    def get_description(self):
        return self.xml.find("description").text

    def get_request_fields(self):
        return self._get_items_by_path(
            "./request",
            ("type", "name", "title", "min", "max", "default")
        )

    def get_response_fields(self):

        elements = self.xml.find("./response")
        if elements is None:
            return []
        items = []
        for element in elements:
            data = {}
            for attr in ("name", "type", "min", "max"):
                data[attr] = element.get(attr, None)

            meaning = element.find('./meaning')
            if meaning is not None:
                data['meaning'] = meaning.get('type')

                conversion = meaning.find('./linear-conversion')
                if conversion is not None:
                    data["conversion"] = "linear-conversion"
                    for key in("input-point0", "output-point0",
                               "input-point1", "output-point1"):
                        data[key] = conversion.get(key, None)

            items.append(data)
        return items

    def get_peripheral(self):
        return self._get_items_by_path(
            "./configuration/peripheral",
            ("type", "name", "title")
        )

    def get_options(self):
        options = self._get_items_by_path(
            "./configuration/options",
            ("type", "name", "title", "min", "max", "default")
        )

        for index, item in enumerate(options or []):
            if item['default'] is not None:
                if "int" in item['type']:
                    options[index]['default'] = int(item['default'])
                elif "float" in item['type']:
                    options[index]['default'] = float(item['default'])
        return options

    def _get_items_by_path(self, path, attrs):
        elements = self.xml.find(path)
        if elements is None:
            return []
        items = []
        for element in elements:
            data = {}
            for attr in attrs:
                data[attr] = element.get(attr, None)
            items.append(data)
        return items


class ZeptoBodyPart(object):

    def __init__(self, plugin, id_, name, peripheral=None, options=None):
        assert isinstance(plugin, ZeptoPlugin)
        self.plugin = plugin

        self._id = id_
        self._name = name
        self._peripheral = peripheral
        self._options = options

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_peripheral(self):
        peripheral = self.plugin.get_peripheral()
        if not peripheral:
            return []
        for item in peripheral:
            if self._peripheral and item['name'] in self._peripheral:
                item['value'] = self._peripheral[item['name']]
        return peripheral

    def get_options(self):
        options = self.plugin.get_options()
        if not options:
            return []
        for item in options:
            if self._options and item['name'] in self._options:
                item['value'] = self._options[item['name']]
        return options


class ZeptoProgram(object):

    def __init__(self, js_source, bodyparts):
        assert all([isinstance(bp, ZeptoBodyPart) for bp in bodyparts])
        self._js_source = js_source
        self._bodyparts = bodyparts
        self._response_type = None

    def compile(self, parameters=None):

        compiler = Compiler()
        root = compiler.init_node(RootNode(), Ctx.ROOT)

        builtins = builtin.create_builtins(compiler, Ctx.BUILTIN)
        root.set_builtins(builtins)

        bodyparts = parse_xml.create_bodyparts(
            compiler, self._bodyparts, Ctx.BODYPART)
        root.set_bodyparts(bodyparts)

        if parameters:
            params = parse_js.create_parameters(
                compiler, parameters, Ctx.PARAM)
            root.set_parameters(params)

        js_tree = parse_js.parse_js_string(compiler, self._js_source)
        source = parse_js.js_parse_tree_to_syntax_tree(compiler, js_tree)
        root.set_source_program(source)

        visitor.check_all_nodes_reachables(compiler, root)
        process_syntax_tree(compiler, root)

        target = vm.convert_to_zepto_vm_small(compiler, root)

        self._response_type = target.reply_type

        code = writer.write_binary(compiler, target)

        return code

    def process_response(self, data):

        assert self._response_type
        assert self._response_type.is_message_type()

        data = data[:]  # make a copy
        data.reverse()
        header = encode.decode_unsigned_int(data)
        assert header % 16 == 0
        size = header / 16
        if size != len(data):
            data = data[-size:]

        return self._response_type.process_reverse_response(data)


def zepto_exec_cmd(bodypart_id, data):
    '''
    Public api function that creates a binary code for a ZEPTOVM_OP_EXEC
    '''

    compiler = Compiler()
    op = compiler.init_node(op_node.ExecOpNode(), Ctx.TARGET)
    op.bodypart_id = bodypart_id
    op.data = bytearray(data)

    code = writer.write_binary(compiler, op)

    return code
