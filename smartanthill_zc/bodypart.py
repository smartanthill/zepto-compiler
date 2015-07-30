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

from smartanthill_zc import expression, encode, node, comparison
from smartanthill_zc.encode import Encoding
from smartanthill_zc.lookup import RootScope
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
        f2l = create_field_to_literal_comparison(
            compiler, ctx, field_type.txt_name)
        self.child_operator_list.add_declaration_list(f2l)

        for current in self.child_type_list.childs_declarations:
            f2f = create_field_to_field_comparison(
                compiler, ctx, field_type.txt_name, current)
            self.child_operator_list.add_declaration_list(f2f)

        self.child_type_list.add_declaration(field_type)


class EncodingHelper(object):

    '''
    Integer encoding helper
    '''

    def __init__(self, encoding, min_value, max_value):
        '''
        Constructor
        '''
        assert min_value <= max_value
        self.encoding = encoding
        self._min_value = min_value
        self._max_value = max_value

    def encode_value(self, compiler, ctx, value):
        '''
        Check value range and encode
        '''
        if value < self._min_value or value > self._max_value:
            compiler.report_error(ctx, 'Value %s outside valid range [%s, %s]',
                                  value, self._min_value, self._max_value)
            value = self._min_value

        if self.encoding == Encoding.UNSIGNED_INT:
            return encode.encode_unsigned_int(value)

        elif self.encoding == Encoding.SIGNED_INT:
            return encode.encode_signed_int(value)
        else:
            assert False

    def decode_value(self, reversed_data):
        '''
        Decode value from data, returns value and bytes read
        '''

        if self.encoding == Encoding.UNSIGNED_INT:
            return encode.decode_unsigned_int(reversed_data)

        elif self.encoding == Encoding.SIGNED_INT:
            return encode.decode_signed_int(reversed_data)
        else:
            assert False


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

    def apply(self, value):
        '''
        Returns scaling of value
        '''
        return value * self._a + self._b

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
        self._number_type = None

    def resolve(self, compiler):
        '''
        resolve
        '''
        self._number_type = self.get_scope(RootScope).lookup_type('_zc_number')
        super(FieldTypeDeclNode, self).resolve(compiler)

    def can_cast_to(self, target_type):
        '''
        This type can be casted to number, by inserting appropiate scaling
        '''
        return self._number_type == target_type

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
        if self.encoding.encoding in [Encoding.SIGNED_INT,
                                      Encoding.UNSIGNED_INT]:
            return math.floor(value + 1)
        else:
            assert False

    def next_down(self, value):
        '''
        Decrements value by the minimum representable amount
        '''
        # TODO check range
        if self.encoding.encoding in [Encoding.SIGNED_INT,
                                      Encoding.UNSIGNED_INT]:
            return math.ceil(value - 1)
        else:
            assert False

    def process_reverse(self, reversed_data):
        '''
        Process response data, data should be in reversed order
        '''
        value = self.encoding.decode_value(reversed_data)

        return self.meaning.apply(value) if self.meaning else value


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

    def process_reverse_response(self, reversed_data):
        '''
        Process response data
        '''
        result = {}
        for each in self.childs_elements:
            current = each.ref_field_type.process_reverse(reversed_data)
            result[each.txt_name] = current

        return result

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
        self.ref_number_literal_type = None

    def resolve(self, compiler):
        '''
        resolve
        '''
        self.ref_number_literal_type = self.get_scope(RootScope).lookup_type(
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
        assert isinstance(child, node.ParameterListNode)
        child.set_parent(self)
        self.child_parameter_list = child

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''

        compiler.resolve_node(self.child_parameter_list)
        return self.get_scope(RootScope).lookup_type(self.txt_type_name)

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
        self.get_scope(RootScope).add_bodypart(compiler, self.txt_name, self)

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
            node.create_parameter_list(
                compiler, ctx, [field_name, '_zc_number_literal']))
        result.append(op)

        # and literal to field
        op2 = compiler.init_node(
            FieldToLiteralCompDeclNode(current, '_zc_boolean'), ctx)
        op2.set_parameter_list(
            node.create_parameter_list(
                compiler, ctx, ['_zc_number_literal', field_name]))
        op2.swap_flag = True
        result.append(op2)

    return result


class FieldToLiteralCompDeclNode(comparison.OperatorDeclNode):

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
        result.txt_op = comparison.swap_comparison(
            expr.txt_operator, self.swap_flag)
        result.ref_declaration = self
        result.ref_member_expr = member

        result.literal_value = orig_value

        result.set_type(self.get_type())

        return result


class FieldToLiteralCompExprNode(node.ExpressionNode):

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
        assert isinstance(child, node.ExpressionNode)
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

        txt_op = comparison.negate_comparison(self.txt_op, negate)

        return comparison.simplify_comparison(txt_op, threshold, target_type)


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
            node.create_parameter_list(
                compiler, et, [field_name, other_field.txt_name]))
        result.append(op)

        op2 = compiler.init_node(
            FieldToFieldCompDeclNode(current, '_zc_boolean'), et)
        op2.set_parameter_list(
            node.create_parameter_list(
                compiler, et, [other_field.txt_name, field_name]))
        result.append(op2)

    return result


class FieldToFieldCompDeclNode(comparison.OperatorDeclNode):

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
        self._number_type = self.get_scope(RootScope).lookup_type('_zc_number')
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
        assert t0.can_cast_to(self._number_type)

        c0 = t0.insert_cast_to(compiler, self._number_type, a0)
        result.set_lhs(c0)

        a1 = expr.child_argument_list.childs_arguments[1]
        t1 = a1.get_type()
        assert t1.can_cast_to(self._number_type)

        c1 = t1.insert_cast_to(compiler, self._number_type, a1)
        result.set_rhs(c1)

        compiler.remove_node(expr.child_argument_list)
        compiler.remove_node(expr)

        result.set_type(self.get_type())

        return result


class FieldToFieldCompExprNode(node.ExpressionNode):

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
        assert isinstance(child, node.ExpressionNode)
        child.set_parent(self)
        self.child_lhs = child

    def set_rhs(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, node.ExpressionNode)
        child.set_parent(self)
        self.child_rhs = child

    def get_subcode_and_threshold(self, negate):
        '''
        simplify >= and <= to < and > by modifying literal value by epsilon
        Also apply an optional negation flag, as helper for code generator,
        since normally if body is executed when condition is true,
        but at implementation, body is jumped when condition is false
        '''
        op = comparison.negate_comparison(self.ref_decl.txt_operator, negate)

        ltype = self.child_lhs.get_type()

        return comparison.simplify_comparison(op, 0.0, ltype)
