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

from smartanthill_zc.lookup import ReturnStmtScope, RootScope,\
    StatementListScope
from smartanthill_zc.node import Node, DeclarationListNode,\
    StmtListNode


class SourceProgramNode(Node):

    '''
    Node class container of a program, similar to a function but
    without parameters
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(SourceProgramNode, self).__init__()
        self.child_statement_list = None
        self._return_scope = ReturnStmtScope(self)

    def set_statement_list(self, child):
        '''
        statement list setter
        '''
        assert isinstance(child, StmtListNode)
        child.set_parent(self)
        self.child_statement_list = child

    def get_scope(self, kind):
        ''''
        Since we don't currently support a function node, RootNode will
        make its job as ReturnStmtScope
        else returns None, do not try to further walk up
        '''
        if kind == ReturnStmtScope:
            return self._return_scope
        elif kind == StatementListScope:
            return None
        else:
            return super(SourceProgramNode, self).get_scope(kind)

    def resolve(self, compiler):
        compiler.resolve_node(self.child_statement_list)


class RootNode(Node):

    '''
    Root node class used as root of the tree
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(RootNode, self).__init__()
        self.child_builtins = None
        self.child_bodyparts = None
        self.child_parameters = None
        self.child_source_program = None
        self._root_scope = RootScope(self)

    def set_builtins(self, child):
        '''
        built-ins setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_builtins = child

    def set_bodyparts(self, child):
        '''
        body-parts setter
        '''
        assert isinstance(child, Node)
        child.set_parent(self)
        self.child_bodyparts = child

    def set_parameters(self, child):
        '''
        parameters setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_parameters = child

    def set_source_program(self, child):
        '''
        program setter
        '''
        assert isinstance(child, SourceProgramNode)
        child.set_parent(self)
        self.child_source_program = child

    def resolve(self, compiler):
        # First built-ins
        compiler.resolve_node(self.child_builtins)
        # Next body-parts and parameters
        compiler.resolve_node(self.child_bodyparts)
        compiler.resolve_node(self.child_parameters)
        # Last user code
        compiler.resolve_node(self.child_source_program)

    def get_scope(self, kind):
        ''''
        Since we don't currently support a function node, RootNode will
        make its job as ReturnStmtScope
        else returns None, do not try to further walk up
        '''
        if kind == RootScope:
            return self._root_scope
        else:
            return super(RootNode, self).get_scope(kind)
