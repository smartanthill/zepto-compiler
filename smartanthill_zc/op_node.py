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

from smartanthill_zc.encode import field_sequence_to_str
from smartanthill_zc.node import Node


class _OpImpl(object):

    '''
    Helper class to map Zepto VM OpCodes and their names
    '''

    def __init__(self, opcode, name):
        '''
        Constructor
        '''
        self.opcode = opcode
        self.name = name


class Op(object):

    '''
    Enum like, assigns a name to each opcode
    '''

    INVALID = _OpImpl(0, '<invalid>')

    DEVICECAPS = _OpImpl(1, 'DEVICECAPS')
    EXEC = _OpImpl(2, 'EXEC')
    PUSHREPLY = _OpImpl(3, 'PUSHREPLY')
    SLEEP = _OpImpl(4, 'SLEEP')
    TRANSMITTER = _OpImpl(5, 'TRANSMITTER')
    MCUSLEEP = _OpImpl(6, 'MCUSLEEP')
    # limited support in Zepto VM-One, full support from Zepto VM-Tiny
    POPREPLIES = _OpImpl(7, 'POPREPLIES')
    EXIT = _OpImpl(8, 'EXIT')
    # limited support in Zepto VM-One, full support from Zepto VM-Tiny
    APPENDTOREPLY = _OpImpl(9, 'APPENDTOREPLY')

    # below, instructions are not supported by Zepto VM-One
    JMP = _OpImpl(10, 'JMP')
    JMPIFREPLYFIELD_LT = _OpImpl(11, 'JMPIFREPLYFIELD_LT')
    JMPIFREPLYFIELD_GT = _OpImpl(12, 'JMPIFREPLYFIELD_GT')
    JMPIFREPLYFIELD_EQ = _OpImpl(13, 'JMPIFREPLYFIELD_EQ')
    JMPIFREPLYFIELD_NE = _OpImpl(14, 'JMPIFREPLYFIELD_NE')
    MOVEREPLYTOFRONT = _OpImpl(15, 'MOVEREPLYTOFRONT')

    # below, instructions are not supported by Zepto VM-Tiny and below
    PUSHEXPR_CONSTANT = _OpImpl(16, 'PUSHEXPR_CONSTANT')
    PUSHEXPR_REPLYFIELD = _OpImpl(17, 'PUSHEXPR_REPLYFIELD')
    EXPRUNOP = _OpImpl(18, 'EXPRUNOP')
    EXPRUNOP_EX = _OpImpl(19, 'EXPRUNOP_EX')
    EXPRUNOP_EX2 = _OpImpl(20, 'EXPRUNOP_EX2')
    EXPRBINOP = _OpImpl(21, 'EXPRBINOP')
    EXPRBINOP_EX = _OpImpl(22, 'EXPRBINOP_EX')
    EXPRBINOP_EX2 = _OpImpl(23, 'EXPRBINOP_EX2')
    JMPIFEXPR_LT = _OpImpl(24, 'JMPIFEXPR_LT')
    JMPIFEXPR_GT = _OpImpl(25, 'JMPIFEXPR_GT')
    JMPIFEXPR_EQ = _OpImpl(26, 'JMPIFEXPR_EQ')
    JMPIFEXPR_NE = _OpImpl(27, 'JMPIFEXPR_NE')
    JMPIFEXPR_EX_LT = _OpImpl(28, 'JMPIFEXPR_EX_LT')
    JMPIFEXPR_EX_GT = _OpImpl(29, 'JMPIFEXPR_EX_GT')
    JMPIFEXPR_EX_EQ = _OpImpl(30, 'JMPIFEXPR_EX_EQ')
    JMPIFEXPR_EX_NE = _OpImpl(31, 'JMPIFEXPR_EX_NE')
    CALL = _OpImpl(32, 'ZEPTOVM_OP_CALL')
    RET = _OpImpl(33, 'ZEPTOVM_OP_RET')
    SWITCH = _OpImpl(34, 'ZEPTOVM_OP_SWITCH')
    SWITCH_EX = _OpImpl(35, 'ZEPTOVM_OP_SWITCH_EX')
    INCANDJMPIF = _OpImpl(36, 'INCANDJMPIF')
    DECANDJMPIF = _OpImpl(37, 'DECANDJMPIF')

    # below, instructions are not supported by Zepto VM-Small and below
    PARALLEL = _OpImpl(38, 'ZEPTOVM_OP_PARALLEL')


