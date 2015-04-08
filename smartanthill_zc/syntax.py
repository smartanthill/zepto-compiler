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

from smartanthill_zc.ECMAScript import ECMAScriptVisitor
from smartanthill_zc.node import *


def make_statement_list(compiler, node):
    assert isinstance(node, StatementNode)

    if isinstance(node, StatementListStmtNode):
        return node

    stmt_list = compiler.init_node(StatementListStmtNode(), node.ctx)
    stmt_list.add_statement(node)

    return stmt_list


def js_tree_to_syntax_tree(compiler, js_tree):
    '''
    Translates an ECMAScript (js) parse tree as returned by antlr4 into a
    syntax tree as used by the zepto compiler, this tree transformation
    replaces syntax directed translation written directly into the grammar
    as used by yacc-lex.
    The antlr parser creates a parse tree from the grammar without actions,
    and at this point the parse tree is transformed into the syntax tree
    needed by the application.
    While this may seem more complex, it is actually almost the same,
    only changing where and when, things take place
    '''

    visitor = _JsSyntaxVisitor(compiler)
    root = visitor.visit(js_tree)

    compiler.checkStage('js_syntax')

    return root


class _JsSyntaxVisitor(ECMAScriptVisitor.ECMAScriptVisitor):

    '''
    Visitor class that implements js_tree_to_syntax_tree function

    The template for the visitor is copy&paste from super class interface
    ECMAScriptVisitor.ECMAScriptVisitor
    '''

    def __init__(self, compiler):
        self.compiler = compiler

    # Visit a parse tree produced by ECMAScriptParser#program.
    def visitProgram(self, ctx):
        root = self.compiler.init_node(RootNode(), ctx)
        stmt_list = self.compiler.init_node(StatementListStmtNode(), ctx)

        elems = ctx.sourceElements()
        if elems:
            elem = elems.sourceElement()
            for current in elem:
                st = current.statement()
                assert st
                stmt = self.visit(st)
                stmt_list.add_statement(stmt)

        root.set_statement_list(stmt_list)
        return root

    # Visit a parse tree produced by ECMAScriptParser#sourceElements.
    def visitSourceElements(self, ctx):
        assert False

    # Visit a parse tree produced by ECMAScriptParser#sourceElement.
    def visitSourceElement(self, ctx):
        assert False

    # Visit a parse tree produced by ECMAScriptParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#mcuSleepStatement.
    def visitMcuSleepStatement(self, ctx):
        stmt = self.compiler.init_node(McuSleepStmtNode(), ctx)

        args = self.visit(ctx.arguments())
        stmt.set_argument_list(args)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#block.
    def visitBlock(self, ctx):
        stmt_list = self.compiler.init_node(StatementListStmtNode(), ctx)

        st_list = ctx.statementList()
        if st_list:
            sts = st_list.statement()
            for current in sts:
                stmt = self.visit(current)
                stmt_list.add_statement(stmt)

        return stmt_list

    # Visit a parse tree produced by ECMAScriptParser#statementList.
    def visitStatementList(self, ctx):
        assert False

    # Visit a parse tree produced by ECMAScriptParser#variableStatement.
    def visitVariableStatement(self, ctx):
        stmt = self.compiler.init_node(VariableDeclarationStmtNode(), ctx)

        var_list = ctx.variableDeclarationList().variableDeclaration()

        assert len(var_list) >= 1

        if len(var_list) > 1:
            self.compiler.reportError(
                ctx,
                "Multiple varible declarations in a single statement not supported")

        stmt.ctx_name = var_list[0].Identifier()
        assert stmt.ctx_name

        ini = var_list[0].initialiser()
        if ini:
            expr = self.visit(ini)
            stmt.set_expression(expr)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx):
        assert False

    # Visit a parse tree produced by ECMAScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx):
        assert False

    # Visit a parse tree produced by ECMAScriptParser#initialiser.
    def visitInitialiser(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx):
        stmt = self.compiler.init_node(NopStmtNode(), ctx)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ifStatement.
    def visitIfStatement(self, ctx):
        stmt = self.compiler.init_node(IfElseStmtNode(), ctx)

        exprCtx = ctx.expressionSequence()
        expr = self.visit(exprCtx)
        assert expr
        stmt.set_expression(expr)

        body = ctx.statement()

        if len(body) == 1:
            body_if = make_statement_list(self.compiler, self.visit(body[0]))
            stmt.set_if_branch(body_if)
        elif len(body) == 2:
            body_if = make_statement_list(self.compiler, self.visit(body[0]))
            stmt.set_if_branch(body_if)
            body_el = make_statement_list(self.compiler, self.visit(body[1]))
            stmt.set_else_branch(body_el)
        else:
            assert False

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#DoStatement.
    def visitDoStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForStatement.
    def visitForStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForVarStatement.
    def visitForVarStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
    def visitForInStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForVarInStatement.
    def visitForVarInStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#continueStatement.
    def visitContinueStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#breakStatement.
    def visitBreakStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#returnStatement.
    def visitReturnStatement(self, ctx):
        stmt = self.compiler.init_node(ReturnStmtNode(), ctx)

        exprCtx = ctx.expressionSequence()
        if exprCtx:
            expr = self.visit(exprCtx)
            assert expr
            stmt.set_expression(expr)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#withStatement.
    def visitWithStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#caseBlock.
    def visitCaseBlock(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#caseClauses.
    def visitCaseClauses(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#caseClause.
    def visitCaseClause(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#defaultClause.
    def visitDefaultClause(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#labelledStatement.
    def visitLabelledStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#throwStatement.
    def visitThrowStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#tryStatement.
    def visitTryStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#catchProduction.
    def visitCatchProduction(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#functionBody.
    def visitFunctionBody(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#elementList.
    def visitElementList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#elision.
    def visitElision(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#propertyNameAndValueList.
    def visitPropertyNameAndValueList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by
    # ECMAScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#propertyName.
    def visitPropertyName(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#propertySetParameterList.
    def visitPropertySetParameterList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#arguments.
    def visitArguments(self, ctx):
        node = self.compiler.init_node(ArgumentListNode(), ctx)

        al = ctx.argumentList()
        if al:
            exprs = al.singleExpression()
            for e in exprs:
                expr = self.visit(e)
                node.add_argument(expr)

        return node

    # Visit a parse tree produced by ECMAScriptParser#argumentList.
    def visitArgumentList(self, ctx):
        assert False

    # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx):
        expr_list = ctx.singleExpression()

        assert len(expr_list) >= 1

        if len(expr_list) > 1:
            self.compiler.reportError(
                ctx,
                "Expression sequence not supported")

        return self.visit(expr_list[0])

    # Visit a parse tree produced by ECMAScriptParser#MethodExpression.
    def visitMethodExpression(self, ctx):
        expr = self.compiler.init_node(MethodCallExprNode(), ctx)

        expr.ctx_base_name = ctx.Identifier()
        expr.ctx_name = ctx.identifierName()
        args = self.visit(ctx.arguments())
        expr.set_argument_list(args)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx):
        expr = self.compiler.init_node(FunctionCallExprNode(), ctx)

        expr.ctx_name = ctx.Identifier()
        args = self.visit(ctx.arguments())
        expr.set_argument_list(args)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx):
        expr = self.compiler.init_node(VariableExprNode(), ctx)
        expr.ctx_name = ctx

        return expr

    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx):
        expr = self.compiler.init_node(NumberLiteralExprNode(), ctx)
        lit = ctx.literal().numericLiteral().DecimalLiteral()
        assert lit
        expr.ctx_literal = lit

        return expr

    # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx):
        return self.visit(ctx.expressionSequence())

    # Visit a parse tree produced by ECMAScriptParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#identifierName.
    def visitIdentifierName(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#reservedWord.
    def visitReservedWord(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#keyword.
    def visitKeyword(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#futureReservedWord.
    def visitFutureReservedWord(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#getter.
    def visitGetter(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#setter.
    def visitSetter(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#eos.
    def visitEos(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#eof.
    def visitEof(self, ctx):
        return self.visitChildren(ctx)
