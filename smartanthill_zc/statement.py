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


from smartanthill_zc import expression, node
from smartanthill_zc.lookup import StatementListScope
from smartanthill_zc.node import (ArgumentListNode, ExpressionNode,
                                  ResolutionHelper, StatementNode,
                                  expression_type_match, resolve_expression)


class StatementListStmtNode(StatementNode):

    '''
    Node class representing an statement list
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StatementListStmtNode, self).__init__()
        self.childs_statements = []
        self._scope = StatementListScope(self)
        self.has_flow_stmt = False

    def add_statement(self, child):
        '''
        statement adder
        '''
        if not child:
            assert False
        assert isinstance(child, StatementNode)
        child.set_parent(self)
        self.childs_statements.append(child)

    def resolve(self, compiler):
        for stmt in self.childs_statements:
            compiler.resolve_node(stmt)
            if self.has_flow_stmt:
                compiler.report_error(stmt.ctx, "Unreachable statement")
            if stmt.is_flow_stmt:
                self.has_flow_stmt = True

    def get_stmt_scope(self):
        ''''
        Returns this node scope
        '''
        return self._scope


def make_statement_list(compiler, stmt):
    '''
    If stmt is instance of StatementListStmtNode, returns stmt.
    Otherwise, creates and returns an StatementListStmtNode holding stmt

    This helper function is used to always use StatementListStmtNode as child
    of statements like if-else, or for loops, even when a single statement
    (without braces) is used.
    '''
    assert isinstance(stmt, StatementNode)

    if isinstance(stmt, StatementListStmtNode):
        return stmt

    stmt_list = compiler.init_node(StatementListStmtNode(), stmt.ctx)
    stmt_list.add_statement(stmt)

    return stmt_list


class NopStmtNode(StatementNode):

    '''
    Node class representing an empty statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NopStmtNode, self).__init__()

    def resolve(self, compiler):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        pass


class ErrorStmtNode(StatementNode):

    '''
    Node class representing a syntax error
    Used as a place holder when we can not return a real statement,
    and returning None is neither possible
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ErrorStmtNode, self).__init__()

    def resolve(self, compiler):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        assert False


class ReturnStmtNode(StatementNode):

    '''
    Node class representing 'return' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ReturnStmtNode, self).__init__()
        self.child_expression = None
        self.is_flow_stmt = True

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

    def resolve(self, compiler):
        resolve_expression(compiler, self, 'child_expression')

        if not self.child_expression.get_type().is_message_type():
            compiler.report_error(
                self.ctx, "Type not valid for reply message")

        self.get_return_scope().add_return_stmt(
            compiler, self.ctx, self.child_expression.get_type())


class VariableDeclarationStmtNode(StatementNode, ResolutionHelper):

    '''
    Node class representing variable declaration statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(VariableDeclarationStmtNode, self).__init__()
        self.txt_name = None
        self.flg_root_scope = False
        self.child_initializer = None

    def set_initializer(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_initializer = child

    def do_resolve_declaration(self, compiler):

        resolve_expression(compiler, self, 'child_initializer')
        # we are adding variable name after resolution of initializer
        # because we don't allow that kind of resolution cycle
        if self.flg_root_scope:
            self.get_root_scope().add_parameter(
                compiler, self.txt_name, self)
        else:
            self.get_stmt_scope().add_variable(
                compiler, self.txt_name, self)

        return self.child_initializer.get_type()


class ExpressionStmtNode(StatementNode):

    '''
    Node class representing an statement that is an expression
    Used for assignments
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ExpressionStmtNode, self).__init__()
        self.child_expression = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

    def resolve(self, compiler):
        resolve_expression(compiler, self, 'child_expression')


class IfElseStmtNode(StatementNode):

    '''
    Node class representing 'if' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(IfElseStmtNode, self).__init__()
        self.child_expression = None
        self.child_if_branch = None
        self.child_else_branch = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

    def set_if_branch(self, child):
        '''
        if_branch setter
        '''
        assert isinstance(child, StatementListStmtNode)
        child.set_parent(self)
        self.child_if_branch = child

    def set_else_branch(self, child):
        '''
        else_branch setter
        '''
        assert isinstance(child, StatementListStmtNode)
        child.set_parent(self)
        self.child_else_branch = child

    def resolve(self, compiler):
        resolve_expression(compiler, self, 'child_expression')
        compiler.resolve_node(self.child_if_branch)
        compiler.resolve_node(self.child_else_branch)

        t = self.get_root_scope().lookup_type('_zc_boolean')

        if not expression_type_match(compiler, t, self, 'child_expression'):
            compiler.report_error(
                self.ctx, "Condition can not be evaluated to boolean")
            # no need to raise here


class McuSleepStmtNode(StatementNode):

    '''
    Node class representing 'mcu_sleep' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(McuSleepStmtNode, self).__init__()
        self.child_argument_list = None
        self._ref_decl = None

    def set_argument_list(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ArgumentListNode)
        child.set_parent(self)
        self.child_argument_list = child

    def resolve(self, compiler):
        compiler.resolve_node(self.child_argument_list)
        decl = self.get_root_scope().lookup_function(
            'mcu_sleep')
        assert decl  # is built in function

        self.child_argument_list.make_match(compiler,
                                            decl.child_parameter_list)

        self._ref_decl = decl

    def get_delay_value(self):
        # if resultion was ok, then we have a single arg, and it is a literal
        assert len(self.child_argument_list.childs_arguments) == 1
        v = self.child_argument_list.childs_arguments[0].get_static_value()
        assert v
        return v


class SimpleForStmtNode(StatementNode):

    '''
    Node class representing a very simple for loop
    declaring a counter variable, with begin and end as integer constants
    incrementing by one at each loop.

    for(int i = 0; i < *N*; i++) {}
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(SimpleForStmtNode, self).__init__()
        self.txt_name = None
        self.child_begin_expression = None
        self.child_end_expression = None
        self.child_statement_list = None
        self._scope = StatementListScope(self)

    def set_begin_expression(self, child):
        '''
        begin_expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_begin_expression = child

    def set_end_expression(self, child):
        '''
        end_expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_end_expression = child

    def set_statement_list(self, child):
        '''
        statement_list setter
        '''
        assert isinstance(child, StatementListStmtNode)
        child.set_parent(self)
        self.child_statement_list = child

    def get_stmt_scope(self):
        ''''
        Returns this node scope
        '''
        assert self._scope
        return self._scope

    def resolve(self, compiler):
        resolve_expression(compiler, self, 'child_begin_expression')
        resolve_expression(compiler, self, 'child_end_expression')
        compiler.resolve_node(self.child_statement_list)


def create_parameters(compiler, data, ctx):
    '''
    Creates an StatementListStmtNode and populates it with
    VariableDeclarationStmtNode with data from dictionary.
    Used for parameters
    '''

    decls = compiler.init_node(node.DeclarationListNode(), ctx)

    if data is not None:
        for key, value in data.iteritems():

            assert isinstance(key, str)
            var = compiler.init_node(VariableDeclarationStmtNode(), ctx)
            var.txt_name = key
            var.flg_root_scope = True

            if isinstance(value, (int, long)):
                expr = compiler.init_node(
                    expression.NumberLiteralExprNode(), ctx)
                expr.set_literal(str(value))
                var.set_initializer(expr)
            else:
                compiler.report_error(
                    ctx, "Invalid data type '%s' at parameter '%s'",
                    type(value).__name__, key)

            decls.add_declaration(var)

    compiler.check_stage('parameter')

    return decls
