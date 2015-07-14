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

import math

from smartanthill_zc import encode, expression
from smartanthill_zc.encode import Encoding
from smartanthill_zc.node import (ArgumentListNode, DeclarationListNode,
                                  ExpressionNode, Node, ResolutionHelper,
                                  TypeDeclNode)


def create_builtins(compiler, root):
    '''
    Creates all built in nodes and adds them to the root
    '''

    ctx = compiler.BUILTIN

    decls = compiler.init_node(DeclarationListNode(), ctx)
    decls.add_declaration(
        compiler.init_node(VoidTypeDeclNode('_zc_void'), ctx))

    num_t = compiler.init_node(NumberTypeDeclNode('_zc_number'), ctx)
    decls.add_declaration(num_t)

    decls.add_declaration(
        compiler.init_node(LiteralTypeDeclNode('_zc_number_literal', num_t),
                           ctx))

    bool_t = compiler.init_node(BasicTypeDeclNode('_zc_boolean'), ctx)
    decls.add_declaration(bool_t)

    decls.add_declaration(
        compiler.init_node(LiteralTypeDeclNode('_zc_boolean_literal', bool_t),
                           ctx))

    mcu = compiler.init_node(McuSleepDeclNode(), ctx)
    mcu.set_parameter_list(
        create_parameter_list(compiler, ctx, ['_zc_number_literal']))
    decls.add_declaration(mcu)

    # unary
    _create_literal_operators(compiler, ctx, decls, ['+', '-'],
                              '_zc_number_literal',
                              ['_zc_number_literal'])

    _create_literal_operators(compiler, ctx, decls,
                              ['!'],
                              '_zc_boolean_literal',
                              ['_zc_boolean_literal'])

    # binary
    _create_literal_operators(compiler, ctx, decls, ['+', '-', '*', '/', '%'],
                              '_zc_number_literal',
                              ['_zc_number_literal', '_zc_number_literal'])

    _create_literal_operators(compiler, ctx, decls,
                              ['<', '>', '<=', '>=', '==', '!='],
                              '_zc_boolean_literal',
                              ['_zc_number_literal', '_zc_number_literal'])

    _create_literal_operators(compiler, ctx, decls,
                              ['&&', '||', '==', '!='],
                              '_zc_boolean_literal',
                              ['_zc_boolean_literal', '_zc_boolean_literal'])

    # logic with one boolean literal

    _create_logic_literal_ops(compiler, ctx, decls,
                              ['&&', '||'],
                              '_zc_boolean',
                              ['_zc_boolean', '_zc_boolean_literal'])

    _create_logic_literal_ops(compiler, ctx, decls,
                              ['&&', '||'],
                              '_zc_boolean',
                              ['_zc_boolean_literal', '_zc_boolean'])

    _create_number_to_literal_comparison(compiler, ctx, decls,
                                         ['<', '>', '<=', '>=', '==', '!='])

    # unary
    _create_operators(compiler, ctx, decls, ['+', '-'],
                      '_zc_number', ['_zc_number'])
    # binary
    _create_operators(compiler, ctx, decls, ['+', '-', '*', '/'],
                      '_zc_number', ['_zc_number', '_zc_number'])

    # number comparison
    _create_number_to_number_comparison(
        compiler, ctx, decls, ['<', '>', '<=', '>=', '==', '!='])

    # boolean comparison
    _create_operators(compiler, ctx, decls, ['==', '!='],
                      '_zc_boolean', ['_zc_boolean', '_zc_boolean'])

    # boolean logic
    _create_operators(compiler, ctx, decls, ['&&', '||'],
                      '_zc_boolean', ['_zc_boolean', '_zc_boolean'])
    _create_operators(
        compiler, ctx, decls, ['!'], '_zc_boolean', ['_zc_boolean'])

    root.set_builtin(decls)
    compiler.check_stage('built-in')


