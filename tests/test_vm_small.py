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
from smartanthill_zc.compiler import Ctx, Compiler
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

    visitor.check_all_nodes_reachables(comp, root)
    compiler.process_syntax_tree(comp, root)

    target = vm.convert_to_zepto_vm_small(comp, root)

    return writer.write_text_op_codes(comp, target, {})


def test_js_small_3():

    code = [u'for( var i = 0; i < 5; i++) {',
            u'  var temp = TempSensor1.Execute();',
            u'  if(temp.Temperature < 36.0 || temp.Temperature > 38.9)',
            u'    return temp;',
            u'  mcu_sleep(5*60);',
            u'}',
            u'return TempSensor1.Execute();']

    out = [
        '/* target vm: Small */',
        '/* mcusleep: True */',
        '/* reply: {INT} */',
        '/* size: 35 bytes */',
        '/* for( var i = 0.0; .. */',
        '|PUSHEXPR_CONSTANT|0|',
        '/* begin_1: */',
        '|EXEC|1|0|[]|',
        '/* if( temp.Temperature<36.0||temp.Temperature>38.9 ) */',
        '|JMPIFREPLYFIELD_LT|0|{INT}|360|(+7):begin_4:|',
        '|JMPIFREPLYFIELD_LT|0|{INT}|390|(+2):end_5:|',
        '/* begin_4: */',
        '|EXIT|ISFIRST|',
        '/* end_5: */',
        '|MCUSLEEP|300|0|',
        '|POPREPLIES|0|',
        '/* ..; i < 5.0; i++ ) */',
        '|INCANDJMPIF|1|5|(-30):begin_1:|',
        '|EXPRUNOP|POP|',
        '|EXEC|1|0|[]|',
        '|EXIT|ISFIRST|']

    assert common_test_run(code) == out


def test_js_small_expr():

    code = [u'for( var i = 0; i < 5; i++) {',
            u'  var temp = TempSensor1.Execute();',
            u'  var a = temp.Temperature;',
            u'  var b = 36.7;',
            u'  mcu_sleep(5*60);',
            u'}',
            u'return TempSensor1.Execute();']

    out = [
        '/* target vm: Small */',
        '/* mcusleep: True */',
        '/* reply: {INT} */',
        '/* size: 30 bytes */',
        '/* for( var i = 0.0; .. */',
        '|PUSHEXPR_CONSTANT|0|',
        '/* begin_1: */',
        '|EXEC|1|0|[]|',
        '|PUSHEXPR_REPLYFIELD|0|{INT}|',
        '|PUSHEXPR_CONSTANT|36.7|',
        '|MCUSLEEP|300|0|',
        '|POPREPLIES|0|',
        '|EXPRUNOP|POP|',
        '|EXPRUNOP|POP|',
        '/* ..; i < 5.0; i++ ) */',
        '|INCANDJMPIF|1|5|(-25):begin_1:|',
        '|EXPRUNOP|POP|',
        '|EXEC|1|0|[]|',
        '|EXIT|ISFIRST|']

    assert common_test_run(code) == out


def test_js_small_comp1():

    code = [u'var temp = TempSensor1.Execute();',
            u'if(temp.Temperature + 1 < 36.6) {',
            u'  mcu_sleep(5*60);',
            u'  return TempSensor1.Execute();',
            u'}',
            u'return temp;']

    out = [
        '/* target vm: Small */',
        '/* mcusleep: True */',
        '/* reply: {INT} */',
        '/* size: 36 bytes */',
        '|EXEC|1|0|[]|',
        '/* if( temp.Temperature+1<36.6 ) */',
        '|PUSHEXPR_REPLYFIELD|0|{INT}|',
        '|EXPRBINOP_EX|*|1,POP|->|0.1|',
        '|EXPRBINOP_EX|+|1,POP|->|1|',
        '|JMPIFEXPR_GT|36.5625|(+11):end_6:|',
        '/* begin_2: */',
        '|MCUSLEEP|300|0|',
        '|POPREPLIES|0|',
        '|EXEC|1|0|[]|',
        '|EXIT|ISFIRST|',
        '/* end_6: */',
        '|EXIT|ISFIRST|']

    assert common_test_run(code) == out


def test_js_small_comp2():

    code = [u'var temp1 = TempSensor1.Execute();',
            u'var temp2 = TempSensor10.Execute();',
            u'if(temp1.Temperature < temp2.Temperature) {',
            u'  mcu_sleep(5*60);',
            u'  return TempSensor1.Execute();',
            u'}',
            u'return temp1;']

    out = [
        '/* target vm: Small */',
        '/* mcusleep: True */',
        '/* reply: {INT} */',
        '/* size: 53 bytes */',
        '|EXEC|1|0|[]|',
        '|EXEC|10|0|[]|',
        '/* if( temp1.Temperature<temp2.Temperature ) */',
        '|PUSHEXPR_REPLYFIELD|0|{INT}|',
        '|EXPRBINOP_EX|*|1,POP|->|0.1|',
        '|PUSHEXPR_REPLYFIELD|1|{INT}|',
        '|EXPRBINOP_EX|*|1,POP|->|0.05|',
        '|EXPRBINOP_EX|+|1,POP|->|10|',
        '|EXPRBINOP|-|',
        '|JMPIFEXPR_GT|-5.96046e-08|(+11):end_7:|',
        '/* begin_3: */',
        '|MCUSLEEP|300|0|',
        '|POPREPLIES|0|',
        '|EXEC|1|0|[]|',
        '|EXIT|ISFIRST|',
        '/* end_7: */',
        '|POPREPLIES|1|',
        '|EXIT|ISFIRST|']

    assert common_test_run(code) == out


def test_js_small_comp3():

    code = [u'var temp = TempSensor1.Execute();',
            u'var temp1 = temp.Temperature + 1;',
            u'var temp2 = TempSensor10.Execute();',
            u'if(temp1 < temp2.Temperature) {',
            u'  mcu_sleep(5*60);',
            u'  return TempSensor1.Execute();',
            u'}',
            u'return temp;']

    out = [
        '/* target vm: Small */',
        '/* mcusleep: True */',
        '/* reply: {INT} */',
        '/* size: 59 bytes */',
        '|EXEC|1|0|[]|',
        '|PUSHEXPR_REPLYFIELD|0|{INT}|',
        '|EXPRBINOP_EX|*|1,POP|->|0.1|',
        '|EXPRBINOP_EX|+|1,POP|->|1|',
        '|EXEC|10|0|[]|',
        '/* if( temp1<temp2.Temperature ) */',
        '|PUSHEXPR_REPLYFIELD|1|{INT}|',
        '|EXPRBINOP_EX|*|1,POP|->|0.05|',
        '|EXPRBINOP_EX|+|1,POP|->|10|',
        '|EXPRBINOP|-|',
        '|JMPIFEXPR_GT|-5.96046e-08|(+11):end_8:|',
        '/* begin_4: */',
        '|MCUSLEEP|300|0|',
        '|POPREPLIES|0|',
        '|EXEC|1|0|[]|',
        '|EXIT|ISFIRST|',
        '/* end_8: */',
        '|POPREPLIES|1|',
        '|EXIT|ISFIRST|']

    assert common_test_run(code) == out
