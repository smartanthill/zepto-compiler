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

from smartanthill_zc import compiler
from smartanthill_zc import parse_js
from smartanthill_zc import visitor
from smartanthill_zc import builtin
from smartanthill_zc.vm import convert_to_zepto_vm_one
from smartanthill_zc.writter import write_text_op_codes
from smartanthill_zc.compiler import Compiler


def main():

#     code = (u'for (var i = 0; i < 5; i++) {'
#             u'  var temp = TemperatureSensor.Execute();'
#             u'  if (temp.Temperature < 36.0 || temp.Temperature > 38.9)'
#             u'    return temp;'
#
#             u'  mcu_sleep(5*60);'
#             u'}'
#             u'return TemperatureSensor.Execute();')


    code = u'mcu_sleep(5*60);\n return TemperatureSensor.Execute();'
    comp = Compiler()
    js_tree = parse_js.parse_js_string(comp, code)
    print '\n'.join(parse_js.dump_antlr_tree(js_tree))
    root = parse_js.js_parse_tree_to_syntax_tree(comp, js_tree)

    builtin.create_builtins(comp, root)
    visitor.check_all_nodes_reachables(comp, root)
    compiler.process_syntax_tree(comp, root)

    print '\n'.join(visitor.dump_tree(root))

    convert_to_zepto_vm_one(comp, root)

    print '\n'.join(write_text_op_codes(comp, root.child_op_list))

# temporary entrance
if __name__ == "__main__":
    sys.exit(main())
