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
from smartanthill_zc.node import ExpressionNode
from smartanthill_zc.visitor import NodeWalker, walk_node_childs
from smartanthill_zc.errors import CompilerError, format_location


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
        self._replacement = None

    def init_node(self, node, ctx):
        '''
        Initializes a node by setting its node_id
        '''
        node.node_id = self.next_node_id
        self.next_node_id += 1
        node.ctx = ctx
        return node

    def remove_node(self, node):
        '''
        Keeps a record of removed node_id
        Later checks may try to verify no refereces are kept
        '''
        self.removed_nodes.append(node.node_id)

    def replace_self(self, node):
        '''
        Helper method used at resolution for node replacement
        '''
        self._replacement = node

    def resolve_node(self, node):
        '''
        Generic node resolution
        '''

        node.resolve(self)

    def resolve_expression(self, parent, child_name):
        '''
        Resolve child expression by attribute name, to allow expression
        replacement
        '''

        expr = getattr(parent, child_name)
        if expr:
            replacement = expr.resolve_expr(self)
            if replacement:
                assert isinstance(replacement, ExpressionNode)
                replacement.set_parent(parent)
                setattr(parent, child_name, self._replacement)

                # resolve again (replacement)
                self.resolve_expression(parent, child_name)
            else:
                expr.get_type()  # has assert inside get_type

    def resolve_expression_list(self, parent, expr_list, i):
        '''
        Resolve child expression list by index, to allow expression
        replacement
        '''
        replacement = expr_list[i].resolve_expr(self)

        if replacement:
            assert isinstance(replacement, ExpressionNode)
            replacement .set_parent(parent)
            expr_list[i] = replacement

            # resolve again (replacement)
            self.resolve_expression_list(parent, expr_list, i)
        else:
            expr_list[i].get_type()

    def report_error(self, ctx, fmt, args=None):
        '''
        Reports an error
        '''
        self.error_flag = True
        if args:
            print format_location(ctx) + fmt % args
        else:
            print format_location(ctx) + fmt

    def syntax_error(self):
        '''
        Reports an error from the parser,
        currently the parser reports the error itself because I can not make
        Antlr to stop printing to console
        '''
#   print("line " + str(line) + ":" + str(column) + " " + msg, file=sys.stderr)
        self.error_flag = True

    def check_stage(self, name):
        '''
        Raises CompilerError if any error was reported on this stage
        '''
        if self.error_flag:
            print "Stage '%s' giving up" % name
            raise CompilerError()


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
        self.compiler = compiler

# pylint: disable=unused-argument
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        '''
        Implements ErrorListener from antlr4
        '''
        self.compiler.syntax_error()


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

    compiler.check_stage('parse_js')

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


def process_syntax_tree(compiler, root):
    '''
    Process a syntax tree, doing all lookup tables, resolution,
    and type checks required
    After this function the tree is fully resolved and ready for intermediate
    code generation
    Resolution of the tree may trigger node replacements,
    and other modifications of the tree, as semantic meaning is needed
    '''

    compiler.resolve_node(root)
    compiler.check_stage('resolve')

    walker = _ResolutionCheckWalker()
    walker.walk_node(root)


class _ResolutionCheckWalker(NodeWalker):

    '''
    Walker class that will check all reachable nodes do not raise when
    get_type() is called and that something is returned
    '''

    def walk_node(self, node):
        assert node
        try:
            m = getattr(node, 'get_type')
            if m:
                t = m()
                if not t:
                    print type(node)
                    assert False
        except AttributeError:
            pass

        walk_node_childs(self, node)
