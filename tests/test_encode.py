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

import random
import sys

import pytest

from smartanthill_zc.encode import encode_unsigned_int, encode_signed_int, \
    decode_unsigned_int, decode_signed_int, encode_bitfield, create_half_float,\
    half_float_next_down, half_float_next_up, half_float_value


def encode_unsigned_helper(max_bytes, value, byte_values):
    enc1 = encode_unsigned_int(max_bytes, value)
    enc2 = bytearray(byte_values)
    assert enc1 == enc2


def test_encode_unsigned_int():

    encode_unsigned_helper(1, 0, [0])
    encode_unsigned_helper(1, 127, [127])

    encode_unsigned_helper(2, 128, [128, 1])
    encode_unsigned_helper(2, 129, [129, 1])
    encode_unsigned_helper(2, 255, [255, 1])
    encode_unsigned_helper(2, 256, [128, 2])
    encode_unsigned_helper(2, 16383, [255, 127])
    encode_unsigned_helper(3, 16511, [255, 128, 1])

    encode_unsigned_helper(3, 16512, [128, 129, 1])

    encode_unsigned_helper(3, 2097151, [255, 255, 127])
    encode_unsigned_helper(4, 2113663, [255, 128, 129, 1])

    encode_unsigned_helper(4, 2113664, [128, 129, 129, 1])
    encode_unsigned_helper(5, 270549119, [255, 128, 129, 129, 1])


def test_encode_unsigned_int_raise_0():
    with pytest.raises(AssertionError):

        encode_unsigned_int(4, -1)


def test_encode_unsigned_int_raise_1():
    with pytest.raises(AssertionError):

        encode_unsigned_int(1, 256)


def encode_signed_helper(max_bytes, value, unsigned_value):
    enc1 = encode_signed_int(max_bytes, value)
    enc2 = encode_unsigned_int(max_bytes, unsigned_value)
    assert enc1 == enc2


def test_encode_signed_int():

    encode_signed_helper(1, -64, 127)
    encode_signed_helper(1, 0, 0)
    encode_signed_helper(1, 63, 126)

    # 2 bytes
    encode_signed_helper(2, -8256, 16511)  # -8256 + 8256 + 128
    encode_signed_helper(2, -65, 129)  # -65 + 8256 + 128

    encode_signed_helper(2, 64, 128)  # 64 + 8256
    encode_signed_helper(2, 8255, 16510)  # 8255 + 8256

    encode_signed_helper(3, -1056832, 2113663)
    encode_signed_helper(3, -8257, 16513)

    encode_signed_helper(3, 8256, 16512)
    encode_signed_helper(3, 1056831, 2113662)

    encode_signed_helper(4, -135274560, 270549119)
    encode_signed_helper(4, -1056833, 2113665)

    encode_signed_helper(4, 1056832, 2113664)
    encode_signed_helper(4, 135274559, 270549118)


def test_encode_signed_int_raise_0():
    with pytest.raises(AssertionError):

        encode_signed_int(1, -129)


def test_encode_signed_int_raise_1():
    with pytest.raises(AssertionError):

        encode_signed_int(1, 128)


def encode_decode_unsigned_helper(max_bytes, value):
    enc = encode_unsigned_int(max_bytes, value)
    res = decode_unsigned_int(enc)
    assert value == res


def test_decode_unsigned_int():

    encode_decode_unsigned_helper(1, 0)
    encode_decode_unsigned_helper(1, 127)

    encode_decode_unsigned_helper(2, 128)
    encode_decode_unsigned_helper(2, 16511)

    encode_decode_unsigned_helper(3, 16512)
    encode_decode_unsigned_helper(3, 2113663)

    encode_decode_unsigned_helper(4, 2113664)


def encode_decode_signed_helper(max_bytes, value):
    enc = encode_signed_int(max_bytes, value)
    res = decode_signed_int(enc)
    assert value == res


def test_decode_signed_int():

    encode_decode_signed_helper(1, -64)
    encode_decode_signed_helper(1, 0)
    encode_decode_signed_helper(1, 63)

    encode_decode_signed_helper(2, -65)
    encode_decode_signed_helper(2, -8256)

    encode_decode_signed_helper(2, 64)
    encode_decode_signed_helper(2, 8255)

    encode_decode_signed_helper(3, -8257)
    encode_decode_signed_helper(3, -1056832)

    encode_decode_signed_helper(3, 8256)
    encode_decode_signed_helper(3, 1056831)

    encode_decode_signed_helper(4, -1056833)

    encode_decode_signed_helper(4, 1056832)