class UnOp(object):

    '''
    ZEPTOVM_OP_EXPRUNOP unary operators
    '''

    POP = _OpImpl(1, 'POP')
    COPY = _OpImpl(2, '=')
    MINUS = _OpImpl(3, '-')
    BITNEG = _OpImpl(4, '~')
    NOT = _OpImpl(5, '!')
    INC = _OpImpl(6, '++')
    DEC = _OpImpl(7, '--')


class BinOp(object):

    '''
    ZEPTOVM_OP_EXPRBINOP binary operators
    '''
    PLUS = _OpImpl(1, '+')
    MINUS = _OpImpl(1, '-')
    MUL = _OpImpl(1, '*')
    DIV = _OpImpl(1, '/')
    SHL = _OpImpl(1, '<<')
    SHR = _OpImpl(1, '>>')
    USHR = _OpImpl(1, '>>>')
    BITAND = _OpImpl(1, '&')
    BITOR = _OpImpl(1, '|')
    AND = _OpImpl(1, '&&')
    OR = _OpImpl(1, '||')


class BitField(object):

    '''
    Represents a flags bitfield, makes it easier to represent flags by name
    '''

    def __init__(self, names):
        '''
        Constructor
        '''
        self.names = names
        self.values = {}

    def set(self, name, value):
        '''
        Sets a flag value by name
        '''

        if name not in self.names:
            assert False

        self.values[name] = value

    def get(self, name):
        '''
        Gets a flag value by name
        '''
        if name not in self.names:
            assert False

        if name in self.values:
            return self.values[name]
        else:
            return False


class OpcodeNode(Node):

    '''
    Base class for virtual machine target operation nodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(OpcodeNode, self).__init__()
        self._byte_size = None

    def write(self, writer):
        '''
        Base method for writing the target tree to the output writer
        '''
        pass

    def get_byte_size(self):
        '''
        byte_size getter that makes sure size if different from zero
        '''
        assert self._byte_size
        return self._byte_size

    def reset_byte_size(self):
        '''
        Resets the size for this node.
        Allows for recalculation
        '''
        self._byte_size = None

    def calculate_byte_size(self, calculator):
        '''
        Calculates the size in bytes for this node.
        Needed by jumps to calculate jump offsets
        '''
        assert not self._byte_size
        begin = calculator.index
        self.write(calculator)
        self._byte_size = calculator.index - begin
        return self._byte_size


class OpListNode(Node):

    '''
    Operation list, container of OpNode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(OpListNode, self).__init__()
        self.childs_operations = []

    def add_operation(self, child):
        '''
        operation adder
        '''
        assert child
        assert isinstance(child, OpcodeNode)
        child.set_parent(self)
        self.childs_operations.append(child)

    def write(self, writer):
        '''
        Write all the child nodes to the output writer
        '''
        for op in self.childs_operations:
            op.write(writer)

    def calculate_byte_size(self, calculator):
        '''
        Calculates the size in bytes for this node.
        Needed by jumps to calculate jump offsets
        '''

        byte_size = 0
        for op in self.childs_operations:
            byte_size += op.calculate_byte_size(calculator)

        return byte_size