class BasicTypeDeclNode(TypeDeclNode):

    '''
    Basic, built-in types are implemented using this class
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(BasicTypeDeclNode, self).__init__(type_name)


class NumberTypeDeclNode(TypeDeclNode):

    '''
    Number, built-in types are implemented using this class
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(NumberTypeDeclNode, self).__init__(type_name)

    def round_up(self, value):
        '''
        Creates a threshold for this value using this type semantics
        '''
        # pylint: disable=no-self-use
        return encode.half_float_value(value)

    def round_down(self, value):
        '''
        Creates a threshold for this value using this type semantics
        '''
        # pylint: disable=no-self-use
        return encode.half_float_value(value)

    def next_up(self, value):
        '''
        Increments value by the minimum representable amount
        '''
        # pylint: disable=no-self-use
        return encode.half_float_next_down(value)

    def next_down(self, value):
        '''
        Decrements value by the minimum representable amount
        '''
        # pylint: disable=no-self-use
        return encode.half_float_next_down(value)


class VoidTypeDeclNode(TypeDeclNode):

    '''
    Basic, built-in types are implemented using this class
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(VoidTypeDeclNode, self).__init__(type_name)

    def can_cast_to(self, target_type):
        '''
        void type can not be casted to anything, not even to void
        '''
        return self.NO_MATCH


class LiteralTypeDeclNode(TypeDeclNode):

    '''
    Built-in number and bool types are implemented using this class
    '''

    def __init__(self, type_name, base_type):
        '''
        Constructor
        '''
        super(LiteralTypeDeclNode, self).__init__(type_name)
        self._base_type = base_type

    def can_cast_to(self, target_type):
        '''
        Literal can be casted to its base type
        '''
        if self == target_type:
            return self.EXACT_MATCH
        elif self._base_type == target_type:
            return self.CAST_MATCH
        else:
            return self.NO_MATCH

    def insert_cast_to(self, compiler, target_type, expr):
        '''
        Inserts a cast to the target (non-literal) type
        '''
        assert self == expr.get_type()
        assert self._base_type == target_type

        c = compiler.init_node(expression.LiteralCastExprNode(), expr.ctx)
        c.set_expression(expr)
        c.set_type(target_type)

        return c


class ParameterDeclNode(Node, ResolutionHelper):

    '''
    Node class used as container of a parameter in a function declaration
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(ParameterDeclNode, self).__init__()
        self.txt_type_name = type_name

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''
        del compiler

        return self.get_root_scope().lookup_type(self.txt_type_name)


class ParameterListNode(Node):

    '''
    Node class used as container of parameters in function declarations
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ParameterListNode, self).__init__()
        self.childs_parameters = []
        self._already_resolved = False

    def add_parameter(self, child):
        '''
        argument adder
        '''
        assert isinstance(child, ParameterDeclNode)
        child.set_parent(self)
        self.childs_parameters.append(child)

    def resolve(self, compiler):
        '''
        resolve
        '''
        assert not self._already_resolved
        for param in self.childs_parameters:
            compiler.resolve_node(param)
        self._already_resolved = True

    def get_size(self):
        return len(self.childs_parameters)

    def get_type_at(self, i):
        return self.childs_parameters[i].get_type()


def create_parameter_list(compiler, ctx, type_list):
    '''
    Creates a ParameterListNode with type_list elements
    '''
    pl = compiler.init_node(ParameterListNode(), ctx)
    for type_name in type_list:
        pl.add_parameter(compiler.init_node(ParameterDeclNode(type_name), ctx))

    return pl


def _create_operator(compiler, ctx, operator, ret_type, type_list):

    op = compiler.init_node(OperatorDeclNode(operator, ret_type), ctx)
    op.set_parameter_list(create_parameter_list(compiler, ctx, type_list))

    return op


def _create_operators(compiler, ctx, decls, op_list, ret_type, type_list):

    for current in op_list:
        op = _create_operator(compiler, ctx, current, ret_type, type_list)
        decls.add_declaration(op)


class OperatorDeclNode(Node, ResolutionHelper):

    '''
    Node class to represent an operator declaration
    '''

    def __init__(self, operator, type_name):
        '''
        Constructor
        '''
        super(OperatorDeclNode, self).__init__()
        self.child_parameter_list = None
        self.txt_operator = operator
        self.txt_type_name = type_name

    def set_parameter_list(self, child):
        '''
        parameter_list setter
        '''
        assert isinstance(child, ParameterListNode)
        child.set_parent(self)
        self.child_parameter_list = child

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''
        compiler.resolve_node(self.child_parameter_list)

        scope = self.get_root_scope()
        scope.add_operator(compiler, self.txt_operator, self)

        return scope.lookup_type(self.txt_type_name)

    def static_evaluate(self, compiler, expr, arg_list):
        '''
        Do static evaluation of expressions when possible
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        return None


