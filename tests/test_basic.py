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

import pytest

from smartanthill_zc import compiler
from smartanthill_zc import syntax
from smartanthill_zc import visitor


def test_js_simple_return():
    comp = compiler.Compiler()
    parse_tree = compiler.parse_js_string(comp, u'return Some.Thing();')
#    print '\n'.join(compiler.dump_antlr_tree(parse_tree))
    comp = compiler.Compiler()
    root = syntax.ecma_script_parse_tree_to_syntax_tree(comp, parse_tree)
    visitor.check_all_nodes_reachables(comp, root)
 
    actual = visitor.dump_tree(root)
    expected = [
                "RootNode",
                "+-StatementListStmtNode",
                "+-+-ReturnStmtNode",
                "+-+-+-MethodCallExprNode base_name='Some' name='Thing'",
                "+-+-+-+-ArgumentListNode"]
    assert actual == expected

