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


from smartanthill_zc import lookup
from smartanthill_zc.node import (ArgumentListNode, ExpressionNode,
                                  expression_type_match, resolve_expression)


class FunctionCallExprNode(ExpressionNode):

    '''
    Node class representing a function call
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionCallExprNode, self).__init__()
        self.txt_name = None
        self.child_argument_list = None

    def set_argument_list(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ArgumentListNode)
        child.set_parent(self)
        self.child_argument_list = child

    def resolve_expr(self, compiler):
        compiler.resolve_node(self.child_argument_list)
        self.set_type(self._declaration.get_type())
        return None


class BodyPartCallExprNode(ExpressionNode):

    '''
    Node class representing a method call
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BodyPartCallExprNode, self).__init__()
        self.txt_bodypart = None
        self.txt_method = None
        self.child_argument_list = None
        self.ref_bodypart_decl = None
        self.ref_method_decl = None

    def set_argument_list(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ArgumentListNode)
        child.set_parent(self)
        self.child_argument_list = child

    def resolve_expr(self, compiler):
        compiler.resolve_node(self.child_argument_list)

        plugin = self.get_root_scope().lookup_plugin(self.txt_bodypart)

        if not plugin:
            compiler.report_error(self.ctx, "Unresolved plug-in name '%s'",
                                  self.txt_bodypart)
            compiler.raise_error()

        method = plugin.lookup_method(self.txt_method)
        if not method:
            compiler.report_error(self.ctx,
                                  "Method '%s' not found at plug-in '%s'" %
                                  (self.txt_method,
                                   self.txt_bodypart))
            compiler.raise_error()

        self.child_argument_list.make_match(compiler,
                                            method.child_parameter_list)

        self.ref_bodypart_decl = plugin
        self.ref_method_decl = method

        self.set_type(self.ref_method_decl.get_type())
        return None

    def get_data_value(self, compiler):
        return self.ref_bodypart_decl.get_data_value(compiler, self)


class MemberAccessExprNode(ExpressionNode):

    '''
    Node class representing a member access, usually a body-part reply
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(MemberAccessExprNode, self).__init__()
        self.txt_member = None
        self.child_expression = None
        self.type_decl = None
        self.member_decl = None

    def set_expression(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

    def resolve_expr(self, compiler):
        resolve_expression(compiler, self, 'child_expression')

        t = self.child_expression.get_type()
        m = t.lookup_member(self.txt_member)
        if not m:
            compiler.report_error(self.ctx, "Member '%s' not found",
                                  self.txt_member)
            compiler.raise_error()

        self.type_decl = t
        self.member_decl = m
        self.set_type(m.get_type())
        return None

    def get_member_field_sequence(self):
        '''
        Creates a field sequence to represent this member
        '''
        return self.member_decl.field_sequence


class NumberLiteralExprNode(ExpressionNode):

    '''
    Node class representing a number literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NumberLiteralExprNode, self).__init__()
        self.txt_literal = None

    def resolve_expr(self, compiler):

        del compiler

        scope = self.get_root_scope()

        self.set_type(scope.lookup_type('_zc_number_literal'))
        return None

    def get_static_value(self):
        '''
        Returns the float value of this literal
        Used for complile-time evaluation of expressions
        TODO check literal for validity
        '''
        return float(self.txt_literal)


class BooleanLiteralExprNode(ExpressionNode):

    '''
    Node class representing a boolean literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BooleanLiteralExprNode, self).__init__()
        self.boolean_value = False

    def resolve_expr(self, compiler):

        del compiler

        scope = self.get_root_scope()
        self.set_type(scope.lookup_type('_zc_boolean_literal'))

        return None

    def get_static_value(self):
        '''
        Returns the float value of this literal
        Used for complile-time evaluation of expressions
        '''
        return self.boolean_value


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

    def set_replaced(self, child):
        '''
        replaced setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_replaced = child

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

    def set_expression(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

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
        self.txt_name = None
        self.ref_decl = None

    def resolve_expr(self, compiler):

        decl = lookup.lookup_variable(self.get_stmt_scope(), self.txt_name)
        if not decl:
            compiler.report_error(
                self.ctx, "Unresolved variable '%s'", self.txt_name)
            compiler.raise_error()

        self.ref_decl = decl

        self.set_type(self.ref_decl.get_type())
        return None


class AssignmentExprNode(ExpressionNode):

    '''
    Node class representing a variable assignment
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(AssignmentExprNode, self).__init__()
        self.txt_name = None
        self.child_rhs = None
        self.ref_decl = None

    def set_rhs(self, child):
        '''
        rhs setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_rhs = child

    def resolve_expr(self, compiler):

        resolve_expression(compiler, self, 'child_rhs')

        decl = lookup.lookup_variable(self.get_stmt_scope(), self.txt_name)
        if not decl:
            compiler.report_error(
                self.ctx, "Unresolved variable '%s'" % self.txt_name)
            compiler.raise_error()

        self.ref_decl = decl
        t = self.ref_decl.get_type()

        if not expression_type_match(compiler, t, self, 'child_rhs'):
            compiler.report_error(
                self.ctx, "Type mismatch on assignment of variable '%s'" %
                self.txt_name)
            # no need to raise here

        self.set_type(self.get_root_scope().lookup_type('_zc_void'))
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
        self.txt_operator = None
        self.child_argument_list = None
        self.ref_decl = None

    def set_argument_list(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ArgumentListNode)
        child.set_parent(self)
        self.child_argument_list = child

    def resolve_expr(self, compiler):
        compiler.resolve_node(self.child_argument_list)
        candidates = self.get_root_scope().lookup_operator(self.txt_operator)

        if len(candidates) == 0:
            compiler.report_error(
                self.ctx, "Unresolved operator '%s'" % self.txt_operator)
            compiler.raise_error()

        self.ref_decl = self.child_argument_list.overload_filter(
            compiler, candidates)
        self.child_argument_list.make_match(
            compiler, self.ref_decl.child_parameter_list)

        self.set_type(self.ref_decl.get_type())
        return self.ref_decl.static_evaluate(compiler, self,
                                             self.child_argument_list)


class LogicOpExprNode(OperatorExprNode):

    '''
    Node class representing a logic operator expression
    '&&', '||' and '!'
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(LogicOpExprNode, self).__init__()


class ArithmeticOpExprNode(OperatorExprNode):

    '''
    Node class representing an arithmetic operator expression
    '+', '-, '*', '/' and '%'
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ArithmeticOpExprNode, self).__init__()


class ComparisonOpExprNode(OperatorExprNode):

    '''
    Node class representing a comparison operator expression
    '<', '>', '<=', '>=', '==' and '!='
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ComparisonOpExprNode, self).__init__()
