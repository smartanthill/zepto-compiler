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
import math


def _encode_unsigned(value):
    '''
    Encoded-*-Int internal implemntation function
    '''

    assert value >= 0
    result = bytearray()

    while value >= 128:
        result.append((value & 0x7f) | 0x80)
        value >>= 7

    result.append(value)

    return result


def get_unsigned_min_max(size):
    '''
    Encoded-Unsigned-Int max and min values    '''

    assert size >= 1
    assert size <= 8
    return (0, 2 ** (8 * size))


def encode_unsigned_int(value):
    '''
    Encoded-Unsigned-Int arithmetic implementation
    '''

    value = long(value)

    return _encode_unsigned(value)


def get_signed_min_max(size):
    '''
    Encoded-Unsigned-Int max and min values    '''

    assert size >= 1
    assert size <= 8
    return (-(2 ** ((8 * size) - 1)), (2 ** ((8 * size) - 1)) - 1)


def encode_signed_int(value):
    '''
    Encoded-Signed-Int arithmetic implementation
    '''

    value = long(value)

    if value >= 0:
        return _encode_unsigned(value << 1)
    else:
        return _encode_unsigned(((~value) << 1) | 1)


def decode_unsigned_int(reversed_data):
    '''
    Encoded-Unsigned-Int decoder implementation
    '''

    assert isinstance(reversed_data, bytearray)

    value = 0
    shift = 0
    while reversed_data[-1] & 0x80 != 0:
        value |= (reversed_data.pop() & 0x7f) << shift
        shift += 7

    value |= reversed_data.pop() << shift

    return value


def decode_signed_int(reversed_data):
    '''
    Encoded-Signed-Int decoder implementation
    '''

    value = decode_unsigned_int(reversed_data)
    if value & 1 == 0:
        return value >> 1
    else:
        return ~(value >> 1)


def encode_half_float(value):
    '''
    Half float encoder implementation
    '''
    enc = create_half_float(value)
    return enc.encode()


class HalfFloatOverflowError(Exception):
    pass


class _HalfFloatBits(object):

    '''
    TODO improve this!!!
    This class holds the internal representation of a half float
    allow bit manipulation and encoding
    '''

    def __init__(self, sign, exp, mantisa):
        '''
        Constructor
        '''
        if exp < 0 or exp >= 31:
            raise HalfFloatOverflowError()

        self.sign = sign
        self.exp = exp
        self.mantisa = mantisa

        if self.mantisa == 0 and self.exp == 0:
            self.sign = 0

        self._check()

    def _check(self):
        '''
        Check this number is a representable half float value
        not infinite nor minus zero
        '''
        assert 0 <= self.exp <= 30
        assert 0 <= self.mantisa <= 0x3ff
        assert self.sign == 0 or self.sign == 1

        if self.exp == 0 and self.mantisa == 0:
            assert self.sign == 0

    def _next(self):
        '''
        Helper to next absolute value
        '''
        if self.mantisa == 0x3ff:
            if self.exp == 30:
                raise HalfFloatOverflowError()
            else:
                self.mantisa = 0
                self.exp += 1
        else:
            self.mantisa += 1

    def _prev(self):
        '''
        Helper to previous absolute value
        '''
        if self.mantisa == 0:
            if self.exp == 0:
                assert False
            else:
                self.mantisa = 0x3ff
                self.exp -= 1
        else:
            self.mantisa -= 1

        if self.mantisa == 0 and self.exp == 0:
            self.sign = 0

    def next_up(self):
        '''
        Increments this half float by the minimum representable value
        '''
        if self.sign == 0:
            self._next()
        else:
            self._prev()

        self._check()

    def next_down(self):
        '''
        Decrements this half float by the minimum representable value
        '''

        if self.mantisa == 0 and self.exp == 0:
            self.sign = 1
            self.mantisa = 1
        elif self.sign == 0:
            self._prev()
        else:
            self._next()

        self._check()

    def encode(self):
        '''
        Creates a bytes with the binary encoding of this half float value
        '''

        by = (self.sign << 15) | (self.exp << 10) | self.mantisa

        assert 0 <= by <= 0xffff

        byte0 = by >> 8
        byte1 = self.mantisa & 0xff

        return [byte0, byte1]

    def get_value(self):
        '''
        Returns the size in bytes of this type
        '''
        if self.mantisa == 0 and self.exp == 0:
            return 0.

        m = self.mantisa
        e = self.exp - 24
        if self.exp != 0:  # normal
            m += 1024
            e -= 1

        if self.sign == 1:
            m *= -1

        return math.ldexp(m, e)


