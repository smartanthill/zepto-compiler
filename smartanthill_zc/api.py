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

from smartanthill_zc.compiler import Compiler
from smartanthill_zc.op_node import ExecOpNode
from smartanthill_zc.writer import write_binary


def zepto_exec_cmd(bodypart_id, data):
    '''
    Public api function that creates a binary code for a ZEPTOVM_OP_EXEC
    '''

    compiler = Compiler()
    op = compiler.init_node(ExecOpNode(), Compiler.NONE)
    op.bodypart_id = bodypart_id
    op.data = data

    code = write_binary(compiler, op)

    return code
