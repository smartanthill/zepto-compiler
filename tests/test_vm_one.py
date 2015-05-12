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
        u'    <field name="Temperature" type="encoded-signed-int&lt;max=2&gt;"',
        u'     min="0" max="255" />',
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

    target = vm.convert_to_zepto_vm_one(comp, root)

    return writer.write_text_op_codes(comp, target)


def test_js_pattern_1():

    code = [u'return TemperatureSensor.Execute();']

    out = ['/* target vm: One */',
           '/* mcusleep: False */',
           '/* reply: {INT} */',
           '/* size: 5 bytes */',
           '|EXEC|1|0|[]|',
           '/* exit|islast */']

    assert common_test_run(code) == out


def test_js_pattern_2():

    code = [u'mcu_sleep(5*60);',
            u'return TemperatureSensor.Execute();']

    out = ['/* target vm: One */',
           '/* mcusleep: True */',
           '/* reply: {INT} */',
           '/* size: 13 bytes */',
           '|MCUSLEEP|300|0|',
           '|EXEC|1|0|[]|',
           '|EXIT|ISFIRST|']

    assert common_test_run(code) == out
