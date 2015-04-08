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
        buf.write(u"j\u01fb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\3\2\5\2t\n\2\3\2\3\2\3\3\6\3y\n\3\r\3\16\3z\3\4")
        buf.write(u"\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0085\n\5\3\6\3\6\3")
        buf.write(u"\6\3\6\3\7\3\7\5\7\u008d\n\7\3\7\3\7\3\b\6\b\u0092\n")
        buf.write(u"\b\r\b\16\b\u0093\3\t\3\t\3\t\3\t\3\n\3\n\3\n\7\n\u009d")
        buf.write(u"\n\n\f\n\16\n\u00a0\13\n\3\13\3\13\5\13\u00a4\n\13\3")
        buf.write(u"\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\5\17\u00b6\n\17\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\5\20\u00c9\n\20\3\20\3\20\5\20\u00cd")
        buf.write(u"\n\20\3\20\3\20\5\20\u00d1\n\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\5\20\u00db\n\20\3\20\3\20\5\20\u00df")
        buf.write(u"\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\5\20\u00f5\n\20\3\21\3\21\5\21\u00f9\n\21\3\21\3\21")
        buf.write(u"\3\22\3\22\5\22\u00ff\n\22\3\22\3\22\3\23\3\23\5\23\u0105")
        buf.write(u"\n\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\26\3\26\5\26\u0117\n\26\3\26")
        buf.write(u"\3\26\5\26\u011b\n\26\5\26\u011d\n\26\3\26\3\26\3\27")
        buf.write(u"\6\27\u0122\n\27\r\27\16\27\u0123\3\30\3\30\3\30\3\30")
        buf.write(u"\5\30\u012a\n\30\3\31\3\31\3\31\5\31\u012f\n\31\3\32")
        buf.write(u"\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write(u"\u0146\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3")
        buf.write(u"\36\3\37\3\37\3\37\3 \3 \3 \3 \5 \u0158\n \3 \3 \3 \3")
        buf.write(u" \3 \3!\3!\3!\7!\u0162\n!\f!\16!\u0165\13!\3\"\5\"\u0168")
        buf.write(u"\n\"\3#\3#\5#\u016c\n#\3#\5#\u016f\n#\3#\5#\u0172\n#")
        buf.write(u"\3#\3#\3$\5$\u0177\n$\3$\3$\3$\5$\u017c\n$\3$\7$\u017f")
        buf.write(u"\n$\f$\16$\u0182\13$\3%\6%\u0185\n%\r%\16%\u0186\3&\3")
        buf.write(u"&\5&\u018b\n&\3&\5&\u018e\n&\3&\3&\3\'\3\'\3\'\7\'\u0195")
        buf.write(u"\n\'\f\'\16\'\u0198\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01ad\n(\3)\3)\3)\5)")
        buf.write(u"\u01b2\n)\3*\3*\3+\3+\5+\u01b8\n+\3+\3+\3,\3,\3,\7,\u01bf")
        buf.write(u"\n,\f,\16,\u01c2\13,\3-\3-\3-\7-\u01c7\n-\f-\16-\u01ca")
        buf.write(u"\13-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01d9")
        buf.write(u"\n.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\5\62\u01e3\n")
        buf.write(u"\62\3\63\3\63\3\63\5\63\u01e8\n\63\3\64\3\64\3\65\3\65")
        buf.write(u"\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\58\u01f7\n8\3")
        buf.write(u"9\39\39\2\2:\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write(u"\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2")
        buf.write(u"\6\3\2+\65\3\2\66\67\3\2;T\3\2Ud\u0200\2s\3\2\2\2\4x")
        buf.write(u"\3\2\2\2\6|\3\2\2\2\b\u0084\3\2\2\2\n\u0086\3\2\2\2\f")
        buf.write(u"\u008a\3\2\2\2\16\u0091\3\2\2\2\20\u0095\3\2\2\2\22\u0099")
        buf.write(u"\3\2\2\2\24\u00a1\3\2\2\2\26\u00a5\3\2\2\2\30\u00a8\3")
        buf.write(u"\2\2\2\32\u00aa\3\2\2\2\34\u00ae\3\2\2\2\36\u00f4\3\2")
        buf.write(u"\2\2 \u00f6\3\2\2\2\"\u00fc\3\2\2\2$\u0102\3\2\2\2&\u0108")
        buf.write(u"\3\2\2\2(\u010e\3\2\2\2*\u0114\3\2\2\2,\u0121\3\2\2\2")
        buf.write(u".\u0125\3\2\2\2\60\u012b\3\2\2\2\62\u0130\3\2\2\2\64")
        buf.write(u"\u0134\3\2\2\2\66\u0145\3\2\2\28\u0147\3\2\2\2:\u014d")
        buf.write(u"\3\2\2\2<\u0150\3\2\2\2>\u0153\3\2\2\2@\u015e\3\2\2\2")
        buf.write(u"B\u0167\3\2\2\2D\u0169\3\2\2\2F\u0176\3\2\2\2H\u0184")
        buf.write(u"\3\2\2\2J\u0188\3\2\2\2L\u0191\3\2\2\2N\u01ac\3\2\2\2")
        buf.write(u"P\u01b1\3\2\2\2R\u01b3\3\2\2\2T\u01b5\3\2\2\2V\u01bb")
        buf.write(u"\3\2\2\2X\u01c3\3\2\2\2Z\u01d8\3\2\2\2\\\u01da\3\2\2")
        buf.write(u"\2^\u01dc\3\2\2\2`\u01de\3\2\2\2b\u01e2\3\2\2\2d\u01e7")
        buf.write(u"\3\2\2\2f\u01e9\3\2\2\2h\u01eb\3\2\2\2j\u01ed\3\2\2\2")
        buf.write(u"l\u01f0\3\2\2\2n\u01f6\3\2\2\2p\u01f8\3\2\2\2rt\5\4\3")
        buf.write(u"\2sr\3\2\2\2st\3\2\2\2tu\3\2\2\2uv\7\2\2\3v\3\3\2\2\2")
        buf.write(u"wy\5\6\4\2xw\3\2\2\2yz\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\5")
        buf.write(u"\3\2\2\2|}\5\b\5\2}\7\3\2\2\2~\u0085\5\f\7\2\177\u0085")
        buf.write(u"\5\20\t\2\u0080\u0085\5\30\r\2\u0081\u0085\5\34\17\2")
        buf.write(u"\u0082\u0085\5$\23\2\u0083\u0085\5\n\6\2\u0084~\3\2\2")
        buf.write(u"\2\u0084\177\3\2\2\2\u0084\u0080\3\2\2\2\u0084\u0081")
        buf.write(u"\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085")
        buf.write(u"\t\3\2\2\2\u0086\u0087\7\3\2\2\u0087\u0088\5T+\2\u0088")
        buf.write(u"\u0089\5n8\2\u0089\13\3\2\2\2\u008a\u008c\7\n\2\2\u008b")
        buf.write(u"\u008d\5\16\b\2\u008c\u008b\3\2\2\2\u008c\u008d\3\2\2")
        buf.write(u"\2\u008d\u008e\3\2\2\2\u008e\u008f\7\13\2\2\u008f\r\3")
        buf.write(u"\2\2\2\u0090\u0092\5\b\5\2\u0091\u0090\3\2\2\2\u0092")
        buf.write(u"\u0093\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2")
        buf.write(u"\2\u0094\17\3\2\2\2\u0095\u0096\7B\2\2\u0096\u0097\5")
        buf.write(u"\22\n\2\u0097\u0098\5n8\2\u0098\21\3\2\2\2\u0099\u009e")
        buf.write(u"\5\24\13\2\u009a\u009b\7\r\2\2\u009b\u009d\5\24\13\2")
        buf.write(u"\u009c\u009a\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c")
        buf.write(u"\3\2\2\2\u009e\u009f\3\2\2\2\u009f\23\3\2\2\2\u00a0\u009e")
        buf.write(u"\3\2\2\2\u00a1\u00a3\7e\2\2\u00a2\u00a4\5\26\f\2\u00a3")
        buf.write(u"\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\25\3\2\2\2\u00a5")
        buf.write(u"\u00a6\7\16\2\2\u00a6\u00a7\5Z.\2\u00a7\27\3\2\2\2\u00a8")
        buf.write(u"\u00a9\7\f\2\2\u00a9\31\3\2\2\2\u00aa\u00ab\6\16\2\2")
        buf.write(u"\u00ab\u00ac\5X-\2\u00ac\u00ad\7\f\2\2\u00ad\33\3\2\2")
        buf.write(u"\2\u00ae\u00af\7P\2\2\u00af\u00b0\7\b\2\2\u00b0\u00b1")
        buf.write(u"\5X-\2\u00b1\u00b2\7\t\2\2\u00b2\u00b5\5\b\5\2\u00b3")
        buf.write(u"\u00b4\7@\2\2\u00b4\u00b6\5\b\5\2\u00b5\u00b3\3\2\2\2")
        buf.write(u"\u00b5\u00b6\3\2\2\2\u00b6\35\3\2\2\2\u00b7\u00b8\7<")
        buf.write(u"\2\2\u00b8\u00b9\5\b\5\2\u00b9\u00ba\7J\2\2\u00ba\u00bb")
        buf.write(u"\7\b\2\2\u00bb\u00bc\5X-\2\u00bc\u00bd\7\t\2\2\u00bd")
        buf.write(u"\u00be\5n8\2\u00be\u00f5\3\2\2\2\u00bf\u00c0\7J\2\2\u00c0")
        buf.write(u"\u00c1\7\b\2\2\u00c1\u00c2\5X-\2\u00c2\u00c3\7\t\2\2")
        buf.write(u"\u00c3\u00c4\5\b\5\2\u00c4\u00f5\3\2\2\2\u00c5\u00c6")
        buf.write(u"\7H\2\2\u00c6\u00c8\7\b\2\2\u00c7\u00c9\5X-\2\u00c8\u00c7")
        buf.write(u"\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write(u"\u00cc\7\f\2\2\u00cb\u00cd\5X-\2\u00cc\u00cb\3\2\2\2")
        buf.write(u"\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0")
        buf.write(u"\7\f\2\2\u00cf\u00d1\5X-\2\u00d0\u00cf\3\2\2\2\u00d0")
        buf.write(u"\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\7\t\2")
        buf.write(u"\2\u00d3\u00f5\5\b\5\2\u00d4\u00d5\7H\2\2\u00d5\u00d6")
        buf.write(u"\7\b\2\2\u00d6\u00d7\7B\2\2\u00d7\u00d8\5\22\n\2\u00d8")
        buf.write(u"\u00da\7\f\2\2\u00d9\u00db\5X-\2\u00da\u00d9\3\2\2\2")
        buf.write(u"\u00da\u00db\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de")
        buf.write(u"\7\f\2\2\u00dd\u00df\5X-\2\u00de\u00dd\3\2\2\2\u00de")
        buf.write(u"\u00df\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\7\t\2")
        buf.write(u"\2\u00e1\u00e2\5\b\5\2\u00e2\u00f5\3\2\2\2\u00e3\u00e4")
        buf.write(u"\7H\2\2\u00e4\u00e5\7\b\2\2\u00e5\u00e6\5Z.\2\u00e6\u00e7")
        buf.write(u"\7S\2\2\u00e7\u00e8\5X-\2\u00e8\u00e9\7\t\2\2\u00e9\u00ea")
        buf.write(u"\5\b\5\2\u00ea\u00f5\3\2\2\2\u00eb\u00ec\7H\2\2\u00ec")
        buf.write(u"\u00ed\7\b\2\2\u00ed\u00ee\7B\2\2\u00ee\u00ef\5\24\13")
        buf.write(u"\2\u00ef\u00f0\7S\2\2\u00f0\u00f1\5X-\2\u00f1\u00f2\7")
        buf.write(u"\t\2\2\u00f2\u00f3\5\b\5\2\u00f3\u00f5\3\2\2\2\u00f4")
        buf.write(u"\u00b7\3\2\2\2\u00f4\u00bf\3\2\2\2\u00f4\u00c5\3\2\2")
        buf.write(u"\2\u00f4\u00d4\3\2\2\2\u00f4\u00e3\3\2\2\2\u00f4\u00eb")
        buf.write(u"\3\2\2\2\u00f5\37\3\2\2\2\u00f6\u00f8\7G\2\2\u00f7\u00f9")
        buf.write(u"\7e\2\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write(u"\u00fa\3\2\2\2\u00fa\u00fb\5n8\2\u00fb!\3\2\2\2\u00fc")
        buf.write(u"\u00fe\7;\2\2\u00fd\u00ff\7e\2\2\u00fe\u00fd\3\2\2\2")
        buf.write(u"\u00fe\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101")
        buf.write(u"\5n8\2\u0101#\3\2\2\2\u0102\u0104\7E\2\2\u0103\u0105")
        buf.write(u"\5X-\2\u0104\u0103\3\2\2\2\u0104\u0105\3\2\2\2\u0105")
        buf.write(u"\u0106\3\2\2\2\u0106\u0107\5n8\2\u0107%\3\2\2\2\u0108")
        buf.write(u"\u0109\7N\2\2\u0109\u010a\7\b\2\2\u010a\u010b\5X-\2\u010b")
        buf.write(u"\u010c\7\t\2\2\u010c\u010d\5\b\5\2\u010d\'\3\2\2\2\u010e")
        buf.write(u"\u010f\7I\2\2\u010f\u0110\7\b\2\2\u0110\u0111\5X-\2\u0111")
        buf.write(u"\u0112\7\t\2\2\u0112\u0113\5*\26\2\u0113)\3\2\2\2\u0114")
        buf.write(u"\u0116\7\n\2\2\u0115\u0117\5,\27\2\u0116\u0115\3\2\2")
        buf.write(u"\2\u0116\u0117\3\2\2\2\u0117\u011c\3\2\2\2\u0118\u011a")
        buf.write(u"\5\60\31\2\u0119\u011b\5,\27\2\u011a\u0119\3\2\2\2\u011a")
        buf.write(u"\u011b\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u0118\3\2\2")
        buf.write(u"\2\u011c\u011d\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f")
        buf.write(u"\7\13\2\2\u011f+\3\2\2\2\u0120\u0122\5.\30\2\u0121\u0120")
        buf.write(u"\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0121\3\2\2\2\u0123")
        buf.write(u"\u0124\3\2\2\2\u0124-\3\2\2\2\u0125\u0126\7?\2\2\u0126")
        buf.write(u"\u0127\5X-\2\u0127\u0129\7\20\2\2\u0128\u012a\5\16\b")
        buf.write(u"\2\u0129\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a/\3\2")
        buf.write(u"\2\2\u012b\u012c\7O\2\2\u012c\u012e\7\20\2\2\u012d\u012f")
        buf.write(u"\5\16\b\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write(u"\61\3\2\2\2\u0130\u0131\7e\2\2\u0131\u0132\7\20\2\2\u0132")
        buf.write(u"\u0133\5\b\5\2\u0133\63\3\2\2\2\u0134\u0135\7Q\2\2\u0135")
        buf.write(u"\u0136\5X-\2\u0136\u0137\5n8\2\u0137\65\3\2\2\2\u0138")
        buf.write(u"\u0139\7T\2\2\u0139\u013a\5\f\7\2\u013a\u013b\58\35\2")
        buf.write(u"\u013b\u0146\3\2\2\2\u013c\u013d\7T\2\2\u013d\u013e\5")
        buf.write(u"\f\7\2\u013e\u013f\5:\36\2\u013f\u0146\3\2\2\2\u0140")
        buf.write(u"\u0141\7T\2\2\u0141\u0142\5\f\7\2\u0142\u0143\58\35\2")
        buf.write(u"\u0143\u0144\5:\36\2\u0144\u0146\3\2\2\2\u0145\u0138")
        buf.write(u"\3\2\2\2\u0145\u013c\3\2\2\2\u0145\u0140\3\2\2\2\u0146")
        buf.write(u"\67\3\2\2\2\u0147\u0148\7C\2\2\u0148\u0149\7\b\2\2\u0149")
        buf.write(u"\u014a\7e\2\2\u014a\u014b\7\t\2\2\u014b\u014c\5\f\7\2")
        buf.write(u"\u014c9\3\2\2\2\u014d\u014e\7D\2\2\u014e\u014f\5\f\7")
        buf.write(u"\2\u014f;\3\2\2\2\u0150\u0151\7K\2\2\u0151\u0152\5n8")
        buf.write(u"\2\u0152=\3\2\2\2\u0153\u0154\7L\2\2\u0154\u0155\7e\2")
        buf.write(u"\2\u0155\u0157\7\b\2\2\u0156\u0158\5@!\2\u0157\u0156")
        buf.write(u"\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write(u"\u015a\7\t\2\2\u015a\u015b\7\n\2\2\u015b\u015c\5B\"\2")
        buf.write(u"\u015c\u015d\7\13\2\2\u015d?\3\2\2\2\u015e\u0163\7e\2")
        buf.write(u"\2\u015f\u0160\7\r\2\2\u0160\u0162\7e\2\2\u0161\u015f")
        buf.write(u"\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163")
        buf.write(u"\u0164\3\2\2\2\u0164A\3\2\2\2\u0165\u0163\3\2\2\2\u0166")
        buf.write(u"\u0168\5\4\3\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2")
        buf.write(u"\2\u0168C\3\2\2\2\u0169\u016b\7\6\2\2\u016a\u016c\5F")
        buf.write(u"$\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016e")
        buf.write(u"\3\2\2\2\u016d\u016f\7\r\2\2\u016e\u016d\3\2\2\2\u016e")
        buf.write(u"\u016f\3\2\2\2\u016f\u0171\3\2\2\2\u0170\u0172\5H%\2")
        buf.write(u"\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173")
        buf.write(u"\3\2\2\2\u0173\u0174\7\7\2\2\u0174E\3\2\2\2\u0175\u0177")
        buf.write(u"\5H%\2\u0176\u0175\3\2\2\2\u0176\u0177\3\2\2\2\u0177")
        buf.write(u"\u0178\3\2\2\2\u0178\u0180\5Z.\2\u0179\u017b\7\r\2\2")
        buf.write(u"\u017a\u017c\5H%\2\u017b\u017a\3\2\2\2\u017b\u017c\3")
        buf.write(u"\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f\5Z.\2\u017e\u0179")
        buf.write(u"\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180")
        buf.write(u"\u0181\3\2\2\2\u0181G\3\2\2\2\u0182\u0180\3\2\2\2\u0183")
        buf.write(u"\u0185\7\r\2\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2")
        buf.write(u"\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187I\3\2")
        buf.write(u"\2\2\u0188\u018a\7\n\2\2\u0189\u018b\5L\'\2\u018a\u0189")
        buf.write(u"\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d\3\2\2\2\u018c")
        buf.write(u"\u018e\7\r\2\2\u018d\u018c\3\2\2\2\u018d\u018e\3\2\2")
        buf.write(u"\2\u018e\u018f\3\2\2\2\u018f\u0190\7\13\2\2\u0190K\3")
        buf.write(u"\2\2\2\u0191\u0196\5N(\2\u0192\u0193\7\r\2\2\u0193\u0195")
        buf.write(u"\5N(\2\u0194\u0192\3\2\2\2\u0195\u0198\3\2\2\2\u0196")
        buf.write(u"\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197M\3\2\2\2\u0198")
        buf.write(u"\u0196\3\2\2\2\u0199\u019a\5P)\2\u019a\u019b\7\20\2\2")
        buf.write(u"\u019b\u019c\5Z.\2\u019c\u01ad\3\2\2\2\u019d\u019e\5")
        buf.write(u"j\66\2\u019e\u019f\7\b\2\2\u019f\u01a0\7\t\2\2\u01a0")
        buf.write(u"\u01a1\7\n\2\2\u01a1\u01a2\5B\"\2\u01a2\u01a3\7\13\2")
        buf.write(u"\2\u01a3\u01ad\3\2\2\2\u01a4\u01a5\5l\67\2\u01a5\u01a6")
        buf.write(u"\7\b\2\2\u01a6\u01a7\5R*\2\u01a7\u01a8\7\t\2\2\u01a8")
        buf.write(u"\u01a9\7\n\2\2\u01a9\u01aa\5B\"\2\u01aa\u01ab\7\13\2")
        buf.write(u"\2\u01ab\u01ad\3\2\2\2\u01ac\u0199\3\2\2\2\u01ac\u019d")
        buf.write(u"\3\2\2\2\u01ac\u01a4\3\2\2\2\u01adO\3\2\2\2\u01ae\u01b2")
        buf.write(u"\5b\62\2\u01af\u01b2\7f\2\2\u01b0\u01b2\5`\61\2\u01b1")
        buf.write(u"\u01ae\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2")
        buf.write(u"\2\u01b2Q\3\2\2\2\u01b3\u01b4\7e\2\2\u01b4S\3\2\2\2\u01b5")
        buf.write(u"\u01b7\7\b\2\2\u01b6\u01b8\5V,\2\u01b7\u01b6\3\2\2\2")
        buf.write(u"\u01b7\u01b8\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba")
        buf.write(u"\7\t\2\2\u01baU\3\2\2\2\u01bb\u01c0\5Z.\2\u01bc\u01bd")
        buf.write(u"\7\r\2\2\u01bd\u01bf\5Z.\2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write(u"\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2")
        buf.write(u"\2\u01c1W\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c8\5Z")
        buf.write(u".\2\u01c4\u01c5\7\r\2\2\u01c5\u01c7\5Z.\2\u01c6\u01c4")
        buf.write(u"\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write(u"\u01c9\3\2\2\2\u01c9Y\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb")
        buf.write(u"\u01cc\7e\2\2\u01cc\u01cd\7\21\2\2\u01cd\u01ce\5b\62")
        buf.write(u"\2\u01ce\u01cf\5T+\2\u01cf\u01d9\3\2\2\2\u01d0\u01d1")
        buf.write(u"\7e\2\2\u01d1\u01d9\5T+\2\u01d2\u01d9\7e\2\2\u01d3\u01d9")
        buf.write(u"\5^\60\2\u01d4\u01d5\7\b\2\2\u01d5\u01d6\5X-\2\u01d6")
        buf.write(u"\u01d7\7\t\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01cb\3\2\2")
        buf.write(u"\2\u01d8\u01d0\3\2\2\2\u01d8\u01d2\3\2\2\2\u01d8\u01d3")
        buf.write(u"\3\2\2\2\u01d8\u01d4\3\2\2\2\u01d9[\3\2\2\2\u01da\u01db")
        buf.write(u"\t\2\2\2\u01db]\3\2\2\2\u01dc\u01dd\5`\61\2\u01dd_\3")
        buf.write(u"\2\2\2\u01de\u01df\78\2\2\u01dfa\3\2\2\2\u01e0\u01e3")
        buf.write(u"\7e\2\2\u01e1\u01e3\5d\63\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write(u"\u01e1\3\2\2\2\u01e3c\3\2\2\2\u01e4\u01e8\5f\64\2\u01e5")
        buf.write(u"\u01e8\5h\65\2\u01e6\u01e8\t\3\2\2\u01e7\u01e4\3\2\2")
        buf.write(u"\2\u01e7\u01e5\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8e\3\2")
        buf.write(u"\2\2\u01e9\u01ea\t\4\2\2\u01eag\3\2\2\2\u01eb\u01ec\t")
        buf.write(u"\5\2\2\u01eci\3\2\2\2\u01ed\u01ee\6\66\3\2\u01ee\u01ef")
        buf.write(u"\7e\2\2\u01efk\3\2\2\2\u01f0\u01f1\6\67\4\2\u01f1\u01f2")
        buf.write(u"\7e\2\2\u01f2m\3\2\2\2\u01f3\u01f7\7\f\2\2\u01f4\u01f7")
        buf.write(u"\7\2\2\3\u01f5\u01f7\68\5\2\u01f6\u01f3\3\2\2\2\u01f6")
        buf.write(u"\u01f4\3\2\2\2\u01f6\u01f5\3\2\2\2\u01f7o\3\2\2\2\u01f8")
        buf.write(u"\u01f9\7\2\2\3\u01f9q\3\2\2\2\60sz\u0084\u008c\u0093")
        buf.write(u"\u009e\u00a3\u00b5\u00c8\u00cc\u00d0\u00da\u00de\u00f4")
        buf.write(u"\u00f8\u00fe\u0104\u0116\u011a\u011c\u0123\u0129\u012e")
        buf.write(u"\u0145\u0157\u0163\u0167\u016b\u016e\u0171\u0176\u017b")
        buf.write(u"\u0180\u0186\u018a\u018d\u0196\u01ac\u01b1\u01b7\u01c0")
        buf.write(u"\u01c8\u01d8\u01e2\u01e7\u01f6")
        return buf.getvalue()


class ECMAScriptParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'mcu_sleep'", u"<INVALID>", u"<INVALID>", 
                     u"'['", u"']'", u"'('", u"')'", u"'{'", u"'}'", u"';'", 
                     u"','", u"'='", u"'?'", u"':'", u"'.'", u"'++'", u"'--'", 
                     u"'+'", u"'-'", u"'~'", u"'!'", u"'*'", u"'/'", u"'%'", 
                     u"'>>'", u"'<<'", u"'>>>'", u"'<'", u"'>'", u"'<='", 
                     u"'>='", u"'=='", u"'!='", u"'==='", u"'!=='", u"'&'", 
                     u"'^'", u"'|'", u"'&&'", u"'||'", u"'*='", u"'/='", 
                     u"'%='", u"'+='", u"'-='", u"'<<='", u"'>>='", u"'>>>='", 
                     u"'&='", u"'^='", u"'|='", u"'null'", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'break'", 
                     u"'do'", u"'instanceof'", u"'typeof'", u"'case'", u"'else'", 
                     u"'new'", u"'var'", u"'catch'", u"'finally'", u"'return'", 
                     u"'void'", u"'continue'", u"'for'", u"'switch'", u"'while'", 
                     u"'debugger'", u"'function'", u"'this'", u"'with'", 
                     u"'default'", u"'if'", u"'throw'", u"'delete'", u"'in'", 
                     u"'try'", u"'class'", u"'enum'", u"'extends'", u"'super'", 
                     u"'const'", u"'export'", u"'import'", u"'implements'", 
                     u"'let'", u"'private'", u"'public'", u"'interface'", 
                     u"'package'", u"'protected'", u"'static'", u"'yield'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"RegularExpressionLiteral", 
                      u"LineTerminator", u"OpenBracket", u"CloseBracket", 
                      u"OpenParen", u"CloseParen", u"OpenBrace", u"CloseBrace", 
                      u"SemiColon", u"Comma", u"Assign", u"QuestionMark", 
                      u"Colon", u"Dot", u"PlusPlus", u"MinusMinus", u"Plus", 
                      u"Minus", u"BitNot", u"Not", u"Multiply", u"Divide", 
                      u"Modulus", u"RightShiftArithmetic", u"LeftShiftArithmetic", 
                      u"RightShiftLogical", u"LessThan", u"MoreThan", u"LessThanEquals", 
                      u"GreaterThanEquals", u"Equals", u"NotEquals", u"IdentityEquals", 
                      u"IdentityNotEquals", u"BitAnd", u"BitXOr", u"BitOr", 
                      u"And", u"Or", u"MultiplyAssign", u"DivideAssign", 
                      u"ModulusAssign", u"PlusAssign", u"MinusAssign", u"LeftShiftArithmeticAssign", 
                      u"RightShiftArithmeticAssign", u"RightShiftLogicalAssign", 
                      u"BitAndAssign", u"BitXorAssign", u"BitOrAssign", 
                      u"NullLiteral", u"BooleanLiteral", u"DecimalLiteral", 
                      u"HexIntegerLiteral", u"OctalIntegerLiteral", u"Break", 
                      u"Do", u"Instanceof", u"Typeof", u"Case", u"Else", 
                      u"New", u"Var", u"Catch", u"Finally", u"Return", u"Void", 
                      u"Continue", u"For", u"Switch", u"While", u"Debugger", 
                      u"Function", u"This", u"With", u"Default", u"If", 
                      u"Throw", u"Delete", u"In", u"Try", u"Class", u"Enum", 
                      u"Extends", u"Super", u"Const", u"Export", u"Import", 
                      u"Implements", u"Let", u"Private", u"Public", u"Interface", 
                      u"Package", u"Protected", u"Static", u"Yield", u"Identifier", 
                      u"StringLiteral", u"WhiteSpaces", u"MultiLineComment", 
                      u"SingleLineComment", u"UnexpectedCharacter" ]

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
    RULE_continueStatement = 15
    RULE_breakStatement = 16
    RULE_returnStatement = 17
    RULE_withStatement = 18
    RULE_switchStatement = 19
    RULE_caseBlock = 20
    RULE_caseClauses = 21
    RULE_caseClause = 22
    RULE_defaultClause = 23
    RULE_labelledStatement = 24
    RULE_throwStatement = 25
    RULE_tryStatement = 26
    RULE_catchProduction = 27
    RULE_finallyProduction = 28
    RULE_debuggerStatement = 29
    RULE_functionDeclaration = 30
    RULE_formalParameterList = 31
    RULE_functionBody = 32
    RULE_arrayLiteral = 33
    RULE_elementList = 34
    RULE_elision = 35
    RULE_objectLiteral = 36
    RULE_propertyNameAndValueList = 37
    RULE_propertyAssignment = 38
    RULE_propertyName = 39
    RULE_propertySetParameterList = 40
    RULE_arguments = 41
    RULE_argumentList = 42
    RULE_expressionSequence = 43
    RULE_singleExpression = 44
    RULE_assignmentOperator = 45
    RULE_literal = 46
    RULE_numericLiteral = 47
    RULE_identifierName = 48
    RULE_reservedWord = 49
    RULE_keyword = 50
    RULE_futureReservedWord = 51
    RULE_getter = 52
    RULE_setter = 53
    RULE_eos = 54
    RULE_eof = 55

    ruleNames =  [ u"program", u"sourceElements", u"sourceElement", u"statement", 
                   u"mcuSleepStatement", u"block", u"statementList", u"variableStatement", 
                   u"variableDeclarationList", u"variableDeclaration", u"initialiser", 
                   u"emptyStatement", u"expressionStatement", u"ifStatement", 
                   u"iterationStatement", u"continueStatement", u"breakStatement", 
                   u"returnStatement", u"withStatement", u"switchStatement", 
                   u"caseBlock", u"caseClauses", u"caseClause", u"defaultClause", 
                   u"labelledStatement", u"throwStatement", u"tryStatement", 
                   u"catchProduction", u"finallyProduction", u"debuggerStatement", 
                   u"functionDeclaration", u"formalParameterList", u"functionBody", 
                   u"arrayLiteral", u"elementList", u"elision", u"objectLiteral", 
                   u"propertyNameAndValueList", u"propertyAssignment", u"propertyName", 
                   u"propertySetParameterList", u"arguments", u"argumentList", 
                   u"expressionSequence", u"singleExpression", u"assignmentOperator", 
                   u"literal", u"numericLiteral", u"identifierName", u"reservedWord", 
                   u"keyword", u"futureReservedWord", u"getter", u"setter", 
                   u"eos", u"eof" ]

    EOF = Token.EOF
    T__0=1
    RegularExpressionLiteral=2
    LineTerminator=3
    OpenBracket=4
    CloseBracket=5
    OpenParen=6
    CloseParen=7
    OpenBrace=8
    CloseBrace=9
    SemiColon=10
    Comma=11
    Assign=12
    QuestionMark=13
    Colon=14
    Dot=15
    PlusPlus=16
    MinusMinus=17
    Plus=18
    Minus=19
    BitNot=20
    Not=21
    Multiply=22
    Divide=23
    Modulus=24
    RightShiftArithmetic=25
    LeftShiftArithmetic=26
    RightShiftLogical=27
    LessThan=28
    MoreThan=29
    LessThanEquals=30
    GreaterThanEquals=31
    Equals=32
    NotEquals=33
    IdentityEquals=34
    IdentityNotEquals=35
    BitAnd=36
    BitXOr=37
    BitOr=38
    And=39
    Or=40
    MultiplyAssign=41
    DivideAssign=42
    ModulusAssign=43
    PlusAssign=44
    MinusAssign=45
    LeftShiftArithmeticAssign=46
    RightShiftArithmeticAssign=47
    RightShiftLogicalAssign=48
    BitAndAssign=49
    BitXorAssign=50
    BitOrAssign=51
    NullLiteral=52
    BooleanLiteral=53
    DecimalLiteral=54
    HexIntegerLiteral=55
    OctalIntegerLiteral=56
    Break=57
    Do=58
    Instanceof=59
    Typeof=60
    Case=61
    Else=62
    New=63
    Var=64
    Catch=65
    Finally=66
    Return=67
    Void=68
    Continue=69
    For=70
    Switch=71
    While=72
    Debugger=73
    Function=74
    This=75
    With=76
    Default=77
    If=78
    Throw=79
    Delete=80
    In=81
    Try=82
    Class=83
    Enum=84
    Extends=85
    Super=86
    Const=87
    Export=88
    Import=89
    Implements=90
    Let=91
    Private=92
    Public=93
    Interface=94
    Package=95
    Protected=96
    Static=97
    Yield=98
    Identifier=99
    StringLiteral=100
    WhiteSpaces=101
    MultiLineComment=102
    SingleLineComment=103
    UnexpectedCharacter=104

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
            self.state = 113
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 112
                self.sourceElements()


            self.state = 115
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
            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self.sourceElement()
                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0)):
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
            self.state = 122
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


        def ifStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.IfStatementContext,0)


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
            self.state = 130
            token = self._input.LA(1)
            if token in [ECMAScriptParser.OpenBrace]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.block()

            elif token in [ECMAScriptParser.Var]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.variableStatement()

            elif token in [ECMAScriptParser.SemiColon]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.emptyStatement()

            elif token in [ECMAScriptParser.If]:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.ifStatement()

            elif token in [ECMAScriptParser.Return]:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.returnStatement()

            elif token in [ECMAScriptParser.T__0]:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
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
            self.state = 132
            self.match(ECMAScriptParser.T__0)
            self.state = 133
            self.arguments()
            self.state = 134
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
            self.state = 136
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 138
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 137
                self.statementList()


            self.state = 140
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
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self.statement()
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0)):
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
            self.state = 147
            self.match(ECMAScriptParser.Var)
            self.state = 148
            self.variableDeclarationList()
            self.state = 149
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.variableDeclaration()
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 152
                    self.match(ECMAScriptParser.Comma)
                    self.state = 153
                    self.variableDeclaration() 
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ECMAScriptParser.Identifier)
            self.state = 161
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 160
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
            self.state = 163
            self.match(ECMAScriptParser.Assign)
            self.state = 164
            self.singleExpression()
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
            self.state = 166
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

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


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
            self.state = 168
            if not (self._input.LA(1) != self.OpenBrace) and (self._input.LA(1) != self.Function):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "(self._input.LA(1) != self.OpenBrace) and (self._input.LA(1) != self.Function)")
            self.state = 169
            self.expressionSequence()
            self.state = 170
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

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


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
            self.state = 172
            self.match(ECMAScriptParser.If)
            self.state = 173
            self.match(ECMAScriptParser.OpenParen)
            self.state = 174
            self.expressionSequence()
            self.state = 175
            self.match(ECMAScriptParser.CloseParen)
            self.state = 176
            self.statement()
            self.state = 179
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 177
                self.match(ECMAScriptParser.Else)
                self.state = 178
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
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

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
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

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

        def expressionSequence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,i)


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
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

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
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

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

        def expressionSequence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,i)


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
            self.state = 242
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(ECMAScriptParser.Do)
                self.state = 182
                self.statement()
                self.state = 183
                self.match(ECMAScriptParser.While)
                self.state = 184
                self.match(ECMAScriptParser.OpenParen)
                self.state = 185
                self.expressionSequence()
                self.state = 186
                self.match(ECMAScriptParser.CloseParen)
                self.state = 187
                self.eos()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(ECMAScriptParser.While)
                self.state = 190
                self.match(ECMAScriptParser.OpenParen)
                self.state = 191
                self.expressionSequence()
                self.state = 192
                self.match(ECMAScriptParser.CloseParen)
                self.state = 193
                self.statement()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.match(ECMAScriptParser.For)
                self.state = 196
                self.match(ECMAScriptParser.OpenParen)
                self.state = 198
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 197
                    self.expressionSequence()


                self.state = 200
                self.match(ECMAScriptParser.SemiColon)
                self.state = 202
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 201
                    self.expressionSequence()


                self.state = 204
                self.match(ECMAScriptParser.SemiColon)
                self.state = 206
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 205
                    self.expressionSequence()


                self.state = 208
                self.match(ECMAScriptParser.CloseParen)
                self.state = 209
                self.statement()
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.match(ECMAScriptParser.For)
                self.state = 211
                self.match(ECMAScriptParser.OpenParen)
                self.state = 212
                self.match(ECMAScriptParser.Var)
                self.state = 213
                self.variableDeclarationList()
                self.state = 214
                self.match(ECMAScriptParser.SemiColon)
                self.state = 216
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 215
                    self.expressionSequence()


                self.state = 218
                self.match(ECMAScriptParser.SemiColon)
                self.state = 220
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 219
                    self.expressionSequence()


                self.state = 222
                self.match(ECMAScriptParser.CloseParen)
                self.state = 223
                self.statement()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 225
                self.match(ECMAScriptParser.For)
                self.state = 226
                self.match(ECMAScriptParser.OpenParen)
                self.state = 227
                self.singleExpression()
                self.state = 228
                self.match(ECMAScriptParser.In)
                self.state = 229
                self.expressionSequence()
                self.state = 230
                self.match(ECMAScriptParser.CloseParen)
                self.state = 231
                self.statement()
                pass

            elif la_ == 6:
                localctx = ECMAScriptParser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 233
                self.match(ECMAScriptParser.For)
                self.state = 234
                self.match(ECMAScriptParser.OpenParen)
                self.state = 235
                self.match(ECMAScriptParser.Var)
                self.state = 236
                self.variableDeclaration()
                self.state = 237
                self.match(ECMAScriptParser.In)
                self.state = 238
                self.expressionSequence()
                self.state = 239
                self.match(ECMAScriptParser.CloseParen)
                self.state = 240
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContinueStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ContinueStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(ECMAScriptParser.Continue, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_continueStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitContinueStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = ECMAScriptParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(ECMAScriptParser.Continue)
            self.state = 246
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 245
                self.match(ECMAScriptParser.Identifier)


            self.state = 248
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.BreakStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(ECMAScriptParser.Break, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_breakStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBreakStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = ECMAScriptParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(ECMAScriptParser.Break)
            self.state = 252
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 251
                self.match(ECMAScriptParser.Identifier)


            self.state = 254
            self.eos()
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


        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


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
        self.enterRule(localctx, 34, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ECMAScriptParser.Return)
            self.state = 258
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 257
                self.expressionSequence()


            self.state = 260
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.WithStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def With(self):
            return self.getToken(ECMAScriptParser.With, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_withStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterWithStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitWithStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitWithStatement(self)
            else:
                return visitor.visitChildren(self)




    def withStatement(self):

        localctx = ECMAScriptParser.WithStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_withStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(ECMAScriptParser.With)
            self.state = 263
            self.match(ECMAScriptParser.OpenParen)
            self.state = 264
            self.expressionSequence()
            self.state = 265
            self.match(ECMAScriptParser.CloseParen)
            self.state = 266
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SwitchStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.SwitchStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Switch(self):
            return self.getToken(ECMAScriptParser.Switch, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def caseBlock(self):
            return self.getTypedRuleContext(ECMAScriptParser.CaseBlockContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_switchStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = ECMAScriptParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(ECMAScriptParser.Switch)
            self.state = 269
            self.match(ECMAScriptParser.OpenParen)
            self.state = 270
            self.expressionSequence()
            self.state = 271
            self.match(ECMAScriptParser.CloseParen)
            self.state = 272
            self.caseBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.CaseBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def caseClauses(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.CaseClausesContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.CaseClausesContext,i)


        def defaultClause(self):
            return self.getTypedRuleContext(ECMAScriptParser.DefaultClauseContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_caseBlock

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCaseBlock(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitCaseBlock(self)
            else:
                return visitor.visitChildren(self)




    def caseBlock(self):

        localctx = ECMAScriptParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 276
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Case:
                self.state = 275
                self.caseClauses()


            self.state = 282
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Default:
                self.state = 278
                self.defaultClause()
                self.state = 280
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.Case:
                    self.state = 279
                    self.caseClauses()




            self.state = 284
            self.match(ECMAScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseClausesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.CaseClausesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def caseClause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.CaseClauseContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_caseClauses

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCaseClauses(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCaseClauses(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitCaseClauses(self)
            else:
                return visitor.visitChildren(self)




    def caseClauses(self):

        localctx = ECMAScriptParser.CaseClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_caseClauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 286
                self.caseClause()
                self.state = 289 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.Case):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.CaseClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Case(self):
            return self.getToken(ECMAScriptParser.Case, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def statementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_caseClause

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCaseClause(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCaseClause(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def caseClause(self):

        localctx = ECMAScriptParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(ECMAScriptParser.Case)
            self.state = 292
            self.expressionSequence()
            self.state = 293
            self.match(ECMAScriptParser.Colon)
            self.state = 295
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 294
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefaultClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.DefaultClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Default(self):
            return self.getToken(ECMAScriptParser.Default, 0)

        def statementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_defaultClause

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDefaultClause(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDefaultClause(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitDefaultClause(self)
            else:
                return visitor.visitChildren(self)




    def defaultClause(self):

        localctx = ECMAScriptParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(ECMAScriptParser.Default)
            self.state = 298
            self.match(ECMAScriptParser.Colon)
            self.state = 300
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 299
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelledStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.LabelledStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_labelledStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLabelledStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLabelledStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitLabelledStatement(self)
            else:
                return visitor.visitChildren(self)




    def labelledStatement(self):

        localctx = ECMAScriptParser.LabelledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_labelledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(ECMAScriptParser.Identifier)
            self.state = 303
            self.match(ECMAScriptParser.Colon)
            self.state = 304
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ThrowStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ThrowStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Throw(self):
            return self.getToken(ECMAScriptParser.Throw, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_throwStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitThrowStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitThrowStatement(self)
            else:
                return visitor.visitChildren(self)




    def throwStatement(self):

        localctx = ECMAScriptParser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(ECMAScriptParser.Throw)
            self.state = 307
            self.expressionSequence()
            self.state = 308
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TryStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.TryStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Try(self):
            return self.getToken(ECMAScriptParser.Try, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def catchProduction(self):
            return self.getTypedRuleContext(ECMAScriptParser.CatchProductionContext,0)


        def finallyProduction(self):
            return self.getTypedRuleContext(ECMAScriptParser.FinallyProductionContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_tryStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitTryStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitTryStatement(self)
            else:
                return visitor.visitChildren(self)




    def tryStatement(self):

        localctx = ECMAScriptParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_tryStatement)
        try:
            self.state = 323
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(ECMAScriptParser.Try)
                self.state = 311
                self.block()
                self.state = 312
                self.catchProduction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.match(ECMAScriptParser.Try)
                self.state = 315
                self.block()
                self.state = 316
                self.finallyProduction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.match(ECMAScriptParser.Try)
                self.state = 319
                self.block()
                self.state = 320
                self.catchProduction()
                self.state = 321
                self.finallyProduction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CatchProductionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.CatchProductionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(ECMAScriptParser.Catch, 0)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_catchProduction

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCatchProduction(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCatchProduction(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitCatchProduction(self)
            else:
                return visitor.visitChildren(self)




    def catchProduction(self):

        localctx = ECMAScriptParser.CatchProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_catchProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(ECMAScriptParser.Catch)
            self.state = 326
            self.match(ECMAScriptParser.OpenParen)
            self.state = 327
            self.match(ECMAScriptParser.Identifier)
            self.state = 328
            self.match(ECMAScriptParser.CloseParen)
            self.state = 329
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FinallyProductionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.FinallyProductionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Finally(self):
            return self.getToken(ECMAScriptParser.Finally, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_finallyProduction

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFinallyProduction(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFinallyProduction(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFinallyProduction(self)
            else:
                return visitor.visitChildren(self)




    def finallyProduction(self):

        localctx = ECMAScriptParser.FinallyProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_finallyProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ECMAScriptParser.Finally)
            self.state = 332
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DebuggerStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.DebuggerStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Debugger(self):
            return self.getToken(ECMAScriptParser.Debugger, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_debuggerStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDebuggerStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDebuggerStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitDebuggerStatement(self)
            else:
                return visitor.visitChildren(self)




    def debuggerStatement(self):

        localctx = ECMAScriptParser.DebuggerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_debuggerStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(ECMAScriptParser.Debugger)
            self.state = 335
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
        self.enterRule(localctx, 60, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(ECMAScriptParser.Function)
            self.state = 338
            self.match(ECMAScriptParser.Identifier)
            self.state = 339
            self.match(ECMAScriptParser.OpenParen)
            self.state = 341
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Identifier:
                self.state = 340
                self.formalParameterList()


            self.state = 343
            self.match(ECMAScriptParser.CloseParen)
            self.state = 344
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 345
            self.functionBody()
            self.state = 346
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
        self.enterRule(localctx, 62, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(ECMAScriptParser.Identifier)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 349
                self.match(ECMAScriptParser.Comma)
                self.state = 350
                self.match(ECMAScriptParser.Identifier)
                self.state = 355
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
        self.enterRule(localctx, 64, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 356
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


        def elision(self):
            return self.getTypedRuleContext(ECMAScriptParser.ElisionContext,0)


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
        self.enterRule(localctx, 66, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(ECMAScriptParser.OpenBracket)
            self.state = 361
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 360
                self.elementList()


            self.state = 364
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 363
                self.match(ECMAScriptParser.Comma)


            self.state = 367
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 366
                self.elision()


            self.state = 369
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


        def elision(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ElisionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ElisionContext,i)


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
        self.enterRule(localctx, 68, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 371
                self.elision()


            self.state = 374
            self.singleExpression()
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 375
                    self.match(ECMAScriptParser.Comma)
                    self.state = 377
                    _la = self._input.LA(1)
                    if _la==ECMAScriptParser.Comma:
                        self.state = 376
                        self.elision()


                    self.state = 379
                    self.singleExpression() 
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElisionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ElisionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_elision

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterElision(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitElision(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitElision(self)
            else:
                return visitor.visitChildren(self)




    def elision(self):

        localctx = ECMAScriptParser.ElisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 385
                self.match(ECMAScriptParser.Comma)
                self.state = 388 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.Comma):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ObjectLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyNameAndValueList(self):
            return self.getTypedRuleContext(ECMAScriptParser.PropertyNameAndValueListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_objectLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterObjectLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitObjectLiteral(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitObjectLiteral(self)
            else:
                return visitor.visitChildren(self)




    def objectLiteral(self):

        localctx = ECMAScriptParser.ObjectLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 392
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 391
                self.propertyNameAndValueList()


            self.state = 395
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 394
                self.match(ECMAScriptParser.Comma)


            self.state = 397
            self.match(ECMAScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyNameAndValueListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.PropertyNameAndValueListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyAssignment(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.PropertyAssignmentContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.PropertyAssignmentContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertyNameAndValueList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyNameAndValueList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyNameAndValueList(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertyNameAndValueList(self)
            else:
                return visitor.visitChildren(self)




    def propertyNameAndValueList(self):

        localctx = ECMAScriptParser.PropertyNameAndValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_propertyNameAndValueList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.propertyAssignment()
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 400
                    self.match(ECMAScriptParser.Comma)
                    self.state = 401
                    self.propertyAssignment() 
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.PropertyAssignmentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertyAssignment

     
        def copyFrom(self, ctx):
            super(ECMAScriptParser.PropertyAssignmentContext, self).copyFrom(ctx)



    class PropertyGetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.PropertyAssignmentContext)
            super(ECMAScriptParser.PropertyGetterContext, self).__init__(parser)
            self.copyFrom(ctx)

        def getter(self):
            return self.getTypedRuleContext(ECMAScriptParser.GetterContext,0)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyGetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyGetter(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertyGetter(self)
            else:
                return visitor.visitChildren(self)


    class PropertyExpressionAssignmentContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.PropertyAssignmentContext)
            super(ECMAScriptParser.PropertyExpressionAssignmentContext, self).__init__(parser)
            self.copyFrom(ctx)

        def propertyName(self):
            return self.getTypedRuleContext(ECMAScriptParser.PropertyNameContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyExpressionAssignment(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyExpressionAssignment(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertyExpressionAssignment(self)
            else:
                return visitor.visitChildren(self)


    class PropertySetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.PropertyAssignmentContext)
            super(ECMAScriptParser.PropertySetterContext, self).__init__(parser)
            self.copyFrom(ctx)

        def setter(self):
            return self.getTypedRuleContext(ECMAScriptParser.SetterContext,0)

        def propertySetParameterList(self):
            return self.getTypedRuleContext(ECMAScriptParser.PropertySetParameterListContext,0)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertySetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertySetter(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertySetter(self)
            else:
                return visitor.visitChildren(self)



    def propertyAssignment(self):

        localctx = ECMAScriptParser.PropertyAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_propertyAssignment)
        try:
            self.state = 426
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.propertyName()
                self.state = 408
                self.match(ECMAScriptParser.Colon)
                self.state = 409
                self.singleExpression()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.getter()
                self.state = 412
                self.match(ECMAScriptParser.OpenParen)
                self.state = 413
                self.match(ECMAScriptParser.CloseParen)
                self.state = 414
                self.match(ECMAScriptParser.OpenBrace)
                self.state = 415
                self.functionBody()
                self.state = 416
                self.match(ECMAScriptParser.CloseBrace)
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 418
                self.setter()
                self.state = 419
                self.match(ECMAScriptParser.OpenParen)
                self.state = 420
                self.propertySetParameterList()
                self.state = 421
                self.match(ECMAScriptParser.CloseParen)
                self.state = 422
                self.match(ECMAScriptParser.OpenBrace)
                self.state = 423
                self.functionBody()
                self.state = 424
                self.match(ECMAScriptParser.CloseBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.PropertyNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)


        def StringLiteral(self):
            return self.getToken(ECMAScriptParser.StringLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertyName

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyName(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyName(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertyName(self)
            else:
                return visitor.visitChildren(self)




    def propertyName(self):

        localctx = ECMAScriptParser.PropertyNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_propertyName)
        try:
            self.state = 431
            token = self._input.LA(1)
            if token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral, ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try, ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield, ECMAScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.identifierName()

            elif token in [ECMAScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.match(ECMAScriptParser.StringLiteral)

            elif token in [ECMAScriptParser.DecimalLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 430
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

    class PropertySetParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.PropertySetParameterListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertySetParameterList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertySetParameterList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertySetParameterList(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertySetParameterList(self)
            else:
                return visitor.visitChildren(self)




    def propertySetParameterList(self):

        localctx = ECMAScriptParser.PropertySetParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_propertySetParameterList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(ECMAScriptParser.Identifier)
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
        self.enterRule(localctx, 82, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(ECMAScriptParser.OpenParen)
            self.state = 437
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                self.state = 436
                self.argumentList()


            self.state = 439
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
        self.enterRule(localctx, 84, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.singleExpression()
            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 442
                self.match(ECMAScriptParser.Comma)
                self.state = 443
                self.singleExpression()
                self.state = 448
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ExpressionSequenceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_expressionSequence

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterExpressionSequence(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitExpressionSequence(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitExpressionSequence(self)
            else:
                return visitor.visitChildren(self)




    def expressionSequence(self):

        localctx = ECMAScriptParser.ExpressionSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expressionSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.singleExpression()
            self.state = 454
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 450
                    self.match(ECMAScriptParser.Comma)
                    self.state = 451
                    self.singleExpression() 
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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


    class ParenthesizedExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.ParenthesizedExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


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


    class MethodExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.MethodExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)
        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)

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



    def singleExpression(self):

        localctx = ECMAScriptParser.SingleExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_singleExpression)
        try:
            self.state = 470
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.MethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(ECMAScriptParser.Identifier)
                self.state = 458
                self.match(ECMAScriptParser.Dot)
                self.state = 459
                self.identifierName()
                self.state = 460
                self.arguments()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.FunctionExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.match(ECMAScriptParser.Identifier)
                self.state = 463
                self.arguments()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.match(ECMAScriptParser.Identifier)
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 465
                self.literal()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.ParenthesizedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 466
                self.match(ECMAScriptParser.OpenParen)
                self.state = 467
                self.expressionSequence()
                self.state = 468
                self.match(ECMAScriptParser.CloseParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 90, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
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
        self.enterRule(localctx, 92, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.numericLiteral()
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
        self.enterRule(localctx, 94, self.RULE_numericLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(ECMAScriptParser.DecimalLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.IdentifierNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def reservedWord(self):
            return self.getTypedRuleContext(ECMAScriptParser.ReservedWordContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_identifierName

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIdentifierName(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIdentifierName(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitIdentifierName(self)
            else:
                return visitor.visitChildren(self)




    def identifierName(self):

        localctx = ECMAScriptParser.IdentifierNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_identifierName)
        try:
            self.state = 480
            token = self._input.LA(1)
            if token in [ECMAScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(ECMAScriptParser.Identifier)

            elif token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral, ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try, ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.reservedWord()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ReservedWordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(ECMAScriptParser.KeywordContext,0)


        def futureReservedWord(self):
            return self.getTypedRuleContext(ECMAScriptParser.FutureReservedWordContext,0)


        def NullLiteral(self):
            return self.getToken(ECMAScriptParser.NullLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(ECMAScriptParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_reservedWord

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterReservedWord(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitReservedWord(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitReservedWord(self)
            else:
                return visitor.visitChildren(self)




    def reservedWord(self):

        localctx = ECMAScriptParser.ReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_reservedWord)
        self._la = 0 # Token type
        try:
            self.state = 485
            token = self._input.LA(1)
            if token in [ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.keyword()

            elif token in [ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.futureReservedWord()

            elif token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
                _la = self._input.LA(1)
                if not(_la==ECMAScriptParser.NullLiteral or _la==ECMAScriptParser.BooleanLiteral):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.KeywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(ECMAScriptParser.Break, 0)

        def Do(self):
            return self.getToken(ECMAScriptParser.Do, 0)

        def Instanceof(self):
            return self.getToken(ECMAScriptParser.Instanceof, 0)

        def Typeof(self):
            return self.getToken(ECMAScriptParser.Typeof, 0)

        def Case(self):
            return self.getToken(ECMAScriptParser.Case, 0)

        def Else(self):
            return self.getToken(ECMAScriptParser.Else, 0)

        def New(self):
            return self.getToken(ECMAScriptParser.New, 0)

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def Catch(self):
            return self.getToken(ECMAScriptParser.Catch, 0)

        def Finally(self):
            return self.getToken(ECMAScriptParser.Finally, 0)

        def Return(self):
            return self.getToken(ECMAScriptParser.Return, 0)

        def Void(self):
            return self.getToken(ECMAScriptParser.Void, 0)

        def Continue(self):
            return self.getToken(ECMAScriptParser.Continue, 0)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)

        def Switch(self):
            return self.getToken(ECMAScriptParser.Switch, 0)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)

        def Debugger(self):
            return self.getToken(ECMAScriptParser.Debugger, 0)

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def This(self):
            return self.getToken(ECMAScriptParser.This, 0)

        def With(self):
            return self.getToken(ECMAScriptParser.With, 0)

        def Default(self):
            return self.getToken(ECMAScriptParser.Default, 0)

        def If(self):
            return self.getToken(ECMAScriptParser.If, 0)

        def Throw(self):
            return self.getToken(ECMAScriptParser.Throw, 0)

        def Delete(self):
            return self.getToken(ECMAScriptParser.Delete, 0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)

        def Try(self):
            return self.getToken(ECMAScriptParser.Try, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_keyword

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterKeyword(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitKeyword(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)




    def keyword(self):

        localctx = ECMAScriptParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            _la = self._input.LA(1)
            if not(((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & ((1 << (ECMAScriptParser.Break - 57)) | (1 << (ECMAScriptParser.Do - 57)) | (1 << (ECMAScriptParser.Instanceof - 57)) | (1 << (ECMAScriptParser.Typeof - 57)) | (1 << (ECMAScriptParser.Case - 57)) | (1 << (ECMAScriptParser.Else - 57)) | (1 << (ECMAScriptParser.New - 57)) | (1 << (ECMAScriptParser.Var - 57)) | (1 << (ECMAScriptParser.Catch - 57)) | (1 << (ECMAScriptParser.Finally - 57)) | (1 << (ECMAScriptParser.Return - 57)) | (1 << (ECMAScriptParser.Void - 57)) | (1 << (ECMAScriptParser.Continue - 57)) | (1 << (ECMAScriptParser.For - 57)) | (1 << (ECMAScriptParser.Switch - 57)) | (1 << (ECMAScriptParser.While - 57)) | (1 << (ECMAScriptParser.Debugger - 57)) | (1 << (ECMAScriptParser.Function - 57)) | (1 << (ECMAScriptParser.This - 57)) | (1 << (ECMAScriptParser.With - 57)) | (1 << (ECMAScriptParser.Default - 57)) | (1 << (ECMAScriptParser.If - 57)) | (1 << (ECMAScriptParser.Throw - 57)) | (1 << (ECMAScriptParser.Delete - 57)) | (1 << (ECMAScriptParser.In - 57)) | (1 << (ECMAScriptParser.Try - 57)))) != 0)):
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

    class FutureReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.FutureReservedWordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(ECMAScriptParser.Class, 0)

        def Enum(self):
            return self.getToken(ECMAScriptParser.Enum, 0)

        def Extends(self):
            return self.getToken(ECMAScriptParser.Extends, 0)

        def Super(self):
            return self.getToken(ECMAScriptParser.Super, 0)

        def Const(self):
            return self.getToken(ECMAScriptParser.Const, 0)

        def Export(self):
            return self.getToken(ECMAScriptParser.Export, 0)

        def Import(self):
            return self.getToken(ECMAScriptParser.Import, 0)

        def Implements(self):
            return self.getToken(ECMAScriptParser.Implements, 0)

        def Let(self):
            return self.getToken(ECMAScriptParser.Let, 0)

        def Private(self):
            return self.getToken(ECMAScriptParser.Private, 0)

        def Public(self):
            return self.getToken(ECMAScriptParser.Public, 0)

        def Interface(self):
            return self.getToken(ECMAScriptParser.Interface, 0)

        def Package(self):
            return self.getToken(ECMAScriptParser.Package, 0)

        def Protected(self):
            return self.getToken(ECMAScriptParser.Protected, 0)

        def Static(self):
            return self.getToken(ECMAScriptParser.Static, 0)

        def Yield(self):
            return self.getToken(ECMAScriptParser.Yield, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_futureReservedWord

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFutureReservedWord(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFutureReservedWord(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFutureReservedWord(self)
            else:
                return visitor.visitChildren(self)




    def futureReservedWord(self):

        localctx = ECMAScriptParser.FutureReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_futureReservedWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            _la = self._input.LA(1)
            if not(((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (ECMAScriptParser.Class - 83)) | (1 << (ECMAScriptParser.Enum - 83)) | (1 << (ECMAScriptParser.Extends - 83)) | (1 << (ECMAScriptParser.Super - 83)) | (1 << (ECMAScriptParser.Const - 83)) | (1 << (ECMAScriptParser.Export - 83)) | (1 << (ECMAScriptParser.Import - 83)) | (1 << (ECMAScriptParser.Implements - 83)) | (1 << (ECMAScriptParser.Let - 83)) | (1 << (ECMAScriptParser.Private - 83)) | (1 << (ECMAScriptParser.Public - 83)) | (1 << (ECMAScriptParser.Interface - 83)) | (1 << (ECMAScriptParser.Package - 83)) | (1 << (ECMAScriptParser.Protected - 83)) | (1 << (ECMAScriptParser.Static - 83)) | (1 << (ECMAScriptParser.Yield - 83)))) != 0)):
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

    class GetterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.GetterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_getter

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterGetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitGetter(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitGetter(self)
            else:
                return visitor.visitChildren(self)




    def getter(self):

        localctx = ECMAScriptParser.GetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_getter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            if not self._input.LT(1).getText().startsWith("get"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._input.LT(1).getText().startsWith(\"get\")")
            self.state = 492
            self.match(ECMAScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SetterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.SetterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_setter

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSetter(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitSetter(self)
            else:
                return visitor.visitChildren(self)




    def setter(self):

        localctx = ECMAScriptParser.SetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_setter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            if not self._input.LT(1).getText().startsWith("set"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._input.LT(1).getText().startsWith(\"set\")")
            self.state = 495
            self.match(ECMAScriptParser.Identifier)
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
        self.enterRule(localctx, 108, self.RULE_eos)
        try:
            self.state = 500
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.match(ECMAScriptParser.SemiColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.match(ECMAScriptParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 499
                if not self._input.LT(1).type == self.CloseBrace:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self._input.LT(1).type == self.CloseBrace")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EofContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.EofContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ECMAScriptParser.EOF, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_eof

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEof(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEof(self)

        def accept(self, visitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitEof(self)
            else:
                return visitor.visitChildren(self)




    def eof(self):

        localctx = ECMAScriptParser.EofContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_eof)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(ECMAScriptParser.EOF)
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
        self._predicates[12] = self.expressionStatement_sempred
        self._predicates[52] = self.getter_sempred
        self._predicates[53] = self.setter_sempred
        self._predicates[54] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressionStatement_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return (self._input.LA(1) != self.OpenBrace) and (self._input.LA(1) != self.Function)
         

    def getter_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self._input.LT(1).getText().startsWith("get")
         

    def setter_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self._input.LT(1).getText().startsWith("set")
         

    def eos_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self._input.LT(1).type == self.CloseBrace
         



