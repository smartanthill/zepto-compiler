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


def common_test_run(code, expected):
    comp = compiler.Compiler()
    js_tree = compiler.parse_js_string(comp, code)

    comp = compiler.Compiler()
    root = syntax.js_tree_to_syntax_tree(comp, js_tree)
    visitor.check_all_nodes_reachables(comp, root)

    actual = visitor.dump_tree(root)

    assert actual == expected


def test_js_simple_return():

    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-ReturnStmtNode",
        "+-+-+-MethodCallExprNode base_name='Some' name='Thing'",
        "+-+-+-+-ArgumentListNode"]

    common_test_run(u'return Some.Thing();', expected)


def test_js_if():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-IfElseStmtNode",
        "+-+-+-VariableExprNode name='i'",
        "+-+-+-StatementListStmtNode",
        "+-+-+-+-NopStmtNode"]

    common_test_run(u'if(i);', expected)


def test_js_if_else():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-IfElseStmtNode",
        "+-+-+-StatementListStmtNode",
        "+-+-+-+-ReturnStmtNode",
        "+-+-+-+-+-NumberLiteralExprNode literal='0'",
        "+-+-+-VariableExprNode name='i'",
        "+-+-+-StatementListStmtNode",
        "+-+-+-+-ReturnStmtNode",
        "+-+-+-+-+-NumberLiteralExprNode literal='15.5'"]

    common_test_run(u'if(i) return 15.5; else {return 0;}', expected)


def test_js_nop():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-NopStmtNode",
        "+-+-NopStmtNode",
        "+-+-NopStmtNode"]

    common_test_run(u';;;', expected)


def test_js_mcu_sleep():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-McuSleepStmtNode",
        "+-+-+-ArgumentListNode",
        "+-+-+-+-NumberLiteralExprNode literal='60'"]

    common_test_run(u'mcu_sleep(60);', expected)


def test_js_var():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-VariableDeclarationStmtNode name='i'"]

    common_test_run(u'var i;', expected)


def test_js_var_init():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-VariableDeclarationStmtNode name='i'",
        "+-+-+-NumberLiteralExprNode literal='60'"]

    common_test_run(u'var i = 60;', expected)


def test_js_var_multi_raise():
    with pytest.raises(compiler.CompilerError):

        common_test_run(u'var i, j;', [])


def test_js_expr_multi_raise():
    with pytest.raises(compiler.CompilerError):

        common_test_run(u'if(i, j);', [])


def test_js_trivial_loop():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-SimpleForStmtNode name='i'",
        "+-+-+-NumberLiteralExprNode literal='0'",
        "+-+-+-NumberLiteralExprNode literal='5'",
        "+-+-+-StatementListStmtNode",
        "+-+-+-+-NopStmtNode"]

    common_test_run(u'for(var i = 0; i < 5; i++) ;', expected)


def test_js_trivial_loop_raise1():
    with pytest.raises(compiler.CompilerError):

        common_test_run(u'for(var i = 0; x < 5; i++) ;', [])


def test_js_trivial_loop_raise2():
    with pytest.raises(compiler.CompilerError):

        common_test_run(u'for(var i = 0; i < 5; x++) ;', [])
