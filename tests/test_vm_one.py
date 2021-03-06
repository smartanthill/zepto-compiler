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

from smartanthill_zc import compiler, parse_js, builtin, vm, writer, visitor,\
    parse_xml
from smartanthill_zc.compiler import Compiler, Ctx
from smartanthill_zc.root import RootNode


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

    param_dict = {'PARAM1': 11}

    xml = '\n'.join(xml)
    code = '\n'.join(code)

    comp = Compiler()
    root = comp.init_node(RootNode(), Ctx.ROOT)

    js_tree = parse_js.parse_js_string(comp, code)
    source = parse_js.js_parse_tree_to_syntax_tree(comp, js_tree)
    root.set_source_program(source)

    builtins = builtin.create_builtins(comp, Ctx.BUILTIN)
    root.set_builtins(builtins)

    bodyparts = parse_xml.parse_test_xml_body_parts(comp, xml, Ctx.BODYPART)
    root.set_bodyparts(bodyparts)

    params = parse_js.create_parameters(comp, param_dict, Ctx.PARAM)
    root.set_parameters(params)

    visitor.check_all_nodes_reachables(comp, root)
    compiler.process_syntax_tree(comp, root)

    target = vm.convert_to_zepto_vm_one(comp, root)

    return writer.write_text_op_codes(comp, target, param_dict)


def test_js_pattern_1():

    code = [u'return TempSensor1.Execute();']

    out = ['/* target vm: One */',
           '/* mcusleep: False */',
           '/* reply: {INT} */',
           '/* size: 3 bytes */',
           '|EXEC|1|0|[]|',
           '/* exit|islast */']

    assert common_test_run(code) == out


def test_js_pattern_2():

    code = [u'mcu_sleep(5*60);',
            u'return TempSensor1.Execute();']

    out = ['/* target vm: One */',
           '/* mcusleep: True */',
           '/* reply: {INT} */',
           '/* size: 9 bytes */',
           '|MCUSLEEP|300|0|',
           '|EXEC|1|0|[]|',
           '|EXIT|ISFIRST|']

    assert common_test_run(code) == out


def test_js_return_array():

    code = [
        u'return [TempSensor1.Execute(), TempSensor2.Execute()];']

    out = ['/* target vm: One */',
           '/* mcusleep: False */',
           '/* reply: {INT,INT} */',
           '/* size: 6 bytes */',
           '|EXEC|1|0|[]|',
           '|EXEC|2|0|[]|',
           '/* exit|islast */']

    assert common_test_run(code) == out


def test_js_actuator():

    code = [
        u'return Actuator1.Execute(10);']

    out = ['/* target vm: One */',
           '/* mcusleep: False */',
           '/* reply: {} */',
           '/* size: 5 bytes */',
           '|EXEC|100|1|[0x14]|',
           '/* exit|islast */']

    assert common_test_run(code) == out


def test_js_parameter():

    code = [
        u'return Actuator1.Execute(PARAM1);']

    out = ['/* target vm: One */',
           '/* mcusleep: False */',
           '/* reply: {} */',
           '/* size: 5 bytes */',
           '|EXEC|100|1|[0x16]|',
           '/* exit|islast */']

    assert common_test_run(code) == out
