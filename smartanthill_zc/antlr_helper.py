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


import antlr4.error.ErrorListener
from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl


def get_token_text(compiler, token):
    '''
    Returns the text of a parser token, checking for reserved names,
    and non-ascii characters
    TODO better check and error report for non-ascii
    '''

    txt = str(token.getText())

    if txt.startswith('_zc_'):
        compiler.report_error(token, "Name '%s' and all names starting with "
                              "'_zc_' are reserved" % txt)

    return txt


def get_reference_text(ctx):
    '''
    Returns the text associated with a context
    used only for comment references with source code
    '''
    return str(ctx.getText())


def get_reference_lines(ctx):
    '''
    Returns the line where this node was found
    used only for comment references with source code
    '''
    if isinstance(ctx, TerminalNodeImpl):  # ctx.symbol is CommonToken
        return (ctx.symbol.line, ctx.symbol.line)
    elif isinstance(ctx, ParserRuleContext):
        return (ctx.start.line, ctx.stop.line)
    else:
        return (0, 0)


class _ProxyAntlrErrorListener(antlr4.error.ErrorListener.ErrorListener):

    '''
    Proxy class that implements antl4 ErrorListener
    used as intermediate of Compiler with antlr4 parser for reporting of errors
    found by the parser
    '''

    def __init__(self, compiler):
        '''
        Constructor
        '''
        self._compiler = compiler

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        '''
        Implements ErrorListener from antlr4
        '''
        # pylint: disable=unused-argument
        self._compiler.syntax_error()


def dump_antlr_tree(tree):
    '''
    Dump an AntLr parse tree to a human readable text format
    Used for debugging and testing
    '''
    antlr_visitor = _DumpAntlrTreeVisitor()
    antlr_visitor.visit(tree)
    return antlr_visitor.result


class _DumpAntlrTreeVisitor(antlr4.ParseTreeVisitor):

    '''
    AntLr tree visitor class used by dump_antlr_tree function
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.result = []
        self.stack = []

    def visitChildren(self, node):
        '''
        Overrides antlr4.ParseTreeVisitor method
        '''
        s = '+-' * len(self.stack) + type(node).__name__
        self.stack.append(len(self.result))
        self.result.append(s)

        for i in range(node.getChildCount()):
            node.getChild(i).accept(self)

        self.stack.pop()

    def visitTerminal(self, node):
        '''
        Overrides antlr4.ParseTreeVisitor method
        '''
        self.result[self.stack[-1]] += " '" + node.getText() + "'"
