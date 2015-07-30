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
from smartanthill_zc import errors, parse_js, visitor
from smartanthill_zc.compiler import Ctx, Compiler
from smartanthill_zc.root import RootNode


def common_test_run(code):
    comp = Compiler()
    root = comp.init_node(RootNode(), Ctx.ROOT)

    js_tree = parse_js.parse_js_string(comp, code)
    source = parse_js.js_parse_tree_to_syntax_tree(comp, js_tree)
    root.set_source_program(source)

    visitor.check_all_nodes_reachables(comp, root)

    actual = visitor.dump_tree(root)

    return actual


def test_js_simple_return():

    expected = [
        "RootNode",
        "+-SourceProgramNode",
        "+-+-StmtListNode",
        "+-+-+-ReturnStmtNode",
        "+-+-+-+-BodyPartCallExprNode bodypart='Some' method='Thing'",
        "+-+-+-+-+-ArgumentListNode"
    ]

    actual = common_test_run(u'return Some.Thing();')
    assert actual == expected


def test_js_if_else():
    expected = [
        "RootNode",
        "+-SourceProgramNode",
        "+-+-StmtListNode",
        "+-+-+-IfElseStmtNode",
        "+-+-+-+-StmtListNode",
        "+-+-+-+-+-ReturnStmtNode",
        "+-+-+-+-+-+-NumberLiteralExprNode literal='0'",
        "+-+-+-+-VariableExprNode name='i'",
        "+-+-+-+-StmtListNode",
        "+-+-+-+-+-ReturnStmtNode",
        "+-+-+-+-+-+-NumberLiteralExprNode literal='15.5'"
    ]

    actual = common_test_run(u'if(i) return 15.5; else {return 0;}')
    assert actual == expected


def test_js_if_without_else():
    common_test_run(u'if(i);')


def test_js_nop():
    expected = [
        "RootNode",
        "+-SourceProgramNode",
        "+-+-StmtListNode",
        "+-+-+-NopStmtNode",
        "+-+-+-NopStmtNode",
        "+-+-+-NopStmtNode"
    ]

    actual = common_test_run(u';;;')
    assert actual == expected


def test_js_mcu_sleep():
    expected = [
        "RootNode",
        "+-SourceProgramNode",
        "+-+-StmtListNode",
        "+-+-+-McuSleepStmtNode",
        "+-+-+-+-ArgumentListNode",
        "+-+-+-+-+-NumberLiteralExprNode literal='60'"
    ]

    actual = common_test_run(u'mcu_sleep(60);')
    assert actual == expected


def test_js_var_init():
    expected = [
        "RootNode",
        "+-SourceProgramNode",
        "+-+-StmtListNode",
        "+-+-+-VariableDeclarationStmtNode name='i'",
        "+-+-+-+-NumberLiteralExprNode literal='60'"
    ]

    actual = common_test_run(u'var i = 60;')
    assert actual == expected


def test_js_var_without_init():
    common_test_run(u'var i;')


def test_js_var_multi_raise():
    with pytest.raises(errors.CompilerError):

        common_test_run(u'var i, j;')


def test_js_expr_multi_raise():
    with pytest.raises(errors.CompilerError):

        common_test_run(u'if(i, j);')


def test_js_trivial_loop():
    expected = [
        "RootNode",
        "+-SourceProgramNode",
        "+-+-StmtListNode",
        "+-+-+-SimpleForStmtNode name='i'",
        "+-+-+-+-NumberLiteralExprNode literal='0'",
        "+-+-+-+-NumberLiteralExprNode literal='5'",
        "+-+-+-+-StmtListNode",
        "+-+-+-+-+-NopStmtNode"
    ]

    actual = common_test_run(u'for(var i = 0; i < 5; i++) ;')
    assert actual == expected


def test_js_trivial_loop_raise1():
    with pytest.raises(errors.CompilerError):

        common_test_run(u'for(var i = 0; x < 5; i++) ;')


def test_js_trivial_loop_raise2():
    with pytest.raises(errors.CompilerError):

        common_test_run(u'for(var i = 0; i < 5; x++) ;')


def test_js_binary_operator():

    expected = [
        "RootNode",
        "+-SourceProgramNode",
        "+-+-StmtListNode",
        "+-+-+-ReturnStmtNode",
        "+-+-+-+-LogicOpExprNode operator='&&'",
        "+-+-+-+-+-ArgumentListNode",
        "+-+-+-+-+-+-VariableExprNode name='some'",
        "+-+-+-+-+-+-VariableExprNode name='other'"
    ]

    actual = common_test_run(u'return some && other;')
    assert actual == expected


def test_js_unary_operator():

    expected = [
        "RootNode",
        "+-SourceProgramNode",
        "+-+-StmtListNode",
        "+-+-+-ReturnStmtNode",
        "+-+-+-+-LogicOpExprNode operator='!'",
        "+-+-+-+-+-ArgumentListNode",
        "+-+-+-+-+-+-VariableExprNode name='some'",
    ]

    actual = common_test_run(u'return !some;')
    assert actual == expected


def test_js_unsuported_operator_raise():
    with pytest.raises(errors.CompilerError):

        common_test_run(u'return some === other;')


def test_js_operator_plus():

    common_test_run(u'return some + other;')


def test_js_operator_modulus():

    common_test_run(u'return some % other;')


def test_js_operator_less_than():

    common_test_run(u'return some < other;')


def test_js_operator_equal():

    common_test_run(u'return some == other;')


def test_js_empty_array_raises():
    with pytest.raises(errors.CompilerError):

        common_test_run(u'return [];')
