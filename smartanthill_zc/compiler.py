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
    istream = antlr4.InputStream.InputStream(data);
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
            if(childResult):
                childs.append(childResult)
        
        result = ''
        if not node.transparent:
            result += type(node).__name__
        if len(childs) != 0:
            result += '('
            for i in range(len(childs)):
                
                if i != 0:
                    result += ','
                
                result += childs[i]
                
            result += ')'
             
        if len(result) != 0:
            return result
        else:
            return None

def tree_to_str(tree):
    visitor = ToStringVisitor()
    result = visitor.visit(tree)
    return result

#Test class 
class TouchVisitor(ECMAScriptVisitor):

    # Visit a parse tree produced by ECMAScriptParser#program.
    def visitProgram(self, ctx):
        ctx.touched = True
        ctx.transparent = False
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#sourceElements.
    def visitSourceElements(self, ctx):
        ctx.touched = True
        ctx.transparent = True
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#sourceElement.
    def visitSourceElement(self, ctx):
        ctx.touched = True
        ctx.transparent = True
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#statement.
    def visitStatement(self, ctx):
        ctx.touched = True
        ctx.transparent = True
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#returnStatement.
    def visitReturnStatement(self, ctx):
        ctx.touched = True;
        ctx.transparent = False
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx):
        ctx.touched = True;
        ctx.transparent = True
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx):
        ctx.touched = True;
        ctx.transparent = False
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx):
        ctx.touched = True;
        ctx.transparent = False
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx):
        ctx.touched = True;
        ctx.transparent = True
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#literal.
    def visitLiteral(self, ctx):
        ctx.touched = True;
        ctx.transparent = True
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx):
        ctx.touched = True;
        ctx.transparent = False
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#eos.
    def visitEos(self, ctx):
        ctx.touched = True;
        ctx.transparent = True
        return self.visitChildren(ctx)


def touch_tree(tree):

    visitor = TouchVisitor()
    visitor.visit(tree)
 

class NotTouchedError(Exception):
    def __init__(self, node):
        self.node = node


class CheckTouchedVisitor(ECMAScriptVisitor):

    def visitChildren(self, node):
        if not node.touched:
            raise NotTouchedError(node)
        
        return super(CheckTouchedVisitor, self).visitChildren(self, node)

def check_touched_tree(tree):

    visitor = TouchVisitor()
    visitor.visit(tree)


def compile_js_string(data):

    tree = parse_js_string(data)
    touch_tree(tree)
    check_touched_tree(tree)

    return tree
