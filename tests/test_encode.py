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

from smartanthill_zc.compiler import Compiler, Ctx
from smartanthill_zc.encode import encode_unsigned_int, encode_signed_int, \
    decode_unsigned_int, decode_signed_int, create_half_float,\
    half_float_next_down, half_float_next_up, half_float_value, Encoding
from smartanthill_zc.op_node import BitField
from smartanthill_zc.parse_xml import get_enconding_helper


def encode_unsigned_helper(value, byte_values):
    enc1 = encode_unsigned_int(value)
    enc2 = bytearray(byte_values)
    assert enc1 == enc2


def test_encode_unsigned_int():

    encode_unsigned_helper(0, [0])
    encode_unsigned_helper(127, [127])

    encode_unsigned_helper(128, [128, 1])
    encode_unsigned_helper(129, [129, 1])
    encode_unsigned_helper(255, [255, 1])
    encode_unsigned_helper(256, [128, 2])
    encode_unsigned_helper(16383, [255, 127])
    encode_unsigned_helper(16511, [255, 128, 1])

    encode_unsigned_helper(16512, [128, 129, 1])

    encode_unsigned_helper(2097151, [255, 255, 127])
    encode_unsigned_helper(2113663, [255, 128, 129, 1])

    encode_unsigned_helper(2113664, [128, 129, 129, 1])
    encode_unsigned_helper(270549119, [255, 128, 129, 129, 1])


def test_encode_unsigned_int_raise_0():
    with pytest.raises(AssertionError):

        encode_unsigned_int(-1)


def encode_signed_helper(value, unsigned_value):
    enc1 = encode_signed_int(value)
    enc2 = encode_unsigned_int(unsigned_value)
    assert enc1 == enc2


def test_encode_signed_int():

    encode_signed_helper(-64, 127)
    encode_signed_helper(0, 0)
    encode_signed_helper(63, 126)

    # 2 bytes
    encode_signed_helper(-8256, 16511)  # -8256 + 8256 + 128
    encode_signed_helper(-65, 129)  # -65 + 8256 + 128

    encode_signed_helper(64, 128)  # 64 + 8256
    encode_signed_helper(8255, 16510)  # 8255 + 8256

    encode_signed_helper(-1056832, 2113663)
    encode_signed_helper(-8257, 16513)

    encode_signed_helper(8256, 16512)
    encode_signed_helper(1056831, 2113662)

    encode_signed_helper(-135274560, 270549119)
    encode_signed_helper(-1056833, 2113665)

    encode_signed_helper(1056832, 2113664)
    encode_signed_helper(135274559, 270549118)


def encode_decode_unsigned_helper(value):
    enc = encode_unsigned_int(value)
    res = decode_unsigned_int(enc)
    assert value == res


def test_decode_unsigned_int():

    encode_decode_unsigned_helper(0)
    encode_decode_unsigned_helper(127)

    encode_decode_unsigned_helper(128)
    encode_decode_unsigned_helper(16511)

    encode_decode_unsigned_helper(16512)
    encode_decode_unsigned_helper(2113663)

    encode_decode_unsigned_helper(2113664)


def encode_decode_signed_helper(value):
    enc = encode_signed_int(value)
    res = decode_signed_int(enc)
    assert value == res


def test_decode_signed_int():

    encode_decode_signed_helper(-64)
    encode_decode_signed_helper(0)
    encode_decode_signed_helper(63)

    encode_decode_signed_helper(-65)
    encode_decode_signed_helper(-8256)

    encode_decode_signed_helper(64)
    encode_decode_signed_helper(8255)

    encode_decode_signed_helper(-8257)
    encode_decode_signed_helper(-1056832)

    encode_decode_signed_helper(8256)
    encode_decode_signed_helper(1056831)

    encode_decode_signed_helper(-1056833)

    encode_decode_signed_helper(1056832)


def test_random_unsigned_int():

    low = 0
    high = 256
    for i in range(1, 9):
        for j in range(10):
            v = random.randint(low, high - 1)
            encode_decode_unsigned_helper(v)

#        print 'unsigned [%s, %s] Ok!' % (low, high)
        low = high
        high *= 256


def test_random_signed_int():

    high = 128
    for i in range(1, 9):
        low = -high
        for j in range(10):
            v = random.randint(low, high - 1)
            encode_decode_signed_helper(v)

#        print 'signed [%s, %s] Ok!' % (low, high)
        high *= 256


def encode_bitfield_helper(flags):

    bits = BitField(["bit0", "bit1", "bit2", "bit3", "bit4", "bit5"])
    for each in flags:
        bits.set(each, True)

    return bits.to_integer()


def test_encode_bitfield():

    assert encode_bitfield_helper([]) == 0
    assert encode_bitfield_helper(["bit0"]) == 1
    assert encode_bitfield_helper(["bit1"]) == 2
    assert encode_bitfield_helper(["bit0", "bit1"]) == 3
    assert encode_bitfield_helper(["bit2"]) == 4
    assert encode_bitfield_helper(["bit3"]) == 8
    assert encode_bitfield_helper(["bit4"]) == 16
    assert encode_bitfield_helper(["bit5"]) == 32


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


def test_encode_min_max_1():

    comp = Compiler()
    helper = get_enconding_helper(comp, Ctx.NONE,
                                  {'type': 'encoded-int[max=1]'})

    assert helper.encoding == Encoding.SIGNED_INT
    assert helper._min_value == -128
    assert helper._max_value == 127


def test_encode_min_max_2():

    comp = Compiler()
    helper = get_enconding_helper(comp, Ctx.NONE,
                                  {'type': 'encoded-int[max=1]',
                                   'min': '1',
                                   'max': '1'})

    assert helper.encoding == Encoding.SIGNED_INT
    assert helper._min_value == 1
    assert helper._max_value == 1


def test_encode_min_max_3():

    comp = Compiler()
    helper = get_enconding_helper(comp, Ctx.NONE,
                                  {'type': 'encoded-uint[max=1]',
                                   'min': '1',
                                   'max': '1'})

    assert helper.encoding == Encoding.UNSIGNED_INT
    assert helper._min_value == 1
    assert helper._max_value == 1


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
