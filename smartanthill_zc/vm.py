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


from smartanthill_zc import array_lit, expression, op_node, comparison
from smartanthill_zc.antlr_helper import (get_reference_lines,
                                          get_reference_text)
from smartanthill_zc.compiler import Ctx
from smartanthill_zc.op_node import ExprOpArg
from smartanthill_zc.visitor import NodeVisitor, visit_node
from smartanthill_zc.writer import BinaryWriter


def convert_to_zepto_vm_one(compiler, root):
    '''
    Process source program and creates a target code tree suitable to run
    at a Zepto VM Level One
    '''
    return _convert_to_zepto_vm(compiler, root, Level.ONE)


def convert_to_zepto_vm_tiny(compiler, root):
    '''
    Process source program and creates a target code tree suitable to run
    at a Zepto VM Level Tiny
    '''
    return _convert_to_zepto_vm(compiler, root, Level.TINY)


def convert_to_zepto_vm_small(compiler, root):
    '''
    Process source program and creates a target code tree suitable to run
    at a Zepto VM Level Small
    '''
    return _convert_to_zepto_vm(compiler, root, Level.SMALL)


def _convert_to_zepto_vm(compiler, root, level):
    v = _ZeptoVmOneVisitor(compiler, _ZeptoVm(level))
    visit_node(v, root.child_source_program)

    target = v.finish()
    target.calculate_byte_size(BinaryWriter(compiler))
    compiler.check_stage('zepto_vm')
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

    def _move_to_front(self, rearrange, i):
        '''
        Helper to move one element to the front
        '''
        if i != 0:
            elem = self._buffer.pop(i)
            self._buffer.insert(0, elem)
            rearrange.add_move(i)

    def _pop_back(self, rearrange, target_size):
        '''
        Helper to remove elements from the back
        '''
        assert len(self._buffer) >= target_size
        if len(self._buffer) != target_size:
            if target_size == 0:
                # pop everything
                self._buffer = []
                rearrange.set_pop_all()
            else:
                count = len(self._buffer) - target_size
                self._buffer = self._buffer[0:target_size]
                rearrange.set_pop(count)

    def remove_reply(self, rearrange, var):
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
                self._move_to_front(rearrange, i)

        # pop it from the back
        assert self._buffer[-1] == var
        self._pop_back(rearrange, len(self._buffer) - 1)

    def clear_for_exit(self, buffer_op, reply):
        '''
        Removes every reply in the reply buffer, with exception of given list
        Used before ZEPTOVM_OP_EXIT to leave only the replies to be sent back
        '''
        self._will_exit = True
        if not reply or len(reply) == 0:
            self._pop_back(buffer_op, 0)
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
                self._move_to_front(buffer_op, pos)

            # remove everything else
            self._pop_back(buffer_op, len(reply))

    def conditional_code_begin(self):
        '''
        Marks the beginning of a conditional block of code.
        We must save the stack state, so at the conditional code end
        we can make the stack state match.
        This way the stack state will not depend on the excution or not
        of the conditional code block
        '''
        self._stack.append(list(self._buffer))

    def conditional_code_end(self, rearrange, was_exit):
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
            self.sort_buffer(rearrange, last)

    def sort_buffer(self, rearrange, target):
        '''
        Sorts the reply buffer to a desired state
        '''
        # first try to find an already sorted slice
        end = reply_buffer_sort_helper(target, self._buffer)

        # then sort the rest
        for i in reversed(range(end)):
            pos = self.find_variable(target[i])
            self._move_to_front(rearrange, pos)

        # last remove the back
        self._pop_back(rearrange, len(target))

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


