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

import cProfile
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

    code = [u'var temp = TempSensor1.Execute();',
            u'if(temp.Temperature + 1 < 36.6) {',
            u'  mcu_sleep(5*60);',
            u'  return TempSensor1.Execute();',
            u'}',
            u'return temp;']

    xml = [
        u'<smartanthill_zc.test>',
        u'  <plugin>',
        u'    <command/>',
        u'    <reply>',
        u'      <field name="Temperature" type="encoded-signed-int[max=2]"',
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
        u'      <field name="Temperature" type="encoded-signed-int[max=2]"',
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
        u'      <field name="abc" type="encoded-signed-int[max=2]" />',
        u'    </command>',
        u'    <reply/>',
        u'    <bodyparts>',
        u'      <bodypart name="Actuator1" id="100" />',
        u'    </bodyparts>',
        u'  </plugin>',
        u'</smartanthill_zc.test>'
    ]

    xml = '\n'.join(xml)
 #   xml2 = '\n'.join(xml2)
    code = '\n'.join(code)
    comp = Compiler()

    bodyparts = parse_xml.parse_test_xml_body_parts(comp, xml)

#    etdump = visitor.dump_tree(bodyparts)
#    print '\n'.join(etdump)

    js_tree = parse_js.parse_js_string(comp, code)
    root = parse_js.js_parse_tree_to_syntax_tree(comp, js_tree)

    builtin.create_builtins(comp, root)

    root.set_bodyparts(bodyparts)

    visitor.check_all_nodes_reachables(comp, root)
    compiler.process_syntax_tree(comp, root)

#    actual = visitor.dump_tree(root)
#    print '\n'.join(actual)

    target = vm.convert_to_zepto_vm_small(comp, root)
    txt = writer.write_text_op_codes(comp, target)
    print '\n'.join(txt)

# temporary entrance
if __name__ == "__main__":
    cProfile.run("main()")
    sys.exit()
