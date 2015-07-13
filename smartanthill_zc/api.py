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

from os.path import basename
from xml.etree import ElementTree

from smartanthill_zc.compiler import Compiler
from smartanthill_zc.op_node import ExecOpNode
from smartanthill_zc.writer import write_binary


class ZeptoPlugin(object):

    def __init__(self, manifest_path):
        self.xml = ElementTree.parse(manifest_path).getroot()
        self.source_dir = basename(manifest_path)

    def get_id(self):
        return self.xml.get("id")

    def get_name(self):
        return self.xml.get("name")

    def get_description(self):
        return self.xml.find("description").text

    def get_peripheral(self):
        pins = self.xml.find("./configuration/peripheral")
        if pins is None:
            return None
        result = []
        for element in pins:
            data = {}
            for key in ("type", "name", "title"):
                data[key] = element.get(key, None)
            result.append(data)
        return result

    def get_options(self):
        options = self.xml.find("./configuration/options")
        if options is None:
            return None
        result = []
        for element in options:
            data = {}
            for key in ("type", "name", "title", "default"):
                data[key] = element.get(key, None)
            result.append(data)
        return result


class ZeptoBodyPart(object):

    def __init__(self, id_, name, plugin, peripheral=None, options=None):
        assert isinstance(plugin, ZeptoPlugin)
        self._id = id_
        self._plugin = plugin
        self._peripheral = peripheral
        self._options = options

    def get_id(self):
        return self._id

    def get_plugin_id(self):
        return self._plugin.get_id()

    def get_peripheral(self):
        peripheral = self._plugin.get_peripheral()
        if not peripheral:
            return None
        for item in peripheral:
            if self._peripheral and item['name'] in self._peripheral:
                item['value'] = self._peripheral[item['name']]
        return peripheral

    def get_options(self):
        options = self._plugin.get_options()
        if not options:
            return None
        for item in options:
            if self._options and item['name'] in self._options:
                item['value'] = self._options[item['name']]
        return options


def zepto_exec_cmd(bodypart_id, data):
    '''
    Public api function that creates a binary code for a ZEPTOVM_OP_EXEC
    '''

    compiler = Compiler()
    op = compiler.init_node(ExecOpNode(), Compiler.NONE)
    op.bodypart_id = bodypart_id
    op.data = data

    code = write_binary(compiler, op)

    return code
