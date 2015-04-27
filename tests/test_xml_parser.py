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


from smartanthill_zc import parse_xml
from smartanthill_zc import parse_js
from smartanthill_zc.compiler import Compiler
import sys
from smartanthill_zc.antlr_helper import dump_antlr_tree


def test_xml_parse():
    
    code = [u'<?xml version="1.1" ?>',
         u'<smartanthill.plugin name="TemperaturePlugin" version="1.0">',
         u'  <description>Short description here</description>',
         u'  <command>',
         u'    <field name="abc" type="encoded-int&lt;max=2&gt;" />',
         u'  </command>',
         u'  <reply>',
         u'    <field name="xyz" type="encoded-int&lt;max=2&gt;" min="0" max="255">',
         u'      <meaning type="float">',
         u'        <linear-conversion input-point0="0" output-point0="20.0"',
         u'          input-point1="100" output-point1="40.0" />',
         u'      </meaning>',
         u'    </field>',
         u'  </reply>',
         u'  <peripheral>Compiler should ignore this</peripheral>',
         u'</smartanthill.plugin>']
 
 
    code = '\n'.join(code)

    comp = Compiler()
    parse_xml.parse_xml_string(comp, code)

    # Don't assert just check it does not fail


def main():

    code = [u'<?xml version="1.1" ?>',
            u'<smartanthill.plugin name="TemperaturePlugin" version="1.0">',
            u'  <description>Short description here</description>',
            u'  <command>',
            u'    <field name="abc" type="encoded-int&lt;max=2&gt;" />',
            u'  </command>',
            u'  <reply>',
            u'    <field name="xyz" type="encoded-int&lt;max=2&gt;" min="0" max="255">',
            u'      <meaning type="float">',
            u'        <linear-conversion input-point0="0" output-point0="20.0"',
            u'          input-point1="100" output-point1="40.0" />',
            u'      </meaning>',
            u'    </field>',
            u'  </reply>',
            u'  <peripheral>Compiler should ignore this</peripheral>',
            u'</smartanthill.plugin>']

    code = '\n'.join(code)

    comp = Compiler()
    xml_tree = parse_xml.parse_xml_string(comp, code)
    print '\n'.join(dump_antlr_tree(xml_tree))
#    root = parse_js.js_parse_tree_to_syntax_tree(comp, js_tree)

# temporary entrance
if __name__ == "__main__":
    sys.exit(main())
