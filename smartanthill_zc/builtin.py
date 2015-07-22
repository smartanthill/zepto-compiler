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

from smartanthill_zc import encode, expression, node, comparison
from smartanthill_zc.node import (
    Node, ResolutionHelper,
    TypeDeclNode, create_parameter_list)


def create_builtins(compiler, ctx):
    '''
    Creates all built in nodes and adds them to the root
    '''

    decls = compiler.init_node(node.DeclarationListNode(), ctx)
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

    comparison.create_number_to_literal_comparison(
        compiler, ctx, decls, ['<', '>', '<=', '>=', '==', '!='])

    # unary
    _create_operators(compiler, ctx, decls, ['+', '-'],
                      '_zc_number', ['_zc_number'])
    # binary
    _create_operators(compiler, ctx, decls, ['+', '-', '*', '/'],
                      '_zc_number', ['_zc_number', '_zc_number'])

    # number comparison
    comparison.create_number_to_number_comparison(
        compiler, ctx, decls, ['<', '>', '<=', '>=', '==', '!='])

    # boolean comparison
    _create_operators(compiler, ctx, decls, ['==', '!='],
                      '_zc_boolean', ['_zc_boolean', '_zc_boolean'])

    # boolean logic
    _create_operators(compiler, ctx, decls, ['&&', '||'],
                      '_zc_boolean', ['_zc_boolean', '_zc_boolean'])
    _create_operators(
        compiler, ctx, decls, ['!'], '_zc_boolean', ['_zc_boolean'])

    compiler.check_stage('built_in')

    return decls


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
        return self._base_type == target_type

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


def _create_operator(compiler, ctx, operator, ret_type, type_list):

    op = compiler.init_node(node.OperatorDeclNode(operator, ret_type), ctx)
    op.set_parameter_list(create_parameter_list(compiler, ctx, type_list))

    return op


def _create_operators(compiler, ctx, decls, op_list, ret_type, type_list):

    for current in op_list:
        op = _create_operator(compiler, ctx, current, ret_type, type_list)
        decls.add_declaration(op)


def _create_literal_operators(compiler, ctx, root, operator_list, ret_type,
                              type_list):

    for current in operator_list:
        op = compiler.init_node(
            NumberLiteralOpDeclNode(current, ret_type), ctx)
        op.set_parameter_list(create_parameter_list(compiler, ctx, type_list))
        root.add_declaration(op)


class NumberLiteralOpDeclNode(node.OperatorDeclNode):

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


class LogicLiteralOpDeclNode(node.OperatorDeclNode):

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
        assert isinstance(child, node.ParameterListNode)
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
