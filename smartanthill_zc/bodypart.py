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

from smartanthill_zc import builtin, expression
from smartanthill_zc.node import (DeclarationListNode, ExpressionNode, Node,
                                  ResolutionHelper, TypeDeclNode)


class FieldTypeFactoryNode(Node):

    '''
    Factory class to create FieldTypeDeclNode and create special comparison
    operators between reply fields and number literals
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FieldTypeFactoryNode, self).__init__()
        self.child_type_list = None
        self.child_operator_list = None
        self._resolved = False

    def set_type_list(self, child):
        '''
        type_list setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_type_list = child

    def set_operator_list(self, child):
        '''
        operator_list setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_operator_list = child

    def resolve(self, compiler):
        '''
        resolve
        '''
        assert not self._resolved
        compiler.resolve_node(self.child_type_list)
        compiler.resolve_node(self.child_operator_list)
        self._resolved = True

    def add_field_type(self, compiler, field_type, ctx):
        '''
        Adds a new FieldTypeDeclNode, and creates related Operators
        '''
        f2l = builtin.create_field_to_literal_comparison(
            compiler, ctx, field_type.txt_name)
        self.child_operator_list.add_declaration_list(f2l)

        for current in self.child_type_list.childs_declarations:
            f2f = builtin.create_field_to_field_comparison(
                compiler, ctx, field_type.txt_name, current)
            self.child_operator_list.add_declaration_list(f2f)

        self.child_type_list.add_declaration(field_type)


class LinearConvertionFloat(object):

    '''
    Linear scale helper
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._a = 1
        self._b = 0
        self._inv_a = 1

    def set_points(self, in0, out0, in1, out1):
        '''
        Initialize the scale by two points
        '''
        in0 = int(in0)
        in1 = int(in1)
        out0 = float(out0)
        out1 = float(out1)
        self._a = (out1 - out0) / (in1 - in0)
        self._inv_a = (in1 - in0) / (out1 - out0)
        self._b = out0 - self._a * in0

    def inverse(self, value):
        '''
        Returns inverse scaling of value
        This method rounds result to exact integer
        or half way (i.e. 1.0, 1.5, 2.0, 2.5, etc)
        '''

        inv = (value - self._b) * self._inv_a
        inv2 = round(inv * 2) / 2  # magic trick to remove round error
        return inv2

    def create_cast(self):
        '''
        Creates a new expression cast
        '''
        # pylint: disable=no-self-use

        return FieldCastExprNode(self._a, self._b)


class FieldCastExprNode(ExpressionNode):

    '''
    Node class representing an automatic conversion from a sensor output value
    to a physical magnitude by linear scaling
    '''

    def __init__(self, a, b):
        '''
        Constructor
        '''
        super(FieldCastExprNode, self).__init__()
        self.child_expression = None
        self.a = a
        self.b = b

    def set_expression(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child


class MemberDeclNode(Node, ResolutionHelper):

    '''
    Aggregate element declaration
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        super(MemberDeclNode, self).__init__()
        self.txt_name = name
        self.ref_field_type = None
        self.field_sequence = None

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''
        del compiler
        assert self.ref_field_type
        return self.ref_field_type


class MessageTypeDeclNode(TypeDeclNode):

    '''
    Aggregate type, used as plug-in method return type
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(MessageTypeDeclNode, self).__init__(type_name)
        self.childs_elements = []
        self.field_sequence = None

    def add_element(self, child):
        '''
        argument adder
        '''
        assert isinstance(child, MemberDeclNode)
        child.set_parent(self)
        self.childs_elements.append(child)

    def resolve(self, compiler):
        '''
        resolve
        '''
        for elem in self.childs_elements:
            compiler.resolve_node(elem)

        self.make_field_sequences()
        super(MessageTypeDeclNode, self).resolve(compiler)

    def is_message_type(self):
        '''
        All instances of this type are valid response types
        '''
        return True

    def lookup_member(self, name):
        '''
        Finds a member of this type, by name
        '''
        for current in self.childs_elements:
            if current.txt_name == name:
                return current

        return None

    def make_field_sequences(self):
        '''
        Creates field-sequence for all members and for the entire type
        '''

        fs = []
        for current in self.childs_elements:
            fs.append(current.ref_field_type.encoding)
            current.field_sequence = tuple(fs)

        self.field_sequence = tuple(fs)


class CommandFieldTypeDeclNode(TypeDeclNode):

    '''
    Types used for commands fields
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(CommandFieldTypeDeclNode, self).__init__(type_name)
        self.encoding = None
        self.min_value = 0
        self.max_value = 0
        self.ref_number_literal_type = None

    def resolve(self, compiler):
        '''
        resolve
        '''
        self.ref_number_literal_type = self.get_root_scope().lookup_type(
            '_zc_number_literal')
        super(CommandFieldTypeDeclNode, self).resolve(compiler)

    def can_cast_from(self, source_type):
        '''
        If self can be constructed from source_type returns True
        Otherwise returns False
        '''
        return source_type == self.ref_number_literal_type

    def insert_cast_from(self, compiler, source_type, expr):
        '''
        Inserts a cast to the target (number) type
        TODO add value and range check
        '''
        assert self.ref_number_literal_type == expr.get_type()
        assert self.ref_number_literal_type == source_type

        c = compiler.init_node(expression.LiteralCastExprNode(), expr.ctx)

        c.set_expression(expr)
        c.set_type(self)

        return c

    def get_encoding(self):
        '''
        Return all the info needed to encode a value under this type
        '''
        return self.encoding


class PluginDeclNode(Node, ResolutionHelper):

    '''
    Declaration of a plugin, shared by several bodyparts
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PluginDeclNode, self).__init__()
        self.child_parameter_list = None
        self.txt_type_name = None

    def set_parameter_list(self, child):
        '''
        parameter_list setter
        '''
        assert isinstance(child, builtin.ParameterListNode)
        child.set_parent(self)
        self.child_parameter_list = child

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''

        compiler.resolve_node(self.child_parameter_list)
        return self.get_root_scope().lookup_type(self.txt_type_name)

    def lookup_method(self, name):
        '''
        Method look-up, currently only 'Execute' method is supported
        and is implemented by this same instance.
        This will change if more than one method support is required
        '''
        return self if name == "Execute" else None


