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

from smartanthill_zc import compiler, parse_xml
from smartanthill_zc import parse_js
from smartanthill_zc import visitor
from smartanthill_zc import builtin
import pytest


def common_test_run(code):

    xml = [
        u'<smartanthill.plugin name="TemperatureSensor" id="1" version="1.0">',
        u'  <description>Short description here</description>',
        u'  <command/>',
        u'  <reply>',
        u'    <field name="Temperature" type="encoded-signed-int&lt;max=2&gt;" min="0" max="255">',
        u'      <meaning type="float">',
        u'        <linear-conversion input-point0="0" output-point0="20.0"',
        u'          input-point1="100" output-point1="40.0" />',
        u'      </meaning>',
        u'    </field>',
        u'  </reply>',
        u'  <peripheral>Right now compiler can ignore this</peripheral>',
        u'</smartanthill.plugin>'
    ]

    xml = '\n'.join(xml)
    code = '\n'.join(code)

    comp = compiler.Compiler()
    js_tree = parse_js.parse_js_string(comp, code)
    root = parse_js.js_parse_tree_to_syntax_tree(comp, js_tree)

    builtin.create_builtins(comp, root)

    xml_tree = parse_xml.parse_xml_string(comp, xml)
    bodyparts = parse_xml.xml_parse_tree_process(comp, xml_tree)
    root.set_bodyparts(bodyparts)

    visitor.check_all_nodes_reachables(comp, root)

    compiler.process_syntax_tree(comp, root)

    actual = visitor.dump_tree(root)

    return actual


def test_js_resolve():

    code = [u'for (var i = 0; i < 5; i++) {'
            u'  var temp = TemperatureSensor.Execute();'
            u'  if (temp.Temperature < 36.0 || temp.Temperature > 38.9)'
            u'    return temp;'

            u'  mcu_sleep(5*60);'
            u'}'
            u'return TemperatureSensor.Execute();']

    common_test_run(code)


def test_js_return_raise():
    with pytest.raises(compiler.CompilerError):

        code = [u'if (true) {'
                u'  return false;'
                u'}'
                u'return 0;']

        common_test_run(code)


def test_js_if_raise():
    with pytest.raises(compiler.CompilerError):

        code = [u'var temp = TemperatureSensor.Execute();'
                u'if (temp) {'
                u'  ;'
                u'}'
                u'return 0;']

        common_test_run(code)


def test_js_var_assignment():

    code = [u'var temp = TemperatureSensor.Execute();'
            u'temp = TemperatureSensor.Execute();']

    common_test_run(code)


def test_js_var_assignment_raise():
    with pytest.raises(compiler.CompilerError):

        code = [u'var temp = 0;'
                u'temp = TemperatureSensor.Execute();']

        common_test_run(code)


def test_js_plugin_unknonwn_raise():
    with pytest.raises(compiler.CompilerError):

        code = [u'var temp = UnknownSensor\n.\nExecute\n(\n)\n;\n']

        common_test_run(code)
