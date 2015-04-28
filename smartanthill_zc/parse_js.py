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
from smartanthill_zc.ECMAScript import ECMAScriptVisitor
from smartanthill_zc.ECMAScript.ECMAScriptLexer import ECMAScriptLexer
from smartanthill_zc.ECMAScript.ECMAScriptParser import ECMAScriptParser
from smartanthill_zc.node import StatementListStmtNode, \
    RootNode, McuSleepStmtNode, VariableDeclarationStmtNode, NopStmtNode, \
    IfElseStmtNode, ErrorStmtNode, SimpleForStmtNode, ReturnStmtNode, \
    BodyPartCallExprNode, FunctionCallExprNode, VariableExprNode, \
    NumberLiteralExprNode, ArgumentListNode, OperatorExprNode, \
    MemberAccessExprNode, AssignmentExprNode, ExpressionStmtNode, \
    BooleanLiteralExprNode, make_statement_list, ProgramNode
from smartanthill_zc.antlr_helper import _ProxyAntlrErrorListener,\
    check_reserved_name


def parse_js_string(compiler, data):
    '''
    Parse unicode string containing java script code
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
    prog = visitor.visit(js_tree)

    root = compiler.init_node(RootNode(), compiler.BUILTIN)

    root.set_program(prog)
    compiler.check_stage('js_syntax')

    return root


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

    def visitChildren(self, node):
        '''
        Overrides antlr4.ParseTreeVisitor method
        Changes default action, from walking down the tree to
        fail with assert, this will expose any parsed node that does not have
        a valid interpretation rule here
        '''
        self._compiler.report_error(node, "Internal Error!")
        self._compiler.report_error(node, "Unmatched parser token")
        assert False

    def init_operator(self, node, node_ctx, op_ctx, expr_list_ctx):
        '''
        Initializes a very generic operator expression.
        Operands go into an argument list exactly the same as methods,
        this should make easier argument match algorithms
        '''

        node = self._compiler.init_node(node, node_ctx)

        assert isinstance(op_ctx, antlr4.TerminalNode)
        if op_ctx.getSymbol().type in [
                ECMAScriptParser.Not,
                ECMAScriptParser.Multiply,
                ECMAScriptParser.Divide,
                ECMAScriptParser.Modulus,
                ECMAScriptParser.Plus,
                ECMAScriptParser.Minus,
                ECMAScriptParser.LessThan,
                ECMAScriptParser.MoreThan,
                ECMAScriptParser.LessThanEquals,
                ECMAScriptParser.GreaterThanEquals,
                ECMAScriptParser.Equals,
                ECMAScriptParser.NotEquals,
                ECMAScriptParser.And,
                ECMAScriptParser.Or]:
            node.tk_operator = op_ctx
        else:
            node.tk_operator = op_ctx  # set it anyway, but report error
            self._compiler.report_error(
                node_ctx, "Operator '%s' not supported", op_ctx.getText())

        arg_list = self._compiler.init_node(ArgumentListNode(), node_ctx)

        for e in expr_list_ctx:
            expr = self.visit(e)
            arg_list.add_argument(expr)

        node.set_argument_list(arg_list)

        return node

    # Visit a parse tree produced by ECMAScriptParser#program.
    def visitProgram(self, ctx):
        prog = self._compiler.init_node(ProgramNode(), ctx)
        stmt_list = self._compiler.init_node(StatementListStmtNode(), ctx)

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
        stmt = self._compiler.init_node(McuSleepStmtNode(), ctx)

        args = self.visit(ctx.arguments())
        stmt.set_argument_list(args)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#block.
    def visitBlock(self, ctx):
        stmt_list = self._compiler.init_node(StatementListStmtNode(), ctx)

        st_list = ctx.statementList()
        if st_list:
            sts = st_list.statement()
            for current in sts:
                stmt = self.visit(current)
                stmt_list.add_statement(stmt)

        return stmt_list

    # Visit a parse tree produced by ECMAScriptParser#variableStatement.
    def visitVariableStatement(self, ctx):
        stmt = self._compiler.init_node(VariableDeclarationStmtNode(), ctx)

        var_list = ctx.variableDeclarationList().variableDeclaration()

        assert len(var_list) >= 1

        if len(var_list) > 1:
            self._compiler.report_error(ctx, "Multiple varible declarations in"
                                        " a single statement not supported")

        stmt.tk_name = check_reserved_name(self._compiler,
                                           var_list[0].Identifier())

        ini = var_list[0].initialiser()
        if ini:
            expr = self.visit(ini.singleExpression())
            stmt.set_initializer(expr)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx):
        stmt = self._compiler.init_node(NopStmtNode(), ctx)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx):
        stmt = self._compiler.init_node(ExpressionStmtNode(), ctx)

        expr = self.visit(ctx.expressionSequence())
        stmt.set_expression(expr)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#ifStatement.
    def visitIfStatement(self, ctx):
        stmt = self._compiler.init_node(IfElseStmtNode(), ctx)

        expr = self.visit(ctx.expressionSequence())
        stmt.set_expression(expr)

        body = ctx.statement()

        if len(body) == 1:
            body_if = make_statement_list(self._compiler, self.visit(body[0]))
            stmt.set_if_branch(body_if)
        elif len(body) == 2:
            body_if = make_statement_list(self._compiler, self.visit(body[0]))
            stmt.set_if_branch(body_if)
            body_el = make_statement_list(self._compiler, self.visit(body[1]))
            stmt.set_else_branch(body_el)
        else:
            assert False

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#DoStatement.
    def visitDoStatement(self, ctx):
        self._compiler.report_error(ctx, "Loop 'do' not supported")

        return self._compiler.init_node(ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx):
        self._compiler.report_error(ctx, "Loop 'while' not supported")

        return self._compiler.init_node(ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForStatement.
    def visitForStatement(self, ctx):
        self._compiler.report_error(
            ctx, "Loop 'for' only supported in the trivial form "
            "'for(var i = ..; i < ..; i++) {..}'")

        return self._compiler.init_node(ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForVarTrivialStatement.
    def visitSimpleForStatement(self, ctx):
        stmt = self._compiler.init_node(SimpleForStmtNode(), ctx)

        id_list = ctx.Identifier()
        assert len(id_list) == 3

        if(id_list[0].getText() == id_list[1].getText() and
           id_list[0].getText() == id_list[2].getText()):

            stmt.tk_name = check_reserved_name(self._compiler, id_list[0])
        else:
            self._compiler.report_error(
                ctx, "Loop 'for' only supported in the trivial form "
                "'for(var i = ..; i < ..; i++) {..}'")

        expr_list = ctx.expressionSequence()
        assert len(expr_list) == 2

        begin = self.visit(expr_list[0])
        stmt.set_begin_expression(begin)

        end = self.visit(expr_list[1])
        stmt.set_end_expression(end)

        sl = make_statement_list(self._compiler, self.visit(ctx.statement()))
        stmt.set_statement_list(sl)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#ForVarStatement.
    def visitForVarStatement(self, ctx):
        self._compiler.report_error(
            ctx, "Loop 'for' only supported in the trivial form "
            "'for(var i = ..; i < ..; i++) {..}'")

        return self._compiler.init_node(ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
    def visitForInStatement(self, ctx):
        self._compiler.report_error(
            ctx, "Loop 'for' only supported in the trivial form "
            "'for(var i = ..; i < ..; i++) {..}'")

        return self._compiler.init_node(ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#ForVarInStatement.
    def visitForVarInStatement(self, ctx):
        self._compiler.report_error(
            ctx, "Loop 'for' only supported in the trivial form "
            "'for(var i = ..; i < ..; i++) {..}'")

        return self._compiler.init_node(ErrorStmtNode(), ctx)

    # Visit a parse tree produced by ECMAScriptParser#returnStatement.
    def visitReturnStatement(self, ctx):
        stmt = self._compiler.init_node(ReturnStmtNode(), ctx)

        exprCtx = ctx.expressionSequence()
        if exprCtx:
            expr = self.visit(exprCtx)
            assert expr
            stmt.set_expression(expr)

        return stmt

    # Visit a parse tree produced by ECMAScriptParser#arguments.
    def visitArguments(self, ctx):
        node = self._compiler.init_node(ArgumentListNode(), ctx)

        al = ctx.argumentList()
        if al:
            exprs = al.singleExpression()
            for e in exprs:
                expr = self.visit(e)
                node.add_argument(expr)

        return node

    # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx):
        expr_list = ctx.singleExpression()

        assert len(expr_list) >= 1

        if len(expr_list) > 1:
            self._compiler.report_error(
                ctx,
                "Expression sequence not supported")

        return self.visit(expr_list[0])

    # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx):
        expr = self._compiler.init_node(FunctionCallExprNode(), ctx)

        expr.tk_name = check_reserved_name(self._compiler, ctx.Identifier())
        args = self.visit(ctx.arguments())
        expr.set_argument_list(args)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx):
        expr = self._compiler.init_node(AssignmentExprNode(), ctx)

        expr.tk_name = check_reserved_name(self._compiler, ctx.Identifier())
        rhs = self.visit(ctx.expressionSequence())
        expr.set_rhs(rhs)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx):
        return self.init_operator(OperatorExprNode(), ctx, ctx.getChild(1),
                                  ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx):
        return self.init_operator(OperatorExprNode(), ctx, ctx.getChild(1),
                                  ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx):
        expr = self._compiler.init_node(VariableExprNode(), ctx)
        expr.tk_name = check_reserved_name(self._compiler, ctx.Identifier())

        return expr

    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx):

        return self.visit(ctx.literal())

    # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx):

        expr = self._compiler.init_node(MemberAccessExprNode(), ctx)
        expr.tk_member_name = check_reserved_name(self._compiler,
                                                  ctx.identifierName())

        e = self.visit(ctx.singleExpression())
        expr.set_expression(e)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#NotExpression.
    def visitNotExpression(self, ctx):
        return self.init_operator(OperatorExprNode(), ctx, ctx.getChild(0),
                                  [ctx.singleExpression()])

    # Visit a parse tree produced by ECMAScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx):
        return self.init_operator(OperatorExprNode(), ctx, ctx.getChild(1),
                                  ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx):
        return self.visit(ctx.expressionSequence())

    # Visit a parse tree produced by ECMAScriptParser#MethodExpression.
    def visitMethodExpression(self, ctx):
        expr = self._compiler.init_node(BodyPartCallExprNode(), ctx)

        expr.tk_base_name = check_reserved_name(self._compiler,
                                                ctx.Identifier())
        expr.tk_name = check_reserved_name(
            self._compiler, ctx.identifierName())
        args = self.visit(ctx.arguments())
        expr.set_argument_list(args)

        return expr

    # Visit a parse tree produced by ECMAScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx):
        return self.init_operator(OperatorExprNode(), ctx, ctx.getChild(1),
                                  ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx):
        return self.init_operator(OperatorExprNode(), ctx, ctx.getChild(1),
                                  ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx):
        return self.init_operator(OperatorExprNode(), ctx, ctx.getChild(1),
                                  ctx.singleExpression())

    # Visit a parse tree produced by ECMAScriptParser#literal.
    def visitLiteral(self, ctx):

        if ctx.numericLiteral():
            expr = self._compiler.init_node(NumberLiteralExprNode(), ctx)
            lit = ctx.numericLiteral().DecimalLiteral()
            expr.tk_literal = lit

            return expr

        elif ctx.BooleanLiteral():

            value = None
            if ctx.BooleanLiteral().getText() == u'true':
                value = True
            elif ctx.BooleanLiteral().getText() == u'false':
                value = False
            else:
                assert False

            expr = self._compiler.init_node(BooleanLiteralExprNode(value), ctx)

            return expr

        else:
            assert False
