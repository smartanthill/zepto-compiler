# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by XmlParser.

class XmlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XmlParser#document.
    def visitDocument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XmlParser#prolog.
    def visitProlog(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XmlParser#xmlDecl.
    def visitXmlDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XmlParser#element.
    def visitElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XmlParser#emptyElemTag.
    def visitEmptyElemTag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XmlParser#sTag.
    def visitSTag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XmlParser#attribute.
    def visitAttribute(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XmlParser#eTag.
    def visitETag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XmlParser#content.
    def visitContent(self, ctx):
        return self.visitChildren(ctx)


