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
    parse_xml, node
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

    bodyparts = parse_xml.parse_test_xml_body_parts(comp, xml, Ctx.BODYPART)
    root.set_bodyparts(bodyparts)

    visitor.check_all_nodes_reachables(comp, root)
    compiler.process_syntax_tree(comp, root)

    target = vm.convert_to_zepto_vm_tiny(comp, root)

    return writer.write_text_op_codes(comp, target)


def test_js_tiny_2():

    code = [u'var temp = TempSensor1.Execute();',
            u'if(temp.Temperature <= 35.0 || temp.Temperature >= 42.0) {',
            u'  mcu_sleep(5*60);',
            u'  temp = TempSensor1.Execute();',
            u'}',
            u'if(temp.Temperature > 36.0 && temp.Temperature < 40.0) {',
            u'  var temp2 = TempSensor1.Execute();',
            u'  if(temp2.Temperature > 38.0)',
            u'    return temp2;',
            u'  mcu_sleep(5*60);',
            u'}',
            u'return TempSensor1.Execute();']

    out = ['/* target vm: Tiny */',
           '/* mcusleep: True */',
           '/* reply: {INT} */',
           '/* size: 69 bytes */',
           '|EXEC|1|0|[]|',
           '/* if( temp.Temperature<=35.0||temp.Temperature>=42.0 ) */',
           '|JMPIFREPLYFIELD_LT|0|{INT}|351|(+7):begin_2:|',
           '|JMPIFREPLYFIELD_LT|0|{INT}|420|(+9):end_6:|',
           '/* begin_2: */',
           '|MCUSLEEP|300|0|',
           '|POPREPLIES|0|',
           '|EXEC|1|0|[]|',
           '/* end_6: */',
           '/* if( temp.Temperature>36.0&&temp.Temperature<40.0 ) */',
           '|JMPIFREPLYFIELD_LT|0|{INT}|361|(+29):end_12:|',
           '|JMPIFREPLYFIELD_GT|0|{INT}|399|(+22):end_12:|',
           '/* begin_6: */',
           '|EXEC|1|0|[]|',
           '/* if( temp2.Temperature>38.0 ) */',
           '|JMPIFREPLYFIELD_LT|1|{INT}|381|(+6):end_10:|',
           '/* begin_9: */',
           '|MOVEREPLYTOFRONT|1|',
           '|POPREPLIES|1|',
           '|EXIT|ISFIRST|',
           '/* end_10: */',
           '|MCUSLEEP|300|0|',
           '|POPREPLIES|1|',
           '/* end_12: */',
           '|POPREPLIES|0|',
           '|EXEC|1|0|[]|',
           '|EXIT|ISFIRST|']

    assert common_test_run(code) == out


def test_js_tiny_3():

    code = [
        u'var a = TempSensor1.Execute();',
        u'var b = TempSensor1.Execute();',
        u'var c = TempSensor1.Execute();',
        u'var d = TempSensor1.Execute();',
        u'if (c.Temperature > 38) {'
        u'  return [TempSensor1.Execute(), b, TempSensor1.Execute(), d];'
        u'}'
        u'return [a, TempSensor1.Execute(), c, TempSensor1.Execute()]']

    out = [
        '/* target vm: Tiny */',
        '/* mcusleep: False */',
        '/* reply: {INT,INT,INT,INT} */',
        '/* size: 53 bytes */',
        '|EXEC|1|0|[]|',
        '|EXEC|1|0|[]|',
        '|EXEC|1|0|[]|',
        '|EXEC|1|0|[]|',
        '/* if( c.Temperature>38 ) */',
        '|JMPIFREPLYFIELD_LT|2|{INT}|381|(+20):end_6:|',
        '/* begin_5: */',
        '|MOVEREPLYTOFRONT|3|',
        '|MOVEREPLYTOFRONT|2|',
        '|POPREPLIES|2|',
        '|EXEC|1|0|[]|',
        '|EXEC|1|0|[]|',
        '|MOVEREPLYTOFRONT|3|',
        '|MOVEREPLYTOFRONT|1|',
        '|MOVEREPLYTOFRONT|3|',
        '|EXIT|ISLAST|',
        '/* end_6: */',
        '|MOVEREPLYTOFRONT|2|',
        '|POPREPLIES|2|',
        '|EXEC|1|0|[]|',
        '|EXEC|1|0|[]|',
        '|MOVEREPLYTOFRONT|2|',
        '|MOVEREPLYTOFRONT|2|',
        '/* exit|islast */']

    assert common_test_run(code) == out


def test_js_tiny_negate():

    code = [u'var temp = TempSensor1.Execute();',
            u'if(!(temp.Temperature <= 35.0 || temp.Temperature >= 42.0)) {',
            u'  mcu_sleep(5*60);',
            u'  temp = TempSensor1.Execute();',
            u'}',
            u'if(!(temp.Temperature > 36.0 && temp.Temperature < 40.0)) {',
            u'  var temp2 = TempSensor1.Execute();',
            u'  if(!(temp2.Temperature > 38.0))',
            u'    return temp2;',
            u'  mcu_sleep(5*60);',
            u'}',
            u'return TempSensor1.Execute();']

    out = ['/* target vm: Tiny */',
           '/* mcusleep: True */',
           '/* reply: {INT} */',
           '/* size: 69 bytes */',
           '|EXEC|1|0|[]|',
           '/* if( !(temp.Temperature<=35.0||temp.Temperature>=42.0) ) */',
           '|JMPIFREPLYFIELD_LT|0|{INT}|351|(+16):end_6:|',
           '|JMPIFREPLYFIELD_GT|0|{INT}|419|(+9):end_6:|',
           '/* begin_2: */',
           '|MCUSLEEP|300|0|',
           '|POPREPLIES|0|',
           '|EXEC|1|0|[]|',
           '/* end_6: */',
           '/* if( !(temp.Temperature>36.0&&temp.Temperature<40.0) ) */',
           '|JMPIFREPLYFIELD_LT|0|{INT}|361|(+7):begin_6:|',
           '|JMPIFREPLYFIELD_LT|0|{INT}|400|(+22):end_12:|',
           '/* begin_6: */',
           '|EXEC|1|0|[]|',
           '/* if( !(temp2.Temperature>38.0) ) */',
           '|JMPIFREPLYFIELD_GT|1|{INT}|380|(+6):end_10:|',
           '/* begin_9: */',
           '|MOVEREPLYTOFRONT|1|',
           '|POPREPLIES|1|',
           '|EXIT|ISFIRST|',
           '/* end_10: */',
           '|MCUSLEEP|300|0|',
           '|POPREPLIES|1|',
           '/* end_12: */',
           '|POPREPLIES|0|',
           '|EXEC|1|0|[]|',
           '|EXIT|ISFIRST|']

    assert common_test_run(code) == out
