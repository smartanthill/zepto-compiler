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


def common_test_run(code):
    comp = compiler.Compiler()
    js_tree = compiler.parse_js_string(comp, code)

    comp = compiler.Compiler()
    root = syntax.js_tree_to_syntax_tree(comp, js_tree)
    visitor.check_all_nodes_reachables(comp, root)

    actual = visitor.dump_tree(root)

    return actual


def test_js_simple_return():

    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-ReturnStmtNode",
        "+-+-+-MethodCallExprNode base_name='Some' name='Thing'",
        "+-+-+-+-ArgumentListNode"
    ]

    actual = common_test_run(u'return Some.Thing();')
    assert actual == expected


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
        "+-+-+-+-+-NumberLiteralExprNode literal='15.5'"
    ]

    actual = common_test_run(u'if(i) return 15.5; else {return 0;}')
    assert actual == expected


def test_js_if_without_else():
    common_test_run(u'if(i);')


def test_js_nop():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-NopStmtNode",
        "+-+-NopStmtNode",
        "+-+-NopStmtNode"
    ]

    actual = common_test_run(u';;;')
    assert actual == expected


def test_js_mcu_sleep():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-McuSleepStmtNode",
        "+-+-+-ArgumentListNode",
        "+-+-+-+-NumberLiteralExprNode literal='60'"
    ]

    actual = common_test_run(u'mcu_sleep(60);')
    assert actual == expected


def test_js_var_init():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-VariableDeclarationStmtNode name='i'",
        "+-+-+-NumberLiteralExprNode literal='60'"
    ]

    actual = common_test_run(u'var i = 60;')
    assert actual == expected


def test_js_var_without_init():
    common_test_run(u'var i;')


def test_js_var_multi_raise():
    with pytest.raises(compiler.CompilerError):

        common_test_run(u'var i, j;')


def test_js_expr_multi_raise():
    with pytest.raises(compiler.CompilerError):

        common_test_run(u'if(i, j);')


def test_js_trivial_loop():
    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-SimpleForStmtNode name='i'",
        "+-+-+-NumberLiteralExprNode literal='0'",
        "+-+-+-NumberLiteralExprNode literal='5'",
        "+-+-+-StatementListStmtNode",
        "+-+-+-+-NopStmtNode"
    ]

    actual = common_test_run(u'for(var i = 0; i < 5; i++) ;')
    assert actual == expected


def test_js_trivial_loop_raise1():
    with pytest.raises(compiler.CompilerError):

        common_test_run(u'for(var i = 0; x < 5; i++) ;')


def test_js_trivial_loop_raise2():
    with pytest.raises(compiler.CompilerError):

        common_test_run(u'for(var i = 0; i < 5; x++) ;')


def test_js_binary_operator():

    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-ReturnStmtNode",
        "+-+-+-OperatorExprNode operator='&&'",
        "+-+-+-+-ArgumentListNode",
        "+-+-+-+-+-VariableExprNode name='some'",
        "+-+-+-+-+-VariableExprNode name='other'"
    ]

    actual = common_test_run(u'return some && other;')
    assert actual == expected


def test_js_unary_operator():

    expected = [
        "RootNode",
        "+-StatementListStmtNode",
        "+-+-ReturnStmtNode",
        "+-+-+-OperatorExprNode operator='!'",
        "+-+-+-+-ArgumentListNode",
        "+-+-+-+-+-VariableExprNode name='some'",
    ]

    actual = common_test_run(u'return !some;')
    assert actual == expected


def test_js_unsuported_operator_raise():
    with pytest.raises(compiler.CompilerError):

        common_test_run(u'return some === other;')


def test_js_operator_plus():

    common_test_run(u'return some + other;')


def test_js_operator_modulus():

    common_test_run(u'return some % other;')


def test_js_operator_less_than():

    common_test_run(u'return some < other;')


def test_js_operator_equal():

    common_test_run(u'return some == other;')