def _create_literal_operators(compiler, ctx, root, operator_list, ret_type,
                              type_list):

    for current in operator_list:
        op = compiler.init_node(
            NumberLiteralOpDeclNode(current, ret_type), ctx)
        op.set_parameter_list(create_parameter_list(compiler, ctx, type_list))
        root.add_declaration(op)


class NumberLiteralOpDeclNode(OperatorDeclNode):

    '''
    Node class to represent an operator declaration with literal arguments
    We use the same class for number literals and boolean literals operators
    '''

    def __init__(self, operator, type_name):
        '''
        Constructor
        '''
        super(NumberLiteralOpDeclNode, self).__init__(operator, type_name)

    def static_evaluate(self, compiler, expr, arg_list):
        '''
        Do static evaluation of expressions when possible
        '''
        # pylint: disable=too-many-branches

        assert isinstance(expr, expression.OperatorExprNode)

        result = compiler.init_node(
            expression.StaticEvaluatedExprNode(), expr.ctx)

        if len(expr.child_argument_list.childs_arguments) == 1:
            rhs = expr.child_argument_list.childs_arguments[
                0].get_static_value()

            if self.txt_operator == '+':  # unary plus
                result.set_static_value(rhs)
            elif self.txt_operator == '-':  # unary minus
                result.set_static_value(- rhs)
            elif self.txt_operator == '!':
                result.set_static_value(not rhs)
            else:
                assert False
        elif len(expr.child_argument_list.childs_arguments) == 2:

            lhs = expr.child_argument_list.childs_arguments[
                0].get_static_value()
            rhs = expr.child_argument_list.childs_arguments[
                1].get_static_value()

            if self.txt_operator == '+':
                result.set_static_value(lhs + rhs)
            elif self.txt_operator == '-':
                result.set_static_value(lhs - rhs)
            elif self.txt_operator == '*':
                result.set_static_value(lhs * rhs)
            elif self.txt_operator == '/':
                result.set_static_value(lhs / rhs)
            elif self.txt_operator == '%':
                result.set_static_value(lhs % rhs)
            elif self.txt_operator == '<':
                result.set_static_value(lhs < rhs)
            elif self.txt_operator == '>':
                result.set_static_value(lhs > rhs)
            elif self.txt_operator == '>=':
                result.set_static_value(lhs >= rhs)
            elif self.txt_operator == '<=':
                result.set_static_value(lhs <= rhs)
            elif self.txt_operator == '==':
                result.set_static_value(lhs == rhs)
            elif self.txt_operator == '!=':
                result.set_static_value(lhs != rhs)
            elif self.txt_operator == '&&':
                result.set_static_value(lhs and rhs)
            elif self.txt_operator == '||':
                result.set_static_value(lhs or rhs)
            else:
                assert False
        else:
            assert False

        result.set_type(self.get_type())
        result.set_replaced(expr)

        return result


def _create_logic_literal_ops(compiler, ctx, root, operator_list, ret_type,
                              type_list):

    for current in operator_list:
        op = compiler.init_node(
            LogicLiteralOpDeclNode(current, ret_type), ctx)
        op.set_parameter_list(create_parameter_list(compiler, ctx, type_list))
        root.add_declaration(op)


