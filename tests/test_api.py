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

from smartanthill_zc import api, errors


def test_api_zepto_exec_cmd():

    code = api.zepto_exec_cmd(0, [1, 2, 3])
    assert code == bytearray([0x02, 0x00, 0x03, 0x01, 0x02, 0x03])


def test_api_1():

    plugin = api.ZeptoPlugin('tests/test_plugin_1.xml')

    sensor2 = api.ZeptoBodyPart(plugin, 1, 'Other')
    sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

    zp = api.ZeptoProgram(
        "return BodyPartName.Execute(PARAM1)", [sensor1, sensor2])
    dynamic_data = {
        "PARAM1": 10
    }

    opcode = zp.compile(dynamic_data)

    # 0x02 opcode for ZEPTOVM_OP_EXEC
    # 0x06 signed encode for bodypart-id '3'
    # 0x01 data length
    # 0x14 signed encode for data value '10'

    assert opcode == bytearray([0x02, 0x06, 0x01, 0x14])


def test_no_param():

    plugin = api.ZeptoPlugin('tests/test_plugin_1.xml')

    sensor2 = api.ZeptoBodyPart(plugin, 1, 'Other')
    sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

    zp = api.ZeptoProgram(
        "return BodyPartName.Execute(10)", [sensor1, sensor2])

    opcode = zp.compile()

    # 0x02 opcode for ZEPTOVM_OP_EXEC
    # 0x06 signed encode for bodypart-id '3'
    # 0x01 data length
    # 0x14 signed encode for data value '10'

    assert opcode == bytearray([0x02, 0x06, 0x01, 0x14])


def test_no_param_error():
    try:
        plugin = api.ZeptoPlugin('tests/test_plugin_1.xml')

        sensor2 = api.ZeptoBodyPart(plugin, 1, 'Other')
        sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

        zp = api.ZeptoProgram(
            "return BodyPartName.Execute(PARAM)", [sensor1, sensor2])

        zp.compile()
        assert False
    except errors.CompilerError as e:
        assert e.value == ["line 1, Unresolved variable 'PARAM'"]


def test_no_arg_error():
    try:
        plugin = api.ZeptoPlugin('tests/test_plugin_1.xml')

        sensor2 = api.ZeptoBodyPart(plugin, 1, 'Other')
        sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

        zp = api.ZeptoProgram(
            "return BodyPartName.Execute()", [sensor1, sensor2])

        zp.compile()
        assert False
    except errors.CompilerError as e:
        assert e.value == [
            "line 1, Wrong number of arguments, need 1 but given 0"]


def test_api_2():

    plugin = api.ZeptoPlugin('tests/test_plugin_2.xml')

    sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

    zp = api.ZeptoProgram(
        "return BodyPartName.Execute()", [sensor1])

    opcode = zp.compile()

    # 0x02 opcode for ZEPTOVM_OP_EXEC
    # 0x06 signed encode for bodypart-id '3'
    # 0x00 data length

    assert opcode == bytearray([0x02, 0x06, 0x00])


def test_api_3():

    plugin = api.ZeptoPlugin('tests/test_plugin_3.xml')

    sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

    zp = api.ZeptoProgram(
        "return BodyPartName.Execute(3, 5)", [sensor1])

    opcode = zp.compile()

    # 0x02 opcode for ZEPTOVM_OP_EXEC
    # 0x06 signed encode for bodypart-id '3'
    # 0x01 data length
    # 0x06 signed encode for data value '3'
    # 0x06 signed encode for data value '5'

    assert opcode == bytearray([0x02, 0x06, 0x02, 0x06, 0x05])


def test_response_1():

    plugin = api.ZeptoPlugin('tests/test_plugin_1.xml')

    sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

    zp = api.ZeptoProgram(
        "return BodyPartName.Execute(2)", [sensor1])

    opcode = zp.compile()

    # 0x02 opcode for ZEPTOVM_OP_EXEC
    # 0x06 signed encode for bodypart-id '3'
    # 0x01 data length
    # 0x04 signed encode for data value '10'
    assert opcode == bytearray([0x02, 0x06, 0x01, 0x04])

    res = zp.process_response(bytearray([0x20, 0x00, 98, 0xcd, 0xcd, 0xcd]))

    assert res == {'xyz': 29.8}


