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

from smartanthill_zc.node import Node, ResolutionHelper, TypeDeclNode
from smartanthill_zc.builtin import ParameterListNode


class _Encoding(object):

    '''
    Helper class to hold encodings extra data
    '''

    def __init__(self, min_value, max_value):
        '''
        Constructor
        '''
        self.min_value = min_value
        self.max_value = max_value


class FieldTypeDeclNode(TypeDeclNode):

    '''
    Types used for message fields
    '''

    SIGNED_INT_2 = _Encoding(-32768L, 32767L)
    UNSIGNED_INT_2 = _Encoding(0L, 65535)

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(FieldTypeDeclNode, self).__init__(type_name)
        self.encoding = 0
        self.meaning = None
        self.min_value = 0
        self.max_value = 0

    def set_encoding(self, encoding):
        self.encoding = encoding
        self.min_value = encoding.min_value
        self.max_value = encoding.max_value

    def resolve(self, compiler):
        '''
        resolve
        '''
        assert not self._resolved
        if self.max_value > self._encoding.max_value:
            compiler.report_error(self.ctx, "Declared max of %s is above type"
                                  " max of '%s'" %
                                  (self.max_value,
                                   self._encoding.max_value))

        if self.min_value < self._encoding.min_value:
            compiler.report_error(self.ctx, "Declared min of %s is under type"
                                  " min of '%s'" %
                                  (self.min_value,
                                   self._encoding.min_value))

        self.get_root_scope().add_type(compiler, self.str_type_name, self)
        self._resolved = True


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
        self.child_field_type = None

    def set_field_type(self, node):
        '''
        field_type setter
        '''
        assert isinstance(node, FieldTypeDeclNode)
        node.set_parent(self)
        self.child_field_type = node

    def do_resolve_declaration(self, compiler):
        '''
        Template method from ResolutionHelper
        '''
        del compiler
        return self.child_field_type


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
#        self._already_resolved = False

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

        self.get_root_scope().add_type(compiler, self.str_type_name, self)
        self._resolved = True

    def is_message_type(self):
        '''
        All instances of this type are valid response types
        '''
        return True

    def lookup_member_type(self, name):
        '''
        Finds a member of this type, by name
        '''
        for current in self.childs_elements:
            if current.str_name == name:
                return current.get_type()

        return None


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

    def can_match_arguments(self, compiler, arg_list):
        '''
        Returns if the given arguments can be used to call this function
        '''
        return self.child_parameter_list.can_match_arguments(compiler,
                                                             arg_list)

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


class BodyPartListNode(Node):

    '''
    Container for body-parts
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BodyPartListNode, self).__init__()
        self.childs_elements = []
        self._resolved = False

    def add_element(self, node):
        '''
        element adder
        '''
        assert isinstance(node, BodyPartDeclNode)
        node.set_parent(self)
        self.childs_elements.append(node)

    def resolve(self, compiler):
        '''
        resolve
        '''
        assert not self._resolved
        for elem in self.childs_elements:
            compiler.resolve_node(elem)

        self._resolved = True
