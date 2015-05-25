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

from smartanthill_zc import builtin
from smartanthill_zc.encode import Encoding, get_encoding_min_max
from smartanthill_zc.node import (DeclarationListNode, Node,
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
        Created a new FieldTypeDeclNode from data in att dictionary
        '''
        t = ''.join(att['type'].split())  # to remove whites

        field_name = self.get_unique_type_name()
        field = compiler.init_node(builtin.FieldTypeDeclNode(field_name), et)

        encoding = None
        max_bytes = 0
        if (t == 'encoded-signed-int[max=2]' or
                t == 'encoded-signed-int<max=2>'):
            encoding = Encoding.SIGNED_INT
            max_bytes = 2
        elif (t == 'encoded-unsigned-int[max=2]' or
              t == 'encoded-unsigned-int<max=2>'):
            encoding = Encoding.UNSIGNED_INT
            max_bytes = 2
        else:
            compiler.report_error(et, "Unknown type '%s'" % t)
            compiler.raise_error()

        min_value, max_value = get_encoding_min_max(encoding, max_bytes)
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

        for current in ['<', '>', '<=', '>=', '==', '!=']:

            # field to literal
            op = compiler.init_node(
                builtin.FieldToLiteralCompDeclNode(current, '_zc_boolean'), et)
            op.set_parameter_list(
                builtin.create_parameter_list(
                    compiler, et, [field_name, '_zc_number_literal']))
            self.child_operator_list.add_declaration(op)

            # and literal to field
            op2 = compiler.init_node(
                builtin.FieldToLiteralCompDeclNode(current, '_zc_boolean'), et)
            op2.set_parameter_list(
                builtin.create_parameter_list(
                    compiler, et, ['_zc_number_literal', field_name]))
            op2.swap_flag = True
            self.child_operator_list.add_declaration(op2)

        return field

    def create_linear_conversion_float(self, in0, out0, in1, out1):
        '''
        Created a new LinearConvertionFloat
        TODO add cache, and verify if already created
        '''
        # pylint: disable=no-self-use

        meaning = LinearConvertionFloat()
        meaning.set_points(in0, out0, in1, out1)
        return meaning


class LinearConvertionFloat(object):

    '''
    Linear scale helper
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._a = 0
        self._b = 0

    def set_points(self, in0, out0, in1, out1):
        '''
        Initialize the scale by two points
        '''
        in0 = int(in0)
        in1 = int(in1)
        out0 = float(out0)
        out1 = float(out1)
        self._a = (out1 - out0) / (in1 - in0)
        self._b = out0 - self._a * in0

    def inverse(self, value):
        '''
        Returns inverse scaling of value
        This method rounds result to exact integer (i.e. 3.0 )
        or half way (i.e. 4.5)
        '''

        inv = (value - self._b) / self._a
        inv2 = round(inv * 2) / 2  # magic trick to remove round error
        return inv2


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
        assert isinstance(child, builtin.ParameterListNode)
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
