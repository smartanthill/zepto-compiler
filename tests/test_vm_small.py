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


def common_test_run(code):

    xml = [
        u'<smartanthill.plugin name="TempSensor" id="1" version="1.0">',
        u'  <description>Short description here</description>',
        u'  <command/>',
        u'  <reply>',
        u'    <field name="Temperature" type="encoded-signed-int[max=2]"',
        u'     min="0" max="500">',
        u'      <meaning type="float">',
        u'        <linear-conversion input-point0="100" output-point0="10.0"',
        u'                       input-point1="200" output-point1="20.0" />',
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

#     xml_tree = parse_xml.parse_xml_string(comp, xml)
#     bodyparts = parse_xml.xml_parse_tree_process(comp, xml_tree)
    bodyparts = parse_xml.parse_xml_body_parts(comp, xml)
    root.set_bodyparts(bodyparts)

    visitor.check_all_nodes_reachables(comp, root)
    compiler.process_syntax_tree(comp, root)

    target = vm.convert_to_zepto_vm_small(comp, root)

    return writer.write_text_op_codes(comp, target)


def test_js_small_3():

    code = [u'for( var i = 0; i < 5; i++) {',
            u'  var temp = TempSensor.Execute();',
            u'  if(temp.Temperature < 36.0 || temp.Temperature > 38.9)',
            u'    return temp;',
            u'  mcu_sleep(5*60);',
            u'}',
            u'return TempSensor.Execute();']

    out = [
        '/* target vm: Small */',
        '/* mcusleep: True */',
        '/* reply: {INT} */',
        '/* size: 48 bytes */',
        '/* for( var i = 0.0; .. */',
        '|PUSHEXPR_CONSTANT|0|',
        '/* begin_1: */',
        '|EXEC|1|0|[]|',
        '/* if( temp.Temperature<36.0||temp.Temperature>38.9 ) */',
        '|JMPIFREPLYFIELD_LT|0|{INT}|360|(+9):begin_4:|',
        '|JMPIFREPLYFIELD_LT|0|{INT}|390|(+2):end_5:|',
        '/* begin_4: */',
        '|EXIT|ISFIRST|',
        '/* end_5: */',
        '|MCUSLEEP|300|0|',
        '|POPREPLIES|0|',
        '/* ..; i < 5.0; i++ ) */',
        '|INCANDJMPIF|1|5|(-41):begin_1:|',
        '|EXPRUNOP|POP|',
        '|EXEC|1|0|[]|',
        '|EXIT|ISFIRST|']

    assert common_test_run(code) == out


def test_js_small_expr():

    code = [u'for( var i = 0; i < 5; i++) {',
            u'  var temp = TempSensor.Execute();',
            u'  var a = temp.Temperature;',
            u'  var b = 36.7;',
            u'  mcu_sleep(5*60);',
            u'}',
            u'return TempSensor.Execute();']

    out = [
        '/* target vm: Small */',
        '/* mcusleep: True */',
        '/* reply: {INT} */',
        '/* size: 40 bytes */',
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
        '|INCANDJMPIF|1|5|(-33):begin_1:|',
        '|EXPRUNOP|POP|',
        '|EXEC|1|0|[]|',
        '|EXIT|ISFIRST|']

    assert common_test_run(code) == out


def test_js_small_comp1():

    code = [u'var temp = TempSensor.Execute();',
            u'if(temp.Temperature + 1 < 36.6) {',
            u'  mcu_sleep(5*60);',
            u'  return TempSensor.Execute();',
            u'}',
            u'return temp;']

    out = [
        '/* target vm: Small */',
        '/* mcusleep: True */',
        '/* reply: {INT} */',
        '/* size: 49 bytes */',
        '|EXEC|1|0|[]|',
        '/* if( temp.Temperature+1<36.6 ) */',
        '|PUSHEXPR_REPLYFIELD|0|{INT}|',
        '|EXPRBINOP_EX|*|1,POP|->|0.1|',
        '|EXPRBINOP_EX|+|1,POP|->|1|',
        '|JMPIFEXPR_GT|36.5625|(+16):end_6:|',
        '/* begin_2: */',
        '|MCUSLEEP|300|0|',
        '|POPREPLIES|0|',
        '|EXEC|1|0|[]|',
        '|EXIT|ISFIRST|',
        '/* end_6: */',
        '|EXIT|ISFIRST|']

    assert common_test_run(code) == out


def test_js_small_comp2():

    code = [u'var temp1 = TempSensor.Execute();',
            u'var temp2 = TempSensor.Execute();',
            u'if(temp1.Temperature < temp2.Temperature) {',
            u'  mcu_sleep(5*60);',
            u'  return TempSensor.Execute();',
            u'}',
            u'return temp1;']

    out = [
        '/* target vm: Small */',
        '/* mcusleep: True */',
        '/* reply: {INT} */',
        '/* size: 64 bytes */',
        '|EXEC|1|0|[]|',
        '|EXEC|1|0|[]|',
        '/* if( temp1.Temperature<temp2.Temperature ) */',
        '|PUSHEXPR_REPLYFIELD|0|{INT}|',
        '|EXPRBINOP_EX|*|1,POP|->|0.1|',
        '|PUSHEXPR_REPLYFIELD|1|{INT}|',
        '|EXPRBINOP_EX|*|1,POP|->|0.1|',
        '|EXPRBINOP|-|',
        '|JMPIFEXPR_GT|-5.96046e-08|(+16):end_7:|',
        '/* begin_3: */',
        '|MCUSLEEP|300|0|',
        '|POPREPLIES|0|',
        '|EXEC|1|0|[]|',
        '|EXIT|ISFIRST|',
        '/* end_7: */',
        '|POPREPLIES|1|',
        '|EXIT|ISFIRST|']

    assert common_test_run(code) == out