class LogicLiteralOpDeclNode(OperatorDeclNode):

    '''
    Node class to represent a logic operator declaration with one literal
    '''

    def __init__(self, operator, type_name):
        '''
        Constructor
        '''
        super(LogicLiteralOpDeclNode, self).__init__(operator, type_name)

    def static_evaluate(self, compiler, expr, arg_list):
        '''
        Do static evaluation of expressions when possible
        '''
        # pylint: disable=too-many-branches

        assert isinstance(expr, expression.LogicOpExprNode)

        result_value = None

        assert len(expr.child_argument_list.childs_arguments) == 2

        lhs = expr.child_argument_list.childs_arguments[0].get_static_value()
        rhs = expr.child_argument_list.childs_arguments[1].get_static_value()

        assert lhs is not None or rhs is not None

        if self.txt_operator == '&&':
            if lhs is False:
                assert rhs is None
                result_value = False
            elif rhs is False:
                assert lhs is None
                result_value = False
            elif lhs is True:
                assert rhs is None
                return expr.child_argument_list.childs_arguments[1]
            elif lhs is None and rhs is True:
                assert lhs is None
                return expr.child_argument_list.childs_arguments[0]
            else:
                assert False

        elif self.txt_operator == '||':
            if lhs is True:
                assert rhs is None
                result_value = True
            elif rhs is True:
                assert lhs is None
                result_value = True
            elif lhs is False and rhs is False:
                assert False  # only one literal
                result_value = False
            elif lhs is False:
                assert rhs is None
                return expr.child_argument_list.childs_arguments[1]
            elif rhs is False:
                assert lhs is None
                return expr.child_argument_list.childs_arguments[0]
            else:
                assert False
        else:
            assert False

        assert result_value is not None

        result = compiler.init_node(
            expression.StaticEvaluatedExprNode(), expr.ctx)

        result.set_static_value(result_value)

        result.set_type(self.get_type())
        result.set_replaced(expr)

        return result


class McuSleepDeclNode(Node, ResolutionHelper):

    '''
    Declaration of built in 'mcu_sleep' function
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(McuSleepDeclNode, self).__init__()
        self.child_parameter_list = None

    def set_parameter_list(self, child):
        '''
        parameter_list setter
        '''
        assert isinstance(child, ParameterListNode)
        child.set_parent(self)
        self.child_parameter_list = child

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''
        compiler.resolve_node(self.child_parameter_list)

        scope = self.get_root_scope()
        scope.add_function(compiler, 'mcu_sleep', self)

        return scope.lookup_type('_zc_void')


class FieldTypeDeclNode(TypeDeclNode):

    '''
    Types used for message fields
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(FieldTypeDeclNode, self).__init__(type_name)
        self.encoding = None
        self.meaning = None
        self.min_value = 0
        self.max_value = 0
        self._number_type = None

    def resolve(self, compiler):
        '''
        resolve
        '''
        self._number_type = self.get_root_scope().lookup_type('_zc_number')
        super(FieldTypeDeclNode, self).resolve(compiler)

    def can_cast_to(self, target_type):
        '''
        This type can be casted to number, by inserting appropiate scaling
        '''
        if self == target_type:
            return self.EXACT_MATCH
        elif self._number_type == target_type:
            return self.CAST_MATCH
        else:
            return self.NO_MATCH

    def insert_cast_to(self, compiler, target_type, expr):
        '''
        Inserts a cast to the target (number) type
        TODO use scaling and <meaning>
        '''
        assert self == expr.get_type()
        assert self._number_type == target_type

        c = None

        if self.meaning:
            c = compiler.init_node(self.meaning.create_cast(), expr.ctx)
        else:
            c = compiler.init_node(expression.LiteralCastExprNode(), expr.ctx)

        c.set_expression(expr)
        c.set_type(target_type)

        return c

    def inverse_meaning(self, value):
        '''
        Inverse function of meaning
        Used for mapping literal number for comparison with
        value returned by a body-part
        '''
        # TODO check range
        assert value
        if self.meaning:
            return self.meaning.inverse(value)
        else:
            return value

    def round_up(self, value):
        '''
        Creates a threshold for this value using this type semantics
        '''
        # pylint: disable=no-self-use
        return math.ceil(value)

    def round_down(self, value):
        '''
        Creates a threshold for this value using this type semantics
        '''
        # pylint: disable=no-self-use
        return math.floor(value)

    def next_up(self, value):
        '''
        Increments value by the minimum representable amount
        '''
        # TODO check range
        if self.encoding in [Encoding.SIGNED_INT, Encoding.UNSIGNED_INT]:
            return math.floor(value + 1)
        else:
            assert False

    def next_down(self, value):
        '''
        Decrements value by the minimum representable amount
        '''
        # TODO check range
        if self.encoding in [Encoding.SIGNED_INT, Encoding.UNSIGNED_INT]:
            return math.ceil(value - 1)
        else:
            assert False