def test_random_unsigned_int():

    low = 0
    high = 256
    for i in range(1, 9):
        for j in range(10):
            v = random.randint(low, high - 1)
            encode_decode_unsigned_helper(i, v)

#        print 'unsigned [%s, %s] Ok!' % (low, high)
        low = high
        high *= 256


def test_random_signed_int():

    high = 128
    for i in range(1, 9):
        low = -high
        for j in range(10):
            v = random.randint(low, high - 1)
            encode_decode_signed_helper(i, v)

#        print 'signed [%s, %s] Ok!' % (low, high)
        high *= 256


def encode_bitfield_helper(bits, value):
    enc = encode_bitfield(bits)
    assert enc == value


def test_encode_bitfield():

    assert encode_bitfield([False]) == 0
    assert encode_bitfield([True]) == 1
    assert encode_bitfield([True, False]) == 2
    assert encode_bitfield([True, True]) == 3
    assert encode_bitfield([True, False, False]) == 4
    assert encode_bitfield([True, False, False, False]) == 8
    assert encode_bitfield([True, False, False, False, False]) == 16
    assert encode_bitfield([True, False, False, False, False, False]) == 32
    assert encode_bitfield([True, False, False,
                            False, False, False, False]) == 64


def _encode_hf_helper(number, ref):
    enc = create_half_float(number)
    b = enc.encode()
    s = b[0] >> 7
    e = (b[0] >> 2) & 0x1f
    m = ((b[0] & 0x03) << 8) | b[1]

    res = '{0:01b} {1:05b} {2:010b}'.format(s, e, m)

    assert res == ref


def test_encode_half_float():

    assert half_float_value(0.) == 0.
    assert half_float_value(1.) == 1.
    assert half_float_value(-1.) == -1.
    assert half_float_value(2048.) == 2048.
    assert half_float_value(2049.) == 2050.
    assert half_float_value(2050.) == 2050.

    # from wikipedia
    _encode_hf_helper(0., '0 00000 0000000000')
    _encode_hf_helper(1., '0 01111 0000000000')
    _encode_hf_helper(1.0009765625, '0 01111 0000000001')  # next after 1
    _encode_hf_helper(65504., '0 11110 1111111111')  # max half
    _encode_hf_helper(6.10352e-5, '0 00001 0000000000')  # min pos normal
    _encode_hf_helper(6.09756e-5, '0 00000 1111111111')  # max subnormal
    _encode_hf_helper(5.96046e-8, '0 00000 0000000001')  # min pos subnormal
    _encode_hf_helper(0.333251953125, '0 01101 0101010101')  # 1/3

    # subnormal range
    _encode_hf_helper(half_float_next_up(0.), '0 00000 0000000001')
    _encode_hf_helper(half_float_next_down(0.), '1 00000 0000000001')

    t1 = half_float_next_down(half_float_next_up(0.))
    _encode_hf_helper(t1, '0 00000 0000000000')
    t2 = half_float_next_up(half_float_next_down(0.))
    _encode_hf_helper(t2, '0 00000 0000000000')

    t3 = half_float_next_up(half_float_next_up(0.))
    _encode_hf_helper(t3, '0 00000 0000000010')

    t4 = half_float_next_down(half_float_next_down(0.))
    _encode_hf_helper(t4, '1 00000 0000000010')

    # normal to subnormal
    _encode_hf_helper(half_float_next_down(6.10352e-5), '0 00000 1111111111')

    _encode_hf_helper(1., '0 01111 0000000000')
    _encode_hf_helper(half_float_next_up(1.), '0 01111 0000000001')
    _encode_hf_helper(half_float_next_down(1.), '0 01110 1111111111')


def main():

    print decode_unsigned_int(bytearray([255, 127]))

    return

    low = 0
    high = 256
    for i in range(1, 9):
        for j in range(10):
            v = random.randint(low, high - 1)
            encode_decode_unsigned_helper(i, v)

        print 'unsigned [%s, %s] Ok!' % (low, high - 1)
        low = high
        high *= 256

    high = 128
    for i in range(1, 9):
        low = -high
        for j in range(10):
            v = random.randint(low, high - 1)
            encode_decode_signed_helper(i, v)

        print 'signed [%s, %s] Ok!' % (low, high - 1)
        high *= 256

    print 'Ok!!!'

# temporary entrance
if __name__ == "__main__":
    sys.exit(main())
