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

import pytest

from smartanthill_zc import builtin, node
from smartanthill_zc import compiler, parse_xml
from smartanthill_zc import parse_js
from smartanthill_zc import visitor
from smartanthill_zc.compiler import Ctx


def common_test_run(code):

    xml = [
        u'<smartanthill_zc.test>',
        u'  <plugin>',
        u'    <command/>',
        u'    <reply>',
        u'      <field name="Temperature" type="encoded-int[max=2]"',
        u'        min="0" max="500"',
        u'        meaning="float"',
        u'        conversion="linear-conversion"',
        u'        input-point0="100" output-point0="10.0"',
        u'        input-point1="200" output-point1="20.0" />',
        u'    </reply>',
        u'    <bodyparts>',
        u'      <bodypart name="TempSensor1" id="1" />',
        u'      <bodypart name="TempSensor2" id="2" />',
        u'    </bodyparts>',
        u'  </plugin>',
        u'  <plugin>',
        u'    <command/>',
        u'    <reply>',
        u'      <field name="Temperature" type="encoded-int[max=2]"',
        u'        min="0" max="500"',
        u'        meaning="float"',
        u'        conversion="linear-conversion"',
        u'        input-point0="100" output-point0="15.0"',
        u'        input-point1="200" output-point1="20.0" />',
        u'    </reply>',
        u'    <bodyparts>',
        u'      <bodypart name="TempSensor10" id="10" />',
        u'    </bodyparts>',
        u'  </plugin>',
        u'  <plugin>',
        u'    <command>',
        u'      <field name="abc" type="encoded-int[max=2]" />',
        u'    </command>',
        u'    <reply/>',
        u'    <bodyparts>',
        u'      <bodypart name="Actuator1" id="100" />',
        u'    </bodyparts>',
        u'  </plugin>',
        u'</smartanthill_zc.test>'
    ]

    xml = '\n'.join(xml)
    code = '\n'.join(code)

    comp = compiler.Compiler()
    root = comp.init_node(node.RootNode(), Ctx.ROOT)

    js_tree = parse_js.parse_js_string(comp, code)
    source = parse_js.js_parse_tree_to_syntax_tree(comp, js_tree)
    root.set_source_program(source)

    builtins = builtin.create_builtins(comp, Ctx.BUILTIN)
    root.set_builtins(builtins)

#     xml_tree = parse_xml.parse_xml_string(comp, xml)
#     bodyparts = parse_xml.xml_parse_tree_process(comp, xml_tree)
    bodyparts = parse_xml.parse_test_xml_body_parts(comp, xml, Ctx.BODYPART)
    root.set_bodyparts(bodyparts)

    visitor.check_all_nodes_reachables(comp, root)

    compiler.process_syntax_tree(comp, root)

    actual = visitor.dump_tree(root)

    return actual


def test_js_resolve():

    code = [u'for (var i = 0; i < 5; i++) {'
            u'  var temp = TempSensor1.Execute();'
            u'  if (temp.Temperature < 36.0 || temp.Temperature > 38.9)'
            u'    return temp;'

            u'  mcu_sleep(5*60);'
            u'}'
            u'return TempSensor1.Execute();']

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

        code = [u'var temp = TempSensor1.Execute();'
                u'if (temp) {'
                u'  ;'
                u'}'
                u'return 0;']

        common_test_run(code)


def test_js_var_assignment():

    code = [u'var temp = TempSensor1.Execute();'
            u'temp = TempSensor1.Execute();']

    common_test_run(code)


def test_js_var_assignment_raise():
    with pytest.raises(compiler.CompilerError):

        code = [u'var temp = 0;'
                u'temp = TempSensor1.Execute();']

        common_test_run(code)


def test_js_plugin_unknonwn_raise():
    with pytest.raises(compiler.CompilerError):

        code = [u'var temp = UnknownSensor\n.\nExecute\n(\n)\n;\n']

        common_test_run(code)