class BodyPartDeclNode(Node):

    '''
    Declaration of a body-part
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BodyPartDeclNode, self).__init__()
        self.ref_plugin = None
        self.txt_name = None
        self.bodypart_id = 0L

    def resolve(self, compiler):
        '''
        resolve
        '''
        assert not self._resolved
        assert self.ref_plugin

        compiler.resolve_node(self.ref_plugin)
        self.get_root_scope().add_bodypart(compiler, self.txt_name, self)

        self._resolved = True


def create_body_parts_manager(compiler, ctx):
    '''
    Creates and initializes a BodyPartsManagerNode instance
    '''
    manager = compiler.init_node(BodyPartsManagerNode(), ctx)
    manager.set_type_list(compiler.init_node(DeclarationListNode(), ctx))
    manager.set_plugin_list(compiler.init_node(DeclarationListNode(), ctx))
    manager.set_body_part_list(compiler.init_node(DeclarationListNode(), ctx))

    factory = compiler.init_node(FieldTypeFactoryNode(), ctx)
    factory.set_type_list(compiler.init_node(DeclarationListNode(), ctx))
    factory.set_operator_list(compiler.init_node(DeclarationListNode(), ctx))

    manager.set_field_type_factory(factory)

    empty_reply = compiler.init_node(
        MessageTypeDeclNode('zc_empty_reply'), ctx)

    manager.set_empty_reply_type(empty_reply)

    return manager


class BodyPartsManagerNode(Node):

    '''
    Container for body-parts and field types factory
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BodyPartsManagerNode, self).__init__()
        self.child_field_type_factory = None
        self.child_type_list = None
        self.child_empty_reply_type = None
        self.child_plugin_list = None
        self.child_body_part_list = None
        self.next_unique = 1
        self._resolved = False

    def set_field_type_factory(self, child):
        '''
        parameter_list setter
        '''
        assert isinstance(child, FieldTypeFactoryNode)
        child.set_parent(self)
        self.child_field_type_factory = child

    def set_type_list(self, child):
        '''
        parameter_list setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_type_list = child

    def set_empty_reply_type(self, child):
        '''
        parameter_list setter
        '''
        assert isinstance(child, MessageTypeDeclNode)
        child.set_parent(self)
        self.child_empty_reply_type = child

    def set_plugin_list(self, child):
        '''
        plugin_list setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_plugin_list = child

    def set_body_part_list(self, child):
        '''
        body_part_list setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_body_part_list = child

    def resolve(self, compiler):
        '''
        resolve
        '''
        assert not self._resolved

        compiler.resolve_node(self.child_field_type_factory)
        compiler.resolve_node(self.child_type_list)
        compiler.resolve_node(self.child_empty_reply_type)
        compiler.resolve_node(self.child_plugin_list)
        compiler.resolve_node(self.child_body_part_list)

        self._resolved = True

    def get_unique_type_name(self, base_name):
        '''
        Returns a unique type name, to be used with types created from
        plug-ins manifests
        '''
        name = base_name + unicode(self.next_unique)
        self.next_unique += 1
        return name
