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


from smartanthill_zc import array_lit, op_node, expression
from smartanthill_zc.antlr_helper import (
    get_reference_text, get_reference_lines)
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
    target.calculate_byte_size(SizeWriter())
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
    target.calculate_byte_size(SizeWriter())
    compiler.check_stage('zepto_vm_tiny')
    return target


def convert_to_zepto_vm_small(compiler, root):
    '''
    Process source program and creates a target code tree suitable to run
    at a Zepto VM Level Small
    '''
    v = _ZeptoVmOneVisitor(compiler, Level.SMALL)
    visit_node(v, root.child_program)

    target = v.finish()
    target.calculate_byte_size(SizeWriter())
    compiler.check_stage('zepto_vm_small')
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

    def clear_for_exit(self, factory, reply):
        '''
        Removes every reply in the reply buffer, with exception of given list
        Used before ZEPTOVM_OP_EXIT to leave only the replies to be sent back
        '''
        self._will_exit = True
        if not reply or len(reply) == 0:
            self._pop_back(factory, 0)
        else:
            # TODO improve algorithm
            begin = 0
            for i in range(len(self._buffer)):
                if self._buffer[i] not in reply:
                    begin = i
                    break

            to_move = []
            for i in reversed(range(begin, len(self._buffer))):
                if self._buffer[i] in reply:
                    to_move.append(self._buffer[i])

            for each in to_move:
                pos = self.find_variable(each)
                self._move_to_front(factory, pos)

            # remove everything else
            self._pop_back(factory, len(reply))

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
            # sort the buffer
            self.sort_buffer(factory, last)

    def sort_buffer(self, factory, target):
        '''
        Sorts the reply buffer to a desired state
        '''
        # first try to find an already sorted slice
        end = reply_buffer_sort_helper(target, self._buffer)

        # then sort the rest
        for i in reversed(range(end)):
            pos = self.find_variable(target[i])
            self._move_to_front(factory, pos)

        # last remove the back
        self._pop_back(factory, len(target))

        assert target == self._buffer


def reply_buffer_sort_helper(target, current):
    '''
    Helper to find what part needs to be sorted
    returns the size of target that needs to be sorted
    It is assumed that current is equal or bigger than target
    '''
    assert len(target) <= len(current)

    begin = len(target)

    for i in range(len(target)):
        if current[i] not in target:
            begin = i
            break

    for i in reversed(range(len(target))):
        j = current.index(target[i])
        if j < begin:
            begin = j
        else:
            return i + 1

    return 0


