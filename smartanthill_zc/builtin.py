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

from smartanthill_zc.node import Node, DeclarationHelper,\
    StaticEvaluatedExprNode, LiteralCastExprNode, TypeDeclNode, \
    OperatorExprNode


def create_builtins(compiler, root):
    '''
    Creates all built in nodes and adds them to the root
    '''

    ctx = compiler.BUILTIN

    root.add_declaration(
        compiler.init_node(VoidTypeDeclNode(u'_zc_void'), ctx))

    num_lit = compiler.init_node(BasicTypeDeclNode(u'_zc_number_literal'), ctx)
    root.add_declaration(num_lit)

    root.add_declaration(
        compiler.init_node(NumberTypeDeclNode(u'_zc_number', num_lit), ctx))

    bool_lit = compiler.init_node(BasicTypeDeclNode(u'_zc_bool_literal'), ctx)
    root.add_declaration(bool_lit)

    root.add_declaration(
        compiler.init_node(NumberTypeDeclNode(u'_zc_bool', bool_lit), ctx))

    mcu = compiler.init_node(McuSleepDeclNode(), ctx)
    mcu.set_parameter_list(
        _create_parameter_list(compiler, ctx, [u'_zc_number_literal']))
    root.add_declaration(mcu)

    root.add_declaration(
        _create_test_plugin_type(compiler, ctx, u'TemperatureSensor'))

    root.add_declaration(
        _create_test_plugin(compiler, ctx, u'TemperatureSensor'))

    _create_literal_operators(compiler, ctx, root, [u'+', u'-', u'*', u'/'],
                              u'_zc_number_literal',
                              [u'_zc_number_literal', u'_zc_number_literal'])

    _create_operators(compiler, ctx, root, [u'+', u'-', u'*', u'/'],
                      u'_zc_number', [u'_zc_number', u'_zc_number'])

    _create_operators(compiler, ctx, root, [u'<', u'>', u'<=', u'>='],
                      u'_zc_bool', [u'_zc_number', u'_zc_number'])

    _create_operators(compiler, ctx, root, [u'==', u'!='],
                      u'_zc_bool', [u'_zc_bool', u'_zc_bool'])

    _create_operators(compiler, ctx, root, [u'&&', u'||'],
                      u'_zc_bool', [u'_zc_bool', u'_zc_bool'])

    _create_operators(compiler, ctx, root, [u'!'], u'_zc_bool', [u'_zc_bool'])

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

    def can_initialize(self, rhs):
        '''
        Returns true if an instance of this type can be initialized with rhs
        '''
        return self.NO_MATCH


class NumberTypeDeclNode(TypeDeclNode):

    '''
    Built-in number and bool types are implemented using this class
    '''

    def __init__(self, type_name, literal_type):
        '''
        Constructor
        '''
        super(NumberTypeDeclNode, self).__init__(type_name)
        self._literal_type = literal_type

    def can_initialize(self, rhs):
        '''
        Returns true if an instance of this type can be initialized with rhs
        '''
        if self == rhs:
            return self.EXACT_MATCH
        elif rhs == self._literal_type:
            return self.CAST_MATCH
        else:
            return self.NO_MATCH

    def insert_cast(self, compiler, rhs_expr):
        '''
        Base method for cast insertion
        '''

        assert rhs_expr.get_type() == self._literal_type

        c = compiler.init_node(LiteralCastExprNode(), rhs_expr.ctx)
        c.set_expression(rhs_expr)
        c.set_type(self)

        return c


class AggregateTypeElementDeclNode(Node, DeclarationHelper):

    '''
    Aggregate type element
    '''

    def __init__(self, name, type_name):
        '''
        Constructor
        '''
        super(AggregateTypeElementDeclNode, self).__init__()
        self.str_name = name
        self.str_type_name = type_name

    def do_resolve_declaration(self, compiler):
        '''
        Template method from DeclarationHelper
        '''
        del compiler
        return self.get_root_scope().lookup_type(self.str_type_name)


class AggregateTypeDeclNode(TypeDeclNode):

    '''
    Aggregate type, used as plug-in method return type
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(AggregateTypeDeclNode, self).__init__(type_name)
        self.childs_elements = []
        self._already_resolved = False

    def add_element(self, node):
        '''
        argument adder
        '''
        assert isinstance(node, AggregateTypeElementDeclNode)
        node.set_parent(self)
        self.childs_elements.append(node)

    def resolve(self, compiler):
        '''
        resolve
        '''
        assert not self._already_resolved
        for elem in self.childs_elements:
            compiler.resolve_node(elem)

        self.get_root_scope().add_type(compiler, self.str_type_name, self)
        self._already_resolved = True

    def lookup_member_type(self, name):
        for current in self.childs_elements:
            if current.str_name == name:
                return current.get_type()

        return None


class ParameterDeclNode(Node, DeclarationHelper):

    '''
    Node class used as container of a parameter in a function declaration
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(ParameterDeclNode, self).__init__()
        self.str_type_name = type_name

    def do_resolve_declaration(self, compiler):
        '''
        Template method from DeclarationHelper
        '''
        del compiler

        return self.get_root_scope().lookup_type(self.str_type_name)


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


