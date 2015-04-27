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

    DEVICECAPS = _OpImpl(1, 'ZEPTOVM_OP_DEVICECAPS')
    EXEC = _OpImpl(2, 'ZEPTOVM_OP_EXEC')
    PUSHREPLY = _OpImpl(3, 'ZEPTOVM_OP_PUSHREPLY')
    SLEEP = _OpImpl(4, 'ZEPTOVM_OP_SLEEP')
    TRANSMITTER = _OpImpl(5, 'ZEPTOVM_OP_TRANSMITTER')
    MCUSLEEP = _OpImpl(6, 'ZEPTOVM_OP_MCUSLEEP')
    # limited support in Zepto VM-One, full support from Zepto VM-Tiny
    POPREPLIES = _OpImpl(7, 'ZEPTOVM_OP_POPREPLIES')
    EXIT = _OpImpl(8, 'ZEPTOVM_OP_EXIT')
    # limited support in Zepto VM-One, full support from Zepto VM-Tiny
    APPENDTOREPLY = _OpImpl(9, 'ZEPTOVM_OP_APPENDTOREPLY')

    # below, instructions are not supported by Zepto VM-One
    JMP = _OpImpl(10, 'ZEPTOVM_OP_JMP')
    JMPIFREPLYFIELD_LT = _OpImpl(11, 'ZEPTOVM_OP_JMPIFREPLYFIELD_LT')
    JMPIFREPLYFIELD_GT = _OpImpl(12, 'ZEPTOVM_OP_JMPIFREPLYFIELD_GT')
    JMPIFREPLYFIELD_EQ = _OpImpl(13, 'ZEPTOVM_OP_JMPIFREPLYFIELD_EQ')
    JMPIFREPLYFIELD_NE = _OpImpl(14, 'ZEPTOVM_OP_JMPIFREPLYFIELD_NE')
    MOVEREPLYTOFRONT = _OpImpl(15, 'ZEPTOVM_OP_MOVEREPLYTOFRONT')

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
        if name not in self.names:
            assert False

        self.values[name] = value
        
    def get(self, name):
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

    def write(self, writer):
        '''
        Base method for writing the target tree to the output writer
        '''
        pass


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

    def __init__(self):
        '''
        Constructor
        '''
        super(PopRepliesOpNode, self).__init__()
        self._opcode = Op.POPREPLIES
        self._replies_count = 0

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