def half_float_value(value):
    '''
    Converts value to a half float and back to float
    Will round its precision to half float, and will raise if overflow
    '''
    hf = create_half_float(value)
    return hf.get_value()


def half_float_next_up(value):
    '''
    Converts value to a half float and increments minimally
    Will round its precision to half float, and will raise if overflow
    '''
    hf = create_half_float(value)
    hf.next_up()
    return hf.get_value()


def half_float_next_down(value):
    '''
    Converts value to a half float and decrements minimally
    Will round its precision to half float, and will raise if overflow
    '''
    hf = create_half_float(value)
    hf.next_down()
    return hf.get_value()


def create_half_float(value):
    '''
    Half float encoder implementation
    '''
    assert isinstance(value, float)
    assert not math.isnan(value)
    assert not math.isinf(value)

    m, e = math.frexp(value)
    if m == 0 and e == 0:
        return _HalfFloatBits(0, 0, 0)

    signbit = 1 if m < 0. else 0

    if e < -24 or e > 16:
        raise HalfFloatOverflowError()
    elif e >= -24 and e <= -14:  # subnormal
        m2 = math.ldexp(m, e + 24)
        m3 = math.fabs(m2)
        m4 = round(m3)
        m5 = math.trunc(m4)

        return _HalfFloatBits(signbit, 0, m5)

    else:  # normal

        m2 = math.ldexp(m, 11)
        m3 = math.fabs(m2)
        m4 = round(m3)
        m5 = math.trunc(m4)
        m6 = m5 - 1024

        return _HalfFloatBits(signbit, e + 14, m6)


class _EncodingImpl(object):

    '''
    Helper class to hold encodings extra data
    '''

    def __init__(self, name, code):
        '''
        Constructor
        '''
        self.name = name
        self.code = code

    def __repr__(self):
        '''
        String representation
        '''
        return self.name


class _EncodingInt(_EncodingImpl):

    '''
    Helper class to hold encodings extra data
    '''

    def __init__(self, name, code):
        '''
        Constructor
        '''
        super(_EncodingInt, self).__init__(name, code)

    def get_min_max(self, max_bytes):
        '''
        Returns [min, max] pair
        '''
        # pylint: disable=no-self-use

        type_min = -2 ** (max_bytes * 8 - 1)
        type_max = 2 ** (max_bytes * 8 - 1) - 1

        return (type_min, type_max)


class _EncodingUInt(_EncodingImpl):

    '''
    Helper class represent unsigned encodings
    '''

    def __init__(self, name, code):
        '''
        Constructor
        '''
        super(_EncodingUInt, self).__init__(name, code)

    def get_min_max(self, max_bytes):
        '''
        Returns [min, max] pair
        '''
        # pylint: disable=no-self-use

        type_max = 2 ** (max_bytes * 8) - 1

        return (0, type_max)


class Encoding(object):

    '''
    Enum like, for FIELD-SEQUENCE
    '''
    END_OF_SEQUENCE = _EncodingImpl('<eos>', 0)
    SIGNED_INT = _EncodingInt('INT', 1)
    UNSIGNED_INT = _EncodingUInt('UINT', 2)


def field_sequence_to_str(field_sequence):
    '''
    makes text representation of a FIELD-SEQUENCE
    '''
    result = []
    for current in field_sequence:
        result.append(current.encoding.name)

    return ','.join(result)
