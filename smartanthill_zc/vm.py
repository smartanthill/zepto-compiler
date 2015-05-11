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
from smartanthill_zc.op_node import JumpDesptination, MoveReplyOpNode,\
    PopRepliesOpNode
import smartanthill_zc.op_node as op
from smartanthill_zc.visitor import NodeVisitor, visit_node
from smartanthill_zc.writer import SizeWriter


def convert_to_zepto_vm_one(compiler, root):
    '''
    Process source program and creates a target code tree suitable to run
    at a Zepto VM Level One
    '''
    v = _ZeptoVmOneVisitor(compiler, Level.ONE)
    visit_node(v, root.child_program)

    target = v.finish()
    compiler.check_stage('zepto_vm_one')
    return target


def convert_to_zepto_vm_tiny(compiler, root):
    '''
    Process source program and creates a target code tree suitable to run
    at a Zepto VM Level Tiny
    '''
    v = _ZeptoVmOneVisitor(compiler, Level.TINY)
    visit_node(v, root.child_program)

    target = v.finish()
    compiler.check_stage('zepto_vm_tiny')
    return target


class _VmLevelImpl(object):

    '''
    Helper class to map vm levels, with their names and description
    '''

    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.fullname = "Zepto VM Level " + name


class Level(object):

    '''
    Enum like, for vm levels
    '''
    ONE = _VmLevelImpl(1, 'One')
    TINY = _VmLevelImpl(2, 'Tiny')
    SMALL = _VmLevelImpl(3, 'Small')
    MEDIUM = _VmLevelImpl(4, 'Medium')


