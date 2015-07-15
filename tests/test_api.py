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

from smartanthill_zc import compiler, api, parse_xml


def test_xml_api_1():

    comp = compiler.Compiler()
    plugin = api.ZeptoPlugin('tests/test_plugin_1.xml')

    sensor1 = api.ZeptoBodyPart(plugin, 1, 'Sensor1')
    sensor2 = api.ZeptoBodyPart(plugin, 2, 'Sensor2')

    bodyparts = parse_xml.create_bodyparts(comp, [sensor1, sensor2])
