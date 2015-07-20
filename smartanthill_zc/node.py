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


from smartanthill_zc import errors
from smartanthill_zc.lookup import ReturnStmtScope, RootScope


class ResolutionHelper(object):

    '''
    Helper base class provides resolution cycle safety
    It must be used by all classes that can be called to resolve
    on demand (as the result of some look-up)
    '''

    _NOT_RESOLVED = 0
    _RESOLVING_NOW = 1
    _RESOLVED_OK = 2
    _RESOLUTION_ERROR = 3

    def __init__(self):
        '''
        Constructor
        '''
        super(ResolutionHelper, self).__init__()
        self._resolved_flag = self._NOT_RESOLVED
        self._resolved_type = None

    def resolve(self, compiler):
        '''
        Resolve, will call template method do_resolve_declaration that needs to
        be at implementing class
        '''
        try:
            if self._resolved_flag == self._NOT_RESOLVED:
                self._resolved_flag = self._RESOLVING_NOW
                self._resolved_type = self.do_resolve_declaration(compiler)
                assert self._resolved_type
                self._resolved_flag = self._RESOLVED_OK
            elif self._resolved_flag == self._RESOLVING_NOW:
                raise errors.ResolutionCycleError()
            elif self._resolved_flag == self._RESOLVED_OK:
                pass
            elif self.resolved_flag == self._RESOLUTION_ERROR:
                pass
            else:
                assert False
        except:
            self._resolved_flag = self._RESOLUTION_ERROR
            self._resolved_type = None
            raise

    def get_type(self):
        '''
        Returns the type of this declaration, if resolve was not called before,
        or it did not complete properly, it will raise an error
        '''

        if self._resolved_flag == self._NOT_RESOLVED:
            raise errors.UnresolvedError()
        elif self._resolved_flag == self._RESOLVING_NOW:
            raise errors.ResolutionCycleError()
        elif self._resolved_flag == self._RESOLVED_OK:
            return self._resolved_type
        elif self._resolved_flag == self._RESOLUTION_ERROR:
            raise errors.PreviousResolutionError()
        else:
            assert False


class Node(object):

    '''
    Base class for all tree nodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(Node, self).__init__()
        self._parent = None
        self._resolved = False

    def get_stmt_scope(self):
        ''''
        Walks the tree up until if find an scope to return
        '''
        return self._parent.get_stmt_scope()

    def get_root_scope(self):
        ''''
         Walks the tree up, until a RootScope to return
         '''
        return self._parent.get_root_scope()

    def get_return_scope(self):
        '''
         Walks the tree up, until a ReturnStmtScope to return
        '''
        return self._parent.get_return_scope()

    def set_parent(self, parent):
        '''
        helper method for setting node parent
        '''
        self._parent = parent

    def get_parent(self):
        '''
        parent getter
        '''
        assert self._parent
        return self._parent


class StatementNode(Node):

    '''
    Base class for all statements nodes
    '''

    def __init__(self):
        super(StatementNode, self).__init__()
        self.is_flow_stmt = False


class ExpressionNode(Node):

    '''
    Base class for all expressions nodes
    '''

    def __init__(self):
        '''
        Never actually called, just let pylint happy
        '''
        super(ExpressionNode, self).__init__()
        self._resolved_type = None

    def resolve_expr(self, compiler):
        '''
        Base implementation of expression resolution template method
        Must be overrided or resolution type must be externally assigned
        '''
        del compiler
        assert self._resolved_type
        return None

    def set_type(self, resolved_type):
        '''
        Type setter, this method can be called only once.
        So type can not change
        '''

        assert resolved_type
        assert not self._resolved_type

        self._resolved_type = resolved_type

    def get_type(self):
        '''
        Returns the type of this expression
        '''
        assert self._resolved_type
        return self._resolved_type

    def assert_resolved(self):
        '''
        Asserts this instance has a resolved type
        '''
        assert self._resolved_type

    def get_static_value(self):
        # pylint: disable=no-self-use
        return None


def resolve_expression(compiler, parent, child_name):
    '''
    Resolve child expression by attribute name, to allow expression
    replacement
    '''

    expr = getattr(parent, child_name)
    if expr:
        replacement = expr.resolve_expr(compiler)
        if replacement and replacement != expr:
            assert isinstance(replacement, ExpressionNode)
            replacement.set_parent(parent)
            setattr(parent, child_name, replacement)

            # resolve again (replacement)
            resolve_expression(compiler, parent, child_name)
        else:
            expr.assert_resolved()


def resolve_expression_list(compiler, parent, expr_list, i):
    '''
    Resolve child expression list by index, to allow expression
    replacement
    '''
    replacement = expr_list[i].resolve_expr(compiler)

    if replacement and replacement != expr_list[i]:
        assert isinstance(replacement, ExpressionNode)
        replacement.set_parent(parent)
        expr_list[i] = replacement

        # resolve again (replacement)
        resolve_expression_list(compiler, parent, expr_list, i)
    else:
        expr_list[i].assert_resolved()


class TypeDeclNode(Node):

    '''
    Base class for types
    '''

    NO_MATCH = 0
    EXACT_MATCH = 1
    CAST_MATCH = 2

    def __init__(self, name):
        '''
        Constructor
        '''
        super(TypeDeclNode, self).__init__()
        self.txt_name = name
        self._resolved = False

    def resolve(self, compiler):
        '''
        Resolve
        '''
        assert not self._resolved
        self.get_root_scope().add_type(compiler, self.txt_name, self)
        self._resolved = True

    def can_cast_to(self, target_type):
        '''
        Base method for type casting
        If self can be casted to target_type returns True
        Otherwise returns False
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument

        return False

    def insert_cast_to(self, compiler, target_type, expr):
        '''
        Inserts a cast to the target type
        Base method will always fail
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument

        assert False

    def can_cast_from(self, source_type):
        '''
        Base method for type casting
        If self can be constructed from source_type returns True
        Otherwise returns False
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument

        return False

    def insert_cast_from(self, compiler, source_type, expr):
        '''
        Inserts a cast from the source type
        Base method will always fail
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument

        assert False

    def is_message_type(self):
        '''
        Types that can go to the reply buffer, should return true here
        Also implies that type knows how to marshall to binary format
        '''
        # pylint: disable=no-self-use
        return False

    def lookup_member(self, name):
        '''
        Base method for type member look up
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument

        return None


