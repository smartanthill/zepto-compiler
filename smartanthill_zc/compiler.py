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
from ECMAScript.ECMAScriptLexer import ECMAScriptLexer
from ECMAScript.ECMAScriptParser import ECMAScriptParser
from ECMAScript.ECMAScriptVisitor import ECMAScriptVisitor


def parse_js_string(data):

    #    input = FileStream(argv[1])
    istream = antlr4.InputStream.InputStream(data)
    lexer = ECMAScriptLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
    tree = parser.program()

    return tree


class ToStringVisitor(ECMAScriptVisitor):

    def visitChildren(self, node):

        n = node.getChildCount()
        childs = []
        for i in range(n):
            c = node.getChild(i)
            childResult = c.accept(self)
            if childResult:
                childs.append(childResult)

        result = ''
#        if not node.transparent:
        result += type(node).__name__
        if childs:
            result += '(%s)' % ','.join(childs)

        return result if result else None


def tree_to_str(tree):
    visitor = ToStringVisitor()
    result = visitor.visit(tree)
    return result

# Test class


class TouchVisitor(ECMAScriptVisitor):

    def visitProgram(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#program. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitSourceElements(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#sourceElements. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitSourceElement(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#sourceElement. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitStatement(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#statement. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitReturnStatement(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#returnStatement. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitExpressionSequence(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#expressionSequence. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitAdditiveExpression(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#AdditiveExpression. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitMultiplicativeExpression(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#MultiplicativeExpression. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitLiteralExpression(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#LiteralExpression. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitLiteral(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#literal. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitNumericLiteral(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#numericLiteral. """

        ctx.touched = True
        return self.visitChildren(ctx)

    def visitEos(self, ctx):
        """ Visit a parse tree produced by ECMAScriptParser#eos. """

        ctx.touched = True
        return self.visitChildren(ctx)


def touch_tree(tree):

    visitor = TouchVisitor()
    visitor.visit(tree)


class NotTouchedError(Exception):

    def __init__(self, node):
        self.node = node


class CheckTouchedVisitor(ECMAScriptVisitor):

    def visitChildren(self, node):
        try:
            if not node.touched:
                raise NotTouchedError(node)
        except AttributeError:
                raise NotTouchedError(node)

        return super(CheckTouchedVisitor, self).visitChildren(node)


def check_touched_tree(tree):

    visitor = CheckTouchedVisitor()
    visitor.visit(tree)


def compile_js_string(data):

    tree = parse_js_string(data)
    touch_tree(tree)
    check_touched_tree(tree)

    return tree
