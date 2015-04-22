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

from smartanthill_zc import compiler, parse_js, builtin, vm, writter, visitor

def common_test_run(code):
    
    code = '\n'.join(code)
    
    comp = compiler.Compiler()
    js_tree = parse_js.parse_js_string(comp, code)

    root = parse_js.js_parse_tree_to_syntax_tree(comp, js_tree)

    builtin.create_builtins(comp, root)
    visitor.check_all_nodes_reachables(comp, root)
    compiler.process_syntax_tree(comp, root)


    vm.convert_to_zepto_vm_one(comp, root)

    return writter.write_text_op_codes(comp, root.child_op_list)


def test_js_pattern_1():

    code = [u'return TemperatureSensor.Execute();']

    out = ['ZEPTOVM_OP_EXEC|0x44|0x00',
           'ZEPTOVM_OP_EXIT|0x02']

    assert common_test_run(code) == out
    
def test_js_pattern_2():

    code = [u'mcu_sleep(5*60);',
            u'return TemperatureSensor.Execute();']

    out = ['ZEPTOVM_OP_MCUSLEEP|0x812c|0x00',
           'ZEPTOVM_OP_EXEC|0x44|0x00',
           'ZEPTOVM_OP_EXIT|0x02']

    assert common_test_run(code) == out
    


