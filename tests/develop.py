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

import sys

from smartanthill_zc import builtin
from smartanthill_zc import compiler, parse_xml
from smartanthill_zc import parse_js
from smartanthill_zc import visitor
from smartanthill_zc.compiler import Compiler
from smartanthill_zc.vm import convert_to_zepto_vm_one, convert_to_zepto_vm_tiny
from smartanthill_zc.writer import write_text_op_codes


def main():

    #     code = [u'for (var i = 0; i < 5; i++) {'
    #             u'  var temp = TemperatureSensor.Execute();'
    #             u'  if (temp.Temperature < 36.0 || temp.Temperature > 38.9)'
    #             u'    return temp;'
    #
    #             u'  mcu_sleep(5*60);'
    #             u'}'
    #             u'return TemperatureSensor.Execute();']
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
    comp = Compiler()

    bodyparts = parse_xml.parse_xml_body_parts(comp, xml)
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

    target = convert_to_zepto_vm_tiny(comp, root)
    txt = write_text_op_codes(comp, target)
    print '\n'.join(txt)

# temporary entrance
if __name__ == "__main__":
    sys.exit(main())
