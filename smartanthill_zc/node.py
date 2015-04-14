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

from smartanthill_zc.lookup import StatementListScope, RootScope,\
    lookup_variable
from smartanthill_zc.errors import CompilerError, ResolutionCycleError,\
    UnresolvedError, PreviousResolutionError, ResolutionError


class _ResolveStatus(object):

    '''
    Enum like class for states of resolution
    '''
    NOT_RESOLVED = 0
    RESOLVING_NOW = 1
    RESOLVED_OK = 2
    RESOLUTION_ERROR = 3


class DeclarationHelper(object):

    '''
    Helper base class used by declarations for resolution
    It provides logic to detect resolution cycles
    '''

    def __init__(self):
        '''
        Never actually called, just let pylint happy
        '''
        self._resolved_flag = _ResolveStatus.NOT_RESOLVED
        self._resolved_type = None

    def resolve(self, compiler):
        '''
        Resolve, will call template method do_resolve_declaration that needs to
        be at implementing class
        '''
        try:
            if self._resolved_flag == _ResolveStatus.NOT_RESOLVED:
                self._resolved_flag = _ResolveStatus.RESOLVING_NOW
                self._resolved_type = self.do_resolve_declaration(compiler)
                assert self._resolved_type
                self._resolved_flag = _ResolveStatus.RESOLVED_OK
            elif self._resolved_flag == _ResolveStatus.RESOLVING_NOW:
                raise ResolutionCycleError()
            elif self._resolved_flag == _ResolveStatus.RESOLVED_OK:
                pass
            elif self.resolved_flag == _ResolveStatus.RESOLUTION_ERROR:
                pass
            else:
                assert False
        except CompilerError:
            self._resolved_flag = _ResolveStatus.RESOLUTION_ERROR
            self._resolved_type = None
            raise

    def get_type(self):
        '''
        Returns the type of this declaration, if resolve was not called before,
        or it did not complete properly, it will raise an error
        '''

        if self._resolved_flag == _ResolveStatus.NOT_RESOLVED:
            raise UnresolvedError()
        elif self._resolved_flag == _ResolveStatus.RESOLVING_NOW:
            raise ResolutionCycleError()
        elif self._resolved_flag == _ResolveStatus.RESOLVED_OK:
            return self._resolved_type
        elif self._resolved_flag == _ResolveStatus.RESOLUTION_ERROR:
            raise PreviousResolutionError()
        else:
            assert False


class Node(object):

    '''
    Base class for all tree nodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._parent = None

    def get_stmt_scope(self):
        ''''
        Walks the tree up until if find an scope to return
        '''
        return self._parent.get_stmt_scope()

    def get_root_scope(self):
        ''''
         Walks the tree up, until a RootScop to return
         '''
        return self._parent.get_root_scope()

    def set_parent(self, parent):
        '''
        helper method for setting node parent
        '''
        self._parent = parent

    def get_parent(self):
        '''
        parent getter
        '''
        assert self._parent
        return self._parent


class StatementNode(Node):

    '''
    Base class for all statements nodes
    '''

    def __init__(self):
        super(StatementNode, self).__init__()

    def resolve_stmt(self, logger):
        pass


class ExpressionNode(Node):

    '''
    Base class for all expressions nodes
    '''

    def __init__(self):
        '''
        Never actually called, just let pylint happy
        '''
        super(ExpressionNode, self).__init__()
        self._resolved_type = None

    def init_expression(self):
        '''
        Constructor
        '''
        self._resolved_type = None

    def set_type(self, resolved_type):
        '''
        Type setter, this method can be called only once.
        So type can not change
        '''

        assert resolved_type
        assert not self._resolved_type

        self._resolved_type = resolved_type

    def get_type(self):
        '''
        Returns the type of this expression
        '''
        assert self._resolved_type

        return self._resolved_type


class RootNode(Node):

    '''
    Root node class used as root of the tree
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(RootNode, self).__init__()
        self.childs_declarations = []
        self.child_statement_list = None
        self._scope = RootScope(self)