def _create_parameter_list(compiler, ctx, type_list):

    pl = compiler.init_node(ParameterListNode(), ctx)
    for type_name in type_list:
        pl.add_parameter(compiler.init_node(ParameterDeclNode(type_name), ctx))

    return pl


def _create_operator(compiler, ctx, operator, ret_type, type_list):

    op = compiler.init_node(OperatorDeclNode(operator, ret_type), ctx)
    op.set_parameter_list(_create_parameter_list(compiler, ctx, type_list))

    return op


def _create_operators(compiler, ctx, root, operator_list, ret_type, type_list):

    for current in operator_list:
        op = _create_operator(compiler, ctx, current, ret_type, type_list)
        root.add_declaration(op)


class OperatorDeclNode(Node, DeclarationHelper):

    '''
    Node class to represent an operator declaration
    '''

    def __init__(self, operator, type_name):
        '''
        Constructor
        '''
        super(OperatorDeclNode, self).__init__()
        self.child_parameter_list = None
        self.str_operator = operator
        self.str_type_name = type_name

    def set_parameter_list(self, node):
        '''
        parameter_list setter
        '''
        assert isinstance(node, ParameterListNode)
        node.set_parent(self)
        self.child_parameter_list = node

    def do_resolve_declaration(self, compiler):
        '''
        Template method from DeclarationHelper
        '''
        compiler.resolve_node(self.child_parameter_list)

        scope = self.get_root_scope()
        scope.add_operator(compiler, self.str_operator, self)

        return scope.lookup_type(self.str_type_name)

    def match_arguments(self, compiler, arg_list):
        '''
        Checks if the given arguments can be used to call this function
        If false, it raises
        '''
        self.child_parameter_list.match_arguments(compiler, arg_list)

    def can_match_arguments(self, compiler, arg_list):
        '''
        Returns if the given arguments can be used to call this function
        '''
        return self.child_parameter_list.can_match_arguments(compiler,
                                                             arg_list)

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
        op.set_parameter_list(_create_parameter_list(compiler, ctx, type_list))
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

        if self.str_operator == u'+':
            result.set_static_value(lhs + rhs)
        elif self.str_operator == u'-':
            result.set_static_value(lhs - rhs)
        elif self.str_operator == u'*':
            result.set_static_value(lhs - rhs)
        elif self.str_operator == u'/':
            result.set_static_value(lhs - rhs)
        else:
            assert False

        result.set_type(self.get_type())
        result.set_replaced(node)

        return result


class McuSleepDeclNode(Node, DeclarationHelper):

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
        Template method from DeclarationHelper
        '''
        compiler.resolve_node(self.child_parameter_list)

        scope = self.get_root_scope()
        scope.add_function(compiler, u'mcu_sleep', self)

        return scope.lookup_type(u'_zc_void')

    def can_match_arguments(self, compiler, arg_list):
        '''
        Returns if the given arguments can be used to call this function
        '''
        return self.child_parameter_list.can_match_arguments(compiler,
                                                             arg_list)


def _create_test_plugin_type(compiler, ctx, name):
    '''
    Temp function to create a test plug-in type
    '''
    a = compiler.init_node(AggregateTypeDeclNode(name + u'_t'), ctx)
    a.add_element(
        compiler.init_node(AggregateTypeElementDeclNode('flag', '_zc_bool'),
                           ctx))

    a.add_element(
        compiler.init_node(AggregateTypeElementDeclNode('value', '_zc_number'),
                           ctx))

    a.add_element(
        compiler.init_node(AggregateTypeElementDeclNode('Temperature',
                                                        '_zc_number'),
                           ctx))

    return a


def _create_test_plugin(compiler, ctx, name):
    '''
    Temp function to create a test plug-in
    '''

    p = compiler.init_node(PluginDeclNode(name, name + u'_t'), ctx)

    p.set_parameter_list(
        compiler.init_node(ParameterListNode(), ctx))

    return p


class PluginDeclNode(Node, DeclarationHelper):

    '''
    Declaration of plug-in
    '''

    def __init__(self, plugin_name, type_name):
        '''
        Constructor
        '''
        super(PluginDeclNode, self).__init__()
        self.child_parameter_list = None
        self.str_plugin_name = plugin_name
        self.str_type_name = type_name

    def set_parameter_list(self, node):
        '''
        parameter_list setter
        '''
        assert isinstance(node, ParameterListNode)
        node.set_parent(self)
        self.child_parameter_list = node

    def do_resolve_declaration(self, compiler):
        '''
        Template method from DeclarationHelper
        '''

        compiler.resolve_node(self.child_parameter_list)

        scope = self.get_root_scope()
        scope.add_plugin(compiler, self.str_plugin_name, self)

        return scope.lookup_type(self.str_type_name)

    def lookup_method(self, name):
        return self if name == "Execute" else None

    def can_match_arguments(self, compiler, arg_list):
        '''
        Returns if the given arguments can be used to call this function
        '''
        return self.child_parameter_list.can_match_arguments(compiler,
                                                             arg_list)
