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
    PUSHEXPR_CONSTANT = _OpImpl(16, 'ZEPTOVM_OP_PUSHEXPR_CONSTANT')
    PUSHEXPR_REPLYFIELD = _OpImpl(17, 'ZEPTOVM_OP_PUSHEXPR_REPLYFIELD')
    EXPRUNOP = _OpImpl(18, 'ZEPTOVM_OP_EXPRUNOP')
    EXPRUNOP_EX = _OpImpl(19, 'ZEPTOVM_OP_EXPRUNOP_EX')
    EXPRUNOP_EX2 = _OpImpl(20, 'ZEPTOVM_OP_EXPRUNOP_EX2')
    EXPRBINOP = _OpImpl(21, 'ZEPTOVM_OP_EXPRBINOP')
    EXPRBINOP_EX = _OpImpl(22, 'ZEPTOVM_OP_EXPRBINOP_EX')
    EXPRBINOP_EX2 = _OpImpl(23, 'ZEPTOVM_OP_EXPRBINOP_EX2')
    JMPIFEXPR_LT = _OpImpl(24, 'ZEPTOVM_OP_JMPIFEXPR_LT')
    JMPIFEXPR_GT = _OpImpl(25, 'ZEPTOVM_OP_JMPIFEXPR_GT')
    JMPIFEXPR_EQ = _OpImpl(26, 'ZEPTOVM_OP_JMPIFEXPR_EQ')
    JMPIFEXPR_NE = _OpImpl(27, 'ZEPTOVM_OP_JMPIFEXPR_NE')
    JMPIFEXPR_EX_LT = _OpImpl(28, 'ZEPTOVM_OP_JMPIFEXPR_EX_LT')
    JMPIFEXPR_EX_GT = _OpImpl(29, 'ZEPTOVM_OP_JMPIFEXPR_EX_GT')
    JMPIFEXPR_EX_EQ = _OpImpl(30, 'ZEPTOVM_OP_JMPIFEXPR_EX_EQ')
    JMPIFEXPR_EX_NE = _OpImpl(31, 'ZEPTOVM_OP_JMPIFEXPR_EX_NE')
    CALL = _OpImpl(32, 'ZEPTOVM_OP_CALL')
    RET = _OpImpl(33, 'ZEPTOVM_OP_RET')
    SWITCH = _OpImpl(34, 'ZEPTOVM_OP_SWITCH')
    SWITCH_EX = _OpImpl(35, 'ZEPTOVM_OP_SWITCH_EX')
    INCANDJMPIF = _OpImpl(36, 'ZEPTOVM_OP_INCANDJMPIF')
    DECANDJMPIF = _OpImpl(37, 'ZEPTOVM_OP_DECANDJMPIF')

    # below, instructions are not supported by Zepto VM-Small and below
    PARALLEL = _OpImpl(38, 'ZEPTOVM_OP_PARALLEL')


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

    def calculate_byte_size(self, calculator):
        '''
        Calculates the size in bytes for this node.
        Needed by jumps to calculate jump offsets
        '''

        begin = calculator.index
        self.write(calculator)
        self._byte_size = calculator.index - begin


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
        self.target_level = 0

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
        writer.write_text('reply: %s' % field_sequence_to_str(self.reply_fs))
        self.child_op_list.write(writer)


class ExecOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_EXEC opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ExecOpNode, self).__init__()
        self._opcode = Op.EXEC
        self.bodypart_id = 0
        self.data = None

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(self._opcode)
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
        self._opcode = Op.PUSHREPLY
        self.data = None

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(self._opcode)
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
        self._opcode = Op.TRANSMITTER
        self._bf = BitField(['ON'])

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(self._opcode)
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
        self._opcode = Op.SLEEP
        self.msec_delay = 0

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(self._opcode)
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
        self._opcode = Op.MCUSLEEP
        self.sec_delay = 0
        self._bf = BitField(['MAYDROPEARLIERINSTRUCTIONS',
                             'TRANSMITTERONWHENBACK'])

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(self._opcode)
        writer.write_uint_4(self.sec_delay)
        writer.write_bitfield(self._bf)


class PopRepliesOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_POPREPLIES opcode
    '''

    def __init__(self, replies_count):
        '''
        Constructor
        '''
        super(PopRepliesOpNode, self).__init__()
        self._opcode = Op.POPREPLIES
        self._replies_count = replies_count

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(self._opcode)
        writer.write_uint_2(self._replies_count)


class ExitOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_EXIT opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ExitOpNode, self).__init__()
        self._opcode = Op.EXIT
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
            writer.write_opcode(self._opcode)
            writer.write_bitfield(self._bf)
            if self._bf.get('FORCED-PADDING-FLAG'):
                writer.write_uint_2(self._opt_padding_to)
        else:
            writer.write_text('exit|islast')


class JumpDesptination(object):

    BEGIN = 'begin:'
    END = 'end:'


class IfOpNode(OpcodeNode):

    '''
    Holder for an if implementation
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(IfOpNode, self).__init__()
        self._opcode = Op.INVALID
        self.child_condition = None
        self.child_body = None

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
        TODO calculate jump size in bytes
        '''

        body = 0
        body_lines = len(self.child_body.childs_operations)
        for current in self.child_body.childs_operations:
            body += current.get_byte_size()  # already calculated

        begin = 0
        begin_lines = 0
        for current in reversed(self.child_condition.childs_operations):
            if current.destination == JumpDesptination.BEGIN:
                current.delta = begin
                current.delta_lines = begin_lines
            elif current.destination == JumpDesptination.END:
                current.delta = begin + body
                current.delta_lines = begin_lines + body_lines
            else:
                assert False

            current.calculate_byte_size(calculator)
            begin += current.get_byte_size()
            begin_lines += 1

        self._byte_size = begin + body

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        # writer.write_text('if')
        self.child_condition.write(writer)
        writer.write_text(JumpDesptination.BEGIN)
        self.child_body.write(writer)
        writer.write_text(JumpDesptination.END)


class JumpIfFieldOpNode(OpcodeNode):

    '''
    Node for  ZEPTOVM_OP_JMPIFREPLYFIELD_XX opcode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(JumpIfFieldOpNode, self).__init__()
        self._opcode = Op.INVALID
        self.reply = 0
        self.field_sequence = None
        self.threshold = 0
        self.destination = None
        self.delta = 0
        self.delta_lines = 0

    def set_subcode(self, subcode):
        '''
        Sets the conditional subcode ['==', '!=', '<', '>']
        '''

        if subcode == '==':
            self._opcode = Op.JMPIFREPLYFIELD_EQ
        elif subcode == '!=':
            self._opcode = Op.JMPIFREPLYFIELD_NE
        elif subcode == '<':
            self._opcode = Op.JMPIFREPLYFIELD_LT
        elif subcode == '>':
            self._opcode = Op.JMPIFREPLYFIELD_GT
        else:
            assert False

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(self._opcode)
        writer.write_int_2(self.reply)
        writer.write_field_sequence(self.field_sequence)
        writer.write_half_float(self.threshold)
        writer.write_delta(self.destination, self.delta, self.delta_lines)


class MoveReplyOpNode(OpcodeNode):

    '''
    Node for ZEPTOVM_OP_POPREPLIES opcode
    '''

    def __init__(self, reply_number):
        '''
        Constructor
        '''
        super(MoveReplyOpNode, self).__init__()
        self._opcode = Op.MOVEREPLYTOFRONT
        self._reply_number = reply_number

    def write(self, writer):
        '''
        Write this node to the output writer
        '''
        writer.write_opcode(self._opcode)
        writer.write_int_2(self._reply_number)