class ReplyBuffer(object):

    '''
    Maintains a record of replies in buffer.
    and creates ZEPTOVM_OP_POPREPLIES and ZEPTOVM_OP_MOVEREPLYTOFRONT
    as needed to rearrange and maintain the buffer.
    Also provides lookup for a reply inside the buffer
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._buffer = []
        self._stack = []
        self._will_exit = False

    def push_reply(self, var):
        '''
        Adds a new reply to the buffer
        '''
        self._buffer.append(var)

    def find_variable(self, var):
        '''
        Looks-up for a reply in the buffer
        '''
        return self._buffer.index(var)

    def _move_to_front(self, factory, i):
        '''
        Helper to move one element to the front
        '''
        if i != 0:
            elem = self._buffer.pop(i)
            self._buffer.insert(0, elem)
            factory.add_move_reply_to_front(i)

    def _pop_back(self, factory, target_size):
        '''
        Helper to remove elements from the back
        '''
        assert len(self._buffer) >= target_size
        if len(self._buffer) != target_size:
            if target_size == 0:
                # pop everything
                self._buffer = []
                factory.add_pop_replies(0)
            else:
                count = len(self._buffer) - target_size
                self._buffer = self._buffer[0:target_size]
                factory.add_pop_replies(count)

    def remove_reply(self, factory, var):
        '''
        Removes a reply from the buffer
        First moves all replies after it to the front,
        and then the required reply is poped from the stack
        '''
        assert len(self._buffer) != 0

        if self._buffer[-1] != var:
            # move to the back
            pos = self.find_variable(var)

            for i in reversed(range(pos + 1, len(self._buffer))):  # reversed?
                self._move_to_front(factory, i)

        # pop it from the back
        assert self._buffer[-1] == var
        self._pop_back(factory, len(self._buffer) - 1)

    def clear_for_exit(self, factory):
        '''
        Removes every reply in the reply buffer
        '''
        self._will_exit = True

        return self._pop_back(factory, 0)

    def reply_for_exit(self, factory, var):
        '''
        Removes every reply in the reply buffer, with exception of one
        Used before ZEPTOVM_OP_EXIT to leave only the reply to be sent back
        '''
        assert len(self._buffer) != 0

        self._will_exit = True
        # move to the front
        pos = self.find_variable(var)
        self._move_to_front(factory, pos)

        # remove everything else
        self._pop_back(factory, 1)

    def conditional_code_begin(self):
        '''
        Marks the beginning of a conditional block of code.
        We must save the stack state, so at the conditional code end
        we can make the stack state match.
        This way the stack state will not depend on the excution or not
        of the conditional code block
        '''
        self._stack.append(list(self._buffer))

    def conditional_code_end(self, factory, was_exit):
        '''
        Marks the end of a conditional block of code that may fall
        We must make the stack state match.
        '''
        if was_exit:
            # Just update
            assert self._will_exit
            self._will_exit = False
            self._buffer = self._stack.pop()

        else:
            # We need to restore the reply buffer before fall
            assert not self._will_exit

            last = self._stack.pop()
            # first try to find an already sorted slice
            end = reply_buffer_sort_helper(last, self._buffer)

            # then sort the rest
            for i in reversed(range(end)):
                pos = self.find_variable(last[i])
                self._move_to_front(factory, pos)

            # last remove the back
            self._pop_back(factory, len(last))

            assert last == self._buffer


def reply_buffer_sort_helper(target, current):
    '''
    Helper to find an slice of the reply buffer that is already sorted
    returns the size of target that needs to be sorted
    It is assumed that current is equal or bigger than target
    '''
    assert len(target) <= len(current)

    if len(target) > 0:
        last = target[-1]
        s = current.index(last) + 1
        if len(target) >= s:
            # try to find an slice that is already sorted
            cu_sl = current[:s]
            ta_sl = target[-s:]
            assert len(cu_sl) == s
            assert len(ta_sl) == s
            if cu_sl == ta_sl:
                return len(target) - s

    return len(target)


class _ZeptoVmOneVisitor(NodeVisitor):

    '''
    Visitor class for a Zepto VM Level One
    This visitor goes through the source tree and creates a target tree
    '''

    def __init__(self, compiler, vm):
        '''
        Constructor
        '''
        self._compiler = compiler
        self._vm = vm

        self._target = compiler.init_node(
            op.TargetProgramNode(), compiler.BUILTIN)
        self._op_list = compiler.init_node(op.OpListNode(), compiler.BUILTIN)

        self._target.set_op_list(self._op_list)
        self._target.vm_level = self._vm

        self._exits = []
        self._mcusleep_invoked = False

        self._replybuffer = ReplyBuffer()

    def _add_exit(self, node):
        '''
        Keep a list of EXIT ops
        '''
        self._add_op(node)
        self._exits.append(node)

    def _add_op(self, node):
        '''
        Add current op, and calculate its size in bytes
        '''
        node.calculate_byte_size(SizeWriter())
        self._op_list.add_operation(node)

    def _assert_level(self, target_vm, ctx):
        '''
        Validates that required operation is supported by the target level
        '''

        if target_vm.number > self._vm.number:
            self._compiler.report_error(
                ctx, "Operation is not supported by " + self._vm.fullname)
            self._compiler.raise_error()

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
                                    + self._vm.fullname)

    def add_move_reply_to_front(self, i):
        '''
        Factory method to add a ZEPTOVM_OP_MOVEREPLYTOFRONT
        '''
        assert i != 0
        move = self._compiler.init_node(MoveReplyOpNode(i), None)
        self._add_op(move)

    def add_pop_replies(self, i):
        '''
        Factory method to add a ZEPTOVM_OP_POPREPLIES
        '''
        if i != 0:
            assert self._vm != Level.ONE

        pop = self._compiler.init_node(PopRepliesOpNode(i), None)
        self._add_op(pop)

    def visit_ProgramNode(self, node):

        fs = node.get_return_scope().get_return_type().field_sequence
        self._target.reply_fs = fs
        visit_node(self, node.child_statement_list)

    def visit_StatementListStmtNode(self, node):
        for each in node.childs_statements:
            visit_node(self, each)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_ReturnStmtNode(self, node):
        if isinstance(node.child_expression, expression.BodyPartCallExprNode):

            self._replybuffer.clear_for_exit(self)
            self.visit_BodyPartCallExprNode(node.child_expression)

        elif isinstance(node.child_expression, expression.VariableExprNode):

            self._assert_level(Level.TINY, node.ctx)

            self._replybuffer.reply_for_exit(
                self, node.child_expression.ref_decl)
        else:
            self._compiler.report_error(
                node.ctx, "Expression at 'return' statement could not be "
                "resolved for " + self._vm.fullname)

        exitop = self._compiler.init_node(op.ExitOpNode(), node.ctx)

        self._add_exit(exitop)

    def visit_McuSleepStmtNode(self, node):
        stmtop = self._compiler.init_node(op.McuSleepOpNode(), node.ctx)
        stmtop.sec_delay = node.get_delay_value()

        self._mcusleep_invoked = True
        self._add_op(stmtop)

    def visit_BodyPartCallExprNode(self, node):
        exprop = self._compiler.init_node(op.ExecOpNode(), node.ctx)
        exprop.bodypart_id = node.ref_bodypart_decl.bodypart_id
        exprop.data = node.get_data_value(self._compiler)

        self._add_op(exprop)

    def visit_IfElseStmtNode(self, node):

        self._assert_level(Level.TINY, node.ctx)

        body = self._compiler.init_node(op.OpListNode(), node.ctx)

        # first visit the body
        temp = self._op_list
        self._op_list = body
        self._replybuffer.conditional_code_begin()
        visit_node(self, node.child_if_branch)

        self._replybuffer.conditional_code_end(
            self, node.child_if_branch.has_flow_stmt)
        self._op_list = temp

        # we will not support side effects on condition, so just return
        if len(body.childs_operations) == 0:
            return

        condition = self._compiler.init_node(op.OpListNode(), node.ctx)

        # then the condition
        visitor = _ZeptoVmIfExprVisitor(
            self._compiler, self._vm, self._replybuffer, condition)

        visit_node(visitor, node.child_expression)

        ifop = self._compiler.init_node(op.IfOpNode(), node.ctx)
        ifop.set_condition(condition)
        ifop.set_body(body)

        self._add_op(ifop)

    def visit_VariableDeclarationStmtNode(self, node):

        if isinstance(node.child_initializer, expression.BodyPartCallExprNode):
            self._assert_level(Level.TINY, node.ctx)
            self._replybuffer.push_reply(node)
            self.visit_BodyPartCallExprNode(node.child_initializer)
        else:
            self._compiler.report_error(
                node.ctx, "Expression at declaration statement could not be "
                "resolved for " + self._vm.fullname)

    def visit_ExpressionStmtNode(self, node):

        if isinstance(node.child_expression, expression.AssignmentExprNode) \
                and isinstance(node.child_expression.child_rhs,
                               expression.BodyPartCallExprNode):

            self._assert_level(Level.TINY, node.ctx)
            self._replybuffer.remove_reply(
                self, node.child_expression.ref_decl)

            self._replybuffer.push_reply(node.child_expression.ref_decl)
            self.visit_BodyPartCallExprNode(node.child_expression.child_rhs)

        else:
            self._compiler.report_error(
                node.ctx, "Expression at statement could not be "
                "resolved for " + self._vm.fullname)


class _ZeptoVmIfExprVisitor(NodeVisitor):

    '''
    Visitor class for the expression inside if
    This visitor goes through the source tree and creates a target tree
    '''

    def __init__(self, compiler, vm, replybuffer, jmp_ops):
        '''
        Constructor
        '''
        self._compiler = compiler
        self._vm = vm

        self._jmp_ops = jmp_ops
        self._replybuffer = replybuffer
        self._negate = True
        self._destination = JumpDesptination.END

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._compiler.report_error(node.ctx, "Expression not supported by "
                                    + self._vm.fullname)

    def visit_OperatorExprNode(self, node):

        if node.txt_operator == '&&':
            assert len(node.child_argument_list.childs_arguments) == 2
            visit_node(self, node.child_argument_list.childs_arguments[0])
            visit_node(self, node.child_argument_list.childs_arguments[1])

        elif node.txt_operator == '||':
            assert len(node.child_argument_list.childs_arguments) == 2
            self._negate = False
            self._destination = JumpDesptination.BEGIN
            visit_node(self, node.child_argument_list.childs_arguments[0])
            self._negate = True
            self._destination = JumpDesptination.END
            visit_node(self, node.child_argument_list.childs_arguments[1])

        else:
            self.default_visit(node)

    def visit_FieldToLiteralComparisonOpExprNode(self, node):

        jmpop = self._compiler.init_node(op.JumpIfFieldOpNode(), node.ctx)
        jmpop.reply = self._replybuffer.find_variable(node.get_variable_decl())
        jmpop.field_sequence = node.get_field_sequence()
        jmpop.destination = self._destination

        sub, th = node.get_subcode_and_threshold(self._negate)
        jmpop.threshold = th
        jmpop.set_subcode(sub)

        self._jmp_ops.add_operation(jmpop)