def create_field_to_literal_comparison(compiler, ctx, field_name):
    '''
    Creates 12 comparison operators for a field and a literal
    '''

    result = []
    for current in ['<', '>', '<=', '>=', '==', '!=']:

        # field to literal
        op = compiler.init_node(
            FieldToLiteralCompDeclNode(current, '_zc_boolean'), ctx)
        op.set_parameter_list(
            create_parameter_list(
                compiler, ctx, [field_name, '_zc_number_literal']))
        result.append(op)

        # and literal to field
        op2 = compiler.init_node(
            FieldToLiteralCompDeclNode(current, '_zc_boolean'), ctx)
        op2.set_parameter_list(
            create_parameter_list(
                compiler, ctx, ['_zc_number_literal', field_name]))
        op2.swap_flag = True
        result.append(op2)

    return result


class FieldToLiteralCompDeclNode(OperatorDeclNode):

    '''
    Node class to represent an very special operator declaration
    for comparison between reply field and number literal
    This comparison is special because it can be optimized by mapping
    reply field and literal to numbers in expression stack,
    or converting number literal to reply field internal type as optimization,
    without using stack expression.
    Also VM level Tiny, only supports the later optimization,
    because stack expression is not available.
    '''

    def __init__(self, operator, type_name):
        '''
        Constructor
        '''
        super(FieldToLiteralCompDeclNode, self).__init__(
            operator, type_name)
        self.swap_flag = False

    def static_evaluate(self, compiler, expr, arg_list):
        '''
        Do replace generic ComparisonOpExprNode by a much more specific
        FieldToLiteralCompExprNode
        '''

        assert isinstance(expr, expression.ComparisonOpExprNode)
        assert len(arg_list.childs_arguments) == 2

        mem = 0 if not self.swap_flag else 1
        lit = 1 if not self.swap_flag else 0

        member = arg_list.childs_arguments[mem]
        assert isinstance(member.get_type(), FieldTypeDeclNode)
        assert isinstance(member, expression.MemberAccessExprNode)
        assert isinstance(member.child_expression, expression.VariableExprNode)

        orig_value = arg_list.childs_arguments[lit].get_static_value()
        assert orig_value

        result = compiler.init_node(FieldToLiteralCompExprNode(), expr.ctx)

        result.set_replaced(expr)
        result.txt_op = swap_comparison(expr.txt_operator, self.swap_flag)
        result.ref_declaration = self
        result.ref_member_expr = member

        result.literal_value = orig_value

        result.set_type(self.get_type())

        return result


_negate_comparison_map = {'==': '!=',
                          '!=': '==',
                          '<': '>=',
                          '>': '<=',
                          '<=': '>',
                          '>=': '<'}


def negate_comparison(txt_op, negate):
    '''
    If negate is False, returns the same txt_op,
    If negate is True, return the negated comparison operator
    '''

    if negate:
        return _negate_comparison_map[txt_op]
    else:
        return txt_op


_negate_logic_map = {'!': '!',
                     '&&': '||',
                     '||': '&&'}