class TargetProgramNode(Node):

    '''
    Container of the target program, and program meta-data
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(TargetProgramNode, self).__init__()
        self.child_op_list = None
        self.vm_level = None
        self.mcusleep_invoked = False
        self.reply_fs = None
        self.byte_size = 0
# entry=NOT_ISFIRST,exit=IS_FIRST

    def set_op_list(self, child):
        '''
        op_list setter
        '''
        assert isinstance(child, OpListNode)
        child.set_parent(self)
        self.child_op_list = child

    def write(self, writer):
        '''
        Write all the child nodes to the output writer
        '''
        writer.write_text('target vm: %s' % self.vm_level.name)
        writer.write_text('mcusleep: %s' % self.mcusleep_invoked)
        writer.write_text('reply: {%s}' % field_sequence_to_str(self.reply_fs))
        writer.write_text('size: %d bytes' % self.byte_size)
        self.child_op_list.write(writer)

    def calculate_byte_size(self, calculator):
        '''
        Calculates the size in bytes for this node.
        Needed by jumps to calculate jump offsets
        '''
        self.byte_size = self.child_op_list.calculate_byte_size(calculator)


class ExecOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_EXEC opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ExecOpNode, self).__init__()
        self.bodypart_id = 0
        self.data = None

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(Op.EXEC)
        writer.write_int_2(self.bodypart_id)
        writer.write_opaque_data_2(self.data)


class PushReplyOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_PUSHREPLY opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PushReplyOpNode, self).__init__()
        self.data = None

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(Op.PUSHREPLY)
        writer.write_opaque_data_2(self.data)


class TransmitterOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_TRANSMITTER opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(TransmitterOpNode, self).__init__()
        self._bf = BitField(['ON'])

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(Op.TRANSMITTER)
        writer.write_bitfield(self._bf)


class SleepOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_SLEEP opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(SleepOpNode, self).__init__()
        self.msec_delay = 0

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(Op.SLEEP)
        writer.write_uint_4(self.msec_delay)


class McuSleepOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_MCUSLEEP opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(McuSleepOpNode, self).__init__()
        self.sec_delay = 0
        self._bf = BitField(['MAYDROPEARLIERINSTRUCTIONS',
                             'TRANSMITTERONWHENBACK'])

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(Op.MCUSLEEP)
        writer.write_uint_4(self.sec_delay)
        writer.write_bitfield(self._bf)


class ExitOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_EXIT opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ExitOpNode, self).__init__()
        self._bf = BitField(['FORCED-PADDING-FLAG', 'ISFIRST', 'ISLAST'])
        self._opt_padding_to = 0
        self.is_implicit = False

    def set_is_first(self):
        assert not self._bf.get('ISLAST')
        self._bf.set('ISFIRST', True)

    def set_is_last(self):
        assert not self._bf.get('ISFIRST')
        self._bf.set('ISLAST', True)

    def try_make_implicit(self):

        if self._bf.get('ISLAST') and not self._bf.get('FORCED-PADDING-FLAG'):
            self.is_implicit = True

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        if not self.is_implicit:
            writer.write_opcode(Op.EXIT)
            writer.write_bitfield(self._bf)
            if self._bf.get('FORCED-PADDING-FLAG'):
                writer.write_uint_2(self._opt_padding_to)
        else:
            writer.write_text('exit|islast')


class JumpLabel(object):

    def __init__(self, begin, end):
        self.begin = 'begin_' + str(begin)
        self.end = 'end_' + str(end)


class ReplyRefs(object):

    def __init(self):
        self.useds_inside = []
        self.useds_after = []
        self.is_exit = False


class IfOpNode(OpcodeNode):

    '''
    Holder for an if implementation
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(IfOpNode, self).__init__()
        self.child_condition = None
        self.child_body = None
        self.txt_condition = None
        self.labels = None

    def set_condition(self, child):
        '''
        condition_op_list setter
        '''
        assert isinstance(child, OpListNode)
        child.set_parent(self)
        self.child_condition = child

    def set_body(self, child):
        '''
        condition_op_list setter
        '''
        assert isinstance(child, OpListNode)
        child.set_parent(self)
        self.child_body = child

    def calculate_byte_size(self, calculator):
        '''
        Set the jumps offsets
        '''

        body = self.child_body.calculate_byte_size(calculator)

        begin = 0
        for current in reversed(self.child_condition.childs_operations):

            if isinstance(current, JumpIfFieldOpNode) or \
                    isinstance(current, JumpIfExprOpNode):
                if current.destination == self.labels.begin:
                    current.delta = begin
                elif current.destination == self.labels.end:
                    current.delta = begin + body
                else:
                    assert False

            begin += current.calculate_byte_size(calculator)

        self._byte_size = begin + body

        return self._byte_size

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_text("if( %s )" % self.txt_condition)
        self.child_condition.write(writer)
        writer.write_text("%s:" % self.labels.begin)
        self.child_body.write(writer)
        writer.write_text("%s:" % self.labels.end)


