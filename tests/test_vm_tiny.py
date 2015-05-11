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
        u'<smartanthill.plugin name="TemperatureSensor" id="1" version="1.0">',
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

    target = vm.convert_to_zepto_vm_tiny(comp, root)

    return writer.write_text_op_codes(comp, target)


def test_js_tiny_2():

    code = [u'var temp = TemperatureSensor.Execute();',
            u'if(temp.Temperature <= 35.0 || temp.Temperature >= 42.0) {',
            u'  mcu_sleep(5*60);',
            u'  temp = TemperatureSensor.Execute();',
            u'}',
            u'if(temp.Temperature > 36.0 && temp.Temperature < 40.0) {',
            u'  var temp2 = TemperatureSensor.Execute();',
            u'  if(temp2.Temperature > 38.0)',
            u'    return temp2;',
            u'  mcu_sleep(5*60);',
            u'}',
            u'return TemperatureSensor.Execute();']

    out = ['/* target vm: Tiny */',
           '/* mcusleep: True */',
           '/* reply: {INT} */',
           '|EXEC|1|0|[]|',
           '|JMPIFREPLYFIELD_LT|0|{INT}|351|(+9):begin:|',
           '|JMPIFREPLYFIELD_LT|0|{INT}|420|(+14):end:|',
           '/* begin: */',
           '|MCUSLEEP|300|0|',
           '|POPREPLIES|0|',
           '|EXEC|1|0|[]|',
           '/* end: */',
           '|JMPIFREPLYFIELD_LT|0|{INT}|361|(+40):end:|',
           '|JMPIFREPLYFIELD_GT|0|{INT}|399|(+31):end:|',
           '/* begin: */',
           '|EXEC|1|0|[]|',
           '|JMPIFREPLYFIELD_LT|1|{INT}|381|(+8):end:|',
           '/* begin: */',
           '|MOVEREPLYTOFRONT|1|',
           '|POPREPLIES|1|',
           '|EXIT|ISFIRST|',
           '/* end: */',
           '|MCUSLEEP|300|0|',
           '|POPREPLIES|1|',
           '/* end: */',
           '|POPREPLIES|0|',
           '|EXEC|1|0|[]|',
           '|EXIT|ISFIRST|']

    assert common_test_run(code) == out