def negate_logic(txt_op, negate):
    '''
    If negate is False, returns the same txt_op,
    If negate is True, return the negated logic operator
    '''

    if negate:
        return _negate_logic_map[txt_op]
    else:
        return txt_op


_swap_comparison_map = {'==': '==',
                        '!=': '!=',
                        '<': '>',
                        '>': '<',
                        '<=': '>=',
                        '>=': '<='}


def swap_comparison(txt_op, swap):
    '''
    If swap is False, returns the same txt_op,
    If swap is True, return the comparison operator needed to swap lhs y rhs
    '''

    if swap:
        return _swap_comparison_map[txt_op]
    else:
        return txt_op


def simplify_comparison(txt_op, value, value_type):

    if txt_op in ['==', '!=']:  # TODO really want to support == and != ?
        return (txt_op, value)
    elif txt_op == '<':
        return ('<', value_type.round_up(value))
    elif txt_op == '>':
        return ('>', value_type.round_down(value))
    elif txt_op == '<=':
        return ('<', value_type.next_up(value))
    elif txt_op == '>=':
        return ('>', value_type.next_down(value))
    else:
        assert False


class FieldToLiteralCompExprNode(ExpressionNode):

    '''
    Node class representing a very special operator comparison expression
    between a reply field and a number literal.
    This kind of expression is created from a regular ComparisonOpExprNode
    by FieldToLiteralCompDeclNode for all expression
    This allows easier detection of this special comparison at a later time
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FieldToLiteralCompExprNode, self).__init__()
        self.child_replaced = None
        self.txt_op = None
        self.ref_declaration = None
        self.ref_member_expr = None
        self.literal_value = None

    def set_replaced(self, child):
        '''
        replaced setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_replaced = child

    def get_variable_decl(self):
        return self.ref_member_expr.child_expression.ref_decl

    def get_field_sequence(self):
        return self.ref_member_expr.get_member_field_sequence()

    def get_subcode_and_threshold(self, negate):
        '''
        Converts the literal value to the reply field type,
        Using reverse linear scaling
        Simplify >= and <= to < and > by modifying literal value by epsilon
        Also apply an optional negation flag, as helper for code generator,
        since normally if body is executed when condition is true,
        but at implementation, body is jumped when condition is false
        '''
        target_type = self.ref_member_expr.get_type()
        threshold = target_type.inverse_meaning(self.literal_value)

        txt_op = negate_comparison(self.txt_op, negate)

        return simplify_comparison(txt_op, threshold, target_type)


def _create_number_to_literal_comparison(compiler, ctx, root, operator_list):

    for current in operator_list:
        op = compiler.init_node(
            NumberToLiteralCompDeclNode(current, '_zc_boolean'), ctx)
        op.set_parameter_list(create_parameter_list(compiler, ctx,
                                                    ['_zc_number',
                                                     '_zc_number_literal']))
        root.add_declaration(op)

        op2 = compiler.init_node(
            NumberToLiteralCompDeclNode(current, '_zc_boolean'), ctx)
        op2.set_parameter_list(create_parameter_list(compiler, ctx,
                                                     ['_zc_number_literal',
                                                      '_zc_number']))
        op2.swap_flag = True
        root.add_declaration(op2)


class NumberToLiteralCompDeclNode(OperatorDeclNode):

    '''
    Node class to represent an special operator declaration
    for comparison between number and number literal
    This comparison is special because it is translated into specific
    ZEPTOVM_OP_JMPIFEXPR_XX operations
    '''

    def __init__(self, operator, type_name):
        '''
        Constructor
        '''
        super(NumberToLiteralCompDeclNode, self).__init__(
            operator, type_name)
        self.swap_flag = False

    def static_evaluate(self, compiler, expr, arg_list):
        '''
        Do replace generic ComparisonOpExprNode by a much more specific
        NumberToLiteralCompExprNode
        '''

        assert isinstance(expr, expression.ComparisonOpExprNode)
        assert len(expr.child_argument_list.childs_arguments) == 2

        result = compiler.init_node(NumberToLiteralCompExprNode(), expr.ctx)
        result.set_argument_list(expr.child_argument_list)
        result.ref_decl = self

        compiler.remove_node(expr)

        result.set_type(self.get_type())

        return result