_jump_if_field_subcode = {'==': Op.JMPIFREPLYFIELD_EQ,
                          '!=': Op.JMPIFREPLYFIELD_NE,
                          '<': Op.JMPIFREPLYFIELD_LT,
                          '>': Op.JMPIFREPLYFIELD_GT}


class JumpIfFieldOpNode(OpcodeNode):

    '''
    Node for  ZEPTOVM_OP_JMPIFREPLYFIELD_XX opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(JumpIfFieldOpNode, self).__init__()
        self._subcode = None
        self.reply = 0
        self.field_sequence = None
        self.threshold = 0
        self.destination = None
        self.delta = 0

    def set_subcode(self, subcode):
        '''
        Sets the conditional subcode ['==', '!=', '<', '>']
        '''
        assert subcode in _jump_if_field_subcode
        self._subcode = subcode

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(_jump_if_field_subcode[self._subcode])
        writer.write_int_2(self.reply)
        writer.write_field_sequence(self.field_sequence)
        writer.write_half_float(self.threshold)
        writer.write_delta(self.delta, self.destination)


class ReplyBufferRearrangeOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_POPREPLIES and ZEPTOVM_OP_MOVEREPLYTOFRONT
    It wraps a set of movements of replies and a final optional pop
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ReplyBufferRearrangeOpNode, self).__init__()
        self.moves = []
        self.pop_number = None

    def add_move(self, index):
        self.moves.append(index)

    def set_pop(self, count):
        self.pop_number = count

    def set_pop_all(self):
        self.pop_number = 0

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        for current in self.moves:
            writer.write_opcode(Op.MOVEREPLYTOFRONT)
            writer.write_int_2(current)

        if self.pop_number != None:
            writer.write_opcode(Op.POPREPLIES)
            writer.write_uint_2(self.pop_number)


class LoopOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_INCANDJMPIF and ZEPTOVM_OP_DECANDJMPIF opcodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(LoopOpNode, self).__init__()
        self.child_body = None
        self.child_condition = None
        self.labels = None
        self.txt_name = None

    def set_body(self, child):
        '''
        body setter
        '''
        assert isinstance(child, OpListNode)
        child.set_parent(self)
        self.child_body = child

    def set_condition(self, child):
        '''
        condition_op_list setter
        '''
        assert isinstance(child, JumpLoopOpNode)
        child.set_parent(self)
        self.child_condition = child

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_text(
            "for( var %s = %s; .." % (self.txt_name, self.init_value))

        writer.write_opcode(Op.PUSHEXPR_CONSTANT)
        writer.write_half_float(self.init_value)

        writer.write_text("%s:" % self.labels.begin)
        self.child_body.write(writer)
        self.child_condition.write(writer)

        writer.write_opcode(Op.EXPRUNOP)
        writer.write_subcode(UnOp.POP)

    def calculate_byte_size(self, calculator):
        '''
        Set the jumps offsets
        Since the jump is at the end of the loop,
        the jump delta depends on the jump instruction itself,
        and the size of the jump instruction depends
        on the encoded size of delta.
        So, we first assign an estimate of delta, calculate the size
        and then iteratively reassign the the delta and recalculate the size
        '''

        body = self.child_body.calculate_byte_size(calculator)

        assert self.child_condition.destination == self.labels.begin

        prev = 0
        jump = 5  # Minimum JumpLoopOpNode size

        while prev != jump:
            prev = jump
            self.child_condition.delta = -(body + jump)
            self.child_condition.reset_byte_size()
            jump = self.child_condition.calculate_byte_size(calculator)

        self._byte_size = body + jump

        return self._byte_size


class JumpLoopOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_INCANDJMPIF and ZEPTOVM_OP_DECANDJMPIF opcodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(JumpLoopOpNode, self).__init__()
        self.is_decrement = False
        self.expr_offset = 1
        self.threshold = 0
        self.destination = None
        self.delta = 0
        self.txt_name = None

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        if self.is_decrement:
            writer.write_text("..; %s > %s; %s-- )" %
                              (self.txt_name, self.threshold, self.txt_name))
            writer.write_opcode(Op.DECANDJMPIF)
        else:
            writer.write_text("..; %s < %s; %s++ )" %
                              (self.txt_name, self.threshold, self.txt_name))
            writer.write_opcode(Op.INCANDJMPIF)

        writer.write_int_2(self.expr_offset)
        writer.write_half_float(self.threshold)
        writer.write_delta(self.delta, self.destination)


_binary_operator_subcode = {'+': BinOp.PLUS,
                            '-': BinOp.MINUS,
                            '*': BinOp.MUL}

_unary_operator_subcode = {'-': UnOp.MINUS,
                           '=': UnOp.COPY,
                           'pop': UnOp.POP}


class ExprOpArg(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.expr_offset = None
        self.pop_flag = True
        self.optional_immediate = None

    def is_default(self):
        return not self.expr_offset and not self.optional_immediate


class ExprOpResult(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.expr_offset = None
        self.insert_flag = False


class ExpressionOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_EXPRUNOP and ZEPTOVM_OP_EXPRBINOP opcodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ExpressionOpNode, self).__init__()
        self._operator = None
        self.args = None
        self.result = ExprOpResult()

    def set_binary_operator(self, txt):
        assert not self._operator
        assert txt in _binary_operator_subcode
        self._operator = _binary_operator_subcode[txt]

    def set_unary_operator(self, txt):
        assert not self._operator
        assert txt in _unary_operator_subcode
        self._operator = _unary_operator_subcode[txt]

    def write(self, writer):
        '''
        Write this node to the output writer
        '''

        assert self._operator
        assert self.args
        assert self.result

        if self._operator in [UnOp.POP, UnOp.COPY, UnOp.MINUS, UnOp.BITNEG,
                              UnOp.NOT, UnOp.INC, UnOp.DEC]:

            assert len(self.args) == 1

            if self.result.expr_offset:
                writer.write_opcode(Op.EXPRUNOP_EX2)
                writer.write_subcode(self._operator)
                writer.write_oparg(self.args[0])
                writer.write_opresult(self.result)
            elif self.args[0].is_default():
                writer.write_opcode(Op.EXPRUNOP)
                writer.write_subcode(self._operator)
            else:
                writer.write_opcode(Op.EXPRUNOP_EX)
                writer.write_subcode(self._operator)
                writer.write_oparg(self.args[0])

        elif self._operator in [BinOp.PLUS, BinOp.MINUS, BinOp.MUL, BinOp.DIV,
                                BinOp.SHL, BinOp.SHR, BinOp.USHR,
                                BinOp.BITAND, BinOp.BITOR,
                                BinOp.AND, BinOp.OR]:
            assert len(self.args) == 2
            if self.result.expr_offset:
                writer.write_opcode(Op.EXPRBINOP_EX2)
                writer.write_subcode(self._operator)
                writer.write_oparg(self.args[0])
                writer.write_oparg(self.args[1])
                writer.write_opresult(self.result)
            elif self.args[0].is_default() and self.args[1].is_default():
                writer.write_opcode(Op.EXPRBINOP)
                writer.write_subcode(self._operator)
            else:
                writer.write_opcode(Op.EXPRBINOP_EX)
                writer.write_subcode(self._operator)
                writer.write_oparg(self.args[0])
                writer.write_oparg(self.args[1])

        else:
            assert False


class FieldCastOpNode(OpcodeNode):

    '''
    Node for linear scaling of a reply field
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FieldCastOpNode, self).__init__()
        self.args = None
        self.a = 1
        self.b = 0
        self.result = ExprOpResult()

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        # First push the field to the stack
        # then multply
        assert self.args
        assert len(self.args) == 1
        assert self.result

        if self.a != 1:

            inmediate = ExprOpArg()
            inmediate.optional_immediate = self.a

            if self.result.expr_offset and self.b == 0:
                writer.write_opcode(Op.EXPRBINOP_EX2)
                writer.write_subcode(BinOp.MUL)
                writer.write_oparg(self.args[0])

                writer.write_oparg(inmediate)
                writer.write_opresult(self.result)
            else:
                writer.write_opcode(Op.EXPRBINOP_EX)
                writer.write_subcode(BinOp.MUL)
                writer.write_oparg(self.args[0])
                writer.write_oparg(inmediate)

        if self.b != 0:
            inmediate = ExprOpArg()
            inmediate.optional_immediate = self.b

            if self.result.expr_offset:
                writer.write_opcode(Op.EXPRBINOP_EX2)
                writer.write_subcode(BinOp.PLUS)
                if self.a == 1:
                    writer.write_oparg(self.args[0])
                else:
                    writer.write_oparg(ExprOpArg())

                writer.write_oparg(inmediate)
                writer.write_opresult(self.result)
            else:
                writer.write_opcode(Op.EXPRBINOP_EX)
                writer.write_subcode(BinOp.PLUS)
                if self.a == 1:
                    writer.write_oparg(self.args[0])
                else:
                    writer.write_oparg(ExprOpArg())
                writer.write_oparg(inmediate)


class PushFieldOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_PUSHEXPR_REPLYFIELD opcodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PushFieldOpNode, self).__init__()
        self.reply = 0
        self.field_sequence = None

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(Op.PUSHEXPR_REPLYFIELD)
        writer.write_int_2(self.reply)
        writer.write_field_sequence(self.field_sequence)


class PushConstantOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_PUSHEXPR_CONSTANT opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PushConstantOpNode, self).__init__()
        self.const_value = 0

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(Op.PUSHEXPR_CONSTANT)
        writer.write_half_float(self.const_value)


_jump_if_expr_subcode = {'==': Op.JMPIFEXPR_EQ,
                         '!=': Op.JMPIFEXPR_NE,
                         '<': Op.JMPIFEXPR_LT,
                         '>': Op.JMPIFEXPR_GT}

_jump_if_expr_ex_subcode = {'==': Op.JMPIFEXPR_EX_EQ,
                            '!=': Op.JMPIFEXPR_EX_NE,
                            '<': Op.JMPIFEXPR_EX_LT,
                            '>': Op.JMPIFEXPR_EX_GT}


class JumpIfExprOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_JMPIFEXPR_XX and ZEPTOVM_OP_JMPIFEXPR_EX_XX opcodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(JumpIfExprOpNode, self).__init__()
        self._subcode = None
        self.args = None
        self.threshold = 0
        self.destination = None
        self.delta = 0

    def set_subcode(self, subcode):
        '''
        Sets the conditional subcode ['==', '!=', '<', '>']
        '''
        assert subcode in _jump_if_field_subcode
        self._subcode = subcode

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        assert len(self.args) == 1
        assert not self.args[0].optional_immediate

        if self.args[0].is_default():
            writer.write_opcode(_jump_if_expr_subcode[self._subcode])
        else:
            writer.write_opcode(_jump_if_expr_ex_subcode[self._subcode])
            writer.write_oparg(self.args[0])

        writer.write_half_float(self.threshold)
        writer.write_delta(self.delta, self.destination)
