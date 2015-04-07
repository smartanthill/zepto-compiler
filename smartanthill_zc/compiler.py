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
from smartanthill_zc.ECMAScript.ECMAScriptLexer import ECMAScriptLexer
from smartanthill_zc.ECMAScript.ECMAScriptParser import ECMAScriptParser


class CompilerError(Exception):

    '''
    Generic error raised when compilation problem occurs
    '''
    pass


class Compiler(object):

    '''
    Holds common information about a compilation and
    provides some helper methods
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.next_node_id = 0
        self.removed_nodes = []
        self.error_flag = False

    def init_node(self, node):
        '''
        Initializes a node by setting its node_id
        '''
        node.node_id = self.next_node_id
        self.next_node_id += 1
        return node

    def remove_node(self, node):
        '''
        Keeps a record of removed node_id
        '''
        self.removed_nodes.append(node.node_id)

    def reportError(self, fmt, args):
        '''
        Reports an error
        '''
        self.error_flag = True
        print fmt % args

    def raiseError(self, fmt, args):
        '''
        Reports an error and raises CompilerError
        '''
        self.error_flag = True
        print fmt % args
        raise CompilerError()

    def syntaxError(self):
        '''
        Reports an error from the parser,
        currently the parser reports the error itself because I can not make
        Antlr to stop printing to console
        '''
#   print("line " + str(line) + ":" + str(column) + " " + msg, file=sys.stderr)
        self.error_flag = True

    def checkStage(self, name):
        '''
        Raises CompilerError if any error was reported on this stage
        '''
        if self.error_flag:
            print "Stage %s giving up because of previous errors" % name
            raise CompilerError()


class _ProxyAntlrErrorListener(antlr4.error.ErrorListener.ErrorListener):

    '''
    Proxy class that implements antl4 ErrorListener
    used as intermediate of Compiler with antlr4 parser for reporting of errors
    found by the parser
    '''

    def __init__(self, compiler):
        self.compiler = compiler

# pylint: disable=unused-argument
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        '''
        Implements ErrorListener from antlr4
        '''
        self.compiler.syntaxError()


def parse_js_string(compiler, data):
    '''
    Parse unicode string containing java script code
    Returns an antlr parse tree
    '''

    #    input = FileStream(argv[1])
    istream = antlr4.InputStream.InputStream(data)
    lexer = ECMAScriptLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
#    parser.removeErrorListener()
    parser.addErrorListener(_ProxyAntlrErrorListener(compiler))
    tree = parser.program()

    compiler.checkStage('parse_js')

    return tree


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
        self.result = []
        self.stack = []

    def visitChildren(self, node):

        s = '+-' * len(self.stack) + type(node).__name__
        self.stack.append(len(self.result))
        self.result.append(s)

        for i in range(node.getChildCount()):
            node.getChild(i).accept(self)

        self.stack.pop()

    def visitTerminal(self, node):
        self.result[self.stack[-1]] += " '" + node.getText() + "'"
