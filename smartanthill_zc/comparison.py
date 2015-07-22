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

from smartanthill_zc import node, expression


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


def create_number_to_literal_comparison(compiler, ctx, root, operator_list):

    for current in operator_list:
        op = compiler.init_node(
            NumberToLiteralCompDeclNode(current, '_zc_boolean'), ctx)
        op.set_parameter_list(
            node.create_parameter_list(compiler, ctx,
                                       ['_zc_number', '_zc_number_literal']))
        root.add_declaration(op)

        op2 = compiler.init_node(
            NumberToLiteralCompDeclNode(current, '_zc_boolean'), ctx)
        op2.set_parameter_list(
            node.create_parameter_list(compiler, ctx,
                                       ['_zc_number_literal', '_zc_number']))
        op2.swap_flag = True
        root.add_declaration(op2)


class NumberToLiteralCompDeclNode(node.OperatorDeclNode):

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


class NumberToLiteralCompExprNode(node.ExpressionNode):

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
        assert isinstance(child, node.ArgumentListNode)
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


def create_number_to_number_comparison(compiler, ctx, root, operator_list):

    for current in operator_list:
        op = compiler.init_node(
            NumberToNumberCompDeclNode(current, '_zc_boolean'), ctx)
        op.set_parameter_list(node.create_parameter_list(compiler, ctx,
                                                         ['_zc_number',
                                                          '_zc_number']))
        root.add_declaration(op)


class NumberToNumberCompDeclNode(node.OperatorDeclNode):

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


class NumberToNumberCompExprNode(node.ExpressionNode):

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
        assert isinstance(child, node.ArgumentListNode)
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
