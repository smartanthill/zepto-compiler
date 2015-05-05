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
from smartanthill_zc.encode import ZeptoEncoder


def write_text_op_codes(compiler, node):
    '''
    Writes target code to text format
    Used for development and testing
    '''
    w = _TextWriter()
    node.write(w)

    compiler.check_stage('write_text')

    return w.get_result()


def check_int_range(max_bytes, value):

    assert max_bytes >= 1
    assert max_bytes <= 8

    lvalue = long(value)

    assert lvalue >= -(2 ** ((8 * max_bytes) - 1))
    assert lvalue <= (2 ** ((8 * max_bytes) - 1)) - 1

    return lvalue


def check_uint_range(max_bytes, value):

    assert max_bytes >= 1
    assert max_bytes <= 8

    lvalue = long(value)

    assert lvalue >= 0
    assert lvalue < 2 ** (8 * max_bytes)

    return lvalue


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

    def write_bytes(self, data):
        '''
        Adds a binary field to current operation
        '''
        if len(data) == 0:
            self._current += '|[]'
        else:
            self._current += '|[0x%s]' % binascii.hexlify(data)

    def write_long(self, value):
        '''
        Adds a binary field to current operation
        '''
        self._current += '|%d' % value

    def write_int_2(self, value):
        '''
        Adds an Encoded-Signed-Int<max=2> field
        '''
        lvalue = check_int_range(2, value)
        self.write_long(lvalue)

    def write_uint_2(self, value):
        '''
        Adds an Encoded-Unsigned-Int<max=2> field
        '''
        lvalue = check_uint_range(2, value)
        self.write_long(lvalue)

    def write_uint_4(self, value):
        '''
        Adds an Encoded-Unsigned-Int<max=4> field
        '''
        lvalue = check_uint_range(4, value)
        self.write_long(lvalue)

    def write_bitfield(self, bits):
        '''
        Adds a bitfield from a list of booleans. MSB completed with 0
        '''
        flags = []
        for current in bits.names:
            if current in bits.values and bits.values[current]:
                flags.append(current)

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
            self.write_bytes([])
        else:
            self.write_uint_2(len(data))
            self.write_bytes(data)

    def write_text(self, text):
        '''
        Add a free text, only for easier testing
        '''
        self._finish_current()
        self._result.append('/* %s */' % text)
