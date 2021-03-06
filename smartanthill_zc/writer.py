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

import binascii

from smartanthill_zc import encode
from smartanthill_zc.encode import (field_sequence_to_str, Encoding)


def write_text_op_codes(compiler, target, parameters):
    '''
    Writes target code to text format
    Used for development and testing
    '''
    target.parameters_encode(compiler, parameters)
    compiler.check_stage('encode')
    target.calculate_byte_size(BinaryWriter(compiler))

    w = _TextWriter(compiler)
    target.write(w)

    compiler.check_stage('write_text')

    return w.get_result()


def write_binary(compiler, target, parameters):
    '''
    Writes target code to binary format
    '''
    target.parameters_encode(compiler, parameters)
    compiler.check_stage('encode')
    target.calculate_byte_size(BinaryWriter(compiler))

    w = BinaryWriter(compiler)
    target.write(w)

    compiler.check_stage('write_binary')

    return w.get_result()


def _check_int_range(max_bytes, value):

    value = long(value)

    min_v, max_v = encode.get_signed_min_max(max_bytes)

    assert value >= min_v
    assert value <= max_v


def _check_uint_range(max_bytes, value):

    value = long(value)

    min_v, max_v = encode.get_unsigned_min_max(max_bytes)

    assert value >= min_v
    assert value <= max_v


class _TextWriter(object):

    '''
    Writer implementation for writing text representation
    Used for development and testing
    '''

    def __init__(self, compiler):
        '''
        Constructor
        '''
        self._result = []
        self._current = None
        self._compiler = compiler

    def create_sub_writer(self):
        '''
        Creates a new sub writer instance
        '''
        return _TextWriter(self._compiler)

    def write_sub_writer(self, sub_writer):
        '''
        Writes the content of another writer instance
        '''

        self._finish_current()

        for each in sub_writer.get_result():
            self._current.append(each)

    def _finish_current(self):
        '''
        Finishes current opcode
        '''
        if self._current:
            self._current += '|'
            self._result.append(self._current)
            self._current = None

    def get_result(self):
        '''
        Returns a list of strings, each with one operation text
        '''
        self._finish_current()

        return self._result

    def write_opcode(self, opcode):
        '''
        Begins a new operation, writes the opcode
        '''
        self._finish_current()

        self._current = '|' + opcode.name

    def write_subcode(self, opcode):
        '''
        Adds 1 byte subcode for ZEPTOVM_OP_EXPRUNOP and ZEPTOVM_OP_EXPRBINOP
        '''
        self._current += '|' + opcode.name

    def write_oparg(self, arg):
        '''
        Adds ZEPTOVM_OP_EXPRUNOP and ZEPTOVM_OP_EXPRBINOP
        OP-POP-FLAG-AND-EXPR-OFFSET | OPTIONAL-IMMEDIATE-OP
        '''
        if arg.optional_immediate:
            self._current += '|->'
            self.write_half_float(arg.optional_immediate)
        elif arg.expr_offset:
            self.write_int_2(arg.expr_offset)
            self._current += ','
            if arg.pop_flag:
                self._current += ',POP'
        else:
            self.write_int_2(1)
            self._current += ',POP'

    def write_opresult(self, res):
        '''
        Adds ZEPTOVM_OP_EXPRUNOP_EX2 and ZEPTOVM_OP_EXPRBINOP_EX2
        PUSH-FLAG-AND-PUSH-EXPR-OFFSET
        '''
        assert res.expr_offset
        self.write_int_2(res.expr_offset)
        if res.insert_flag:
            self._current += ',INSERT'

    def _write_bytes(self, data):
        '''
        Adds a binary field to current operation
        '''
        if len(data) == 0:
            self._current += '|[]'
        else:
            # python 2.6 needs str(data)
            self._current += '|[0x%s]' % binascii.hexlify(str(data))

    def write_long(self, value):
        '''
        Adds a binary field to current operation
        '''
        self._current += '|%d' % long(value)

    def write_int_2(self, value):
        '''
        Adds an Encoded-Signed-Int<max=2> field
        '''
        _check_int_range(2, value)
        self.write_long(value)

    def write_uint_2(self, value):
        '''
        Adds an Encoded-Unsigned-Int<max=2> field
        '''
        _check_uint_range(2, value)
        self.write_long(value)

    def write_uint_4(self, value):
        '''
        Adds an Encoded-Unsigned-Int<max=4> field
        '''
        _check_uint_range(4, value)
        self.write_long(value)

    def write_half_float(self, value):
        '''
        Adds a half-float field
        '''
        self._current += '|%g' % value

    def write_field_sequence(self, fs):
        '''
        Adds a half-float field
        '''
        self._current += '|{%s}' % field_sequence_to_str(fs)

    def write_delta(self, delta, destination):
        '''
        Adds a half-float field
        '''
        self._current += '|(%+d):%s:' % (delta, destination)

    def write_bitfield(self, bits):
        '''
        Adds a bitfield
        '''
        flags = bits.to_flag_list()

        if len(flags) == 0:
            self._current += '|0'
        else:
            self._current += '|' + ','.join(flags)

    def write_opaque_data_2(self, data):
        '''
        Adds an opaque data binary field to current operation
        First adds a field with the data size, and data itself after it
        '''
        if not data:
            self.write_uint_2(0)
            self._write_bytes([])
        else:
            self.write_uint_2(len(data))
            self._write_bytes(data)

    def write_text(self, text):
        '''
        Add a free text, only for easier testing
        '''
        self._finish_current()
        self._result.append('/* %s */' % text)


