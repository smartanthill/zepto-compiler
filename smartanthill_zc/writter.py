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
from smartanthill_zc.encode import ZeptoEncoder
import binascii


def write_text_op_codes(compiler, node):
    '''
    Writes target code to text format
    Used for development and testing
    '''
    w = _TextWriter()
    node.write(w)

    compiler.check_stage('write_text')

    return w.get_result()


class _TextWriter(object):

    '''
    Writer implementation for writing text representation
    Used for development and testing
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self._encoder = ZeptoEncoder()
        self._result = []
        self._current = None

    def get_result(self):
        '''
        Returns a list of strings, each with one operation text
        '''
        if self._current:
            self._result.append(self._current)
            self._current = None

        return self._result

    def write_opcode(self, node):
        '''
        Begins a new operation, writes the opcode
        '''
        if self._current:
            self._result.append(self._current)

        self._current = node.opcode.name

    def write_bytes(self, data):
        '''
        Adds a binary field to current operation
        '''
        self._current += '|0x' + binascii.hexlify(data)

    def write_int_2(self, value):
        '''
        Adds an Encoded-Signed-Int<max=2> field
        '''
        self.write_bytes(self._encoder.encode_signed_int(2, value))

    def write_uint_2(self, value):
        '''
        Adds an Encoded-Unsigned-Int<max=2> field
        '''
        self.write_bytes(self._encoder.encode_unsigned_int(2, value))

    def write_uint_4(self, value):
        '''
        Adds an Encoded-Unsigned-Int<max=4> field
        '''
        self.write_bytes(self._encoder.encode_unsigned_int(4, value))

    def write_bitfield(self, bits):
        '''
        Adds a bitfield from a list of booleans. MSB completed with 0
        '''
        self.write_bytes(bytearray([self._encoder.encode_bitfield(bits)]))

    def write_opaque_data(self, max_size_bytes, data):
        '''
        Adds an opaque data binary field to current operation
        First adds a field with the data size, and data itself after it
        '''
        if not data:
            self.write_bytes(self._encoder.encode_unsigned_int(max_size_bytes,
                                                               0))
        else:
            self.write_bytes(self._encoder.encode_unsigned_int(max_size_bytes,
                                                               len(data)))
            self.write_bytes(data)
