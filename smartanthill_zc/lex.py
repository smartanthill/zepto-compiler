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

import ply.lex as lex


class ZeptoLexer(object):
    # List of token names.   This is always required
    tokens = (
        "NUMBER",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "LPAREN",
        "RPAREN",
    )

    # Regular expression rules for simple tokens
    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"
    t_LPAREN = r"\("
    t_RPAREN = r"\)"

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_NUMBER(self, t):
        r"\d+"
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = " \t"

    @staticmethod
    def t_error(t):
        """ Error handling rule """
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)

    def parse(self, data):
        self.lexer.input(data)
        token = True
        while token:
            token = self.lexer.token()
            if not token:
                break
            yield token
        raise StopIteration()