class NumberToLiteralCompExprNode(ExpressionNode):

    '''
    Node class representing an special operator comparison expression
    between a number and a number literal.
    This kind of expression is created from a regular ComparisonOpExprNode
    by NumberToLiteralCompDeclNode for all expressions that match
    This allows easier detection of this special comparison at a later time
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NumberToLiteralCompExprNode, self).__init__()
        self.child_argument_list = None
        self.ref_decl = None

    def set_argument_list(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ArgumentListNode)
        child.set_parent(self)
        self.child_argument_list = child

    def get_expression(self):
        assert len(self.child_argument_list.childs_arguments) == 2

        i = 0 if not self.ref_decl.swap_flag else 1
        return self.child_argument_list.childs_arguments[i]

    def get_literal(self):
        assert len(self.child_argument_list.childs_arguments) == 2

        i = 1 if not self.ref_decl.swap_flag else 0
        return self.child_argument_list.childs_arguments[i]

    def get_subcode_and_threshold(self, negate):
        '''
        simplify >= and <= to < and > by modifying literal value by epsilon
        Also apply an optional negation flag, as helper for code generator,
        since normally if body is executed when condition is true,
        but at implementation, body is jumped when condition is false
        '''

        op = swap_comparison(
            self.ref_decl.txt_operator, self.ref_decl.swap_flag)

        op = negate_comparison(op, negate)

        threshold = self.get_literal().get_static_value()
        assert threshold
        ltype = self.get_expression().get_type()

        return simplify_comparison(op, threshold, ltype)


def _create_number_to_number_comparison(compiler, ctx, root, operator_list):

    for current in operator_list:
        op = compiler.init_node(
            NumberToNumberCompDeclNode(current, '_zc_boolean'), ctx)
        op.set_parameter_list(create_parameter_list(compiler, ctx,
                                                    ['_zc_number',
                                                     '_zc_number']))
        root.add_declaration(op)


class NumberToNumberCompDeclNode(OperatorDeclNode):

    '''
    Node class to represent an special operator declaration
    for comparison between number and number literal
    This comparison is special because it is translated into specific
    ZEPTOVM_OP_JMPIFEXPR_XX operations
    '''

    def __init__(self, operator, type_name):
        '''
        Constructor
        '''
        super(NumberToNumberCompDeclNode, self).__init__(
            operator, type_name)

    def static_evaluate(self, compiler, expr, arg_list):
        '''
        Do replace generic ComparisonOpExprNode by a much more specific
        NumberToLiteralCompExprNode
        '''

        assert isinstance(expr, expression.ComparisonOpExprNode)
        assert len(expr.child_argument_list.childs_arguments) == 2

        result = compiler.init_node(NumberToNumberCompExprNode(), expr.ctx)
        result.set_argument_list(expr.child_argument_list)
        result.ref_decl = self

        compiler.remove_node(expr)

        result.set_type(self.get_type())

        return result


class NumberToNumberCompExprNode(ExpressionNode):

    '''
    Node class representing an special operator comparison expression
    between a number and a number literal.
    This kind of expression is created from a regular ComparisonOpExprNode
    by NumberToLiteralCompDeclNode for all expressions that match
    This allows easier detection of this special comparison at a later time
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NumberToNumberCompExprNode, self).__init__()
        self.child_argument_list = None
        self.ref_decl = None

    def set_argument_list(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ArgumentListNode)
        child.set_parent(self)
        self.child_argument_list = child

    def get_subcode_and_threshold(self, negate):
        '''
        simplify >= and <= to < and > by modifying literal value by epsilon
        Also apply an optional negation flag, as helper for code generator,
        since normally if body is executed when condition is true,
        but at implementation, body is jumped when condition is false
        '''
        op = negate_comparison(self.ref_decl.txt_operator, negate)

        ltype = self.child_argument_list.childs_arguments[0].get_type()

        return simplify_comparison(op, 0.0, ltype)


