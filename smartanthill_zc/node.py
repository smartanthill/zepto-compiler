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
        super(DeclarationHelper, self).__init__()
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
        super(Node, self).__init__()
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

    def resolve_expr(self, compiler):
        '''
        Base implementation of expression resolution template method
        Must be overrided or resolution type must be externally assigned
        '''
        del compiler

        self.assert_resolved()
        return None

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

    def assert_resolved(self):
        '''
        Asserts this instance has a resolved type
        '''
        assert self._resolved_type

    def get_static_value(self):
        # pylint: disable=no-self-use
        return None


class TypeDeclNode(Node):

    '''
    Base class for types
    '''

    NO_MATCH = 0
    EXACT_MATCH = 1
    CAST_MATCH = 2

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(TypeDeclNode, self).__init__()
        self.str_type_name = type_name
        self._resolved = False

    def resolve(self, compiler):
        '''
        Resolve
        '''
        assert not self._resolved
        self.get_root_scope().add_type(compiler, self.str_type_name, self)
        self._resolved = True

    def can_initialize(self, rhs):
        '''
        Returns true if an instance of this type can be initialized with rhs
        Base implementation returns true if both types are the same instance,
        otherwise false
        '''
        if self == rhs:
            return self.EXACT_MATCH
        else:
            return self.NO_MATCH

    def insert_cast(self, compiler, rhs_expr):
        '''
        Base method for cast insertion
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument

        assert False

    def lookup_member(self, name):
        '''
        Base method for type member look up
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument

        return None


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

    def overload_filter(self, compiler, decl_list):
        '''
        From a list declarations, returns one that can match the arguments,
        if no candidate is found, reports error an raises
        '''
        exact_match = []
        cast_match = []
        for current in decl_list:
            r = self.can_match(current.child_parameter_list)

            if r == TypeDeclNode.NO_MATCH:
                pass
            elif r == TypeDeclNode.EXACT_MATCH:
                exact_match.append(current)
            elif r == TypeDeclNode.CAST_MATCH:
                cast_match.append(current)
            else:
                assert False

        if len(exact_match) == 1:
            return exact_match[0]
        elif len(exact_match) == 0:
            if len(cast_match) == 1:
                self.make_match(compiler, cast_match[0].child_parameter_list)
                return cast_match[0]
            elif len(cast_match) == 0:
                compiler.report_error(
                    self.ctx, "None of candidates can match the arguments")
                raise ResolutionError()
            elif len(cast_match) > 1:
                compiler.report_error(
                    self.ctx, "More than a candidate can match the arguments")
                raise ResolutionError()
            else:
                assert False
        else:
            assert False

    def can_match(self, decl):
        '''
        If this argument list can not used to initialize given argument list
        Returns TypeDeclNode.NO_MATCH when there is no chance to make it match
        TypeDeclNode.EXACT_MATCH when match does not need any cast
        and TypeDeclNode.CAST_MATCH when it can match but casting needed
        '''
        if len(self.childs_arguments) != decl.get_size():
            return TypeDeclNode.NO_MATCH

        result = TypeDeclNode.EXACT_MATCH
        for i in range(len(self.childs_arguments)):
            t = decl.get_type_at(i)
            r = t.can_initialize(self.childs_arguments[i].get_type())

            if r == TypeDeclNode.NO_MATCH:
                return TypeDeclNode.NO_MATCH
            elif r == TypeDeclNode.EXACT_MATCH:
                pass
            elif r == TypeDeclNode.CAST_MATCH:
                result = TypeDeclNode.CAST_MATCH
            else:
                assert False

        return result

    def make_match(self, compiler, decl):
        '''
        Makes this argument list to initialize given declaration,
        inserting casts if required.
        '''

        if len(self.childs_arguments) != decl.get_size():
            compiler.report_error(
                self.ctx, "Wrong number of arguments, given %s but need %s" %
                str(decl.get_size()), str(len(self.childs_arguments)))
            raise ResolutionError()

        for i in range(len(self.childs_arguments)):
            t = decl.get_type_at(i)
            r = t.can_initialize(self.childs_arguments[i].get_type())

            if r == TypeDeclNode.NO_MATCH:
                compiler.report_error(
                    self.ctx, "Argument type mismatch at position %s" & str(i))
                raise ResolutionError()
            elif r == TypeDeclNode.EXACT_MATCH:
                pass
            elif r == TypeDeclNode.CAST_MATCH:
                e = t.insert_cast(compiler, self.childs_arguments[i])
                e.set_parent(self)
                self.childs_arguments[i] = e
            else:
                assert False


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
        if not node:
            assert False
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

        compiler.resolve_expression(self, 'child_initializer')
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
        compiler.resolve_expression(self, 'child_expression')
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
        assert decl  # is built in function

        self.child_argument_list.make_match(compiler,
                                            decl.child_parameter_list)

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
        compiler.resolve_expression(self, 'child_begin_expression')
        compiler.resolve_expression(self, 'child_end_expression')
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
        self._plugin_declaration = None
        self._method_declaration = None

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
            self.ctx_base_name.getText())

        if not plugin:
            compiler.report_error(self.ctx, "Unresolved plug-in '%s'",
                                  self.ctx_base_name.getText())
            raise ResolutionError()

        method = plugin.lookup_method(self.ctx_name.getText())
        if not method:
            compiler.report_error(self.ctx,
                                  "Method '%s' not found at plug-in '%s'" %
                                  (self.ctx_name.getText(),
                                   self.ctx_base_name.getText()))
            raise ResolutionError()

        self.child_argument_list.make_match(compiler,
                                            method.child_parameter_list)

        self._plugin_declaration = plugin
        self._method_declaration = method

        self.set_type(self._method_declaration.get_type())
        return None