#     def get_root(self):
#         ''''
#         Returns this node, since it is a RootNode
#         '''
#         return self

    def get_root_scope(self):
        ''''
         Walks the tree up, until a RootScop to return
         '''
        return self._scope

    def get_stmt_scope(self):
        ''''
        Returns None, since there is no more tree to walk up
        '''
        return None

    def add_declaration(self, node):
        '''
        statement adder
        '''
        node.set_parent(self)
        self.childs_declarations.append(node)

    def set_statement_list(self, child):
        '''
        statement_list setter
        '''
        assert isinstance(child, StatementListStmtNode)
        child.set_parent(self)
        self.child_statement_list = child

    def resolve(self, compiler):
        # First built-ins
        for decl in self.childs_declarations:
            compiler.resolve_node(decl)
        # Next user code
        compiler.resolve_node(self.child_statement_list)


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
        node.set_parent(self)
        self.childs_arguments.append(node)

    def resolve(self, compiler):
        for i in range(len(self.childs_arguments)):
            compiler.resolve_expression_list(self, self.childs_arguments, i)


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
        self._scope = StatementListScope(self)

    def add_statement(self, node):
        '''
        statement adder
        '''
        assert isinstance(node, StatementNode)
        node.set_parent(self)
        self.childs_statements.append(node)

    def resolve(self, compiler):
        for stmt in self.childs_statements:
            compiler.resolve_node(stmt)

    def get_stmt_scope(self):
        ''''
        Returns this node scope
        '''
        return self._scope


class NopStmtNode(StatementNode):

    '''
    Node class representing an empty statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NopStmtNode, self).__init__()


class ErrorStmtNode(StatementNode):

    '''
    Node class representing a syntax error
    Used as a place holder when we can not return a real statement,
    and returning None is neither possible
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ErrorStmtNode, self).__init__()


class ReturnStmtNode(StatementNode):

    '''
    Node class representing 'return' statement
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
        node.set_parent(self)
        self.child_expression = node

    def resolve(self, compiler):
        compiler.resolve_expression(self, 'child_expression')


class VariableDeclarationStmtNode(StatementNode, DeclarationHelper):

    '''
    Node class representing variable declaration statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(VariableDeclarationStmtNode, self).__init__()
        self.ctx_name = None
        self.child_initializer = None

    def set_initializer(self, node):
        '''
        expression setter
        '''
        assert isinstance(node, ExpressionNode)
        node.set_parent(self)
        self.child_initializer = node

    def do_resolve_declaration(self, compiler):

        compiler.resolved_expression(self, 'child_initializer')
        # we are adding variable name after resolution of initializer
        # because we need avoid posible resolution cycle
        self.get_stmt_scope().add_variable(
            compiler, self.ctx_name.getText(), self)

        return self.child_initializer.get_type()