def expression_type_match(compiler, lhs_type, parent, child_name):
    '''
    Helper function for expression type matching
    If no match possible just returns false
    If exact match returns true
    If can match but needs cast, inserts cast and returns true
    '''
    expr = getattr(parent, child_name)
    expr_type = expr.get_type()

    if expr_type == lhs_type:
        return True
    elif expr_type.can_cast_to(lhs_type):
        cast = expr_type.insert_cast_to(compiler, lhs_type, expr)
        cast.set_parent(parent)
        setattr(parent, child_name, cast)
        return True
    else:
        return False


class RootNode(Node):

    '''
    Root node class used as root of the tree
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(RootNode, self).__init__()
        self.child_builtins = None
        self.child_bodyparts = None
        self.child_parameters = None
        self.child_source_program = None
        self._scope = RootScope(self)

    def get_root_scope(self):
        ''''
         Walks the tree up, until a RootScop to return
         '''
        return self._scope

    def set_builtins(self, child):
        '''
        built-ins setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_builtins = child

    def set_bodyparts(self, child):
        '''
        body-parts setter
        '''
        assert isinstance(child, Node)
        child.set_parent(self)
        self.child_bodyparts = child

    def set_parameters(self, child):
        '''
        parameters setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_parameters = child

    def set_source_program(self, child):
        '''
        program setter
        '''
        assert isinstance(child, SourceProgramNode)
        child.set_parent(self)
        self.child_source_program = child

    def resolve(self, compiler):
        # First built-ins
        compiler.resolve_node(self.child_builtins)
        # Next body-parts and parameters
        compiler.resolve_node(self.child_bodyparts)
        compiler.resolve_node(self.child_parameters)
        # Last user code
        compiler.resolve_node(self.child_source_program)


class DeclarationListNode(Node):

    '''
    Node class representing a list of declaration, used as container
    of built-ins and plug-ins data
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(DeclarationListNode, self).__init__()
        self.childs_declarations = []

    def add_declaration(self, child):
        '''
        statement adder
        '''
        assert child
        assert isinstance(child, Node)
        child.set_parent(self)
        self.childs_declarations.append(child)

    def add_declaration_list(self, childs):
        '''
        add each declaration in list helper
        '''
        for each in childs:
            self.add_declaration(each)

    def resolve(self, compiler):
        for decl in self.childs_declarations:
            compiler.resolve_node(decl)