class MemberAccessExprNode(ExpressionNode):

    '''
    Node class representing a method call
    '''

    def __init__(self, member_name):
        '''
        Constructor
        '''
        super(MemberAccessExprNode, self).__init__()
        self.txt_member_name = member_name
        self.child_expression = None

    def set_expression(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ExpressionNode)
        node.set_parent(self)
        self.child_expression = node

    def resolve_expr(self, compiler):
        compiler.resolve_expression(self, 'child_expression')

        t = self.child_expression.get_type()
        m = t.lookup_member_type(self.txt_member_name.getText())
        if not m:
            compiler.report_error(self.ctx, "Member '%s' not found",
                                  self.txt_member_name.getText())
            raise ResolutionError()

        self.set_type(m)
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

        del compiler

        scope = self.get_root_scope()

        self.set_type(scope.lookup_type(u'_zc_number_literal'))
        return None

    def get_static_value(self):
        '''
        Returns the float value of this literal
        Used for complile-time evaluation of expressions
        '''
        return float(self.ctx_literal.getText())


class StaticEvaluatedExprNode(ExpressionNode):

    '''
    Node class representing an statically (compile-time) evaluated expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StaticEvaluatedExprNode, self).__init__()
        self.child_replaced = None
        self._static_value = None

    def set_replaced(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ExpressionNode)
        node.set_parent(self)
        self.child_replaced = node

    def set_static_value(self, static_value):
        '''
        Value setter
        Sets the evaluated value for the replaced expression
        '''
        self._static_value = static_value

    def get_static_value(self):
        '''
        Value getter
        '''
        return self._static_value


class LiteralCastExprNode(ExpressionNode):

    '''
    Node class representing an automatic cast from literal to non-literal type
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(LiteralCastExprNode, self).__init__()
        self.child_expression = None

    def set_expression(self, node):
        '''
        argument_list setter
        '''
        assert isinstance(node, ExpressionNode)
        node.set_parent(self)
        self.child_expression = node

    def get_static_value(self):
        return self.child_expression.get_static_value()


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

        if len(candidates) == 0:
            compiler.report_error(
                self.ctx, "Unresolved operator '%s'" %
                self.ctx_operator.getText())
            raise ResolutionError()

        self._declaration = self.child_argument_list.overload_filter(
            compiler, candidates)

        self.set_type(self._declaration.get_type())
        return self._declaration.static_evaluate(compiler, self,
                                                 self.child_argument_list)
