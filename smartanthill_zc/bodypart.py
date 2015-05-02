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

from smartanthill_zc.builtin import ParameterListNode
from smartanthill_zc.node import (LiteralCastExprNode, Node, ResolutionHelper,
                                  TypeDeclNode)


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

    def set_type_list(self, node):
        '''
        type_list setter
        '''
        assert isinstance(node, DeclarationListNode)
        node.set_parent(self)
        self.child_type_list = node

    def set_operator_list(self, node):
        '''
        operator_list setter
        '''
        assert isinstance(node, DeclarationListNode)
        node.set_parent(self)
        self.child_operator_list = node

    def get_unique_type_name(self):
        '''
        Returns a unique type name, to be used with types created from
        plug-ins manifests
        '''
        name = u'_zc_field_type_' + unicode(self.next_unique)
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

    def create_field_type(self, compiler, ctx, att):
        '''
        Created a new FieldTypeDeclNode from data in att dictionary or
        returns a previously created one if all data matches
        '''
        t = ''.join(att['type'].split())  # to remove whites

        field_name = self.get_unique_type_name()
        field = compiler.init_node(FieldTypeDeclNode(field_name), ctx)

        encoding = None
        if t == 'encoded-signed-int&lt;max=2&gt;':
            encoding = Encoding.SIGNED_INT_2
        elif t == 'encoded-unsigned-int&lt;max=2&gt;':
            encoding = Encoding.UNSIGNED_INT_2
        else:
            compiler.report_error(ctx, "Unknown type '%s'" % t)
            compiler.raise_error()

        min_value = encoding.min_value
        try:
            if 'min' in att:
                min_value = long(att['min'])
                if min_value < encoding.min_value:
                    compiler.report_error(
                        ctx, "Declared min (%s) is lower that type min (%s)"
                        % (min_value, encoding.min_value))
                    min_value = encoding.min_value

        except:
            compiler.report_error(ctx, "Bad min '%s'" % att['min'])

        max_value = encoding.max_value
        try:
            if 'max' in att:
                max_value = long(att['max'])
                if max_value > encoding.max_value:
                    compiler.report_error(
                        ctx, "Declared max (%s) is grater than type min (%s)"
                        % (max_value, encoding.max_value))
                    max_value = encoding.max_value
        except:
            compiler.report_error(ctx, "Bad max '%s'" % att['max'])

        field.encoding = encoding
        field.min_value = min_value
        field.max_value = max_value

        self.child_type_list.add_declaration(field)

        for current in [u'<', u'>', u'<=', u'>=']:
            op = compiler.init_node(
                FieldToLiteralComparisonOpDeclNode(current, u'_zc_bool'), ctx)
            op.set_parameter_list(
                create_parameter_list(compiler, ctx,
                                      [field_name, u'_zc_number_literal']))
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
        assert not self._resolved

        scope = self.get_root_scope()
        scope.add_type(compiler, self.str_type_name, self)

        self._number_type = scope.lookup_type(u'_zc_number')
        self._resolved = True

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

        c = compiler.init_node(LiteralCastExprNode(), expr.ctx)
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
        self.str_name = name
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

    def add_element(self, node):
        '''
        argument adder
        '''
        assert isinstance(node, MemberDeclNode)
        node.set_parent(self)
        self.childs_elements.append(node)

    def resolve(self, compiler):
        '''
        resolve
        '''
        assert not self._resolved
        for elem in self.childs_elements:
            compiler.resolve_node(elem)

        self.make_field_sequences()

        self.get_root_scope().add_type(compiler, self.str_type_name, self)
        self._resolved = True

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
            if current.str_name == name:
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
        self.str_plugin_name = ''
        self.bodypart_id = 0L

    def set_parameter_list(self, node):
        '''
        parameter_list setter
        '''
        assert isinstance(node, ParameterListNode)
        node.set_parent(self)
        self.child_parameter_list = node

    def set_reply_type(self, node):
        '''
        reply_type setter
        '''
        assert isinstance(node, MessageTypeDeclNode)
        node.set_parent(self)
        self.child_reply_type = node

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''

        compiler.resolve_node(self.child_parameter_list)
        compiler.resolve_node(self.child_reply_type)

        scope = self.get_root_scope()
        scope.add_plugin(compiler, self.str_plugin_name, self)

        return self.child_reply_type

    def lookup_method(self, name):
        '''
        Method look-up, currently only 'Execute' method is supported
        and is implemented by this same instance.
        This will change if more than one method support is required
        '''
        return self if name == "Execute" else None

    def get_data_value(self, encoder, node):
        '''
        Here we must encode the caller arguments as it was specified in
        plug-in manifest for this body part
        '''
        # pylint: disable=no-self-use
        result = []

        for current in node.child_argument_list.childs_arguments:
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

    def set_field_type_factory(self, node):
        '''
        parameter_list setter
        '''
        assert isinstance(node, FieldTypeFactoryNode)
        node.set_parent(self)
        self.child_field_type_factory = node

    def set_body_part_list(self, node):
        '''
        parameter_list setter
        '''
        assert isinstance(node, DeclarationListNode)
        node.set_parent(self)
        self.child_body_part_list = node

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

    def static_evaluate(self, compiler, node, arg_list):
        '''
        Do replace generic OperatorExprNode by a much more specific
        FieldToLiteralComparisonOpExprNode
        '''

        assert isinstance(node, OperatorExprNode)
        assert len(arg_list.childs_arguments) == 2

        member = arg_list.childs_arguments[0]
        assert isinstance(member.get_type(), FieldTypeDeclNode)

        orig_value = arg_list.childs_arguments[1].get_static_value()
        value = member.get_type().inverse_meaning(orig_value)

        assert isinstance(member, MemberAccessExprNode)
        reply_expr = member.child_expression
        field_sequence = member.get_member_field_sequence()

        expr = compiler.init_node(
            FieldToLiteralComparisonOpExprNode(), node.ctx)

        expr.set_replaced(node)
        expr.ref_declaration = self
        expr.ref_reply_expr = reply_expr

        expr.field_sequence = field_sequence
        expr.value = value

        expr.set_type(self.get_type())

        return expr


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

    def set_replaced(self, node):
        '''
        replaced setter
        '''
        assert isinstance(node, ExpressionNode)
        node.set_parent(self)
        self.child_replaced = node
