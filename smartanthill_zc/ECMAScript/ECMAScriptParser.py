# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ECMAScriptListener import ECMAScriptListener
    from .ECMAScriptVisitor import ECMAScriptVisitor
else:
    from ECMAScriptListener import ECMAScriptListener
    from ECMAScriptVisitor import ECMAScriptVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"g\u0141\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\3\2\5\2<\n\2\3\2\3\2\3\3\6\3A\n\3\r\3\16\3B\3\4\3")
        buf.write(u"\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5O\n\5\3\6\3\6\3")
        buf.write(u"\6\3\6\3\7\3\7\5\7W\n\7\3\7\3\7\3\b\6\b\\\n\b\r\b\16")
        buf.write(u"\b]\3\t\3\t\3\t\3\t\3\n\3\n\3\n\7\ng\n\n\f\n\16\nj\13")
        buf.write(u"\n\3\13\3\13\5\13n\n\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write(u"\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\177\n\17")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\5\20\u00a2\n\20\3\20\3\20\5\20\u00a6\n\20\3")
        buf.write(u"\20\3\20\5\20\u00aa\n\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\5\20\u00b4\n\20\3\20\3\20\5\20\u00b8\n\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write(u"\u00ce\n\20\3\21\3\21\5\21\u00d2\n\21\3\21\3\21\3\22")
        buf.write(u"\3\22\3\22\3\22\5\22\u00da\n\22\3\22\3\22\3\22\3\22\3")
        buf.write(u"\22\3\23\3\23\3\23\7\23\u00e4\n\23\f\23\16\23\u00e7\13")
        buf.write(u"\23\3\24\5\24\u00ea\n\24\3\25\3\25\5\25\u00ee\n\25\3")
        buf.write(u"\25\3\25\3\26\3\26\3\26\7\26\u00f5\n\26\f\26\16\26\u00f8")
        buf.write(u"\13\26\3\27\3\27\5\27\u00fc\n\27\3\27\3\27\3\30\3\30")
        buf.write(u"\3\30\7\30\u0103\n\30\f\30\16\30\u0106\13\30\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u011b\n\31\3\31")
        buf.write(u"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31")
        buf.write(u"\u0132\n\31\f\31\16\31\u0135\13\31\3\32\3\32\3\33\3\33")
        buf.write(u"\5\33\u013b\n\33\3\34\3\34\3\35\3\35\3\35\2\3\60\36\2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write(u"\64\668\2\b\3\2\27\31\3\2\23\24\3\2\35 \3\2!$\3\2*\64")
        buf.write(u"\3\3\13\13\u0154\2;\3\2\2\2\4@\3\2\2\2\6D\3\2\2\2\bN")
        buf.write(u"\3\2\2\2\nP\3\2\2\2\fT\3\2\2\2\16[\3\2\2\2\20_\3\2\2")
        buf.write(u"\2\22c\3\2\2\2\24k\3\2\2\2\26o\3\2\2\2\30r\3\2\2\2\32")
        buf.write(u"t\3\2\2\2\34w\3\2\2\2\36\u00cd\3\2\2\2 \u00cf\3\2\2\2")
        buf.write(u"\"\u00d5\3\2\2\2$\u00e0\3\2\2\2&\u00e9\3\2\2\2(\u00eb")
        buf.write(u"\3\2\2\2*\u00f1\3\2\2\2,\u00f9\3\2\2\2.\u00ff\3\2\2\2")
        buf.write(u"\60\u011a\3\2\2\2\62\u0136\3\2\2\2\64\u013a\3\2\2\2\66")
        buf.write(u"\u013c\3\2\2\28\u013e\3\2\2\2:<\5\4\3\2;:\3\2\2\2;<\3")
        buf.write(u"\2\2\2<=\3\2\2\2=>\7\2\2\3>\3\3\2\2\2?A\5\6\4\2@?\3\2")
        buf.write(u"\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\5\3\2\2\2DE\5\b\5")
        buf.write(u"\2E\7\3\2\2\2FO\5\f\7\2GO\5\20\t\2HO\5\30\r\2IO\5\32")
        buf.write(u"\16\2JO\5\34\17\2KO\5\36\20\2LO\5 \21\2MO\5\n\6\2NF\3")
        buf.write(u"\2\2\2NG\3\2\2\2NH\3\2\2\2NI\3\2\2\2NJ\3\2\2\2NK\3\2")
        buf.write(u"\2\2NL\3\2\2\2NM\3\2\2\2O\t\3\2\2\2PQ\7\3\2\2QR\5,\27")
        buf.write(u"\2RS\58\35\2S\13\3\2\2\2TV\7\t\2\2UW\5\16\b\2VU\3\2\2")
        buf.write(u"\2VW\3\2\2\2WX\3\2\2\2XY\7\n\2\2Y\r\3\2\2\2Z\\\5\b\5")
        buf.write(u"\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^\17\3\2\2")
        buf.write(u"\2_`\7@\2\2`a\5\22\n\2ab\58\35\2b\21\3\2\2\2ch\5\24\13")
        buf.write(u"\2de\7\f\2\2eg\5\24\13\2fd\3\2\2\2gj\3\2\2\2hf\3\2\2")
        buf.write(u"\2hi\3\2\2\2i\23\3\2\2\2jh\3\2\2\2km\7c\2\2ln\5\26\f")
        buf.write(u"\2ml\3\2\2\2mn\3\2\2\2n\25\3\2\2\2op\7\r\2\2pq\5\60\31")
        buf.write(u"\2q\27\3\2\2\2rs\7\13\2\2s\31\3\2\2\2tu\5\60\31\2uv\7")
        buf.write(u"\13\2\2v\33\3\2\2\2wx\7N\2\2xy\7\7\2\2yz\5\60\31\2z{")
        buf.write(u"\7\b\2\2{~\5\b\5\2|}\7>\2\2}\177\5\b\5\2~|\3\2\2\2~\177")
        buf.write(u"\3\2\2\2\177\35\3\2\2\2\u0080\u0081\7:\2\2\u0081\u0082")
        buf.write(u"\5\b\5\2\u0082\u0083\7H\2\2\u0083\u0084\7\7\2\2\u0084")
        buf.write(u"\u0085\5\60\31\2\u0085\u0086\7\b\2\2\u0086\u0087\58\35")
        buf.write(u"\2\u0087\u00ce\3\2\2\2\u0088\u0089\7H\2\2\u0089\u008a")
        buf.write(u"\7\7\2\2\u008a\u008b\5\60\31\2\u008b\u008c\7\b\2\2\u008c")
        buf.write(u"\u008d\5\b\5\2\u008d\u00ce\3\2\2\2\u008e\u008f\7F\2\2")
        buf.write(u"\u008f\u0090\7\7\2\2\u0090\u0091\7@\2\2\u0091\u0092\7")
        buf.write(u"c\2\2\u0092\u0093\7\r\2\2\u0093\u0094\5\60\31\2\u0094")
        buf.write(u"\u0095\7\13\2\2\u0095\u0096\7c\2\2\u0096\u0097\7\35\2")
        buf.write(u"\2\u0097\u0098\5\60\31\2\u0098\u0099\7\13\2\2\u0099\u009a")
        buf.write(u"\7c\2\2\u009a\u009b\7\21\2\2\u009b\u009c\7\b\2\2\u009c")
        buf.write(u"\u009d\5\b\5\2\u009d\u00ce\3\2\2\2\u009e\u009f\7F\2\2")
        buf.write(u"\u009f\u00a1\7\7\2\2\u00a0\u00a2\5\60\31\2\u00a1\u00a0")
        buf.write(u"\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write(u"\u00a5\7\13\2\2\u00a4\u00a6\5\60\31\2\u00a5\u00a4\3\2")
        buf.write(u"\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9")
        buf.write(u"\7\13\2\2\u00a8\u00aa\5\60\31\2\u00a9\u00a8\3\2\2\2\u00a9")
        buf.write(u"\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\7\b\2")
        buf.write(u"\2\u00ac\u00ce\5\b\5\2\u00ad\u00ae\7F\2\2\u00ae\u00af")
        buf.write(u"\7\7\2\2\u00af\u00b0\7@\2\2\u00b0\u00b1\5\22\n\2\u00b1")
        buf.write(u"\u00b3\7\13\2\2\u00b2\u00b4\5\60\31\2\u00b3\u00b2\3\2")
        buf.write(u"\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b7")
        buf.write(u"\7\13\2\2\u00b6\u00b8\5\60\31\2\u00b7\u00b6\3\2\2\2\u00b7")
        buf.write(u"\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\7\b\2")
        buf.write(u"\2\u00ba\u00bb\5\b\5\2\u00bb\u00ce\3\2\2\2\u00bc\u00bd")
        buf.write(u"\7F\2\2\u00bd\u00be\7\7\2\2\u00be\u00bf\5\60\31\2\u00bf")
        buf.write(u"\u00c0\7Q\2\2\u00c0\u00c1\5\60\31\2\u00c1\u00c2\7\b\2")
        buf.write(u"\2\u00c2\u00c3\5\b\5\2\u00c3\u00ce\3\2\2\2\u00c4\u00c5")
        buf.write(u"\7F\2\2\u00c5\u00c6\7\7\2\2\u00c6\u00c7\7@\2\2\u00c7")
        buf.write(u"\u00c8\5\24\13\2\u00c8\u00c9\7Q\2\2\u00c9\u00ca\5\60")
        buf.write(u"\31\2\u00ca\u00cb\7\b\2\2\u00cb\u00cc\5\b\5\2\u00cc\u00ce")
        buf.write(u"\3\2\2\2\u00cd\u0080\3\2\2\2\u00cd\u0088\3\2\2\2\u00cd")
        buf.write(u"\u008e\3\2\2\2\u00cd\u009e\3\2\2\2\u00cd\u00ad\3\2\2")
        buf.write(u"\2\u00cd\u00bc\3\2\2\2\u00cd\u00c4\3\2\2\2\u00ce\37\3")
        buf.write(u"\2\2\2\u00cf\u00d1\7C\2\2\u00d0\u00d2\5\60\31\2\u00d1")
        buf.write(u"\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2")
        buf.write(u"\2\u00d3\u00d4\58\35\2\u00d4!\3\2\2\2\u00d5\u00d6\7J")
        buf.write(u"\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d9\7\7\2\2\u00d8\u00da")
        buf.write(u"\5$\23\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write(u"\u00db\3\2\2\2\u00db\u00dc\7\b\2\2\u00dc\u00dd\7\t\2")
        buf.write(u"\2\u00dd\u00de\5&\24\2\u00de\u00df\7\n\2\2\u00df#\3\2")
        buf.write(u"\2\2\u00e0\u00e5\7c\2\2\u00e1\u00e2\7\f\2\2\u00e2\u00e4")
        buf.write(u"\7c\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5")
        buf.write(u"\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6%\3\2\2\2\u00e7")
        buf.write(u"\u00e5\3\2\2\2\u00e8\u00ea\5\4\3\2\u00e9\u00e8\3\2\2")
        buf.write(u"\2\u00e9\u00ea\3\2\2\2\u00ea\'\3\2\2\2\u00eb\u00ed\7")
        buf.write(u"\5\2\2\u00ec\u00ee\5*\26\2\u00ed\u00ec\3\2\2\2\u00ed")
        buf.write(u"\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\7\6\2")
        buf.write(u"\2\u00f0)\3\2\2\2\u00f1\u00f6\5\60\31\2\u00f2\u00f3\7")
        buf.write(u"\f\2\2\u00f3\u00f5\5\60\31\2\u00f4\u00f2\3\2\2\2\u00f5")
        buf.write(u"\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2")
        buf.write(u"\2\u00f7+\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fb\7\7")
        buf.write(u"\2\2\u00fa\u00fc\5.\30\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc")
        buf.write(u"\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\7\b\2\2\u00fe")
        buf.write(u"-\3\2\2\2\u00ff\u0104\5\60\31\2\u0100\u0101\7\f\2\2\u0101")
        buf.write(u"\u0103\5\60\31\2\u0102\u0100\3\2\2\2\u0103\u0106\3\2")
        buf.write(u"\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105/\3")
        buf.write(u"\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\b\31\1\2\u0108")
        buf.write(u"\u0109\7\26\2\2\u0109\u011b\5\60\31\16\u010a\u010b\7")
        buf.write(u"c\2\2\u010b\u010c\7\r\2\2\u010c\u011b\5\60\31\7\u010d")
        buf.write(u"\u010e\7c\2\2\u010e\u010f\7\20\2\2\u010f\u0110\7c\2\2")
        buf.write(u"\u0110\u011b\5,\27\2\u0111\u0112\7c\2\2\u0112\u011b\5")
        buf.write(u",\27\2\u0113\u011b\7c\2\2\u0114\u011b\5\64\33\2\u0115")
        buf.write(u"\u011b\5(\25\2\u0116\u0117\7\7\2\2\u0117\u0118\5\60\31")
        buf.write(u"\2\u0118\u0119\7\b\2\2\u0119\u011b\3\2\2\2\u011a\u0107")
        buf.write(u"\3\2\2\2\u011a\u010a\3\2\2\2\u011a\u010d\3\2\2\2\u011a")
        buf.write(u"\u0111\3\2\2\2\u011a\u0113\3\2\2\2\u011a\u0114\3\2\2")
        buf.write(u"\2\u011a\u0115\3\2\2\2\u011a\u0116\3\2\2\2\u011b\u0133")
        buf.write(u"\3\2\2\2\u011c\u011d\f\r\2\2\u011d\u011e\t\2\2\2\u011e")
        buf.write(u"\u0132\5\60\31\16\u011f\u0120\f\f\2\2\u0120\u0121\t\3")
        buf.write(u"\2\2\u0121\u0132\5\60\31\r\u0122\u0123\f\13\2\2\u0123")
        buf.write(u"\u0124\t\4\2\2\u0124\u0132\5\60\31\f\u0125\u0126\f\n")
        buf.write(u"\2\2\u0126\u0127\t\5\2\2\u0127\u0132\5\60\31\13\u0128")
        buf.write(u"\u0129\f\t\2\2\u0129\u012a\7(\2\2\u012a\u0132\5\60\31")
        buf.write(u"\n\u012b\u012c\f\b\2\2\u012c\u012d\7)\2\2\u012d\u0132")
        buf.write(u"\5\60\31\t\u012e\u012f\f\17\2\2\u012f\u0130\7\20\2\2")
        buf.write(u"\u0130\u0132\7c\2\2\u0131\u011c\3\2\2\2\u0131\u011f\3")
        buf.write(u"\2\2\2\u0131\u0122\3\2\2\2\u0131\u0125\3\2\2\2\u0131")
        buf.write(u"\u0128\3\2\2\2\u0131\u012b\3\2\2\2\u0131\u012e\3\2\2")
        buf.write(u"\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134")
        buf.write(u"\3\2\2\2\u0134\61\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0137")
        buf.write(u"\t\6\2\2\u0137\63\3\2\2\2\u0138\u013b\7\66\2\2\u0139")
        buf.write(u"\u013b\5\66\34\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2")
        buf.write(u"\2\2\u013b\65\3\2\2\2\u013c\u013d\7\67\2\2\u013d\67\3")
        buf.write(u"\2\2\2\u013e\u013f\t\7\2\2\u013f9\3\2\2\2\34;BNV]hm~")
        buf.write(u"\u00a1\u00a5\u00a9\u00b3\u00b7\u00cd\u00d1\u00d9\u00e5")
        buf.write(u"\u00e9\u00ed\u00f6\u00fb\u0104\u011a\u0131\u0133\u013a")
        return buf.getvalue()


class ECMAScriptParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'mcu_sleep'", u"<INVALID>", u"'['", 
                     u"']'", u"'('", u"')'", u"'{'", u"'}'", u"';'", u"','", 
                     u"'='", u"'?'", u"':'", u"'.'", u"'++'", u"'--'", u"'+'", 
                     u"'-'", u"'~'", u"'!'", u"'*'", u"'/'", u"'%'", u"'>>'", 
                     u"'<<'", u"'>>>'", u"'<'", u"'>'", u"'<='", u"'>='", 
                     u"'=='", u"'!='", u"'==='", u"'!=='", u"'&'", u"'^'", 
                     u"'|'", u"'&&'", u"'||'", u"'*='", u"'/='", u"'%='", 
                     u"'+='", u"'-='", u"'<<='", u"'>>='", u"'>>>='", u"'&='", 
                     u"'^='", u"'|='", u"'null'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'break'", u"'do'", u"'instanceof'", 
                     u"'typeof'", u"'case'", u"'else'", u"'new'", u"'var'", 
                     u"'catch'", u"'finally'", u"'return'", u"'void'", u"'continue'", 
                     u"'for'", u"'switch'", u"'while'", u"'debugger'", u"'function'", 
                     u"'this'", u"'with'", u"'default'", u"'if'", u"'throw'", 
                     u"'delete'", u"'in'", u"'try'", u"'class'", u"'enum'", 
                     u"'extends'", u"'super'", u"'const'", u"'export'", 
                     u"'import'", u"'implements'", u"'let'", u"'private'", 
                     u"'public'", u"'interface'", u"'package'", u"'protected'", 
                     u"'static'", u"'yield'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"LineTerminator", u"OpenBracket", 
                      u"CloseBracket", u"OpenParen", u"CloseParen", u"OpenBrace", 
                      u"CloseBrace", u"SemiColon", u"Comma", u"Assign", 
                      u"QuestionMark", u"Colon", u"Dot", u"PlusPlus", u"MinusMinus", 
                      u"Plus", u"Minus", u"BitNot", u"Not", u"Multiply", 
                      u"Divide", u"Modulus", u"RightShiftArithmetic", u"LeftShiftArithmetic", 
                      u"RightShiftLogical", u"LessThan", u"MoreThan", u"LessThanEquals", 
                      u"GreaterThanEquals", u"Equals", u"NotEquals", u"IdentityEquals", 
                      u"IdentityNotEquals", u"BitAnd", u"BitXOr", u"BitOr", 
                      u"And", u"Or", u"MultiplyAssign", u"DivideAssign", 
                      u"ModulusAssign", u"PlusAssign", u"MinusAssign", u"LeftShiftArithmeticAssign", 
                      u"RightShiftArithmeticAssign", u"RightShiftLogicalAssign", 
                      u"BitAndAssign", u"BitXorAssign", u"BitOrAssign", 
                      u"NullLiteral", u"BooleanLiteral", u"DecimalLiteral", 
                      u"HexIntegerLiteral", u"Break", u"Do", u"Instanceof", 
                      u"Typeof", u"Case", u"Else", u"New", u"Var", u"Catch", 
                      u"Finally", u"Return", u"Void", u"Continue", u"For", 
                      u"Switch", u"While", u"Debugger", u"Function", u"This", 
                      u"With", u"Default", u"If", u"Throw", u"Delete", u"In", 
                      u"Try", u"Class", u"Enum", u"Extends", u"Super", u"Const", 
                      u"Export", u"Import", u"Implements", u"Let", u"Private", 
                      u"Public", u"Interface", u"Package", u"Protected", 
                      u"Static", u"Yield", u"Identifier", u"WhiteSpaces", 
                      u"MultiLineComment", u"SingleLineComment", u"UnexpectedCharacter" ]

    RULE_program = 0
    RULE_sourceElements = 1
    RULE_sourceElement = 2
    RULE_statement = 3
    RULE_mcuSleepStatement = 4
    RULE_block = 5
    RULE_statementList = 6
    RULE_variableStatement = 7
    RULE_variableDeclarationList = 8
    RULE_variableDeclaration = 9
    RULE_initialiser = 10
    RULE_emptyStatement = 11
    RULE_expressionStatement = 12
    RULE_ifStatement = 13
    RULE_iterationStatement = 14
    RULE_returnStatement = 15
    RULE_functionDeclaration = 16
    RULE_formalParameterList = 17
    RULE_functionBody = 18
    RULE_arrayLiteral = 19
    RULE_elementList = 20
    RULE_arguments = 21
    RULE_argumentList = 22
    RULE_singleExpression = 23
    RULE_assignmentOperator = 24
    RULE_literal = 25
    RULE_numericLiteral = 26
    RULE_eos = 27

    ruleNames =  [ u"program", u"sourceElements", u"sourceElement", u"statement", 
                   u"mcuSleepStatement", u"block", u"statementList", u"variableStatement", 
                   u"variableDeclarationList", u"variableDeclaration", u"initialiser", 
                   u"emptyStatement", u"expressionStatement", u"ifStatement", 
                   u"iterationStatement", u"returnStatement", u"functionDeclaration", 
                   u"formalParameterList", u"functionBody", u"arrayLiteral", 
                   u"elementList", u"arguments", u"argumentList", u"singleExpression", 
                   u"assignmentOperator", u"literal", u"numericLiteral", 
                   u"eos" ]

    EOF = Token.EOF
    T__0=1
    LineTerminator=2
    OpenBracket=3
    CloseBracket=4
    OpenParen=5
    CloseParen=6
    OpenBrace=7
    CloseBrace=8
    SemiColon=9
    Comma=10
    Assign=11
    QuestionMark=12
    Colon=13
    Dot=14
    PlusPlus=15
    MinusMinus=16
    Plus=17
    Minus=18
    BitNot=19
    Not=20
    Multiply=21
    Divide=22
    Modulus=23
    RightShiftArithmetic=24
    LeftShiftArithmetic=25
    RightShiftLogical=26
    LessThan=27
    MoreThan=28
    LessThanEquals=29
    GreaterThanEquals=30
    Equals=31
    NotEquals=32
    IdentityEquals=33
    IdentityNotEquals=34
    BitAnd=35
    BitXOr=36
    BitOr=37
    And=38
    Or=39
    MultiplyAssign=40
    DivideAssign=41
    ModulusAssign=42
    PlusAssign=43
    MinusAssign=44
    LeftShiftArithmeticAssign=45
    RightShiftArithmeticAssign=46
    RightShiftLogicalAssign=47
    BitAndAssign=48
    BitXorAssign=49
    BitOrAssign=50
    NullLiteral=51
    BooleanLiteral=52
    DecimalLiteral=53
    HexIntegerLiteral=54
    Break=55
    Do=56
    Instanceof=57
    Typeof=58
    Case=59
    Else=60
    New=61
    Var=62
    Catch=63
    Finally=64
    Return=65
    Void=66
    Continue=67
    For=68
    Switch=69
    While=70
    Debugger=71
    Function=72
    This=73
    With=74
    Default=75
    If=76
    Throw=77
    Delete=78
    In=79
    Try=80
    Class=81
    Enum=82
    Extends=83
    Super=84
    Const=85
    Export=86
    Import=87
    Implements=88
    Let=89
    Private=90
    Public=91
    Interface=92
    Package=93
    Protected=94
    Static=95
    Yield=96
    Identifier=97
    WhiteSpaces=98
    MultiLineComment=99
    SingleLineComment=100
    UnexpectedCharacter=101

    def __init__(self, input):
        super(ECMAScriptParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None





    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ECMAScriptParser.EOF, 0)

        def sourceElements(self):
            return self.getTypedRuleContext(ECMAScriptParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_program

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitProgram(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ECMAScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Var))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (ECMAScriptParser.Return - 65)) | (1 << (ECMAScriptParser.For - 65)) | (1 << (ECMAScriptParser.While - 65)) | (1 << (ECMAScriptParser.If - 65)) | (1 << (ECMAScriptParser.Identifier - 65)))) != 0):
                self.state = 56
                self.sourceElements()


            self.state = 59
            self.match(ECMAScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SourceElementsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.SourceElementsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sourceElement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SourceElementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SourceElementContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_sourceElements

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSourceElements(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSourceElements(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitSourceElements(self)
            else:
                return visitor.visitChildren(self)




    def sourceElements(self):

        localctx = ECMAScriptParser.SourceElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sourceElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.sourceElement()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Var))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (ECMAScriptParser.Return - 65)) | (1 << (ECMAScriptParser.For - 65)) | (1 << (ECMAScriptParser.While - 65)) | (1 << (ECMAScriptParser.If - 65)) | (1 << (ECMAScriptParser.Identifier - 65)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SourceElementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.SourceElementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_sourceElement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSourceElement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSourceElement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitSourceElement(self)
            else:
                return visitor.visitChildren(self)




    def sourceElement(self):

        localctx = ECMAScriptParser.SourceElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sourceElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableStatementContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.EmptyStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.IfStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.IterationStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ReturnStatementContext,0)


        def mcuSleepStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.McuSleepStatementContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ECMAScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 76
            token = self._input.LA(1)
            if token in [ECMAScriptParser.OpenBrace]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.block()

            elif token in [ECMAScriptParser.Var]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.variableStatement()

            elif token in [ECMAScriptParser.SemiColon]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.emptyStatement()

            elif token in [ECMAScriptParser.OpenBracket, ECMAScriptParser.OpenParen, ECMAScriptParser.Not, ECMAScriptParser.BooleanLiteral, ECMAScriptParser.DecimalLiteral, ECMAScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.expressionStatement()

            elif token in [ECMAScriptParser.If]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.ifStatement()

            elif token in [ECMAScriptParser.Do, ECMAScriptParser.For, ECMAScriptParser.While]:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.iterationStatement()

            elif token in [ECMAScriptParser.Return]:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.returnStatement()

            elif token in [ECMAScriptParser.T__0]:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.mcuSleepStatement()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class McuSleepStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.McuSleepStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def arguments(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentsContext,0)


        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_mcuSleepStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMcuSleepStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMcuSleepStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitMcuSleepStatement(self)
            else:
                return visitor.visitChildren(self)




    def mcuSleepStatement(self):

        localctx = ECMAScriptParser.McuSleepStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mcuSleepStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ECMAScriptParser.T__0)
            self.state = 79
            self.arguments()
            self.state = 80
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_block

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ECMAScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 84
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Var))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (ECMAScriptParser.Return - 65)) | (1 << (ECMAScriptParser.For - 65)) | (1 << (ECMAScriptParser.While - 65)) | (1 << (ECMAScriptParser.If - 65)) | (1 << (ECMAScriptParser.Identifier - 65)))) != 0):
                self.state = 83
                self.statementList()


            self.state = 86
            self.match(ECMAScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.StatementListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_statementList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitStatementList(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = ECMAScriptParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                self.statement()
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Var))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (ECMAScriptParser.Return - 65)) | (1 << (ECMAScriptParser.For - 65)) | (1 << (ECMAScriptParser.While - 65)) | (1 << (ECMAScriptParser.If - 65)) | (1 << (ECMAScriptParser.Identifier - 65)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.VariableStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationListContext,0)


        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_variableStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVariableStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVariableStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitVariableStatement(self)
            else:
                return visitor.visitChildren(self)




    def variableStatement(self):

        localctx = ECMAScriptParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ECMAScriptParser.Var)
            self.state = 94
            self.variableDeclarationList()
            self.state = 95
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.VariableDeclarationListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_variableDeclarationList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVariableDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVariableDeclarationList(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitVariableDeclarationList(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarationList(self):

        localctx = ECMAScriptParser.VariableDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variableDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.variableDeclaration()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 98
                self.match(ECMAScriptParser.Comma)
                self.state = 99
                self.variableDeclaration()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.VariableDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def initialiser(self):
            return self.getTypedRuleContext(ECMAScriptParser.InitialiserContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_variableDeclaration

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = ECMAScriptParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ECMAScriptParser.Identifier)
            self.state = 107
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Assign:
                self.state = 106
                self.initialiser()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitialiserContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.InitialiserContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_initialiser

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterInitialiser(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitInitialiser(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitInitialiser(self)
            else:
                return visitor.visitChildren(self)




    def initialiser(self):

        localctx = ECMAScriptParser.InitialiserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_initialiser)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ECMAScriptParser.Assign)
            self.state = 110
            self.singleExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EmptyStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.EmptyStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SemiColon(self):
            return self.getToken(ECMAScriptParser.SemiColon, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_emptyStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)




    def emptyStatement(self):

        localctx = ECMAScriptParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ECMAScriptParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ExpressionStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def SemiColon(self):
            return self.getToken(ECMAScriptParser.SemiColon, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_expressionStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = ECMAScriptParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.singleExpression(0)
            self.state = 115
            self.match(ECMAScriptParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.IfStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(ECMAScriptParser.If, 0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.StatementContext,i)


        def Else(self):
            return self.getToken(ECMAScriptParser.Else, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_ifStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIfStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = ECMAScriptParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ECMAScriptParser.If)
            self.state = 118
            self.match(ECMAScriptParser.OpenParen)
            self.state = 119
            self.singleExpression(0)
            self.state = 120
            self.match(ECMAScriptParser.CloseParen)
            self.state = 121
            self.statement()
            self.state = 124
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 122
                self.match(ECMAScriptParser.Else)
                self.state = 123
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.IterationStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_iterationStatement

     
        def copyFrom(self, ctx):
            super(ECMAScriptParser.IterationStatementContext, self).copyFrom(ctx)



    class SimpleForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.SimpleForStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)
        def Identifier(self, i=None):
            if i is None:
                return self.getTokens(ECMAScriptParser.Identifier)
            else:
                return self.getToken(ECMAScriptParser.Identifier, i)
        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSimpleForStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSimpleForStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitSimpleForStatement(self)
            else:
                return visitor.visitChildren(self)


    class DoStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.DoStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Do(self):
            return self.getToken(ECMAScriptParser.Do, 0)
        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDoStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDoStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitDoStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForVarInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.ForVarInStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)
        def variableDeclaration(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationContext,0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForVarInStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForVarInStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitForVarInStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.ForStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.WhileStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitWhileStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.ForInStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)
        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForInStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForInStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitForInStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForVarStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.ForVarStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)
        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationListContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForVarStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForVarStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitForVarStatement(self)
            else:
                return visitor.visitChildren(self)



    def iterationStatement(self):

        localctx = ECMAScriptParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 203
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(ECMAScriptParser.Do)
                self.state = 127
                self.statement()
                self.state = 128
                self.match(ECMAScriptParser.While)
                self.state = 129
                self.match(ECMAScriptParser.OpenParen)
                self.state = 130
                self.singleExpression(0)
                self.state = 131
                self.match(ECMAScriptParser.CloseParen)
                self.state = 132
                self.eos()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(ECMAScriptParser.While)
                self.state = 135
                self.match(ECMAScriptParser.OpenParen)
                self.state = 136
                self.singleExpression(0)
                self.state = 137
                self.match(ECMAScriptParser.CloseParen)
                self.state = 138
                self.statement()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.SimpleForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(ECMAScriptParser.For)
                self.state = 141
                self.match(ECMAScriptParser.OpenParen)
                self.state = 142
                self.match(ECMAScriptParser.Var)
                self.state = 143
                self.match(ECMAScriptParser.Identifier)
                self.state = 144
                self.match(ECMAScriptParser.Assign)
                self.state = 145
                self.singleExpression(0)
                self.state = 146
                self.match(ECMAScriptParser.SemiColon)
                self.state = 147
                self.match(ECMAScriptParser.Identifier)
                self.state = 148
                self.match(ECMAScriptParser.LessThan)
                self.state = 149
                self.singleExpression(0)
                self.state = 150
                self.match(ECMAScriptParser.SemiColon)
                self.state = 151
                self.match(ECMAScriptParser.Identifier)
                self.state = 152
                self.match(ECMAScriptParser.PlusPlus)
                self.state = 153
                self.match(ECMAScriptParser.CloseParen)
                self.state = 154
                self.statement()
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.match(ECMAScriptParser.For)
                self.state = 157
                self.match(ECMAScriptParser.OpenParen)
                self.state = 159
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral))) != 0) or _la==ECMAScriptParser.Identifier:
                    self.state = 158
                    self.singleExpression(0)


                self.state = 161
                self.match(ECMAScriptParser.SemiColon)
                self.state = 163
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral))) != 0) or _la==ECMAScriptParser.Identifier:
                    self.state = 162
                    self.singleExpression(0)


                self.state = 165
                self.match(ECMAScriptParser.SemiColon)
                self.state = 167
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral))) != 0) or _la==ECMAScriptParser.Identifier:
                    self.state = 166
                    self.singleExpression(0)


                self.state = 169
                self.match(ECMAScriptParser.CloseParen)
                self.state = 170
                self.statement()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 171
                self.match(ECMAScriptParser.For)
                self.state = 172
                self.match(ECMAScriptParser.OpenParen)
                self.state = 173
                self.match(ECMAScriptParser.Var)
                self.state = 174
                self.variableDeclarationList()
                self.state = 175
                self.match(ECMAScriptParser.SemiColon)
                self.state = 177
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral))) != 0) or _la==ECMAScriptParser.Identifier:
                    self.state = 176
                    self.singleExpression(0)


                self.state = 179
                self.match(ECMAScriptParser.SemiColon)
                self.state = 181
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral))) != 0) or _la==ECMAScriptParser.Identifier:
                    self.state = 180
                    self.singleExpression(0)


                self.state = 183
                self.match(ECMAScriptParser.CloseParen)
                self.state = 184
                self.statement()
                pass

            elif la_ == 6:
                localctx = ECMAScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 186
                self.match(ECMAScriptParser.For)
                self.state = 187
                self.match(ECMAScriptParser.OpenParen)
                self.state = 188
                self.singleExpression(0)
                self.state = 189
                self.match(ECMAScriptParser.In)
                self.state = 190
                self.singleExpression(0)
                self.state = 191
                self.match(ECMAScriptParser.CloseParen)
                self.state = 192
                self.statement()
                pass

            elif la_ == 7:
                localctx = ECMAScriptParser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 194
                self.match(ECMAScriptParser.For)
                self.state = 195
                self.match(ECMAScriptParser.OpenParen)
                self.state = 196
                self.match(ECMAScriptParser.Var)
                self.state = 197
                self.variableDeclaration()
                self.state = 198
                self.match(ECMAScriptParser.In)
                self.state = 199
                self.singleExpression(0)
                self.state = 200
                self.match(ECMAScriptParser.CloseParen)
                self.state = 201
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ReturnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(ECMAScriptParser.Return, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_returnStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitReturnStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = ECMAScriptParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ECMAScriptParser.Return)
            self.state = 207
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral))) != 0) or _la==ECMAScriptParser.Identifier:
                self.state = 206
                self.singleExpression(0)


            self.state = 209
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.FunctionDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(ECMAScriptParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_functionDeclaration

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = ECMAScriptParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(ECMAScriptParser.Function)
            self.state = 212
            self.match(ECMAScriptParser.Identifier)
            self.state = 213
            self.match(ECMAScriptParser.OpenParen)
            self.state = 215
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Identifier:
                self.state = 214
                self.formalParameterList()


            self.state = 217
            self.match(ECMAScriptParser.CloseParen)
            self.state = 218
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 219
            self.functionBody()
            self.state = 220
            self.match(ECMAScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.FormalParameterListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i=None):
            if i is None:
                return self.getTokens(ECMAScriptParser.Identifier)
            else:
                return self.getToken(ECMAScriptParser.Identifier, i)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_formalParameterList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFormalParameterList(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFormalParameterList(self)
            else:
                return visitor.visitChildren(self)




    def formalParameterList(self):

        localctx = ECMAScriptParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(ECMAScriptParser.Identifier)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 223
                self.match(ECMAScriptParser.Comma)
                self.state = 224
                self.match(ECMAScriptParser.Identifier)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.FunctionBodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sourceElements(self):
            return self.getTypedRuleContext(ECMAScriptParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_functionBody

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFunctionBody(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = ECMAScriptParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Var))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (ECMAScriptParser.Return - 65)) | (1 << (ECMAScriptParser.For - 65)) | (1 << (ECMAScriptParser.While - 65)) | (1 << (ECMAScriptParser.If - 65)) | (1 << (ECMAScriptParser.Identifier - 65)))) != 0):
                self.state = 230
                self.sourceElements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ArrayLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def elementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.ElementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_arrayLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = ECMAScriptParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ECMAScriptParser.OpenBracket)
            self.state = 235
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral))) != 0) or _la==ECMAScriptParser.Identifier:
                self.state = 234
                self.elementList()


            self.state = 237
            self.match(ECMAScriptParser.CloseBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ElementListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_elementList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterElementList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitElementList(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitElementList(self)
            else:
                return visitor.visitChildren(self)




    def elementList(self):

        localctx = ECMAScriptParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.singleExpression(0)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 240
                self.match(ECMAScriptParser.Comma)
                self.state = 241
                self.singleExpression(0)
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ArgumentsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argumentList(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_arguments

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArguments(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArguments(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = ECMAScriptParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ECMAScriptParser.OpenParen)
            self.state = 249
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.OpenBracket) | (1 << ECMAScriptParser.OpenParen) | (1 << ECMAScriptParser.Not) | (1 << ECMAScriptParser.BooleanLiteral) | (1 << ECMAScriptParser.DecimalLiteral))) != 0) or _la==ECMAScriptParser.Identifier:
                self.state = 248
                self.argumentList()


            self.state = 251
            self.match(ECMAScriptParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ArgumentListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_argumentList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArgumentList(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = ECMAScriptParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.singleExpression(0)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 254
                self.match(ECMAScriptParser.Comma)
                self.state = 255
                self.singleExpression(0)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SingleExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.SingleExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_singleExpression

     
        def copyFrom(self, ctx):
            super(ECMAScriptParser.SingleExpressionContext, self).copyFrom(ctx)


    class FunctionExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.FunctionExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)
        def arguments(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFunctionExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFunctionExpression(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.AssignmentExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.LogicalOrExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.LogicalAndExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.ParenthesizedExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.LiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(ECMAScriptParser.LiteralContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLiteralExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArrayLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.ArrayLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def arrayLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArrayLiteralContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArrayLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArrayLiteralExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitArrayLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class MemberDotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.MemberDotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMemberDotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMemberDotExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitMemberDotExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.NotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitNotExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.IdentifierExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.RelationalExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)


    class MethodExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.MethodExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self, i=None):
            if i is None:
                return self.getTokens(ECMAScriptParser.Identifier)
            else:
                return self.getToken(ECMAScriptParser.Identifier, i)
        def arguments(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMethodExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitMethodExpression(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.EqualityExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.AdditiveExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.MultiplicativeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)



    def singleExpression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ECMAScriptParser.SingleExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_singleExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 262
                self.match(ECMAScriptParser.Not)
                self.state = 263
                self.singleExpression(12)
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.AssignmentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 264
                self.match(ECMAScriptParser.Identifier)
                self.state = 265
                self.match(ECMAScriptParser.Assign)
                self.state = 266
                self.singleExpression(5)
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 267
                self.match(ECMAScriptParser.Identifier)
                self.state = 268
                self.match(ECMAScriptParser.Dot)
                self.state = 269
                self.match(ECMAScriptParser.Identifier)
                self.state = 270
                self.arguments()
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.FunctionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 271
                self.match(ECMAScriptParser.Identifier)
                self.state = 272
                self.arguments()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 273
                self.match(ECMAScriptParser.Identifier)
                pass

            elif la_ == 6:
                localctx = ECMAScriptParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 274
                self.literal()
                pass

            elif la_ == 7:
                localctx = ECMAScriptParser.ArrayLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 275
                self.arrayLiteral()
                pass

            elif la_ == 8:
                localctx = ECMAScriptParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 276
                self.match(ECMAScriptParser.OpenParen)
                self.state = 277
                self.singleExpression(0)
                self.state = 278
                self.match(ECMAScriptParser.CloseParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 303
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = ECMAScriptParser.MultiplicativeExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 282
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 283
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.Multiply) | (1 << ECMAScriptParser.Divide) | (1 << ECMAScriptParser.Modulus))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 284
                        self.singleExpression(12)
                        pass

                    elif la_ == 2:
                        localctx = ECMAScriptParser.AdditiveExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 285
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 286
                        _la = self._input.LA(1)
                        if not(_la==ECMAScriptParser.Plus or _la==ECMAScriptParser.Minus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 287
                        self.singleExpression(11)
                        pass

                    elif la_ == 3:
                        localctx = ECMAScriptParser.RelationalExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 288
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 289
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.LessThan) | (1 << ECMAScriptParser.MoreThan) | (1 << ECMAScriptParser.LessThanEquals) | (1 << ECMAScriptParser.GreaterThanEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 290
                        self.singleExpression(10)
                        pass

                    elif la_ == 4:
                        localctx = ECMAScriptParser.EqualityExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 291
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 292
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.Equals) | (1 << ECMAScriptParser.NotEquals) | (1 << ECMAScriptParser.IdentityEquals) | (1 << ECMAScriptParser.IdentityNotEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 293
                        self.singleExpression(9)
                        pass

                    elif la_ == 5:
                        localctx = ECMAScriptParser.LogicalAndExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 294
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 295
                        self.match(ECMAScriptParser.And)
                        self.state = 296
                        self.singleExpression(8)
                        pass

                    elif la_ == 6:
                        localctx = ECMAScriptParser.LogicalOrExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 297
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 298
                        self.match(ECMAScriptParser.Or)
                        self.state = 299
                        self.singleExpression(7)
                        pass

                    elif la_ == 7:
                        localctx = ECMAScriptParser.MemberDotExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 300
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 301
                        self.match(ECMAScriptParser.Dot)
                        self.state = 302
                        self.match(ECMAScriptParser.Identifier)
                        pass

             
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.AssignmentOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_assignmentOperator

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = ECMAScriptParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.MultiplyAssign) | (1 << ECMAScriptParser.DivideAssign) | (1 << ECMAScriptParser.ModulusAssign) | (1 << ECMAScriptParser.PlusAssign) | (1 << ECMAScriptParser.MinusAssign) | (1 << ECMAScriptParser.LeftShiftArithmeticAssign) | (1 << ECMAScriptParser.RightShiftArithmeticAssign) | (1 << ECMAScriptParser.RightShiftLogicalAssign) | (1 << ECMAScriptParser.BitAndAssign) | (1 << ECMAScriptParser.BitXorAssign) | (1 << ECMAScriptParser.BitOrAssign))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.LiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BooleanLiteral(self):
            return self.getToken(ECMAScriptParser.BooleanLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_literal

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ECMAScriptParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        try:
            self.state = 312
            token = self._input.LA(1)
            if token in [ECMAScriptParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(ECMAScriptParser.BooleanLiteral)

            elif token in [ECMAScriptParser.DecimalLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.numericLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.NumericLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(ECMAScriptParser.DecimalLiteral, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_numericLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitNumericLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitNumericLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteral(self):

        localctx = ECMAScriptParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_numericLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(ECMAScriptParser.DecimalLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EosContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.EosContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SemiColon(self):
            return self.getToken(ECMAScriptParser.SemiColon, 0)

        def EOF(self):
            return self.getToken(ECMAScriptParser.EOF, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_eos

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEos(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEos(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = ECMAScriptParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            _la = self._input.LA(1)
            if not(_la==ECMAScriptParser.EOF or _la==ECMAScriptParser.SemiColon):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.singleExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def singleExpression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 13)
         



