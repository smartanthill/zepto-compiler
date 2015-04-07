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

    _node_id = 0
    
    def __init__(self):
        '''
        Constructor
        '''
        self.node_id = Node._node_id
        Node._node_id += 1
        self.parent = None

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
    def __init__(self):
        '''
        Constructor
        '''
        super(StatementNode, self).__init__()

class ExpressionNode(Node):
    '''
    Base class for all expressions nodes
    '''
    def __init__(self):
        '''
        Constructor
        '''
        super(ExpressionNode, self).__init__()


class RootNode(Node):
    '''
    Root node class used as root of the tree
    '''
    def __init__(self):
        '''
        Constructor
        '''
        super(RootNode, self).__init__()
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
        super(ArgumentListNode, self).__init__()
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
        super(StatementListStmtNode, self).__init__()
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
    def __init__(self):
        '''
        Constructor
        '''
        super(NopStmtNode, self).__init__()
    

class ReturnStmtNode(StatementNode):
    '''
    Node class representing a return statement with expression
    '''
    def __init__(self):
        '''
        Constructor
        '''
        super(ReturnStmtNode, self).__init__()
        self.child_expression = None
        
    def set_expression(self, node):
        '''
        expression setter
        '''
        assert isinstance(node, ExpressionNode)
        self.set_parent(node)
        self.child_expression = node


class FunctionCallExprNode(ExpressionNode):
    '''
    Node class representing a function call
    '''
    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionCallExprNode, self).__init__()
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
        super(MethodCallExprNode, self).__init__()
        self.base_name = None
        self.name = None
        self.child_argument_list = None

    def set_argument_list(self, node):
        '''
        argument_list setter  
        '''
        assert isinstance(node, ArgumentListNode)
        self.set_parent(node)
        self.child_argument_list = node