def test_response_2():

    plugin = api.ZeptoPlugin('tests/test_plugin_1.xml')

    sensor2 = api.ZeptoBodyPart(plugin, 1, 'Other')
    sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

    zp = api.ZeptoProgram(
        "return [BodyPartName.Execute(2), Other.Execute(3)]",
        [sensor1, sensor2])

    opcode = zp.compile()

    # 0x02 opcode for ZEPTOVM_OP_EXEC
    # 0x06 signed encode for bodypart-id '3'
    # 0x01 data length
    # 0x04 signed encode for data value '2'
    # 0x02 opcode for ZEPTOVM_OP_EXEC
    # 0x06 signed encode for bodypart-id '1'
    # 0x01 data length
    # 0x06 signed encode for data value '3'

    assert opcode == bytearray(
        [0x02, 0x06, 0x01, 0x04, 0x02, 0x02, 0x01, 0x06])

    res = zp.process_response(bytearray([0x40, 0x00, 98, 0x00, 100]))

    assert res == [{'xyz': 29.8}, {'xyz': 30.0}]


def test_dynamic_data_1():

    plugin = api.ZeptoPlugin('tests/test_plugin_1.xml')

    sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

    zp = api.ZeptoProgram(
        "return BodyPartName.Execute(PARAM1)", [sensor1])

    opcode = zp.compile({"PARAM1": 5})

    assert opcode == zp.compile({"PARAM1": "5"})
    assert opcode == zp.compile({"PARAM1": 5.0})
    assert opcode == zp.compile({"PARAM1": "5.0"})


def test_bad_dynamic_data_error():
    try:
        plugin = api.ZeptoPlugin('tests/test_plugin_3.xml')

        sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

        zp = api.ZeptoProgram(
            "return BodyPartName.Execute(PARAM1, PARAM2)", [sensor1])

        zp.compile({"PARAM1": "x", "PARAM2": []})

        assert False

    except errors.CompilerError as e:
        assert e.value == [
            "parameter PARAM1, Value 'x' is not valid",
            "parameter PARAM2, Value type must be string or number"]


def test_bad_dynamic_data_error_2():
    try:
        plugin = api.ZeptoPlugin('tests/test_plugin_3.xml')

        sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

        zp = api.ZeptoProgram(
            "return BodyPartName.Execute(PARAM1, PARAM2)", [sensor1])

        zp.compile({"PARAM1": "100000", "PARAM2": "-1"})

        assert False

    except errors.CompilerError as e:
        assert '%s' % e == "parameter PARAM1, Value 100000.0 outside valid "\
            "range [-32768, 32767]; "\
            "parameter PARAM2, Value -1.0 outside valid range [0, 255]"


def test_discrete_argument_1():

    plugin = api.ZeptoPlugin('tests/test_plugin_4.xml')

    sensor1 = api.ZeptoBodyPart(plugin, 3, 'BodyPartName')

    zp = api.ZeptoProgram(
        "return BodyPartName.Execute(1)", [sensor1])

    opcode = zp.compile()

    # 0x02 opcode for ZEPTOVM_OP_EXEC
    # 0x06 signed encode for bodypart-id '3'
    # 0x01 data length
    # 0x04 unsigned encode for data value '1'
    # 0x02 opcode for ZEPTOVM_OP_EXEC
    # 0x06 signed encode for bodypart-id '1'
    # 0x01 data length
    # 0x06 signed encode for data value '3'

    assert opcode == bytearray(
        [0x02, 0x06, 0x01, 0x01])


def test_discrete_argument_error_1():

    try:
        plugin = api.ZeptoPlugin('tests/test_plugin_4.xml')

        sensor1 = api.ZeptoBodyPart(plugin, 4, 'BodyPartName')

        zp = api.ZeptoProgram(
            "return BodyPartName.Execute(2)", [sensor1])

        zp.compile()

    except errors.CompilerError as e:
        assert '%s' % e == "line 1, Value 2.0 not allowed"
