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

import smartanthill_zc.node as node

from smartanthill_zc.node import (Node, ResolutionHelper, TypeDeclNode,
    ExpressionNode, DeclarationListNode)
from smartanthill_zc.builtin import (ParameterListNode, OperatorDeclNode,
    create_parameter_list)


class _EncodingImpl(object):

    '''
    Helper class to hold encodings extra data
    '''

    def __init__(self, name, code, min_value, max_value):
        '''
        Constructor
        '''
        self.name = name
        self.code = code
        self.min_value = min_value
        self.max_value = max_value

    def __repr__(self):
        '''
        String representation
        '''
        return self.name


class Encoding(object):

    '''
    Enum like, for FIELD-SEQUENCE
    '''
    END_OF_SEQUENCE = _EncodingImpl('<eos>', 0, 0, 0)
    SIGNED_INT_2 = _EncodingImpl('SIGNED_INT', 1, -32768L, 32767L)
    UNSIGNED_INT_2 = _EncodingImpl('UNSIGNED_INT', 2, 0L, 65535)


def field_sequence_to_str(field_sequence):
    '''
    makes text representation of a FIELD-SEQUENCE
    '''
    result = []
    for current in field_sequence:
        result.append(current.name)

    return ','.join(result)


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
        self.next_unique = 1
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

    def get_unique_type_name(self):
        '''
        Returns a unique type name, to be used with types created from
        plug-ins manifests
        '''
        name = '_zc_field_type_' + unicode(self.next_unique)
        self.next_unique += 1
        return name

    def resolve(self, compiler):
        '''
        resolve
        '''
        assert not self._resolved
        compiler.resolve_node(self.child_type_list)
        compiler.resolve_node(self.child_operator_list)
        self._resolved = True

    def create_field_type(self, compiler, et, att):
        '''
        Created a new FieldTypeDeclNode from data in att dictionary or
        returns a previously created one if all data matches
        '''
        t = ''.join(att['type'].split())  # to remove whites

        field_name = self.get_unique_type_name()
        field = compiler.init_node(FieldTypeDeclNode(field_name), et)

        encoding = None
        if t == 'encoded-signed-int<max=2>':
            encoding = Encoding.SIGNED_INT_2
        elif t == 'encoded-unsigned-int<max=2>S':
            encoding = Encoding.UNSIGNED_INT_2
        else:
            compiler.report_error(et, "Unknown type '%s'" % t)
            compiler.raise_error()

        min_value = encoding.min_value
        try:
            if 'min' in att:
                min_value = long(att['min'])
                if min_value < encoding.min_value:
                    compiler.report_error(
                        et, "Declared min (%s) is lower that type min (%s)"
                        % (min_value, encoding.min_value))
                    min_value = encoding.min_value

        except:
            compiler.report_error(et, "Bad min '%s'" % att['min'])

        max_value = encoding.max_value
        try:
            if 'max' in att:
                max_value = long(att['max'])
                if max_value > encoding.max_value:
                    compiler.report_error(
                        et, "Declared max (%s) is grater than type min (%s)"
                        % (max_value, encoding.max_value))
                    max_value = encoding.max_value
        except:
            compiler.report_error(et, "Bad max '%s'" % att['max'])

        field.encoding = encoding
        field.min_value = min_value
        field.max_value = max_value

        self.child_type_list.add_declaration(field)

        for current in ['<', '>', '<=', '>=']:
            op = compiler.init_node(
                FieldToLiteralComparisonOpDeclNode(current, '_zc_bool'), et)
            op.set_parameter_list(
                create_parameter_list(compiler, et,
                                      [field_name, '_zc_number_literal']))
            self.child_operator_list.add_declaration(op)

        return field


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

        c = compiler.init_node(node.LiteralCastExprNode(), expr.ctx)
        c.set_expression(expr)
        c.set_type(target_type)

        return c

    def inverse_meaning(self, value):
        '''
        TODO add the inverse function of meaning here
        Used for mapping literal number for comparison with
        value returned by a body-part
        '''
        assert value
        return value


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

            fs_current = list(fs)
            fs_current.append(Encoding.END_OF_SEQUENCE)

            current.field_sequence = fs_current

        fs.append(Encoding.END_OF_SEQUENCE)
        self.field_sequence = fs