def _make_labels(ctx):
    '''
    Helper to create an OpListNode from an StatementListStmtNode
    '''
    begin, end = get_reference_lines(ctx)
    return op_node.JumpLabel(begin, end + 1)


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
            op_node.TargetProgramNode(), compiler.BUILTIN)
        self._op_list = compiler.init_node(
            op_node.OpListNode(), compiler.BUILTIN)

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
        move = self._compiler.init_node(op_node.MoveReplyOpNode(i), None)
        self._add_op(move)

    def add_pop_replies(self, i):
        '''
        Factory method to add a ZEPTOVM_OP_POPREPLIES
        '''
        if i != 0:
            assert self._vm != Level.ONE

        pop = self._compiler.init_node(op_node.PopRepliesOpNode(i), None)
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

            self._replybuffer.clear_for_exit(self, [])
            self.visit_BodyPartCallExprNode(node.child_expression)

        elif isinstance(node.child_expression, expression.VariableExprNode):

            self._assert_level(Level.TINY, node.ctx)

            self._replybuffer.clear_for_exit(
                self, [node.child_expression.ref_decl])
        elif isinstance(node.child_expression, array_lit.ArrayLiteralExprNode):

            already_here = []
            target_order = []
            bodypart_call = []

            for current in node.child_expression.childs_expressions:

                if isinstance(current, expression.BodyPartCallExprNode):

                    target_order.append(current)
                    bodypart_call.append(current)

                elif isinstance(current, expression.VariableExprNode):

                    target_order.append(current.ref_decl)
                    already_here.append(current.ref_decl)

                else:
                    self._compiler.report_error(
                        current.ctx, "Expression at 'return' statement could "
                        "not be resolved for " + self._vm.fullname)

            self._replybuffer.clear_for_exit(self, already_here)
            for current in bodypart_call:
                self.visit_BodyPartCallExprNode(current)
                self._replybuffer.push_reply(current)

            self._replybuffer.sort_buffer(self, target_order)

        else:
            self._compiler.report_error(
                node.ctx, "Expression at 'return' statement could not be "
                "resolved for " + self._vm.fullname)

        exitop = self._compiler.init_node(op_node.ExitOpNode(), node.ctx)

        self._add_exit(exitop)

    def visit_McuSleepStmtNode(self, node):
        stmtop = self._compiler.init_node(op_node.McuSleepOpNode(), node.ctx)
        stmtop.sec_delay = node.get_delay_value()

        self._mcusleep_invoked = True
        self._add_op(stmtop)

    def visit_BodyPartCallExprNode(self, node):
        exprop = self._compiler.init_node(op_node.ExecOpNode(), node.ctx)
        exprop.bodypart_id = node.ref_bodypart_decl.bodypart_id
        exprop.data = node.get_data_value(self._compiler)

        self._add_op(exprop)

    def visit_IfElseStmtNode(self, node):

        self._assert_level(Level.TINY, node.ctx)

        body = self._compiler.init_node(
            op_node.OpListNode(), node.child_if_branch.ctx)

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

        condition = self._compiler.init_node(op_node.OpListNode(), node.ctx)
        labels = _make_labels(node.child_if_branch.ctx)
        # then the condition
        visitor = _ZeptoVmIfExprVisitor(
            self._compiler, self._vm, self._replybuffer, condition, labels)

        visit_node(visitor, node.child_expression)

        ifop = self._compiler.init_node(op_node.IfOpNode(), node.ctx)
        ifop.set_condition(condition)
        ifop.set_body(body)
        ifop.txt_condition = get_reference_text(node.child_expression.ctx)
        ifop.labels = labels

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

    def visit_SimpleForStmtNode(self, node):

        self._assert_level(Level.SMALL, node.ctx)

        body = self._compiler.init_node(
            op_node.OpListNode(), node.child_statement_list.ctx)

        # first visit the body
        temp = self._op_list
        self._op_list = body
        self._replybuffer.conditional_code_begin()
        visit_node(self, node.child_statement_list)

        self._replybuffer.conditional_code_end(
            self, node.child_statement_list.has_flow_stmt)
        self._op_list = temp

        # we will not support side effects on condition, so just return
        if len(body.childs_operations) == 0:
            return

        # TODO add alot of checks
        labels = _make_labels(node.child_statement_list.ctx)

        init = self._compiler.init_node(
            op_node.PushConstantOpNode(), node.child_begin_expression.ctx)
        init.const_value = node.child_begin_expression.get_static_value()

        condition = self._compiler.init_node(
            op_node.JumpLoopOpNode(), node.ctx)
        condition.threshold = node.child_end_expression.get_static_value()
        condition.destination = labels.begin

        forop = self._compiler.init_node(op_node.LoopOpNode(), node.ctx)
        forop.set_initialization(init)
        forop.set_condition(condition)
        forop.set_body(body)
        forop.txt_initialization = get_reference_text(
            node.child_begin_expression.ctx)
        forop.txt_condition = get_reference_text(node.child_end_expression.ctx)
        forop.labels = labels

        self._add_op(forop)


class _ZeptoVmIfExprVisitor(NodeVisitor):

    '''
    Visitor class for the expression inside if
    This visitor goes through the source tree and creates a target tree
    '''

    def __init__(self, compiler, vm, replybuffer, jmp_ops, labels):
        '''
        Constructor
        '''
        self._compiler = compiler
        self._vm = vm

        self._jmp_ops = jmp_ops
        self._replybuffer = replybuffer
        self._negate = True
        self._labels = labels
        self._destination = labels.end

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
            self._destination = self._labels.begin
            visit_node(self, node.child_argument_list.childs_arguments[0])
            self._negate = True
            self._destination = self._labels.end
            visit_node(self, node.child_argument_list.childs_arguments[1])

        else:
            self.default_visit(node)

    def visit_FieldToLiteralComparisonOpExprNode(self, node):

        jmpop = self._compiler.init_node(op_node.JumpIfFieldOpNode(), node.ctx)
        jmpop.reply = self._replybuffer.find_variable(node.get_variable_decl())
        jmpop.field_sequence = node.get_field_sequence()
        jmpop.destination = self._destination

        sub, th = node.get_subcode_and_threshold(self._negate)
        jmpop.threshold = th
        jmpop.set_subcode(sub)

        self._jmp_ops.add_operation(jmpop)