def create_field_to_field_comparison(compiler, et, field_name, other_field):
    '''
    Creates a list of 12 comparison operators, between two fields
    It creates the six comparisons (>, <, >=, <=, ==, !=)
    each one has two copies swaping lhs and rhs
    '''

    result = []
    for current in ['<', '>', '<=', '>=', '==', '!=']:

        op = compiler.init_node(
            FieldToFieldCompDeclNode(current, '_zc_boolean'), et)
        op.set_parameter_list(
            create_parameter_list(
                compiler, et, [field_name, other_field.txt_name]))
        result.append(op)

        op2 = compiler.init_node(
            FieldToFieldCompDeclNode(current, '_zc_boolean'), et)
        op2.set_parameter_list(
            create_parameter_list(
                compiler, et, [other_field.txt_name, field_name]))
        result.append(op2)

    return result


class FieldToFieldCompDeclNode(OperatorDeclNode):

    '''
    Node class to represent an very special operator declaration
    for comparison between two reply fields
    This comparison is special because it can be optimized by mapping
    reply field and literal to numbers in expression stack,
    or converting one reply field to the type of the other as optimization,
    using fewer stack operations.
    aX+b >= cY+d  =>  X >= (c/a)Y+(d-b)/a => X - (c/a)Y >= (d-b)/a
    '''

    def __init__(self, operator, type_name):
        '''
        Constructor
        '''
        super(FieldToFieldCompDeclNode, self).__init__(
            operator, type_name)
        self._number_type = None

    def resolve(self, compiler):
        '''
        resolve
        '''
        self._number_type = self.get_root_scope().lookup_type('_zc_number')
        super(FieldToFieldCompDeclNode, self).resolve(compiler)

    def static_evaluate(self, compiler, expr, arg_list):
        '''
        Do replace generic ComparisonOpExprNode by a much more specific
        FieldToLiteralCompExprNode
        '''

        assert isinstance(expr, expression.ComparisonOpExprNode)
        assert len(expr.child_argument_list.childs_arguments) == 2

        result = compiler.init_node(FieldToFieldCompExprNode(), expr.ctx)
        result.ref_decl = self

        a0 = expr.child_argument_list.childs_arguments[0]
        t0 = a0.get_type()
        assert t0.can_cast_to(self._number_type) == TypeDeclNode.CAST_MATCH

        c0 = t0.insert_cast_to(compiler, self._number_type, a0)
        result.set_lhs(c0)

        a1 = expr.child_argument_list.childs_arguments[1]
        t1 = a1.get_type()
        assert t1.can_cast_to(self._number_type) == TypeDeclNode.CAST_MATCH

        c1 = t1.insert_cast_to(compiler, self._number_type, a1)
        result.set_rhs(c1)

        compiler.remove_node(expr.child_argument_list)
        compiler.remove_node(expr)

        result.set_type(self.get_type())

        return result


class FieldToFieldCompExprNode(ExpressionNode):

    '''
    Node class representing a very special operator comparison expression
    between two reply fields.
    This kind of expression is created from a regular ComparisonOpExprNode
    by FieldToFieldCompDeclNode for all expression
    This allows easier detection of this special comparison at a later time
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FieldToFieldCompExprNode, self).__init__()
        self.child_lhs = None
        self.child_rhs = None
        self.ref_decl = None

    def set_lhs(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_lhs = child

    def set_rhs(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_rhs = child

    def get_subcode_and_threshold(self, negate):
        '''
        simplify >= and <= to < and > by modifying literal value by epsilon
        Also apply an optional negation flag, as helper for code generator,
        since normally if body is executed when condition is true,
        but at implementation, body is jumped when condition is false
        '''
        op = negate_comparison(self.ref_decl.txt_operator, negate)

        ltype = self.child_lhs.get_type()

        return simplify_comparison(op, 0.0, ltype)
