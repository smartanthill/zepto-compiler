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

from smartanthill_zc.visitor import NodeWalker, walk_node_childs
from smartanthill_zc.errors import CompilerError
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.ParserRuleContext import ParserRuleContext


class BuiltinCtx(object):

    '''
    This class is used as context on built in code, to allow format_location
    '''

    def __init__(self, text):
        self.text = text


def format_location(ctx):
    '''
    Returns formated string with location in source code of given ctx
    '''

    if isinstance(ctx, BuiltinCtx):
        return ctx.text + ', '
    elif isinstance(ctx, TerminalNodeImpl):  # ctx.symbol is CommonToken
        return 'line %s, ' % str(ctx.symbol.line)
    elif isinstance(ctx, ParserRuleContext):
        if ctx.start.line == ctx.stop.line:
            return 'line %s, ' % str(ctx.start.line)
        else:
            return 'lines %s-%s, ' % (str(ctx.start.line), str(ctx.stop.line))


class Compiler(object):

    '''
    Holds common information about a compilation and
    provides some helper methods
    '''

    BUILTIN = BuiltinCtx('<builtin>')

    def __init__(self):
        '''
        Constructor
        '''
        self.next_node_id = 0
        self.removed_nodes = []
        self.error_flag = False

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

    def get_unique_type_name(self):
        '''
        Returns a unique type name, to be used with types created from
        plug-ins manifests
        '''
        return '_zc_type_' + str(self.next_node_id)

    def resolve_node(self, node):
        '''
        Generic node resolution
        '''
        if node:
            node.resolve(self)

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
            self.raise_error()

    def raise_error(self):
        '''
        Raises CompilerError
        '''
        # pylint: disable=no-self-use
        raise CompilerError()


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
