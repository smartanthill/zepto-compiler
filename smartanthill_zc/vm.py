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

from smartanthill_zc import expression
from smartanthill_zc.op_node import (ExecOpNode, ExitOpNode, McuSleepOpNode,
                                     OpListNode, TargetProgramNode)
from smartanthill_zc.visitor import NodeVisitor, visit_node


def convert_to_zepto_vm_one(compiler, root):
    '''
    Process source program and creates a target code tree suitable to run
    at a Zepto VM Level One
    '''
    v = _ZeptoVmOneVisitor(compiler)
    visit_node(v, root.child_program)

    target = v.finish()
    compiler.check_stage('zepto_vm_one')
    return target


class _VmLevelImpl(object):

    '''
    Helper class to map vm levels, with their names and description
    '''

    def __init__(self, name):
        self.name = name
        self.fullname = "Zepto VM Level " + name


class Level(object):

    '''
    Enum like, for vm levels
    '''
    ONE = _VmLevelImpl('One')
    TINY = _VmLevelImpl('Tiny')
    SMALL = _VmLevelImpl('Small')
    MEDIUM = _VmLevelImpl('Medium')


class ReplyBufferRef(object):

    def __init__(self, index):
        self._index = index
        self._valid = True

    def invalidate(self):
        self._valid = False


class ReplyBuffer(object):

    def __init__(self):

        self._buffer = []
        self._buffer = []
        self._references = []

    def push_reply(self, data_type, data):

        ref = ReplyBufferRef(len(self._buffer))
        self._buffer.append((data_type, data))
        return ref

    def pop_replys(self, count):
        if count == 0:
            for current in self._references:
                current.invalidate()

            self._buffer = []
            self._references = []
        else:
            assert False

    def match_reply_type(self, return_types):

        if len(return_types) != len(self._buffer):
            return False

        for i in range(len(return_types)):
            if return_types[i] != self._buffer[i][0]:
                return False

        return True


class _ZeptoVmOneVisitor(NodeVisitor):

    '''
    Visitor class for a Zepto VM Level One
    This visitor goes through the source tree and creates a target tree

    '''
    VM = Level.ONE

    def __init__(self, compiler):
        '''
        Constructor
        '''
        self._compiler = compiler
        self._vm = Level.ONE

        self._target = compiler.init_node(
            TargetProgramNode(), compiler.BUILTIN)
        self._op_list = compiler.init_node(OpListNode(), compiler.BUILTIN)

        self._target.set_op_list(self._op_list)
        self._target.vm_level = self._vm

        self._exits = []
        self._mcusleep_invoked = False

    def _add_exit(self, node):
        '''
        Keep a list of EXIT ops
        '''
        self._exits.append(node)

    def finish(self):
        '''
        Finished visiting nodes, make all required adjustments and return
        the ops list
        '''

        self._target.mcusleep_invoked = self._mcusleep_invoked

        for each in self._exits:
            if self._mcusleep_invoked:
                each.set_is_first()
            else:
                each.set_is_last()

        if self._op_list.childs_operations[-1] == self._exits[-1]:
            self._exits[-1].try_make_implicit()

        return self._target

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._compiler.report_error(node.ctx, "Statement not supported by "
                                    + self.VM.fullname)

    def visit_ProgramNode(self, node):

        fs = node.get_return_scope().get_return_type().field_sequence
        self._target.reply_field_sequence = fs
        visit_node(self, node.child_statement_list)

    def visit_StatementListStmtNode(self, node):
        for each in node.childs_statements:
            visit_node(self, each)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_ReturnStmtNode(self, node):
        # pylint: disable=unidiomatic-typecheck
        if type(node.child_expression) is expression.BodyPartCallExprNode:
            visit_node(self, node.child_expression)
        else:
            self._compiler.report_error(
                node.ctx, "Expression at 'return' statement could not be "
                "resolved for " + self.VM.fullname)

        op = self._compiler.init_node(ExitOpNode(), node.ctx)

        self._op_list.add_operation(op)
        self._add_exit(op)

    def visit_McuSleepStmtNode(self, node):
        op = self._compiler.init_node(McuSleepOpNode(), node.ctx)
        op.sec_delay = node.get_delay_value()

        self._op_list.add_operation(op)
        self._mcusleep_invoked = True

    def visit_BodyPartCallExprNode(self, node):
        op = self._compiler.init_node(ExecOpNode(), node.ctx)
        op.bodypart_id = node.ref_bodypart_decl.bodypart_id
        op.data = node.get_data_value(self._compiler)

        self._op_list.add_operation(op)