class BinaryWriter(object):

    '''
    Writer implementation for writing binary representation
    '''

    def __init__(self, compiler):
        '''
        Constructor
        '''
        self._result = bytearray()
        self._compiler = compiler

    def create_sub_writer(self):
        '''
        Creates a sub writer
        '''
        return BinaryWriter(self._compiler)

    def write_sub_writer(self, sub_writer):
        '''
        Writes the content of another writer instance
        '''
        assert isinstance(sub_writer, BinaryWriter)

        self._write_bytes(sub_writer.get_result())

    def get_result(self):
        '''
        Returns a list of strings, each with one operation text
        '''
        # self._finish_current()

        return self._result

    def _write_bytes(self, data):
        '''
        Adds a binary field to current operation
        '''
        for each in data:
            self._result.append(each)

    def _write_byte(self, data):
        '''
        Adds a binary field to current operation
        '''
        self._result.append(data)

    def get_size(self):
        '''
        Returns the size, used to calculate jumps sizes
        '''
        return len(self._result)

    def write_opcode(self, opcode):
        '''
        Begins a new operation, writes the opcode
        '''
        # self._finish_current()

        self._write_byte(opcode.opcode)

    def write_subcode(self, subcode):
        '''
        Adds 1 byte subcode for ZEPTOVM_OP_EXPRUNOP and ZEPTOVM_OP_EXPRBINOP
        '''
        self._write_byte(subcode.opcode)

    def write_oparg(self, arg):
        '''
        Adds ZEPTOVM_OP_EXPRUNOP and ZEPTOVM_OP_EXPRBINOP
        OP-POP-FLAG-AND-EXPR-OFFSET | OPTIONAL-IMMEDIATE-OP
        '''
        if arg.optional_immediate:
            self.write_int_2(0)
            self.write_half_float(arg.optional_immediate)
        elif arg.expr_offset:
            val = arg.expr_offset * 2
            if arg.pop_flag:
                val += 1

            self.write_int_2(val)
        else:
            self.write_int_2(3)

    def write_opresult(self, res):
        '''
        Adds ZEPTOVM_OP_EXPRUNOP_EX2 and ZEPTOVM_OP_EXPRBINOP_EX2
        PUSH-FLAG-AND-PUSH-EXPR-OFFSET
        '''
        assert res.expr_offset
        val = res.expr_offset * 2
        if res.insert_flag:
            val += 1

        self.write_int_2(val)

    def write_int_2(self, value):
        '''
        Adds an Encoded-Signed-Int<max=2> field
        '''
        _check_int_range(2, value)
        enc = encode.encode_signed_int(value)
        self._write_bytes(enc)

    def write_uint_2(self, value):
        '''
        Adds an Encoded-Unsigned-Int<max=2> field
        '''
        _check_uint_range(2, value)
        enc = encode.encode_unsigned_int(value)
        self._write_bytes(enc)

    def write_uint_4(self, value):
        '''
        Adds an Encoded-Unsigned-Int<max=4> field
        '''
        _check_uint_range(4, value)
        enc = encode.encode_unsigned_int(value)
        self._write_bytes(enc)

    def write_half_float(self, value):
        '''
        Adds a half-float field
        '''
        enc = encode.encode_half_float(value)
        self._write_bytes(enc)

    def write_field_sequence(self, fs):
        '''
        Adds a field-sequence field
        '''
        enc = bytearray()
        for current in fs:
            enc.append(current.encoding.code)

        enc.append(Encoding.END_OF_SEQUENCE.code)
        self._write_bytes(enc)

    def write_delta(self, delta, destination):
        '''
        Adds jump delta
        '''
        # pylint: disable=unused-argument
        self.write_int_2(delta)

    def write_bitfield(self, bits):
        '''
        Adds a bitfield
        '''
        self.write_int_2(bits.to_integer())

    def write_opaque_data_2(self, data):
        '''
        Adds an opaque data binary field to current operation
        First adds a field with the data size, and data itself after it
        '''
        if not data:
            self.write_uint_2(0)
        else:
            self.write_uint_2(len(data))
            self._write_bytes(data)

    def write_text(self, text):
        '''
        Add a free text, only for easier testing
        Nothing to do in binary modes
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        pass
