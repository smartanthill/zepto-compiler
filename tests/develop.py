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

import math
import sys

from smartanthill_zc import builtin, vm, writer, encode
from smartanthill_zc import compiler, parse_xml
from smartanthill_zc import parse_js
from smartanthill_zc import visitor
from smartanthill_zc.compiler import Compiler
from smartanthill_zc.encode import create_half_float, half_float_value,\
    half_float_next_down


def main():

    code = [u'var temp = TempSensor.Execute();',
            u'if(temp.Temperature <= 35.0 || temp.Temperature >= 42.0) {',
            u'  mcu_sleep(5*60);',
            u'  temp = TempSensor.Execute();',
            u'}',
            u'if(temp.Temperature > 36.0 && temp.Temperature < 40.0) {',
            u'  var temp2 = TempSensor.Execute();',
            u'  if(temp2.Temperature > 38.0)',
            u'    return temp2;',
            u'  mcu_sleep(5*60);',
            u'}',
            u'return TempSensor.Execute();']

#        u'return [TempSensor.Execute(), TempSensor.Execute()];']
    #             u'  if (temp.Temperature < 36.0 || temp.Temperature > 38.9)'
    #             u'    return temp;'
    #
    #             u'  mcu_sleep(5*60);'
    #             u'}'
    #             u'return TemperatureSensor.Execute();']
    #     code = [u'var temp = TemperatureSensor.Execute();',
    #             u'if(temp.Temperature <= 35.0 || temp.Temperature >= 42.0) {',
    #             u'  mcu_sleep(5*60);',
    #             u'  temp = TemperatureSensor.Execute();',
    #             u'}',
    #             u'if(temp.Temperature > 36.0 && temp.Temperature < 40.0) {',
    #             u'  var temp2 = TemperatureSensor.Execute();',
    #             u'  if(temp2.Temperature > 38.0)',
    #             u'    return temp2;',
    #             u'  mcu_sleep(5*60);',
    #             u'}',
    #             u'return TemperatureSensor.Execute();']

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
 #   xml2 = '\n'.join(xml2)
    code = '\n'.join(code)
    comp = Compiler()

    bodyparts = parse_xml.parse_xml_body_part_list(comp, [xml])
    etdump = visitor.dump_tree(bodyparts)

    print '\n'.join(etdump)

    js_tree = parse_js.parse_js_string(comp, code)
    root = parse_js.js_parse_tree_to_syntax_tree(comp, js_tree)

    builtin.create_builtins(comp, root)

#    xml_tree = parse_xml.parse_xml_string(comp, xml)
#    bodyparts = parse_xml.xml_parse_tree_process(comp, xml_tree)
    root.set_bodyparts(bodyparts)

    visitor.check_all_nodes_reachables(comp, root)
    compiler.process_syntax_tree(comp, root)

    actual = visitor.dump_tree(root)

    print '\n'.join(actual)

    target = vm.convert_to_zepto_vm_small(comp, root)
    txt = writer.write_text_op_codes(comp, target)
    print '\n'.join(txt)

# temporary entrance
if __name__ == "__main__":
    sys.exit(main())