class IfElseStmtNode(StatementNode):

    '''
    Node class representing 'if' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(IfElseStmtNode, self).__init__()
        self.child_expression = None
        self.child_if_branch = None
        self.child_else_branch = None

    def set_expression(self, node):
        '''
        expression setter
        '''
        assert isinstance(node, ExpressionNode)
        node.set_parent(self)
        self.child_expression = node

    def set_if_branch(self, node):
        '''
        if_branch setter
        '''
        assert isinstance(node, StatementListStmtNode)
        node.set_parent(self)
        self.child_if_branch = node

    def set_else_branch(self, node):
        '''
        else_branch setter
        '''
        assert isinstance(node, StatementListStmtNode)
        node.set_parent(self)
        self.child_else_branch = node

    def resolve(self, compiler):
        compiler.resolved_expression(self, 'child_expression')
        compiler.resolve_node(self.child_if_branch)
        compiler.resolve_node(self.child_else_branch)

        # add expression type check


class McuSleepStmtNode(StatementNode):

    '''
    Node class representing 'mcu_sleep' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(McuSleepStmtNode, self).__init__()
        self.child_argument_list = None
        self._declaration = None

    def set_argument_list(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ArgumentListNode)
        node.set_parent(self)
        self.child_argument_list = node

    def resolve(self, compiler):
        compiler.resolve_node(self.child_argument_list)
        decl = self.get_root_scope().lookup_function(
            u'mcu_sleep')
        assert decl
        decl.match_arguments(compiler, self.child_argument_list)

        self._declaration = decl


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
        super(SimpleForStmtNode, self).__init__()
        self.ctx_name = None
        self.child_begin_expression = None
        self.child_end_expression = None
        self.child_statement_list = None
        self._scope = StatementListScope(self)

    def set_begin_expression(self, node):
        '''
        begin_expression setter
        '''
        assert isinstance(node, ExpressionNode)
        node.set_parent(self)
        self.child_begin_expression = node

    def set_end_expression(self, node):
        '''
        end_expression setter
        '''
        assert isinstance(node, ExpressionNode)
        node.set_parent(self)
        self.child_end_expression = node

    def set_statement_list(self, node):
        '''
        statement_list setter
        '''
        assert isinstance(node, StatementListStmtNode)
        node.set_parent(self)
        self.child_statement_list = node

    def get_stmt_scope(self):
        ''''
        Returns this node scope
        '''
        assert self._scope
        return self._scope

    def resolve(self, compiler):
        compiler.resolved_expression(self, 'child_begin_expression')
        compiler.resolved_expression(self, 'child_end_expression')
        compiler.resolve_node(self.child_statement_list)


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
        node.set_parent(self)
        self.child_argument_list = node

    def resolve_expr(self, compiler):
        compiler.resolve_node(self.child_argument_list)
        self.set_type(self._declaration.get_type())
        return None


class MethodCallExprNode(ExpressionNode):

    '''
    Node class representing a method call
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(MethodCallExprNode, self).__init__()
        self.ctx_base_name = None
        self.ctx_name = None
        self.child_argument_list = None
        self._declaration = None

    def set_argument_list(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ArgumentListNode)
        node.set_parent(self)
        self.child_argument_list = node

    def resolve_expr(self, compiler):
        compiler.resolve_node(self.child_argument_list)

        plugin = self.get_root_scope().lookup_plugin(
            compiler, self.ctx_base_name.getText())

        if not plugin:
            compiler.report_error(self.ctx, "Unresolved plug-in '%s'",
                                  self.ctx_base_name.getText())
            raise ResolutionError()

        if self.ctx_name.getText() != u'Execute':
            compiler.report_error(self.ctx, "Plug-in method '%s' not found",
                                  self.ctx_name.getText())
            raise ResolutionError()

        # check arguemnt list
        self._declaration = plugin

        self.set_type(self._declaration.get_type())
        return None


class NumberLiteralExprNode(ExpressionNode):

    '''
    Node class representing a number literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NumberLiteralExprNode, self).__init__()
        self.ctx_literal = None

    def resolve_expr(self, compiler):
        scope = self.get_root_scope()

        self.set_type(scope.lookup_type(u'_zc_number_literal'))
        return None


class VariableExprNode(ExpressionNode):

    '''
    Node class representing a variable use
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(VariableExprNode, self).__init__()
        self.ctx_name = None
        self._declaration = None

    def resolve_expr(self, compiler):

        assert not self._declaration

        decl = lookup_variable(self.get_stmt_scope(), self.ctx_name.getText())
        if not decl:
            compiler.report_error(
                self.ctx, "Unresolved variable '%s'", self.ctx_name.getText())
            raise ResolutionError()

        self._declaration = decl

        self.set_type(self._declaration.get_type())
        return None


class OperatorExprNode(ExpressionNode):

    '''
    Node class representing a operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(OperatorExprNode, self).__init__()
        self.ctx_operator = None
        self.child_argument_list = None
        self._declaration = None

    def set_argument_list(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ArgumentListNode)
        node.set_parent(self)
        self.child_argument_list = node

    def resolve_expr(self, compiler):
        compiler.resolve_node(self.child_argument_list)
        candidates = self.get_root_scope().lookup_operator(
            self.ctx_operator.getText())
        self._declaration = self.child_argument_list.filter(candidates)

        self.set_type(self._declaration.get_type())
        return None
