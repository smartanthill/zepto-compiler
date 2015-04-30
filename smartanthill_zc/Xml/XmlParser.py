# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function

from io import StringIO

from antlr4 import *

package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .XmlParserListener import XmlParserListener
    from .XmlParserVisitor import XmlParserVisitor
else:
    from XmlParserListener import XmlParserListener
    from XmlParserVisitor import XmlParserVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\16a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\3\2\5\2\26\n\2\3\2\3\2\3\2\3")
        buf.write(u"\3\3\3\3\4\3\4\3\4\7\4 \n\4\f\4\16\4#\13\4\3\4\5\4&\n")
        buf.write(u"\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\6\3\6\3\6\3")
        buf.write(u"\6\7\6\65\n\6\f\6\16\68\13\6\3\6\5\6;\n\6\3\6\3\6\3\7")
        buf.write(u"\3\7\3\7\3\7\7\7C\n\7\f\7\16\7F\13\7\3\7\5\7I\n\7\3\7")
        buf.write(u"\3\7\3\b\3\b\3\b\3\b\3\t\5\tR\n\t\3\t\3\t\3\t\5\tW\n")
        buf.write(u"\t\3\t\3\t\3\n\7\n\\\n\n\f\n\16\n_\13\n\3\n\2\2\13\2")
        buf.write(u"\4\6\b\n\f\16\20\22\2\2b\2\25\3\2\2\2\4\32\3\2\2\2\6")
        buf.write(u"\34\3\2\2\2\b.\3\2\2\2\n\60\3\2\2\2\f>\3\2\2\2\16L\3")
        buf.write(u"\2\2\2\20Q\3\2\2\2\22]\3\2\2\2\24\26\5\4\3\2\25\24\3")
        buf.write(u"\2\2\2\25\26\3\2\2\2\26\27\3\2\2\2\27\30\5\b\5\2\30\31")
        buf.write(u"\7\2\2\3\31\3\3\2\2\2\32\33\5\6\4\2\33\5\3\2\2\2\34!")
        buf.write(u"\7\7\2\2\35\36\7\f\2\2\36 \5\16\b\2\37\35\3\2\2\2 #\3")
        buf.write(u"\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"%\3\2\2\2#!\3\2\2\2$&")
        buf.write(u"\7\f\2\2%$\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\7\n\2\2(\7")
        buf.write(u"\3\2\2\2)/\5\n\6\2*+\5\f\7\2+,\5\22\n\2,-\5\20\t\2-/")
        buf.write(u"\3\2\2\2.)\3\2\2\2.*\3\2\2\2/\t\3\2\2\2\60\61\7\5\2\2")
        buf.write(u"\61\66\7\16\2\2\62\63\7\f\2\2\63\65\5\16\b\2\64\62\3")
        buf.write(u"\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67:\3")
        buf.write(u"\2\2\28\66\3\2\2\29;\7\f\2\2:9\3\2\2\2:;\3\2\2\2;<\3")
        buf.write(u"\2\2\2<=\7\t\2\2=\13\3\2\2\2>?\7\5\2\2?D\7\16\2\2@A\7")
        buf.write(u"\f\2\2AC\5\16\b\2B@\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2")
        buf.write(u"\2\2EH\3\2\2\2FD\3\2\2\2GI\7\f\2\2HG\3\2\2\2HI\3\2\2")
        buf.write(u"\2IJ\3\2\2\2JK\7\b\2\2K\r\3\2\2\2LM\7\16\2\2MN\7\13\2")
        buf.write(u"\2NO\7\r\2\2O\17\3\2\2\2PR\7\f\2\2QP\3\2\2\2QR\3\2\2")
        buf.write(u"\2RS\3\2\2\2ST\7\6\2\2TV\7\16\2\2UW\7\f\2\2VU\3\2\2\2")
        buf.write(u"VW\3\2\2\2WX\3\2\2\2XY\7\b\2\2Y\21\3\2\2\2Z\\\5\b\5\2")
        buf.write(u"[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^\23\3\2\2\2")
        buf.write(u"_]\3\2\2\2\r\25!%.\66:DHQV]")
        return buf.getvalue()


class XmlParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'<'", u"'</'", 
                     u"'<?xml'", u"'>'", u"'/>'", u"'?>'" ]

    symbolicNames = [ u"<INVALID>", u"CharData", u"Comment", u"LT", u"LT_SLASH", 
                      u"XML_DECL", u"GT", u"SLASH_GT", u"QUESTION_GT", u"Eq", 
                      u"S", u"AttValue", u"Name" ]

    RULE_document = 0
    RULE_prolog = 1
    RULE_xmlDecl = 2
    RULE_element = 3
    RULE_emptyElemTag = 4
    RULE_sTag = 5
    RULE_attribute = 6
    RULE_eTag = 7
    RULE_content = 8

    ruleNames =  [ u"document", u"prolog", u"xmlDecl", u"element", u"emptyElemTag", 
                   u"sTag", u"attribute", u"eTag", u"content" ]

    EOF = Token.EOF
    CharData=1
    Comment=2
    LT=3
    LT_SLASH=4
    XML_DECL=5
    GT=6
    SLASH_GT=7
    QUESTION_GT=8
    Eq=9
    S=10
    AttValue=11
    Name=12

    def __init__(self, input):
        super(XmlParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class DocumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(XmlParser.DocumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(XmlParser.ElementContext,0)


        def EOF(self):
            return self.getToken(XmlParser.EOF, 0)

        def prolog(self):
            return self.getTypedRuleContext(XmlParser.PrologContext,0)


        def getRuleIndex(self):
            return XmlParser.RULE_document

        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterDocument(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitDocument(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = XmlParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            _la = self._input.LA(1)
            if _la==XmlParser.XML_DECL:
                self.state = 18
                self.prolog()


            self.state = 21
            self.element()
            self.state = 22
            self.match(XmlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrologContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(XmlParser.PrologContext, self).__init__(parent, invokingState)
            self.parser = parser

        def xmlDecl(self):
            return self.getTypedRuleContext(XmlParser.XmlDeclContext,0)


        def getRuleIndex(self):
            return XmlParser.RULE_prolog

        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterProlog(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitProlog(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitProlog(self)
            else:
                return visitor.visitChildren(self)




    def prolog(self):

        localctx = XmlParser.PrologContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prolog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.xmlDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class XmlDeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(XmlParser.XmlDeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def S(self, i=None):
            if i is None:
                return self.getTokens(XmlParser.S)
            else:
                return self.getToken(XmlParser.S, i)

        def attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(XmlParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XmlParser.AttributeContext,i)


        def getRuleIndex(self):
            return XmlParser.RULE_xmlDecl

        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterXmlDecl(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitXmlDecl(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitXmlDecl(self)
            else:
                return visitor.visitChildren(self)




    def xmlDecl(self):

        localctx = XmlParser.XmlDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_xmlDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(XmlParser.XML_DECL)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 27
                    self.match(XmlParser.S)
                    self.state = 28
                    self.attribute() 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 35
            _la = self._input.LA(1)
            if _la==XmlParser.S:
                self.state = 34
                self.match(XmlParser.S)


            self.state = 37
            self.match(XmlParser.QUESTION_GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(XmlParser.ElementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XmlParser.RULE_element

     
        def copyFrom(self, ctx):
            super(XmlParser.ElementContext, self).copyFrom(ctx)



    class EmptyTagRuleContext(ElementContext):

        def __init__(self, parser, ctx): # actually a XmlParser.ElementContext)
            super(XmlParser.EmptyTagRuleContext, self).__init__(parser)
            self.copyFrom(ctx)

        def emptyElemTag(self):
            return self.getTypedRuleContext(XmlParser.EmptyElemTagContext,0)


        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterEmptyTagRule(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitEmptyTagRule(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitEmptyTagRule(self)
            else:
                return visitor.visitChildren(self)


    class SeTagRuleContext(ElementContext):

        def __init__(self, parser, ctx): # actually a XmlParser.ElementContext)
            super(XmlParser.SeTagRuleContext, self).__init__(parser)
            self.copyFrom(ctx)

        def sTag(self):
            return self.getTypedRuleContext(XmlParser.STagContext,0)

        def content(self):
            return self.getTypedRuleContext(XmlParser.ContentContext,0)

        def eTag(self):
            return self.getTypedRuleContext(XmlParser.ETagContext,0)


        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterSeTagRule(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitSeTagRule(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitSeTagRule(self)
            else:
                return visitor.visitChildren(self)



    def element(self):

        localctx = XmlParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_element)
        try:
            self.state = 44
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = XmlParser.EmptyTagRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.emptyElemTag()
                pass

            elif la_ == 2:
                localctx = XmlParser.SeTagRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.sTag()
                self.state = 41
                self.content()
                self.state = 42
                self.eTag()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EmptyElemTagContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(XmlParser.EmptyElemTagContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XmlParser.Name, 0)

        def S(self, i=None):
            if i is None:
                return self.getTokens(XmlParser.S)
            else:
                return self.getToken(XmlParser.S, i)

        def attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(XmlParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XmlParser.AttributeContext,i)


        def getRuleIndex(self):
            return XmlParser.RULE_emptyElemTag

        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterEmptyElemTag(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitEmptyElemTag(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitEmptyElemTag(self)
            else:
                return visitor.visitChildren(self)




    def emptyElemTag(self):

        localctx = XmlParser.EmptyElemTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_emptyElemTag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(XmlParser.LT)
            self.state = 47
            self.match(XmlParser.Name)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 48
                    self.match(XmlParser.S)
                    self.state = 49
                    self.attribute() 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 56
            _la = self._input.LA(1)
            if _la==XmlParser.S:
                self.state = 55
                self.match(XmlParser.S)


            self.state = 58
            self.match(XmlParser.SLASH_GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class STagContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(XmlParser.STagContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XmlParser.Name, 0)

        def S(self, i=None):
            if i is None:
                return self.getTokens(XmlParser.S)
            else:
                return self.getToken(XmlParser.S, i)

        def attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(XmlParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XmlParser.AttributeContext,i)


        def getRuleIndex(self):
            return XmlParser.RULE_sTag

        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterSTag(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitSTag(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitSTag(self)
            else:
                return visitor.visitChildren(self)




    def sTag(self):

        localctx = XmlParser.STagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sTag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(XmlParser.LT)
            self.state = 61
            self.match(XmlParser.Name)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 62
                    self.match(XmlParser.S)
                    self.state = 63
                    self.attribute() 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 70
            _la = self._input.LA(1)
            if _la==XmlParser.S:
                self.state = 69
                self.match(XmlParser.S)


            self.state = 72
            self.match(XmlParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(XmlParser.AttributeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XmlParser.Name, 0)

        def Eq(self):
            return self.getToken(XmlParser.Eq, 0)

        def AttValue(self):
            return self.getToken(XmlParser.AttValue, 0)

        def getRuleIndex(self):
            return XmlParser.RULE_attribute

        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterAttribute(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitAttribute(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = XmlParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(XmlParser.Name)
            self.state = 75
            self.match(XmlParser.Eq)
            self.state = 76
            self.match(XmlParser.AttValue)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ETagContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(XmlParser.ETagContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XmlParser.Name, 0)

        def S(self, i=None):
            if i is None:
                return self.getTokens(XmlParser.S)
            else:
                return self.getToken(XmlParser.S, i)

        def getRuleIndex(self):
            return XmlParser.RULE_eTag

        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterETag(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitETag(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitETag(self)
            else:
                return visitor.visitChildren(self)




    def eTag(self):

        localctx = XmlParser.ETagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_eTag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if _la==XmlParser.S:
                self.state = 78
                self.match(XmlParser.S)


            self.state = 81
            self.match(XmlParser.LT_SLASH)
            self.state = 82
            self.match(XmlParser.Name)
            self.state = 84
            _la = self._input.LA(1)
            if _la==XmlParser.S:
                self.state = 83
                self.match(XmlParser.S)


            self.state = 86
            self.match(XmlParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(XmlParser.ContentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def element(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(XmlParser.ElementContext)
            else:
                return self.getTypedRuleContext(XmlParser.ElementContext,i)


        def getRuleIndex(self):
            return XmlParser.RULE_content

        def enterRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.enterContent(self)

        def exitRule(self, listener):
            if isinstance( listener, XmlParserListener ):
                listener.exitContent(self)

        def accept(self, visitor):
            if isinstance( visitor, XmlParserVisitor ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = XmlParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XmlParser.LT:
                self.state = 88
                self.element()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