class BodyPartDeclNode(Node, ResolutionHelper):

    '''
    Declaration of a body-part
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BodyPartDeclNode, self).__init__()
        self.child_parameter_list = None
        self.child_reply_type = None
        self.txt_name = None
        self.bodypart_id = 0L

    def set_parameter_list(self, child):
        '''
        parameter_list setter
        '''
        assert isinstance(child, ParameterListNode)
        child.set_parent(self)
        self.child_parameter_list = child

    def set_reply_type(self, child):
        '''
        reply_type setter
        '''
        assert isinstance(child, MessageTypeDeclNode)
        child.set_parent(self)
        self.child_reply_type = child

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''

        compiler.resolve_node(self.child_parameter_list)
        compiler.resolve_node(self.child_reply_type)

        scope = self.get_root_scope()
        scope.add_plugin(compiler, self.txt_name, self)

        return self.child_reply_type

    def lookup_method(self, name):
        '''
        Method look-up, currently only 'Execute' method is supported
        and is implemented by this same instance.
        This will change if more than one method support is required
        '''
        return self if name == "Execute" else None

    def get_data_value(self, encoder, caller):
        '''
        Here we must encode the caller arguments as it was specified in
        plug-in manifest for this body part
        '''
        # pylint: disable=no-self-use
        result = []

        for current in caller.child_argument_list.childs_arguments:
            enc = encoder.encode_unsigned_int(2, current.get_static_value())
            result.extend(enc)

        return result


def create_body_parts_manager(compiler, ctx):
    '''
    Creates and initializes a BodyPartsManagerNode instance
    '''
    manager = compiler.init_node(BodyPartsManagerNode(), ctx)
    manager.set_body_part_list(compiler.init_node(DeclarationListNode(), ctx))

    factory = compiler.init_node(FieldTypeFactoryNode(), ctx)
    factory.set_type_list(compiler.init_node(DeclarationListNode(), ctx))
    factory.set_operator_list(compiler.init_node(DeclarationListNode(), ctx))

    manager.set_field_type_factory(factory)

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
        self.child_body_part_list = None
        self._resolved = False

    def set_field_type_factory(self, child):
        '''
        parameter_list setter
        '''
        assert isinstance(child, FieldTypeFactoryNode)
        child.set_parent(self)
        self.child_field_type_factory = child

    def set_body_part_list(self, child):
        '''
        parameter_list setter
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
        compiler.resolve_node(self.child_body_part_list)
        self._resolved = True


class FieldToLiteralComparisonOpDeclNode(OperatorDeclNode):

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
        super(FieldToLiteralComparisonOpDeclNode, self).__init__(
            operator, type_name)

    def static_evaluate(self, compiler, expr, arg_list):
        '''
        Do replace generic OperatorExprNode by a much more specific
        FieldToLiteralComparisonOpExprNode
        '''

        assert isinstance(expr, node.OperatorExprNode)
        assert len(arg_list.childs_arguments) == 2

        member = arg_list.childs_arguments[0]
        assert isinstance(member.get_type(), FieldTypeDeclNode)

        orig_value = arg_list.childs_arguments[1].get_static_value()
        value = member.get_type().inverse_meaning(orig_value)

        assert isinstance(member, node.MemberAccessExprNode)
        reply_expr = member.child_expression
        field_sequence = member.get_member_field_sequence()

        result = compiler.init_node(
            FieldToLiteralComparisonOpExprNode(), expr.ctx)

        result.set_replaced(expr)
        result.ref_declaration = self
        result.ref_reply_expr = reply_expr

        result.field_sequence = field_sequence
        result.value = value

        result.set_type(self.get_type())

        return result


class FieldToLiteralComparisonOpExprNode(ExpressionNode):

    '''
    Node class representing a very special operator comparison expression
    between a reply field and a number literal.
    This kind of expression is created from a regular OperatorExprNode
    by FieldToLiteralComparisonOpDeclNode for all expression
    This allows easier detection of this special comparison at a later time
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FieldToLiteralComparisonOpExprNode, self).__init__()
        self.child_replaced = None
        self.ref_declaration = None
        self.ref_reply_expr = None
#        self.operator = None
        self.field_sequence = None
        self.value = None

    def set_replaced(self, child):
        '''
        replaced setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_replaced = child