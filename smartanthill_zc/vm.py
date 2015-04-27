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

from smartanthill_zc.node import BodyPartCallExprNode
from smartanthill_zc.visitor import NodeVisitor, visit_node
from smartanthill_zc.encode import ZeptoEncoder
from smartanthill_zc.op_node import OpListNode, McuSleepOpNode, \
    ExecOpNode, ExitOpNode


def convert_to_zepto_vm_one(compiler, root):
    '''
    Process source program and creates a target code tree suitable to run
    at a Zepto VM Level One
    '''
    v = _ZeptoVmOneVisitor(compiler)
    visit_node(v, root.child_program)

    op_list = v.get_op_list()
    root.set_op_list(op_list)
    compiler.check_stage('zepto_vm_one')


class Level(object):

    ONE = 1
    TINY = 2
    SMALL = 3
    MEDIUM = 4


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
    VM_NAME = "Zepto VM Level One"

    def __init__(self, compiler):
        '''
        Constructor
        '''
        self._compiler = compiler
        self._encoder = ZeptoEncoder()
        self.op_list = compiler.init_node(OpListNode(), compiler.BUILTIN)
        self._exits = []
        self._has_mcu_sleep = False

    def get_op_list(self):
        '''
        Finished visiting nodes, make all required adjustments and return
        the ops list
        '''
        
        for each in self._exits:
            if self._has_mcu_sleep:
                each.set_is_first()
            else:
                each.set_is_last()

        if isinstance(self.op_list.childs_operations[-1], ExitOpNode):
            self.op_list.childs_operations[-1].try_make_implicit()
            
        return self.op_list

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._compiler.report_error(node.ctx, "Statement not supported by "
                                    + self.VM_NAME)

    def visit_ProgramNode(self, node):
        visit_node(self, node.child_statement_list)

    def visit_StatementListStmtNode(self, node):
        for each in node.childs_statements:
            visit_node(self, each)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_ReturnStmtNode(self, node):
        # pylint: disable=unidiomatic-typecheck
        if type(node.child_expression) is BodyPartCallExprNode:
            visit_node(self, node.child_expression)
        else:
            self._compiler.report_error(
                node.ctx, "Expression at 'return' statement could not be "
                "resolved for " + self.VM_NAME)

        op = self._compiler.init_node(ExitOpNode(), node.ctx)

        self.op_list.add_operation(op)
        self._exits.append(op)

    def visit_McuSleepStmtNode(self, node):
        op = self._compiler.init_node(McuSleepOpNode(), node.ctx)
        op.sec_delay = node.get_delay_value()

        self.op_list.add_operation(op)
        self._has_mcu_sleep = True

    def visit_BodyPartCallExprNode(self, node):
        op = self._compiler.init_node(ExecOpNode(), node.ctx)
        op.bodypart_id = node.bodypart_decl.bodypart_id
        op.data = node.get_data_value(self._compiler)

        self.op_list.add_operation(op)
