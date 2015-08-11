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
from smartanthill_zc import array
from smartanthill_zc import expression, statement, node
from smartanthill_zc.ECMAScript import ECMAScriptVisitor
from smartanthill_zc.ECMAScript.ECMAScriptLexer import ECMAScriptLexer
from smartanthill_zc.ECMAScript.ECMAScriptParser import ECMAScriptParser
from smartanthill_zc.antlr_helper import (_ProxyAntlrErrorListener,
                                          get_token_text)
from smartanthill_zc.node import StmtListNode
from smartanthill_zc.root import SourceProgramNode


def parse_js_string(compiler, data):
    '''
    Parse string containing java script code
    Returns an antlr parse tree
    '''

    #    input = FileStream(argv[1])
    istream = antlr4.InputStream.InputStream(data)
    lexer = ECMAScriptLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
#    parser.removeErrorListener()
    parser.addErrorListener(_ProxyAntlrErrorListener(compiler))
    tree = parser.program()

    compiler.check_stage('parse_js')

    return tree


def _parse_js_expression(compiler, data, ctx):
    '''
    Parse string containing constant expression
    Returns a node tree with expression node
    '''

    #    input = FileStream(argv[1])
    istream = antlr4.InputStream.InputStream(data)
    lexer = ECMAScriptLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
#    parser.removeErrorListener()
    parser.addErrorListener(_ProxyAntlrErrorListener(compiler))
    tree = parser.singleExpression()

    check = _FilterParameterExpressionVisitor(ctx, compiler)
    check.visit(tree)

    visitor = _JsSyntaxVisitor(compiler)
    expr = visitor.visit(tree)

    return expr


class _FilterParameterExpressionVisitor(ECMAScriptVisitor.ECMAScriptVisitor):

    '''
    Visitor class that implements js_tree_to_syntax_tree function

    The template for the visitor is copy&paste from super class interface
    ECMAScriptVisitor.ECMAScriptVisitor
    '''

    def __init__(self, ctx, compiler):
        '''
        Constructor
        '''
        self.ctx = ctx
        self._compiler = compiler

    def visitChildren(self, current):
        '''
        Overrides antlr4.ParseTreeVisitor method
        Changes default action, from walking down the tree to
        fail with assert, this will expose any parsed node that does not have
        a valid interpretation rule here
        '''
        self._compiler.report_error(
            self.ctx,
            "Unsupported parameter value '%s'" % str(current.getText()))

    # Visit a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx):
        self.visit(ctx.singleExpression(0))
        self.visit(ctx.singleExpression(1))

    # Visit a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx):
        self.visit(ctx.singleExpression(0))
        self.visit(ctx.singleExpression(1))

    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx):
        pass

    # Visit a parse tree produced by ECMAScriptParser#NotExpression.
    def visitNotExpression(self, ctx):
        self.visit(ctx.singleExpression(0))

    # Visit a parse tree produced by ECMAScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx):
        self.visit(ctx.singleExpression(0))
        self.visit(ctx.singleExpression(1))

    # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx):
        self.visit(ctx.singleExpression(0))

    # Visit a parse tree produced by ECMAScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx):
        self.visit(ctx.singleExpression(0))
        self.visit(ctx.singleExpression(1))

    # Visit a parse tree produced by ECMAScriptParser#UnaryExpression.
    def visitUnaryExpression(self, ctx):
        self.visit(ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx):
        self.visit(ctx.singleExpression(0))
        self.visit(ctx.singleExpression(1))

    # Visit a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx):
        self.visit(ctx.singleExpression(0))
        self.visit(ctx.singleExpression(1))


def create_parameters(compiler, data, ctx):
    '''
    Creates an StmtListNode and populates it with
    VariableDeclarationStmtNode with data from dictionary.
    Used for parameters
    '''

    decls = compiler.init_node(node.DeclarationListNode(), ctx)

    for key in data.keys():

        assert isinstance(key, str)
        var = compiler.init_node(
            statement.ParameterDeclarationStmtNode(), ctx)
        var.txt_name = key

        decls.add_declaration(var)

    compiler.check_stage('parameter')

    return decls


