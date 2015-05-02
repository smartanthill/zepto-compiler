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

from smartanthill_zc.node import (DeclarationListNode, LiteralCastExprNode,
                                  Node, OperatorExprNode, ResolutionHelper,
                                  StaticEvaluatedExprNode, TypeDeclNode)


def create_builtins(compiler, root):
    '''
    Creates all built in nodes and adds them to the root
    '''

    ctx = compiler.BUILTIN

    decls = compiler.init_node(DeclarationListNode(), ctx)
    decls.add_declaration(
        compiler.init_node(VoidTypeDeclNode('_zc_void'), ctx))

    num_t = compiler.init_node(BasicTypeDeclNode('_zc_number'), ctx)
    decls.add_declaration(num_t)

    decls.add_declaration(
        compiler.init_node(LiteralTypeDeclNode('_zc_number_literal', num_t),
                           ctx))

    bool_t = compiler.init_node(BasicTypeDeclNode('_zc_bool'), ctx)
    decls.add_declaration(bool_t)

    decls.add_declaration(
        compiler.init_node(LiteralTypeDeclNode('_zc_bool_literal', bool_t),
                           ctx))

    mcu = compiler.init_node(McuSleepDeclNode(), ctx)
    mcu.set_parameter_list(
        create_parameter_list(compiler, ctx, ['_zc_number_literal']))
    decls.add_declaration(mcu)

    _create_literal_operators(compiler, ctx, decls, ['+', '-', '*', '/'],
                              '_zc_number_literal',
                              ['_zc_number_literal', '_zc_number_literal'])

    _create_operators(compiler, ctx, decls, ['+', '-', '*', '/'],
                      '_zc_number', ['_zc_number', '_zc_number'])

    _create_operators(compiler, ctx, decls, ['<', '>', '<=', '>='],
                      '_zc_bool', ['_zc_number', '_zc_number'])

    _create_operators(compiler, ctx, decls, ['==', '!='],
                      '_zc_bool', ['_zc_bool', '_zc_bool'])

    _create_operators(compiler, ctx, decls, ['&&', '||'],
                      '_zc_bool', ['_zc_bool', '_zc_bool'])

    _create_operators(compiler, ctx, decls, ['!'], '_zc_bool', ['_zc_bool'])

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

        c = compiler.init_node(LiteralCastExprNode(), expr.ctx)
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

    def add_parameter(self, node):
        '''
        argument adder
        '''
        assert isinstance(node, ParameterDeclNode)
        node.set_parent(self)
        self.childs_parameters.append(node)

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

    def set_parameter_list(self, node):
        '''
        parameter_list setter
        '''
        assert isinstance(node, ParameterListNode)
        node.set_parent(self)
        self.child_parameter_list = node

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''
        compiler.resolve_node(self.child_parameter_list)

        scope = self.get_root_scope()
        scope.add_operator(compiler, self.txt_operator, self)

        return scope.lookup_type(self.txt_type_name)

    def static_evaluate(self, compiler, node, arg_list):
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
    Node class to represent an operator declaration
    '''

    def __init__(self, operator, type_name):
        '''
        Constructor
        '''
        super(NumberLiteralOpDeclNode, self).__init__(operator, type_name)

    def static_evaluate(self, compiler, node, arg_list):
        '''
        Do static evaluation of expressions when possible
        '''

        assert isinstance(node, OperatorExprNode)
        assert len(node.child_argument_list.childs_arguments) == 2

        lhs = node.child_argument_list.childs_arguments[0].get_static_value()
        rhs = node.child_argument_list.childs_arguments[1].get_static_value()

        result = compiler.init_node(StaticEvaluatedExprNode(), node.ctx)

        if self.txt_operator == '+':
            result.set_static_value(lhs + rhs)
        elif self.txt_operator == '-':
            result.set_static_value(lhs - rhs)
        elif self.txt_operator == '*':
            result.set_static_value(lhs * rhs)
        elif self.txt_operator == '/':
            result.set_static_value(lhs / rhs)
        else:
            assert False

        result.set_type(self.get_type())
        result.set_replaced(node)

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

    def set_parameter_list(self, node):
        '''
        parameter_list setter
        '''
        assert isinstance(node, ParameterListNode)
        node.set_parent(self)
        self.child_parameter_list = node

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''
        compiler.resolve_node(self.child_parameter_list)

        scope = self.get_root_scope()
        scope.add_function(compiler, 'mcu_sleep', self)

        return scope.lookup_type('_zc_void')
