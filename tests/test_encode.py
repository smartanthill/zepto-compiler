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

import sys
import pytest
import random

from smartanthill_zc.encode import encode_unsigned_int, encode_signed_int, \
    decode_unsigned_int, decode_signed_int, encode_bitfield


def encode_unsigned_helper(max_bytes, value, byte_values):
    enc1 = encode_unsigned_int(max_bytes, value)
    enc2 = bytearray(byte_values)
    assert enc1 == enc2

def test_encode_unsigned_int():

    encode_unsigned_helper(1, 0, [0])
    encode_unsigned_helper(1, 127, [127])

    encode_unsigned_helper(2, 128, [128, 0])
    encode_unsigned_helper(2, 129, [128, 1])
    encode_unsigned_helper(2, 255, [128, 127])
    encode_unsigned_helper(2, 256, [129, 0])
    encode_unsigned_helper(2, 16511, [255, 127])

    encode_unsigned_helper(3, 16512, [128, 128, 0])
    encode_unsigned_helper(3, 2113663, [255, 255, 127])

    encode_unsigned_helper(4, 2113664, [128, 128, 128, 0])
    encode_unsigned_helper(4, 270549119, [255, 255, 255, 127])


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

    encode_signed_helper(1, -64, 0)
    encode_signed_helper(1, 0, 64)
    encode_signed_helper(1, 63, 127)

    # 2 bytes
    encode_signed_helper(2, -8256, 128)  # -8256 + 8256 + 128
    encode_signed_helper(2, -65, 8319)  # -65 + 8256 + 128

    encode_signed_helper(2, 64, 8320)  # 64 + 8256
    encode_signed_helper(2, 8255, 16511) # 8255 + 8256

    encode_signed_helper(3, -1056832 , 16512)
    encode_signed_helper(3, -8257, 1065087)

    encode_signed_helper(3, 8256, 1065088)
    encode_signed_helper(3, 1056831, 2113663)

    encode_signed_helper(4, -135274560, 2113664)
    encode_signed_helper(4, -1056833, 136331391)

    encode_signed_helper(4, 1056832, 136331392)
    encode_signed_helper(4, 135274559, 270549119)


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

