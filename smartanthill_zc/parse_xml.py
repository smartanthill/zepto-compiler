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


import antlr4

from smartanthill_zc.parse_js import _ProxyAntlrErrorListener
from smartanthill_zc.Xml.XmlLexer import XmlLexer
from smartanthill_zc.Xml.XmlParser import XmlParser


def parse_xml_string(compiler, data):
    '''
    Parse unicode string containing xml plug-in manifest
    Returns an antlr parse tree
    '''
    #    input = FileStream(argv[1])
    istream = antlr4.InputStream.InputStream(data)
    lexer = XmlLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = XmlParser(stream)
#    parser.removeErrorListener()
    parser.addErrorListener(_ProxyAntlrErrorListener(compiler))
    tree = parser.document()

    compiler.check_stage('parse_xml')

    return tree