class SourceProgramNode(Node):

    '''
    Node class container of a program, similar to a function but
    without parameters
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(SourceProgramNode, self).__init__()
        self.child_statement_list = None
        self._return_scope = ReturnStmtScope(self)

    def get_stmt_scope(self):
        ''''
        Returns None, do not try to further walk up
        '''
        return None

    def get_return_scope(self):
        '''
        Returns return scope
        Since we don't currently support a function node, RootNode will
        make its job
        '''
        return self._return_scope

    def set_statement_list(self, child):
        '''
        statement_list setter
        '''
        assert isinstance(child, StatementNode)
        child.set_parent(self)
        self.child_statement_list = child

    def resolve(self, compiler):
        compiler.resolve_node(self.child_statement_list)


class ArgumentListNode(Node):

    '''
    Node class used as container of arguments in function calls
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ArgumentListNode, self).__init__()
        self.childs_arguments = []

    def add_argument(self, child):
        '''
        argument adder
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.childs_arguments.append(child)

    def resolve(self, compiler):
        for i in range(len(self.childs_arguments)):
            resolve_expression_list(compiler, self, self.childs_arguments, i)

    def overload_filter(self, compiler, decl_list):
        '''
        From a list declarations, returns one that can match the arguments,
        if no candidate is found, reports error an raises
        '''
        exact_match = []
        cast_match = []
        for current in decl_list:
            r = self.can_match(current.child_parameter_list)

            if r == TypeDeclNode.NO_MATCH:
                pass
            elif r == TypeDeclNode.EXACT_MATCH:
                exact_match.append(current)
            elif r == TypeDeclNode.CAST_MATCH:
                cast_match.append(current)
            else:
                assert False

        if len(exact_match) == 1:
            return exact_match[0]
        elif len(exact_match) == 0:
            if len(cast_match) == 1:
                return cast_match[0]
            elif len(cast_match) == 0:
                compiler.report_error(
                    self.ctx, "None of candidates can match the arguments")
                compiler.raise_error()
            elif len(cast_match) > 1:
                compiler.report_error(
                    self.ctx, "More than a candidate can match the arguments")
                compiler.raise_error()
            else:
                assert False
        else:
            assert False

    def can_match(self, params):
        '''
        If this argument list can not used to initialize given argument list
        Returns TypeDeclNode.NO_MATCH when there is no chance to make it match
        TypeDeclNode.EXACT_MATCH when match does not need any cast
        and TypeDeclNode.CAST_MATCH when it can match but casting needed
        '''
        if len(self.childs_arguments) != params.get_size():
            return TypeDeclNode.NO_MATCH

        result = TypeDeclNode.EXACT_MATCH
        for i in range(len(self.childs_arguments)):

            source = self.childs_arguments[i].get_type()
            target = params.get_type_at(i)

            if source == target:
                pass
            elif source.can_cast_to(target):
                result = TypeDeclNode.CAST_MATCH
            elif target.can_cast_from(source):
                result = TypeDeclNode.CAST_MATCH
            else:
                return TypeDeclNode.NO_MATCH

        return result

    def make_match(self, compiler, params):
        '''
        Makes this argument list to initialize given declaration,
        inserting casts if required.
        '''

        if len(self.childs_arguments) != params.get_size():
            compiler.report_error(
                self.ctx, "Wrong number of arguments, given %s but need %s" % (
                    str(params.get_size()), str(len(self.childs_arguments))))
            compiler.raise_error()

        for i in range(len(self.childs_arguments)):
            target = params.get_type_at(i)
            source = self.childs_arguments[i].get_type()

            if source == target:
                pass
            elif source.can_cast_to(target):
                e = source.insert_cast_to(
                    compiler, target, self.childs_arguments[i])
                e.set_parent(self)
                self.childs_arguments[i] = e
            elif target.can_cast_from(source):
                e = target.insert_cast_from(
                    compiler, source, self.childs_arguments[i])
                e.set_parent(self)
                self.childs_arguments[i] = e
            else:
                # shouldn't reach here
                assert False
