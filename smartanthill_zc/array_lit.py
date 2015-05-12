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


from smartanthill_zc.node import (ExpressionNode, resolve_expression_list,
                                  TypeDeclNode)


def _create_array_type_name(expressions):
    '''
    Creates the name of an array type, from a list of expressions
    '''
    txts = []
    for current in expressions:
        txts.append(current.get_type().txt_name)

    name = '_zc_array<%s>' % ','.join(txts)
    return name


class ArrayMessageTypeDeclNode(TypeDeclNode):

    '''
    Aggregate of message type, used with array return
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(ArrayMessageTypeDeclNode, self).__init__(type_name)
        self.refs_element_types = []
        self.field_sequence = None

    def resolve(self, compiler):
        '''
        resolve
        '''
        fs = []
        for elem in self.refs_element_types:
            fs.extend(elem.field_sequence)

        self.field_sequence = tuple(fs)
        super(ArrayMessageTypeDeclNode, self).resolve(compiler)

    def is_message_type(self):
        '''
        All instances of this type are valid response types
        '''
        return True


class ArrayLiteralExprNode(ExpressionNode):

    '''
    Node class representing an array literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ArrayLiteralExprNode, self).__init__()
        self.childs_expressions = []
        self.child_expression_type = None

    def add_expression(self, child):
        '''
        argument adder
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.childs_expressions.append(child)

    def set_expression_type(self, child):
        '''
        expression_type setter
        TODO the fisrt expression to create the type, is the owner
        '''
        assert isinstance(child, TypeDeclNode)
        child.set_parent(self)
        self.child_expression_type = child

    def resolve_expr(self, compiler):
        for i in range(len(self.childs_expressions)):
            resolve_expression_list(compiler, self, self.childs_expressions, i)

        scope = self.get_root_scope()

        name = _create_array_type_name(self.childs_expressions)
        t = scope.lookup_type(name)
        if not t:
            t = ArrayMessageTypeDeclNode(name)
            for current in self.childs_expressions:
                t.refs_element_types.append(current.get_type())

            # The first expression to create the node, is the parent
            self.set_expression_type(t)
            compiler.resolve_node(t)

        self.set_type(t)
        return None
