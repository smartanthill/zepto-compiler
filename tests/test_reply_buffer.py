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

from smartanthill_zc.vm import reply_buffer_sort_helper


def test_reply_buffer_1():

    target = ['a', 'b', 'c', 'd']
    current = ['a', 'b', 'c', 'd']

    assert reply_buffer_sort_helper(target, current) == 0


def test_reply_buffer_2():

    target = ['a', 'b', 'c', 'd']
    current = ['a', 'b', 'c', 'd', 'e', 'f']

    assert reply_buffer_sort_helper(target, current) == 0


def test_reply_buffer_3():

    target = ['a', 'b', 'c', 'd']
    current = ['b', 'c', 'd', 'e', 'f', 'a']

    assert reply_buffer_sort_helper(target, current) == 1


def test_reply_buffer_4():

    target = ['a', 'b', 'c', 'd']
    current = ['c', 'd', 'e', 'b', 'f', 'a']

    assert reply_buffer_sort_helper(target, current) == 2


def test_reply_buffer_5():

    target = ['a', 'b', 'c', 'd']
    current = ['d', 'e', 'b', 'f', 'a', 'c']

    assert reply_buffer_sort_helper(target, current) == 3


def test_reply_buffer_6():

    target = ['a', 'b', 'c', 'd']
    current = ['e', 'a', 'b', 'c', 'd', 'f']

    assert reply_buffer_sort_helper(target, current) == len(target)


def test_reply_buffer_7():

    target = ['a', 'b', 'c', 'd']
    current = ['a', 'b', 'e', 'c', 'd', 'f']

    assert reply_buffer_sort_helper(target, current) == len(target)


def test_reply_buffer_8():

    target = []
    current = ['a', 'b', 'e', 'c', 'd', 'f']

    assert reply_buffer_sort_helper(target, current) == len(target)


def test_reply_buffer_9():

    target = ['a', 'b', 'c', 'd']
    current = ['c', 'a', 'b', 'd']

    assert reply_buffer_sort_helper(target, current) == 2