class ExpressionStack(object):

    '''
    Maintains a record of expressions in stack
    and creates any needed operation to rearrange and maintain the stack.
    Also provides lookup for a named expression inside the stack

    Current implementation separates expression stack in two parts,
    the bottom part is for named expressions, that is declared variables.
    While the top of the stack is for temporary expression evaluation.

    TODO this class has two different responsibilities, split in two classes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._args = []
        self._expression_stack = []
        self._nameds = []
        self._conditional_stack = []

    def init_args(self):

        self._expression_stack.append(self._args)
        self._args = []

    def get_args(self):
        assert len(self._expression_stack) > 0
        assert self._args
        temp = self._args
        self._args = self._expression_stack.pop()
        return temp

    def push_temp(self):
        '''
        Adds a new expression to the stack
        '''
        self._args.append(ExprOpArg())

    def push_constant(self, value):
        '''
        Adds a new expression to the stack
        '''
        ref = ExprOpArg()
        ref.optional_immediate = value
        self._args.append(ref)

    def push_variable(self, var):
        ref = ExprOpArg()
        ref.expr_offset = self.find_variable(var)
        self._args.append(ref)

    def add_variable(self, factory, var):
        '''
        Adds an temp expression as a variable name
        '''
        assert len(self._expression_stack) == 0
        assert len(self._args) == 1
        if self._args[0].is_default():
            self._args.pop()
            self._nameds.append(var)
        elif self._args[0].optional_immediate:
            factory.add_const_push(self._args[0].optional_immediate, var.ctx)
            self._args = []
            self._nameds.append(var)
        elif self._args[0].expr_offset:
            factory.add_copy_push(self._args, var.ctx)
            self._args = []
            self._nameds.append(var)
        else:
            assert False

    def find_variable(self, var):
        '''
        Looks-up for a variable in the stack
        '''
        return self._nameds.index(var)

    def assert_no_temps(self):
        assert len(self._expression_stack) == 0
        assert len(self._args) == 0

    def _pop_variable(self, factory):
        '''
        Removes a variable from the stack
        TODO currently only remove the last in the stack
        '''
        self.assert_no_temps()
        assert len(self._nameds) != 0

        self._nameds.pop()
        factory.add_pop_expression()

    def conditional_code_begin(self):
        '''
        Marks the beginning of a conditional block of code.
        We must save the stack state, so at the conditional code end
        we can make the stack state match.
        This way the stack state will not depend on the execution or not
        of the conditional code block
        '''
        self.assert_no_temps()
        self._conditional_stack.append(list(self._nameds))

    def conditional_code_end(self, factory, was_exit):
        '''
        Marks the end of a conditional block of code that may fall
        We must make the stack state match.
        '''
        self.assert_no_temps()
        if was_exit:
            # Just update
            self._nameds = self._conditional_stack.pop()

        else:
            # We need to restore the reply buffer before fall

            last = self._conditional_stack.pop()

            count = len(self._nameds) - len(last)
            assert count >= 0
            # pylint: disable=unused-variable
            for i in range(count):
                self._pop_variable(factory)

            assert self._nameds == last


def _make_labels(ctx):
    '''
    Helper to create an OpListNode from an StatementListStmtNode
    '''
    begin, end = get_reference_lines(ctx)
    return op_node.JumpLabel(begin, end + 1)


class _ZeptoVm(object):

    '''
    Aggregate class to hold reference to the vm level,
    the expression stack and the reply buffer
    '''

    def __init__(self, level):
        '''
        Constructor
        '''
        self.level = level
        self.buffer = ReplyBuffer()
        self.stack = ExpressionStack()

    def assert_level(self, compiler, target_vm, ctx):
        '''
        Validates that required operation is supported by the target level
        '''

        if target_vm.number > self.level.number:
            compiler.report_error(
                ctx, "Operation is not supported by " + self.level.fullname)
            compiler.raise_error()


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
            op_node.TargetProgramNode(), Ctx.TARGET)
        self._op_list = compiler.init_node(
            op_node.OpListNode(), Ctx.TARGET)

        self._target.set_op_list(self._op_list)
        self._target.vm_level = self._vm.level

        self._exits = []
        self._mcusleep_invoked = False

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
                                    + self._vm.level.fullname)

    def add_reply_rearrange(self):
        '''
        Factory method to add ReplyBufferRearrangeOpNode
        that will write ZEPTOVM_OP_MOVEREPLYTOFRONT and ZEPTOVM_OP_POPREPLIES
        to rearrange or sort the reply buffer to certain state
        '''

        op = self._compiler.init_node(op_node.ReplyBufferRearrangeOpNode(),
                                      None)
        self._add_op(op)
        return op

    def add_pop_expression(self):
        op = self._compiler.init_node(op_node.ExpressionOpNode(), None)
        op.set_unary_operator('pop')
        op.args = [ExprOpArg()]
        self._add_op(op)

    def add_const_push(self, const_value, ctx):
        '''
        Factory method to push a constant value into the stack
        '''
        op = self._compiler.init_node(op_node.PushConstantOpNode(), ctx)
        op.const_value = const_value
        self._add_op(op)

    def add_copy_push(self, args, ctx):
        '''
        Factory method to push a constant value into the stack
        '''
        op = self._compiler.init_node(op_node.ExpressionOpNode(), ctx)
        op.set_unary_operator('=')
        op.args = args
        self._add_op(op)

    def _visit_expression(self, node):
        '''
        Helper method to create an expression visitor an call it
        '''

        visitor = _ZeptoVmExprVisitor(self._compiler, self._vm, self._op_list)

        visit_node(visitor, node)

    def _visit_conditional(self, stmt_list):
        '''
        Helper method to create an expression visitor an call it
        '''

        body = self._compiler.init_node(
            op_node.OpListNode(), stmt_list.ctx)

        temp = self._op_list
        self._op_list = body
        self._vm.buffer.conditional_code_begin()
        self._vm.stack.conditional_code_begin()

        visit_node(self, stmt_list)

        rearrange = self.add_reply_rearrange()
        self._vm.buffer.conditional_code_end(
            rearrange, stmt_list.has_flow_stmt)
        self._vm.stack.conditional_code_end(
            self, stmt_list.has_flow_stmt)
        self._op_list = temp

        return body

    def visit_SourceProgramNode(self, node):

        rt = node.get_return_scope().get_return_type()
        self._target.reply_type = rt
        visit_node(self, node.child_statement_list)

    def visit_StatementListStmtNode(self, node):
        for each in node.childs_statements:
            visit_node(self, each)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_ReturnStmtNode(self, node):
        if isinstance(node.child_expression, expression.BodyPartCallExprNode):

            rearrange = self.add_reply_rearrange()
            self._vm.buffer.clear_for_exit(rearrange, [])
            self._BodyPartCallExprNode(node.child_expression)

        elif isinstance(node.child_expression, expression.VariableExprNode):

            self._vm.assert_level(self._compiler, Level.TINY, node.ctx)

            rearrange = self.add_reply_rearrange()
            self._vm.buffer.clear_for_exit(
                rearrange, [node.child_expression.ref_decl])
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
                        "not be resolved for " + self._vm.level.fullname)

            # first rearrange to drop everything not needed
            rearrange = self.add_reply_rearrange()
            self._vm.buffer.clear_for_exit(rearrange, already_here)
            for current in bodypart_call:
                self._BodyPartCallExprNode(current)
                self._vm.buffer.push_reply(current)

            # rearrange again to put things in the right order
            rearrange = self.add_reply_rearrange()
            self._vm.buffer.sort_buffer(rearrange, target_order)

        else:
            self._compiler.report_error(
                node.ctx, "Expression at 'return' statement could not be "
                "resolved for " + self._vm.level.fullname)

        exitop = self._compiler.init_node(op_node.ExitOpNode(), node.ctx)

        self._add_exit(exitop)

    def visit_McuSleepStmtNode(self, node):
        stmtop = self._compiler.init_node(op_node.McuSleepOpNode(), node.ctx)
        stmtop.sec_delay = node.get_delay_value()

        self._mcusleep_invoked = True
        self._add_op(stmtop)

    def _BodyPartCallExprNode(self, node):
        exprop = self._compiler.init_node(op_node.ExecOpNode(), node.ctx)
        exprop.bodypart_id = node.ref_bodypart_decl.bodypart_id

        if len(node.child_argument_list.childs_arguments) == 0:
            pass
        elif len(node.child_argument_list.childs_arguments) == 1:
            exprop.encode_helper = node.child_argument_list.childs_arguments[
                0].get_type().get_encoding()
            exprop.data_value = node.child_argument_list.childs_arguments[
                0].get_static_value()
        else:
            assert False

        self._add_op(exprop)

    def visit_IfElseStmtNode(self, node):

        self._vm.assert_level(self._compiler, Level.TINY, node.ctx)

        # first, check for tautology condition
        # TODO add comment to output, an report warning
        val = node.child_expression.get_static_value()
        if val is True:
            # just add statements
            visit_node(self, node.child_if_branch)
            return
        elif val is False:
            # do nothing
            return
        else:
            assert val is None

        # second visit the body
        body = self._visit_conditional(node.child_if_branch)

        # we will not support side effects on condition, so just return
        if len(body.childs_operations) == 0:
            return

        condition = self._compiler.init_node(op_node.OpListNode(), node.ctx)
        labels = _make_labels(node.child_if_branch.ctx)
        # then the condition
        visitor = _ZeptoVmIfExprVisitor(
            self._compiler, self._vm, condition, labels)

        visit_node(visitor, node.child_expression)

        ifop = self._compiler.init_node(op_node.IfOpNode(), node.ctx)
        ifop.set_condition(condition)
        ifop.set_body(body)
        ifop.txt_condition = get_reference_text(node.child_expression.ctx)
        ifop.labels = labels

        self._add_op(ifop)

    def visit_VariableDeclarationStmtNode(self, node):

        if isinstance(node.child_initializer, expression.BodyPartCallExprNode):
            self._vm.assert_level(self._compiler, Level.TINY, node.ctx)
            self._vm.buffer.push_reply(node)
            self._BodyPartCallExprNode(node.child_initializer)
        else:
            self._vm.assert_level(self._compiler, Level.SMALL, node.ctx)
            self._visit_expression(node.child_initializer)
            self._vm.stack.add_variable(self, node)

    def visit_ExpressionStmtNode(self, node):

        if isinstance(node.child_expression, expression.AssignmentExprNode):
            if isinstance(node.child_expression.child_rhs,
                          expression.BodyPartCallExprNode):

                self._vm.assert_level(self._compiler, Level.TINY, node.ctx)
                rearrange = self.add_reply_rearrange()
                self._vm.buffer.remove_reply(
                    rearrange, node.child_expression.ref_decl)

                self._vm.buffer.push_reply(node.child_expression.ref_decl)
                self._BodyPartCallExprNode(node.child_expression.child_rhs)
            else:
                self._vm.assert_level(self._compiler, Level.SMALL, node.ctx)
                self._visit_expression(node.child_expression)
                self._expressionstack.add_variable(node)

        else:
            self._compiler.report_error(
                node.ctx, "Expression at statement could not be "
                "resolved for " + self._vm.level.fullname)

    def visit_SimpleForStmtNode(self, node):

        self._vm.assert_level(self._compiler, Level.SMALL, node.ctx)

        # first visit the body
        body = self._visit_conditional(node.child_statement_list)

        # we will not support side effects on condition, so just return
        if len(body.childs_operations) == 0:
            return

        # TODO add alot of checks
        labels = _make_labels(node.child_statement_list.ctx)

        init_value = node.child_begin_expression.get_static_value()

        condition = self._compiler.init_node(
            op_node.JumpLoopOpNode(), node.ctx)
        condition.threshold = node.child_end_expression.get_static_value()
        condition.destination = labels.begin
        condition.txt_name = node.txt_name

        forop = self._compiler.init_node(op_node.LoopOpNode(), node.ctx)
        forop.init_value = init_value
        forop.set_condition(condition)
        forop.set_body(body)
        forop.labels = labels
        forop.txt_name = node.txt_name

        self._add_op(forop)


class _ZeptoVmIfExprVisitor(NodeVisitor):

    '''
    Visitor class for the expression inside if
    This visitor goes through the source tree and creates a target tree
    '''

    def __init__(self, compiler, vm, jmp_ops, labels):
        '''
        Constructor
        '''
        self._compiler = compiler
        self._vm = vm
        self._jmp_ops = jmp_ops
        self._negate = False
        self._labels = labels
        self._destination = labels.end

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._compiler.report_error(node.ctx, "Expression not supported by "
                                    + self._vm.level.fullname)

    def _visit_expression(self, node):
        '''
        Helper method to create an expression visitor an call it
        '''

        visitor = _ZeptoVmExprVisitor(self._compiler, self._vm, self._jmp_ops)

        visit_node(visitor, node)

    def visit_LogicOpExprNode(self, node):

        txt_op = comparison.negate_logic(node.txt_operator, self._negate)
        if txt_op == '&&':
            assert len(node.child_argument_list.childs_arguments) == 2
            visit_node(self, node.child_argument_list.childs_arguments[0])
            visit_node(self, node.child_argument_list.childs_arguments[1])

        elif txt_op == '||':
            assert len(node.child_argument_list.childs_arguments) == 2
            self._negate = not self._negate
            self._destination = self._labels.begin
            visit_node(self, node.child_argument_list.childs_arguments[0])
            self._negate = not self._negate
            self._destination = self._labels.end
            visit_node(self, node.child_argument_list.childs_arguments[1])

        elif txt_op == '!':
            assert len(node.child_argument_list.childs_arguments) == 1
            self._negate = not self._negate
            visit_node(self, node.child_argument_list.childs_arguments[0])
        else:
            assert False

    def visit_FieldToLiteralCompExprNode(self, node):

        jmpop = self._compiler.init_node(op_node.JumpIfFieldOpNode(), node.ctx)
        jmpop.reply = self._vm.buffer.find_variable(node.get_variable_decl())
        jmpop.field_sequence = node.get_field_sequence()
        jmpop.destination = self._destination

        # instead of executing the body when condition is true,
        # jump off the body when condition is false,
        # so condition needs to be negated
        sub, th = node.get_subcode_and_threshold(not self._negate)
        jmpop.threshold = th
        jmpop.set_subcode(sub)

        self._jmp_ops.add_operation(jmpop)

    def visit_NumberToLiteralCompExprNode(self, node):

        self._vm.assert_level(self._compiler, Level.SMALL, node.ctx)

        jmpop = self._compiler.init_node(op_node.JumpIfExprOpNode(), node.ctx)

        self._vm.stack.init_args()
        self._visit_expression(node.get_expression())
        jmpop.args = self._vm.stack.get_args()

        jmpop.destination = self._destination

        # instead of executing the body when condition is true,
        # jump off the body when condition is false,
        # so condition needs to be negated
        sub, th = node.get_subcode_and_threshold(not self._negate)
        jmpop.threshold = th
        jmpop.set_subcode(sub)

        self._jmp_ops.add_operation(jmpop)

    def visit_NumberToNumberCompExprNode(self, node):

        self._vm.assert_level(self._compiler, Level.SMALL, node.ctx)

        assert len(node.child_argument_list.childs_arguments) == 2

        self._vm.stack.init_args()

        self._visit_expression(node.child_argument_list.childs_arguments[0])
        self._visit_expression(node.child_argument_list.childs_arguments[1])

        op = self._compiler.init_node(op_node.ExpressionOpNode(), node.ctx)
        op.set_binary_operator('-')
        op.args = self._vm.stack.get_args()

        self._jmp_ops.add_operation(op)

        self._vm.stack.init_args()
        self._vm.stack.push_temp()

        jmpop = self._compiler.init_node(op_node.JumpIfExprOpNode(), node.ctx)

        jmpop.args = self._vm.stack.get_args()

        jmpop.destination = self._destination

        # instead of executing the body when condition is true,
        # jump off the body when condition is false,
        # so condition needs to be negated
        sub, th = node.get_subcode_and_threshold(not self._negate)
        jmpop.threshold = th
        jmpop.set_subcode(sub)

        self._jmp_ops.add_operation(jmpop)

    def visit_FieldToFieldCompExprNode(self, node):

        # TODO current logic is equal to NumberToNumber, add real optimization
        self._vm.assert_level(self._compiler, Level.SMALL, node.ctx)

        self._vm.stack.init_args()

        self._visit_expression(node.child_lhs)
        self._visit_expression(node.child_rhs)

        op = self._compiler.init_node(op_node.ExpressionOpNode(), node.ctx)
        op.set_binary_operator('-')
        op.args = self._vm.stack.get_args()

        self._jmp_ops.add_operation(op)

        self._vm.stack.init_args()
        self._vm.stack.push_temp()

        jmpop = self._compiler.init_node(op_node.JumpIfExprOpNode(), node.ctx)

        jmpop.args = self._vm.stack.get_args()

        jmpop.destination = self._destination

        # instead of executing the body when condition is true,
        # jump off the body when condition is false,
        # so condition needs to be negated
        sub, th = node.get_subcode_and_threshold(not self._negate)
        jmpop.threshold = th
        jmpop.set_subcode(sub)

        self._jmp_ops.add_operation(jmpop)


class _ZeptoVmExprVisitor(NodeVisitor):

    '''
    Visitor class for the expression inside if
    This visitor goes through the source tree and creates a target tree
    '''

    def __init__(self, compiler, vm, ops):
        '''
        Constructor
        '''
        self._compiler = compiler
        self._vm = vm
        self._ops = ops

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._compiler.report_error(node.ctx, "Expression not supported by "
                                    + self._vm.level.fullname)
        self._compiler.raise_error()

    def visit_MemberAccessExprNode(self, node):

        op = self._compiler.init_node(
            op_node.PushFieldOpNode(), node.ctx)

        assert isinstance(node.child_expression, expression.VariableExprNode)

        op.reply = self._vm.buffer.find_variable(
            node.child_expression.ref_decl)
        op.field_sequence = node.get_member_field_sequence()

        self._vm.stack.push_temp()
        self._ops.add_operation(op)

    def visit_NumberLiteralExprNode(self, node):

        self._vm.stack.push_constant(node.get_static_value())

    def visit_StaticEvaluatedExprNode(self, node):

        self._vm.stack.push_constant(node.get_static_value())

    def visit_ArithmeticOpExprNode(self, node):

        if node.txt_operator in ['+', '-']:
            assert len(node.child_argument_list.childs_arguments) == 2

            self._vm.stack.init_args()

            visit_node(
                self, node.child_argument_list.childs_arguments[0])
            visit_node(
                self, node.child_argument_list.childs_arguments[1])

            op = self._compiler.init_node(
                op_node.ExpressionOpNode(), node.ctx)
            op.set_binary_operator(node.txt_operator)
            op.args = self._vm.stack.get_args()

            self._vm.stack.push_temp()
            self._ops.add_operation(op)

        else:
            self.default_visit(node)

    def visit_VariableExprNode(self, node):
        self._vm.stack.push_variable(node.ref_decl)

    def visit_LiteralCastExprNode(self, node):
        # TODO insert real convertion here
        visit_node(self, node.child_expression)

    def visit_FieldCastExprNode(self, node):

        if node.a != 1 or node.b != 0:
            self._vm.stack.init_args()

        visit_node(self, node.child_expression)

        if node.a != 1:
            self._vm.stack.push_constant(node.a)

            op = self._compiler.init_node(
                op_node.ExpressionOpNode(), node.ctx)

            op.set_binary_operator('*')
            op.args = self._vm.stack.get_args()
            self._ops.add_operation(op)

            if node.b != 0:
                self._vm.stack.init_args()
            self._vm.stack.push_temp()

        if node.b != 0:
            self._vm.stack.push_constant(node.b)

            op = self._compiler.init_node(
                op_node.ExpressionOpNode(), node.ctx)

            op.set_binary_operator('+')
            op.args = self._vm.stack.get_args()

            self._ops.add_operation(op)

            self._vm.stack.push_temp()