def js_parse_tree_to_syntax_tree(compiler, js_tree):
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
    source = visitor.visit(js_tree)

    compiler.check_stage('js_syntax')

    return source


class _JsSyntaxVisitor(ECMAScriptVisitor.ECMAScriptVisitor):

    '''
    Visitor class that implements js_tree_to_syntax_tree function

    The template for the visitor is copy&paste from super class interface
    ECMAScriptVisitor.ECMAScriptVisitor
    '''

    def __init__(self, compiler):
        '''
        Constructor
        '''
        self._compiler = compiler

    def visitChildren(self, current):
        '''
        Overrides antlr4.ParseTreeVisitor method
        Changes default action, from walking down the tree to
        fail with assert, this will expose any parsed node that does not have
        a valid interpretation rule here
        '''
        self._compiler.report_error(current, "Internal Error!")
        self._compiler.report_error(current, "Unmatched parser token")
        assert False

    def init_operator(self, op, node_ctx, op_ctx, expr_list_ctx):
        '''
        Initializes a very generic operator expression.
        Operands go into an argument list exactly the same as methods,
        this should make easier argument match algorithms
        '''

        op = self._compiler.init_node(op, node_ctx)
        text = get_token_text(self._compiler, op_ctx)
        op.txt_operator = text

        if text not in ['!', '&&', '||',
                        '*', '/', '%', '+', '-',
                        '<', '>', '<=', '>=', '==', '!=']:
            self._compiler.report_error(
                node_ctx, "Operator '%s' not supported" % text)

        arg_list = self._compiler.init_node(node.ArgumentListNode(), node_ctx)

        for e in expr_list_ctx:
            expr = self.visit(e)
            arg_list.add_argument(expr)

        op.set_argument_list(arg_list)

        return op

    # Visit a parse tree produced by ECMAScriptParser#program.
    def visitProgram(self, ctx):
        prog = self._compiler.init_node(SourceProgramNode(), ctx)
        stmt_list = self._compiler.init_node(
            StmtListNode(), ctx)

        elems = ctx.sourceElements()
        if elems:
            elem = elems.sourceElement()
            for current in elem:
                st = current.statement()
                assert st
                stmt = self.visit(st)
                stmt_list.add_statement(stmt)

        prog.set_statement_list(stmt_list)
        return prog

    # Visit a parse tree produced by ECMAScriptParser#statement.
    def visitStatement(self, ctx):
        return ctx.getChild(0).accept(self)

    # Visit a parse tree produced by ECMAScriptParser#mcuSleepStatement.
    def visitMcuSleepStatement(self, ctx):
        stmt = self._compiler.init_node(statement.McuSleepStmtNode(), ctx)

        args = self.visit(ctx.arguments())
        stmt.set_argument_list(args)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#block.
    def visitBlock(self, ctx):
        stmt_list = self._compiler.init_node(
            StmtListNode(), ctx)

        st_list = ctx.statementList()
        if st_list:
            sts = st_list.statement()
            for current in sts:
                stmt = self.visit(current)
                stmt_list.add_statement(stmt)

        return stmt_list

    # Visit a parse tree produced by ECMAScriptParser#variableStatement.
    def visitVariableStatement(self, ctx):
        stmt = self._compiler.init_node(
            statement.VariableDeclarationStmtNode(), ctx)

        var_list = ctx.variableDeclarationList().variableDeclaration()

        assert len(var_list) >= 1

        if len(var_list) > 1:
            self._compiler.report_error(ctx, "Multiple varible declarations in"
                                        " a single statement not supported")

        stmt.txt_name = get_token_text(self._compiler,
                                       var_list[0].Identifier())

        ini = var_list[0].initialiser()
        if ini:
            expr = self.visit(ini.singleExpression())
            stmt.set_initializer(expr)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx):
        stmt = self._compiler.init_node(statement.NopStmtNode(), ctx)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx):
        stmt = self._compiler.init_node(statement.ExpressionStmtNode(), ctx)

        expr = self.visit(ctx.singleExpression())
        stmt.set_expression(expr)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#ifStatement.
    def visitIfStatement(self, ctx):
        stmt = self._compiler.init_node(statement.IfElseStmtNode(), ctx)

        expr = self.visit(ctx.singleExpression())
        stmt.set_expression(expr)

        body = ctx.statement()

        if len(body) == 1:
            body_if = statement.make_statement_list(
                self._compiler, self.visit(body[0]))
            stmt.set_if_branch(body_if)
        elif len(body) == 2:
            body_if = statement.make_statement_list(
                self._compiler, self.visit(body[0]))
            stmt.set_if_branch(body_if)
            body_el = statement.make_statement_list(
                self._compiler, self.visit(body[1]))
            stmt.set_else_branch(body_el)
        else:
            assert False

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#DoStatement.
    def visitDoStatement(self, ctx):
        self._compiler.report_error(ctx, "Loop 'do' not supported")

        return self._compiler.init_node(statement.ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx):
        self._compiler.report_error(ctx, "Loop 'while' not supported")

        return self._compiler.init_node(statement.ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForStatement.
    def visitForStatement(self, ctx):
        self._compiler.report_error(
            ctx, "Loop 'for' only supported in the trivial form "
            "'for(var i = ..; i < ..; i++) {..}'")

        return self._compiler.init_node(statement.ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForVarTrivialStatement.
    def visitSimpleForStatement(self, ctx):
        stmt = self._compiler.init_node(statement.SimpleForStmtNode(), ctx)

        id_list = ctx.Identifier()
        assert len(id_list) == 3

        txt0 = get_token_text(self._compiler, id_list[0])
        txt1 = get_token_text(self._compiler, id_list[1])
        txt2 = get_token_text(self._compiler, id_list[2])

        if txt0 == txt1 and txt1 == txt2:

            stmt.txt_name = txt0
        else:
            self._compiler.report_error(
                ctx, "Loop 'for' only supported in the trivial form "
                "'for(var i = ..; i < ..; i++) {..}'")

        expr_list = ctx.singleExpression()
        assert len(expr_list) == 2

        begin = self.visit(expr_list[0])
        stmt.set_begin_expression(begin)

        end = self.visit(expr_list[1])
        stmt.set_end_expression(end)

        sl = statement.make_statement_list(
            self._compiler, self.visit(ctx.statement()))
        stmt.set_statement_list(sl)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#ForVarStatement.
    def visitForVarStatement(self, ctx):
        self._compiler.report_error(
            ctx, "Loop 'for' only supported in the trivial form "
            "'for(var i = ..; i < ..; i++) {..}'")

        return self._compiler.init_node(statement.ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
    def visitForInStatement(self, ctx):
        self._compiler.report_error(
            ctx, "Loop 'for' only supported in the trivial form "
            "'for(var i = ..; i < ..; i++) {..}'")

        return self._compiler.init_node(statement.ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForVarInStatement.
    def visitForVarInStatement(self, ctx):
        self._compiler.report_error(
            ctx, "Loop 'for' only supported in the trivial form "
            "'for(var i = ..; i < ..; i++) {..}'")

        return self._compiler.init_node(statement.ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#returnStatement.
    def visitReturnStatement(self, ctx):
        stmt = self._compiler.init_node(statement.ReturnStmtNode(), ctx)

        exprCtx = ctx.singleExpression()
        if exprCtx:
            expr = self.visit(exprCtx)
            assert expr
            stmt.set_expression(expr)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#arguments.
    def visitArguments(self, ctx):
        args = self._compiler.init_node(node.ArgumentListNode(), ctx)

        al = ctx.argumentList()
        if al:
            exprs = al.singleExpression()
            for e in exprs:
                expr = self.visit(e)
                args.add_argument(expr)

        return args

    # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx):
        expr = self._compiler.init_node(expression.FunctionCallExprNode(), ctx)

        expr.txt_name = get_token_text(self._compiler, ctx.Identifier())
        args = self.visit(ctx.arguments())
        expr.set_argument_list(args)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx):
        expr = self._compiler.init_node(expression.AssignmentExprNode(), ctx)

        expr.txt_name = get_token_text(self._compiler, ctx.Identifier())
        rhs = self.visit(ctx.singleExpression())
        expr.set_rhs(rhs)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx):
        return self.init_operator(expression.LogicOpExprNode(), ctx,
                                  ctx.getChild(1), ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx):
        return self.init_operator(expression.LogicOpExprNode(), ctx,
                                  ctx.getChild(1), ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx):
        expr = self._compiler.init_node(expression.VariableExprNode(), ctx)
        expr.txt_name = get_token_text(self._compiler, ctx.Identifier())

        return expr

    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx):

        return self.visit(ctx.literal())

    # Visit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx):

        expr = self._compiler.init_node(array.ArrayLiteralExprNode(), ctx)

        elems = ctx.arrayLiteral().elementList()

        if not elems:
            self._compiler.report_error(
                ctx,
                "Empty array expression not supported")
        else:
            exprs = elems.singleExpression()
            assert len(exprs) >= 1
            for current in exprs:
                e = self.visit(current)
                expr.add_expression(e)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx):

        expr = self._compiler.init_node(expression.MemberAccessExprNode(), ctx)
        expr.txt_member = get_token_text(self._compiler, ctx.Identifier())

        e = self.visit(ctx.singleExpression())
        expr.set_expression(e)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#NotExpression.
    def visitNotExpression(self, ctx):
        return self.init_operator(expression.LogicOpExprNode(), ctx,
                                  ctx.getChild(0), [ctx.singleExpression()])

    # Visit a parse tree produced by ECMAScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx):
        return self.init_operator(expression.ComparisonOpExprNode(), ctx,
                                  ctx.getChild(1), ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx):
        return self.visit(ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#MethodExpression.
    def visitMethodExpression(self, ctx):
        expr = self._compiler.init_node(expression.BodyPartCallExprNode(), ctx)

        expr.txt_bodypart = get_token_text(self._compiler, ctx.Identifier(0))
        expr.txt_method = get_token_text(self._compiler, ctx.Identifier(1))
        args = self.visit(ctx.arguments())
        expr.set_argument_list(args)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx):
        return self.init_operator(expression.ComparisonOpExprNode(), ctx,
                                  ctx.getChild(1), ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#UnaryExpression.
    def visitUnaryExpression(self, ctx):
        return self.init_operator(expression.UnaryOpExprNode(), ctx,
                                  ctx.getChild(0), [ctx.singleExpression()])

    # Visit a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx):
        return self.init_operator(expression.ArithmeticOpExprNode(), ctx,
                                  ctx.getChild(1), ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx):
        return self.init_operator(expression.ArithmeticOpExprNode(), ctx,
                                  ctx.getChild(1), ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#literal.
    def visitLiteral(self, ctx):

        if ctx.numericLiteral():
            expr = self._compiler.init_node(
                expression.NumberLiteralExprNode(), ctx)
            lit = ctx.numericLiteral().DecimalLiteral()
            expr.txt_literal = get_token_text(self._compiler, lit)

            return expr

        elif ctx.BooleanLiteral():

            text = get_token_text(self._compiler, ctx.BooleanLiteral())

            assert text == 'true' or text == 'false'

            expr = self._compiler.init_node(
                expression.BooleanLiteralExprNode(), ctx)
            expr.boolean_value = True if text == 'true' else False

            return expr

        else:
            assert False
