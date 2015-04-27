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
from smartanthill_zc import parse_js
from smartanthill_zc.errors import CompilerError
from smartanthill_zc.antlr_helper import dump_antlr_tree


def test_js_simple_return():
    comp = compiler.Compiler()
    js_tree = parse_js.parse_js_string(comp, u'return Some.Thing();')
    actual = dump_antlr_tree(js_tree)
    expected = [
        "ProgramContext '<EOF>'",
        "+-SourceElementsContext",
        "+-+-SourceElementContext",
        "+-+-+-StatementContext",
        "+-+-+-+-ReturnStatementContext 'return'",
        "+-+-+-+-+-ExpressionSequenceContext",
        "+-+-+-+-+-+-MethodExpressionContext 'Some' '.'",
        "+-+-+-+-+-+-+-IdentifierNameContext 'Thing'",
        "+-+-+-+-+-+-+-ArgumentsContext '(' ')'",
        "+-+-+-+-+-EosContext ';'"]
    assert actual == expected


def test_js_unsuported_grammar():
    with pytest.raises(CompilerError):
        comp = compiler.Compiler()
        parse_js.parse_js_string(comp, u'function problem() {;}')

