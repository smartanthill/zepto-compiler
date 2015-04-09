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


class Node(object):

    '''
    Base class for all tree nodes
    '''

    def get_root(self):
        ''''
        Returns the root of the tree
        '''
        assert self.parent
        return self.parent.get_root()

    def set_parent(self, node):
        '''
        helper method for setting node parent
        '''
        node.parent = self


class StatementNode(Node):

    '''
    Base class for all statements nodes
    '''
    pass


class ExpressionNode(Node):

    '''
    Base class for all expressions nodes
    '''
    pass


class RootNode(Node):

    '''
    Root node class used as root of the tree
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.child_statement_list = None

    def get_root(self):
        ''''
        Returns the root of the tree
        '''
        return self

    def set_statement_list(self, node):
        '''
        statement_list setter
        '''
        assert isinstance(node, StatementListStmtNode)
        self.set_parent(node)
        self.child_statement_list = node


class ArgumentListNode(Node):

    '''
    Node class used as container of arguments in function calls
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.childs_arguments = []

    def add_argument(self, node):
        '''
        argument adder
        '''
        assert isinstance(node, ExpressionNode)
        self.set_parent(node)
        self.childs_arguments.append(node)


class StatementListStmtNode(StatementNode):

    '''
    Node class representing an statement list
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.childs_statements = []

    def add_statement(self, node):
        '''
        statement adder
        '''
        assert isinstance(node, StatementNode)
        self.set_parent(node)
        self.childs_statements.append(node)


class NopStmtNode(StatementNode):

    '''
    Node class representing an empty statement
    '''
    pass


class ErrorStmtNode(StatementNode):

    '''
    Node class representing a syntax error
    Used as a place holder when we can not return a real statement,
    and returning None is neither possible
    '''
    pass


class ReturnStmtNode(StatementNode):

    '''
    Node class representing 'return' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.child_expression = None

    def set_expression(self, node):
        '''
        expression setter
        '''
        assert isinstance(node, ExpressionNode)
        self.set_parent(node)
        self.child_expression = node


class VariableDeclarationStmtNode(StatementNode):

    '''
    Node class representing variable declaration statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ctx_name = None
        self.child_expression = None

    def set_expression(self, node):
        '''
        expression setter
        '''
        assert isinstance(node, ExpressionNode)
        self.set_parent(node)
        self.child_expression = node


class IfElseStmtNode(StatementNode):

    '''
    Node class representing 'if' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.child_expression = None
        self.child_if_branch = None
        self.child_else_branch = None

    def set_expression(self, node):
        '''
        expression setter
        '''
        assert isinstance(node, ExpressionNode)
        self.set_parent(node)
        self.child_expression = node

    def set_if_branch(self, node):
        '''
        if_branch setter
        '''
        assert isinstance(node, StatementListStmtNode)
        self.set_parent(node)
        self.child_if_branch = node

    def set_else_branch(self, node):
        '''
        else_branch setter
        '''
        assert isinstance(node, StatementListStmtNode)
        self.set_parent(node)
        self.child_else_branch = node


class McuSleepStmtNode(StatementNode):

    '''
    Node class representing 'mcu_sleep' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.child_argument_list = None

    def set_argument_list(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ArgumentListNode)
        self.set_parent(node)
        self.child_argument_list = node


class SimpleForStmtNode(StatementNode):

    '''
    Node class representing a very simple for loop
    declaring a counter variable, with begin and end as integer constants
    incrementing by one at each loop.

    for(int i = 0; i < *N*; i++) {}
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ctx_name = None
        self.child_begin_expression = None
        self.child_end_expression = None
        self.child_statement_list = None

    def set_begin_expression(self, node):
        '''
        begin_expression setter
        '''
        assert isinstance(node, ExpressionNode)
        self.set_parent(node)
        self.child_begin_expression = node

    def set_end_expression(self, node):
        '''
        end_expression setter
        '''
        assert isinstance(node, ExpressionNode)
        self.set_parent(node)
        self.child_end_expression = node

    def set_statement_list(self, node):
        '''
        statement_list setter
        '''
        assert isinstance(node, StatementListStmtNode)
        self.set_parent(node)
        self.child_statement_list = node


class FunctionCallExprNode(ExpressionNode):

    '''
    Node class representing a function call
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ctx_name = None
        self.child_argument_list = None

    def set_argument_list(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ArgumentListNode)
        self.set_parent(node)
        self.child_argument_list = node


class MethodCallExprNode(ExpressionNode):

    '''
    Node class representing a method call
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ctx_base_name = None
        self.ctx_name = None
        self.child_argument_list = None

    def set_argument_list(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ArgumentListNode)
        self.set_parent(node)
        self.child_argument_list = node


class NumberLiteralExprNode(ExpressionNode):

    '''
    Node class representing a number literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ctx_literal = None


class VariableExprNode(ExpressionNode):

    '''
    Node class representing a variable use
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ctx_name = None


class OperatorExprNode(ExpressionNode):

    '''
    Node class representing a operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ctx_operator = None
        self.child_argument_list = None

    def set_argument_list(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ArgumentListNode)
        self.set_parent(node)
        self.child_argument_list = node
