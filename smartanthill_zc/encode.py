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


class ZeptoEncoder(object):

    '''
    Encoder class, used for easier replacement of encoding strategy if needed
    Also has a cache of already encoded values
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._unsigneds = {}
        self._signeds = {}

    def encode_unsigned_int(self, max_bytes, value):
        '''
        Encode an Encoded-Unsigned-Int
        '''
        if value not in self._unsigneds:
            self._unsigneds[value] = encode_unsigned_int(max_bytes, value)

        return self._unsigneds[value]

    def encode_signed_int(self, max_bytes, value):
        '''
        Encode an Encoded-Signed-Int
        '''
        if value not in self._signeds:
            self._signeds[value] = encode_signed_int(max_bytes, value)

        return self._signeds[value]

    def encode_bitfield(self, bits):
        '''
        Encode a bit field
        '''
        # pylint: disable=no-self-use

        return encode_bitfield(bits)


def _encode_unsigned(value):
    '''
    Encoded-*-Int internal implemntation function
    '''

    result = bytearray()
    not_last = False

    while value >= 128:
        current = value % 128
        if not_last:
            current += 128

        not_last = True
        result.append(current)

        value /= 128
        value -= 1

    if not_last:
        value += 128

    result.append(value)

    result.reverse()

    return result


def encode_unsigned_int(max_bytes, value):
    '''
    Encoded-Unsigned-Int arithmetic implementation
    '''
    assert max_bytes >= 1
    assert max_bytes <= 8

    value = int(value)

    assert value >= 0
    assert value < 2 ** (8 * max_bytes)

    return _encode_unsigned(value)


def encode_signed_int(max_bytes, value):
    '''
    Encoded-Signed-Int arithmetic implementation
    '''

    assert max_bytes >= 1
    assert max_bytes <= 8

    value = int(value)

    assert value >= -(2 ** ((8 * max_bytes) - 1))
    assert value <= (2 ** ((8 * max_bytes) - 1)) - 1

    if value >= 0:

        limit = 64
        while value >= limit:
            limit *= 128
            limit += 64

        return _encode_unsigned(value + limit)
    else:
        limit = 64
        gap = 0
        while value < -limit:
            limit *= 128
            limit += 64

            gap *= 128
            gap += 128

        return _encode_unsigned(value + limit + gap)


def decode_unsigned_int(byte_list):
    '''
    Encoded-Unsigned-Int decoder implementation
    '''

    i = 0
    value = 0
    while byte_list[i] >= 128:
        assert byte_list[i] < 256

        c = byte_list[i] - 128 + 1

        value += c
        value *= 128
        i += 1

    assert byte_list[i] >= 0
    assert byte_list[i] < 128
    value += byte_list[i]

    assert len(byte_list) == i + 1

    return value


def decode_signed_int(byte_list):
    '''
    Encoded-Signed-Int decoder implementation
    '''

    value = decode_unsigned_int(byte_list)
    base = 0
    half = 64
    while value >= (base * 128) + 128:
        base *= 128
        base += 128

        half *= 128

    if value - base < half:
        # negative
        return value - half - base - base / 2
    else:
        # positive
        return value - half - base + base / 2


def encode_bitfield(bits):
    '''
    Bit field encoder implementation
    '''

    assert len(bits) >= 0
    assert len(bits) <= 7

    i = 1
    result = 0
    for current in reversed(bits):
        if current:
            result += i

        i *= 2

    return result
