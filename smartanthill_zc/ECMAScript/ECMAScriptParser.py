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
        buf.write(u"j\u020c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\3\2\5\2t\n\2\3\2\3\2\3\3\6\3y\n\3\r\3\16\3z\3\4")
        buf.write(u"\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0086\n\5\3\6\3")
        buf.write(u"\6\3\6\3\6\3\7\3\7\5\7\u008e\n\7\3\7\3\7\3\b\6\b\u0093")
        buf.write(u"\n\b\r\b\16\b\u0094\3\t\3\t\3\t\3\t\3\n\3\n\3\n\7\n\u009e")
        buf.write(u"\n\n\f\n\16\n\u00a1\13\n\3\13\3\13\5\13\u00a5\n\13\3")
        buf.write(u"\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\5\17\u00b7\n\17\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00da")
        buf.write(u"\n\20\3\20\3\20\5\20\u00de\n\20\3\20\3\20\5\20\u00e2")
        buf.write(u"\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00ec")
        buf.write(u"\n\20\3\20\3\20\5\20\u00f0\n\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\5\20\u0106\n\20\3\21\3\21\5")
        buf.write(u"\21\u010a\n\21\3\21\3\21\3\22\3\22\5\22\u0110\n\22\3")
        buf.write(u"\22\3\22\3\23\3\23\5\23\u0116\n\23\3\23\3\23\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\26\3\26\5\26\u0128\n\26\3\26\3\26\5\26\u012c\n\26\5")
        buf.write(u"\26\u012e\n\26\3\26\3\26\3\27\6\27\u0133\n\27\r\27\16")
        buf.write(u"\27\u0134\3\30\3\30\3\30\3\30\5\30\u013b\n\30\3\31\3")
        buf.write(u"\31\3\31\5\31\u0140\n\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write(u"\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\5\34\u0157\n\34\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(u" \3 \5 \u0169\n \3 \3 \3 \3 \3 \3!\3!\3!\7!\u0173\n!")
        buf.write(u"\f!\16!\u0176\13!\3\"\5\"\u0179\n\"\3#\3#\5#\u017d\n")
        buf.write(u"#\3#\5#\u0180\n#\3#\5#\u0183\n#\3#\3#\3$\5$\u0188\n$")
        buf.write(u"\3$\3$\3$\5$\u018d\n$\3$\7$\u0190\n$\f$\16$\u0193\13")
        buf.write(u"$\3%\6%\u0196\n%\r%\16%\u0197\3&\3&\5&\u019c\n&\3&\5")
        buf.write(u"&\u019f\n&\3&\3&\3\'\3\'\3\'\7\'\u01a6\n\'\f\'\16\'\u01a9")
        buf.write(u"\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\3(\3(\5(\u01be\n(\3)\3)\3)\5)\u01c3\n)\3*\3*\3+")
        buf.write(u"\3+\5+\u01c9\n+\3+\3+\3,\3,\3,\7,\u01d0\n,\f,\16,\u01d3")
        buf.write(u"\13,\3-\3-\3-\7-\u01d8\n-\f-\16-\u01db\13-\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01ea\n.\3/\3/\3\60\3")
        buf.write(u"\60\3\61\3\61\3\62\3\62\5\62\u01f4\n\62\3\63\3\63\3\63")
        buf.write(u"\5\63\u01f9\n\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3")
        buf.write(u"\67\3\67\3\67\38\38\38\58\u0208\n8\39\39\39\2\2:\2\4")
        buf.write(u"\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write(u"\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\6\3\2+\65\3\2\66")
        buf.write(u"\67\3\2;T\3\2Ud\u0213\2s\3\2\2\2\4x\3\2\2\2\6|\3\2\2")
        buf.write(u"\2\b\u0085\3\2\2\2\n\u0087\3\2\2\2\f\u008b\3\2\2\2\16")
        buf.write(u"\u0092\3\2\2\2\20\u0096\3\2\2\2\22\u009a\3\2\2\2\24\u00a2")
        buf.write(u"\3\2\2\2\26\u00a6\3\2\2\2\30\u00a9\3\2\2\2\32\u00ab\3")
        buf.write(u"\2\2\2\34\u00af\3\2\2\2\36\u0105\3\2\2\2 \u0107\3\2\2")
        buf.write(u"\2\"\u010d\3\2\2\2$\u0113\3\2\2\2&\u0119\3\2\2\2(\u011f")
        buf.write(u"\3\2\2\2*\u0125\3\2\2\2,\u0132\3\2\2\2.\u0136\3\2\2\2")
        buf.write(u"\60\u013c\3\2\2\2\62\u0141\3\2\2\2\64\u0145\3\2\2\2\66")
        buf.write(u"\u0156\3\2\2\28\u0158\3\2\2\2:\u015e\3\2\2\2<\u0161\3")
        buf.write(u"\2\2\2>\u0164\3\2\2\2@\u016f\3\2\2\2B\u0178\3\2\2\2D")
        buf.write(u"\u017a\3\2\2\2F\u0187\3\2\2\2H\u0195\3\2\2\2J\u0199\3")
        buf.write(u"\2\2\2L\u01a2\3\2\2\2N\u01bd\3\2\2\2P\u01c2\3\2\2\2R")
        buf.write(u"\u01c4\3\2\2\2T\u01c6\3\2\2\2V\u01cc\3\2\2\2X\u01d4\3")
        buf.write(u"\2\2\2Z\u01e9\3\2\2\2\\\u01eb\3\2\2\2^\u01ed\3\2\2\2")
        buf.write(u"`\u01ef\3\2\2\2b\u01f3\3\2\2\2d\u01f8\3\2\2\2f\u01fa")
        buf.write(u"\3\2\2\2h\u01fc\3\2\2\2j\u01fe\3\2\2\2l\u0201\3\2\2\2")
        buf.write(u"n\u0207\3\2\2\2p\u0209\3\2\2\2rt\5\4\3\2sr\3\2\2\2st")
        buf.write(u"\3\2\2\2tu\3\2\2\2uv\7\2\2\3v\3\3\2\2\2wy\5\6\4\2xw\3")
        buf.write(u"\2\2\2yz\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\5\3\2\2\2|}\5\b")
        buf.write(u"\5\2}\7\3\2\2\2~\u0086\5\f\7\2\177\u0086\5\20\t\2\u0080")
        buf.write(u"\u0086\5\30\r\2\u0081\u0086\5\34\17\2\u0082\u0086\5\36")
        buf.write(u"\20\2\u0083\u0086\5$\23\2\u0084\u0086\5\n\6\2\u0085~")
        buf.write(u"\3\2\2\2\u0085\177\3\2\2\2\u0085\u0080\3\2\2\2\u0085")
        buf.write(u"\u0081\3\2\2\2\u0085\u0082\3\2\2\2\u0085\u0083\3\2\2")
        buf.write(u"\2\u0085\u0084\3\2\2\2\u0086\t\3\2\2\2\u0087\u0088\7")
        buf.write(u"\3\2\2\u0088\u0089\5T+\2\u0089\u008a\5n8\2\u008a\13\3")
        buf.write(u"\2\2\2\u008b\u008d\7\n\2\2\u008c\u008e\5\16\b\2\u008d")
        buf.write(u"\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2")
        buf.write(u"\2\u008f\u0090\7\13\2\2\u0090\r\3\2\2\2\u0091\u0093\5")
        buf.write(u"\b\5\2\u0092\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write(u"\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\17\3\2\2\2\u0096")
        buf.write(u"\u0097\7B\2\2\u0097\u0098\5\22\n\2\u0098\u0099\5n8\2")
        buf.write(u"\u0099\21\3\2\2\2\u009a\u009f\5\24\13\2\u009b\u009c\7")
        buf.write(u"\r\2\2\u009c\u009e\5\24\13\2\u009d\u009b\3\2\2\2\u009e")
        buf.write(u"\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2")
        buf.write(u"\2\u00a0\23\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a4\7")
        buf.write(u"e\2\2\u00a3\u00a5\5\26\f\2\u00a4\u00a3\3\2\2\2\u00a4")
        buf.write(u"\u00a5\3\2\2\2\u00a5\25\3\2\2\2\u00a6\u00a7\7\16\2\2")
        buf.write(u"\u00a7\u00a8\5Z.\2\u00a8\27\3\2\2\2\u00a9\u00aa\7\f\2")
        buf.write(u"\2\u00aa\31\3\2\2\2\u00ab\u00ac\6\16\2\2\u00ac\u00ad")
        buf.write(u"\5X-\2\u00ad\u00ae\7\f\2\2\u00ae\33\3\2\2\2\u00af\u00b0")
        buf.write(u"\7P\2\2\u00b0\u00b1\7\b\2\2\u00b1\u00b2\5X-\2\u00b2\u00b3")
        buf.write(u"\7\t\2\2\u00b3\u00b6\5\b\5\2\u00b4\u00b5\7@\2\2\u00b5")
        buf.write(u"\u00b7\5\b\5\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2")
        buf.write(u"\2\u00b7\35\3\2\2\2\u00b8\u00b9\7<\2\2\u00b9\u00ba\5")
        buf.write(u"\b\5\2\u00ba\u00bb\7J\2\2\u00bb\u00bc\7\b\2\2\u00bc\u00bd")
        buf.write(u"\5X-\2\u00bd\u00be\7\t\2\2\u00be\u00bf\5n8\2\u00bf\u0106")
        buf.write(u"\3\2\2\2\u00c0\u00c1\7J\2\2\u00c1\u00c2\7\b\2\2\u00c2")
        buf.write(u"\u00c3\5X-\2\u00c3\u00c4\7\t\2\2\u00c4\u00c5\5\b\5\2")
        buf.write(u"\u00c5\u0106\3\2\2\2\u00c6\u00c7\7H\2\2\u00c7\u00c8\7")
        buf.write(u"\b\2\2\u00c8\u00c9\7B\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb")
        buf.write(u"\7\16\2\2\u00cb\u00cc\5X-\2\u00cc\u00cd\7\f\2\2\u00cd")
        buf.write(u"\u00ce\7e\2\2\u00ce\u00cf\7\36\2\2\u00cf\u00d0\5X-\2")
        buf.write(u"\u00d0\u00d1\7\f\2\2\u00d1\u00d2\7e\2\2\u00d2\u00d3\7")
        buf.write(u"\22\2\2\u00d3\u00d4\7\t\2\2\u00d4\u00d5\5\b\5\2\u00d5")
        buf.write(u"\u0106\3\2\2\2\u00d6\u00d7\7H\2\2\u00d7\u00d9\7\b\2\2")
        buf.write(u"\u00d8\u00da\5X-\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3")
        buf.write(u"\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dd\7\f\2\2\u00dc")
        buf.write(u"\u00de\5X-\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write(u"\u00de\u00df\3\2\2\2\u00df\u00e1\7\f\2\2\u00e0\u00e2")
        buf.write(u"\5X-\2\u00e1\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write(u"\u00e3\3\2\2\2\u00e3\u00e4\7\t\2\2\u00e4\u0106\5\b\5")
        buf.write(u"\2\u00e5\u00e6\7H\2\2\u00e6\u00e7\7\b\2\2\u00e7\u00e8")
        buf.write(u"\7B\2\2\u00e8\u00e9\5\22\n\2\u00e9\u00eb\7\f\2\2\u00ea")
        buf.write(u"\u00ec\5X-\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write(u"\u00ec\u00ed\3\2\2\2\u00ed\u00ef\7\f\2\2\u00ee\u00f0")
        buf.write(u"\5X-\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write(u"\u00f1\3\2\2\2\u00f1\u00f2\7\t\2\2\u00f2\u00f3\5\b\5")
        buf.write(u"\2\u00f3\u0106\3\2\2\2\u00f4\u00f5\7H\2\2\u00f5\u00f6")
        buf.write(u"\7\b\2\2\u00f6\u00f7\5Z.\2\u00f7\u00f8\7S\2\2\u00f8\u00f9")
        buf.write(u"\5X-\2\u00f9\u00fa\7\t\2\2\u00fa\u00fb\5\b\5\2\u00fb")
        buf.write(u"\u0106\3\2\2\2\u00fc\u00fd\7H\2\2\u00fd\u00fe\7\b\2\2")
        buf.write(u"\u00fe\u00ff\7B\2\2\u00ff\u0100\5\24\13\2\u0100\u0101")
        buf.write(u"\7S\2\2\u0101\u0102\5X-\2\u0102\u0103\7\t\2\2\u0103\u0104")
        buf.write(u"\5\b\5\2\u0104\u0106\3\2\2\2\u0105\u00b8\3\2\2\2\u0105")
        buf.write(u"\u00c0\3\2\2\2\u0105\u00c6\3\2\2\2\u0105\u00d6\3\2\2")
        buf.write(u"\2\u0105\u00e5\3\2\2\2\u0105\u00f4\3\2\2\2\u0105\u00fc")
        buf.write(u"\3\2\2\2\u0106\37\3\2\2\2\u0107\u0109\7G\2\2\u0108\u010a")
        buf.write(u"\7e\2\2\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write(u"\u010b\3\2\2\2\u010b\u010c\5n8\2\u010c!\3\2\2\2\u010d")
        buf.write(u"\u010f\7;\2\2\u010e\u0110\7e\2\2\u010f\u010e\3\2\2\2")
        buf.write(u"\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112")
        buf.write(u"\5n8\2\u0112#\3\2\2\2\u0113\u0115\7E\2\2\u0114\u0116")
        buf.write(u"\5X-\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write(u"\u0117\3\2\2\2\u0117\u0118\5n8\2\u0118%\3\2\2\2\u0119")
        buf.write(u"\u011a\7N\2\2\u011a\u011b\7\b\2\2\u011b\u011c\5X-\2\u011c")
        buf.write(u"\u011d\7\t\2\2\u011d\u011e\5\b\5\2\u011e\'\3\2\2\2\u011f")
        buf.write(u"\u0120\7I\2\2\u0120\u0121\7\b\2\2\u0121\u0122\5X-\2\u0122")
        buf.write(u"\u0123\7\t\2\2\u0123\u0124\5*\26\2\u0124)\3\2\2\2\u0125")
        buf.write(u"\u0127\7\n\2\2\u0126\u0128\5,\27\2\u0127\u0126\3\2\2")
        buf.write(u"\2\u0127\u0128\3\2\2\2\u0128\u012d\3\2\2\2\u0129\u012b")
        buf.write(u"\5\60\31\2\u012a\u012c\5,\27\2\u012b\u012a\3\2\2\2\u012b")
        buf.write(u"\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u0129\3\2\2")
        buf.write(u"\2\u012d\u012e\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130")
        buf.write(u"\7\13\2\2\u0130+\3\2\2\2\u0131\u0133\5.\30\2\u0132\u0131")
        buf.write(u"\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0132\3\2\2\2\u0134")
        buf.write(u"\u0135\3\2\2\2\u0135-\3\2\2\2\u0136\u0137\7?\2\2\u0137")
        buf.write(u"\u0138\5X-\2\u0138\u013a\7\20\2\2\u0139\u013b\5\16\b")
        buf.write(u"\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b/\3\2")
        buf.write(u"\2\2\u013c\u013d\7O\2\2\u013d\u013f\7\20\2\2\u013e\u0140")
        buf.write(u"\5\16\b\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write(u"\61\3\2\2\2\u0141\u0142\7e\2\2\u0142\u0143\7\20\2\2\u0143")
        buf.write(u"\u0144\5\b\5\2\u0144\63\3\2\2\2\u0145\u0146\7Q\2\2\u0146")
        buf.write(u"\u0147\5X-\2\u0147\u0148\5n8\2\u0148\65\3\2\2\2\u0149")
        buf.write(u"\u014a\7T\2\2\u014a\u014b\5\f\7\2\u014b\u014c\58\35\2")
        buf.write(u"\u014c\u0157\3\2\2\2\u014d\u014e\7T\2\2\u014e\u014f\5")
        buf.write(u"\f\7\2\u014f\u0150\5:\36\2\u0150\u0157\3\2\2\2\u0151")
        buf.write(u"\u0152\7T\2\2\u0152\u0153\5\f\7\2\u0153\u0154\58\35\2")
        buf.write(u"\u0154\u0155\5:\36\2\u0155\u0157\3\2\2\2\u0156\u0149")
        buf.write(u"\3\2\2\2\u0156\u014d\3\2\2\2\u0156\u0151\3\2\2\2\u0157")
        buf.write(u"\67\3\2\2\2\u0158\u0159\7C\2\2\u0159\u015a\7\b\2\2\u015a")
        buf.write(u"\u015b\7e\2\2\u015b\u015c\7\t\2\2\u015c\u015d\5\f\7\2")
        buf.write(u"\u015d9\3\2\2\2\u015e\u015f\7D\2\2\u015f\u0160\5\f\7")
        buf.write(u"\2\u0160;\3\2\2\2\u0161\u0162\7K\2\2\u0162\u0163\5n8")
        buf.write(u"\2\u0163=\3\2\2\2\u0164\u0165\7L\2\2\u0165\u0166\7e\2")
        buf.write(u"\2\u0166\u0168\7\b\2\2\u0167\u0169\5@!\2\u0168\u0167")
        buf.write(u"\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write(u"\u016b\7\t\2\2\u016b\u016c\7\n\2\2\u016c\u016d\5B\"\2")
        buf.write(u"\u016d\u016e\7\13\2\2\u016e?\3\2\2\2\u016f\u0174\7e\2")
        buf.write(u"\2\u0170\u0171\7\r\2\2\u0171\u0173\7e\2\2\u0172\u0170")
        buf.write(u"\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write(u"\u0175\3\2\2\2\u0175A\3\2\2\2\u0176\u0174\3\2\2\2\u0177")
        buf.write(u"\u0179\5\4\3\2\u0178\u0177\3\2\2\2\u0178\u0179\3\2\2")
        buf.write(u"\2\u0179C\3\2\2\2\u017a\u017c\7\6\2\2\u017b\u017d\5F")
        buf.write(u"$\2\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f")
        buf.write(u"\3\2\2\2\u017e\u0180\7\r\2\2\u017f\u017e\3\2\2\2\u017f")
        buf.write(u"\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0183\5H%\2")
        buf.write(u"\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184")
        buf.write(u"\3\2\2\2\u0184\u0185\7\7\2\2\u0185E\3\2\2\2\u0186\u0188")
        buf.write(u"\5H%\2\u0187\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write(u"\u0189\3\2\2\2\u0189\u0191\5Z.\2\u018a\u018c\7\r\2\2")
        buf.write(u"\u018b\u018d\5H%\2\u018c\u018b\3\2\2\2\u018c\u018d\3")
        buf.write(u"\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190\5Z.\2\u018f\u018a")
        buf.write(u"\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write(u"\u0192\3\2\2\2\u0192G\3\2\2\2\u0193\u0191\3\2\2\2\u0194")
        buf.write(u"\u0196\7\r\2\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2")
        buf.write(u"\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198I\3\2")
        buf.write(u"\2\2\u0199\u019b\7\n\2\2\u019a\u019c\5L\'\2\u019b\u019a")
        buf.write(u"\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019e\3\2\2\2\u019d")
        buf.write(u"\u019f\7\r\2\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2\2")
        buf.write(u"\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\7\13\2\2\u01a1K\3")
        buf.write(u"\2\2\2\u01a2\u01a7\5N(\2\u01a3\u01a4\7\r\2\2\u01a4\u01a6")
        buf.write(u"\5N(\2\u01a5\u01a3\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7")
        buf.write(u"\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8M\3\2\2\2\u01a9")
        buf.write(u"\u01a7\3\2\2\2\u01aa\u01ab\5P)\2\u01ab\u01ac\7\20\2\2")
        buf.write(u"\u01ac\u01ad\5Z.\2\u01ad\u01be\3\2\2\2\u01ae\u01af\5")
        buf.write(u"j\66\2\u01af\u01b0\7\b\2\2\u01b0\u01b1\7\t\2\2\u01b1")
        buf.write(u"\u01b2\7\n\2\2\u01b2\u01b3\5B\"\2\u01b3\u01b4\7\13\2")
        buf.write(u"\2\u01b4\u01be\3\2\2\2\u01b5\u01b6\5l\67\2\u01b6\u01b7")
        buf.write(u"\7\b\2\2\u01b7\u01b8\5R*\2\u01b8\u01b9\7\t\2\2\u01b9")
        buf.write(u"\u01ba\7\n\2\2\u01ba\u01bb\5B\"\2\u01bb\u01bc\7\13\2")
        buf.write(u"\2\u01bc\u01be\3\2\2\2\u01bd\u01aa\3\2\2\2\u01bd\u01ae")
        buf.write(u"\3\2\2\2\u01bd\u01b5\3\2\2\2\u01beO\3\2\2\2\u01bf\u01c3")
        buf.write(u"\5b\62\2\u01c0\u01c3\7f\2\2\u01c1\u01c3\5`\61\2\u01c2")
        buf.write(u"\u01bf\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2")
        buf.write(u"\2\u01c3Q\3\2\2\2\u01c4\u01c5\7e\2\2\u01c5S\3\2\2\2\u01c6")
        buf.write(u"\u01c8\7\b\2\2\u01c7\u01c9\5V,\2\u01c8\u01c7\3\2\2\2")
        buf.write(u"\u01c8\u01c9\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb")
        buf.write(u"\7\t\2\2\u01cbU\3\2\2\2\u01cc\u01d1\5Z.\2\u01cd\u01ce")
        buf.write(u"\7\r\2\2\u01ce\u01d0\5Z.\2\u01cf\u01cd\3\2\2\2\u01d0")
        buf.write(u"\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2")
        buf.write(u"\2\u01d2W\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d9\5Z")
        buf.write(u".\2\u01d5\u01d6\7\r\2\2\u01d6\u01d8\5Z.\2\u01d7\u01d5")
        buf.write(u"\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write(u"\u01da\3\2\2\2\u01daY\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc")
        buf.write(u"\u01dd\7e\2\2\u01dd\u01de\7\21\2\2\u01de\u01df\5b\62")
        buf.write(u"\2\u01df\u01e0\5T+\2\u01e0\u01ea\3\2\2\2\u01e1\u01e2")
        buf.write(u"\7e\2\2\u01e2\u01ea\5T+\2\u01e3\u01ea\7e\2\2\u01e4\u01ea")
        buf.write(u"\5^\60\2\u01e5\u01e6\7\b\2\2\u01e6\u01e7\5X-\2\u01e7")
        buf.write(u"\u01e8\7\t\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01dc\3\2\2")
        buf.write(u"\2\u01e9\u01e1\3\2\2\2\u01e9\u01e3\3\2\2\2\u01e9\u01e4")
        buf.write(u"\3\2\2\2\u01e9\u01e5\3\2\2\2\u01ea[\3\2\2\2\u01eb\u01ec")
        buf.write(u"\t\2\2\2\u01ec]\3\2\2\2\u01ed\u01ee\5`\61\2\u01ee_\3")
        buf.write(u"\2\2\2\u01ef\u01f0\78\2\2\u01f0a\3\2\2\2\u01f1\u01f4")
        buf.write(u"\7e\2\2\u01f2\u01f4\5d\63\2\u01f3\u01f1\3\2\2\2\u01f3")
        buf.write(u"\u01f2\3\2\2\2\u01f4c\3\2\2\2\u01f5\u01f9\5f\64\2\u01f6")
        buf.write(u"\u01f9\5h\65\2\u01f7\u01f9\t\3\2\2\u01f8\u01f5\3\2\2")
        buf.write(u"\2\u01f8\u01f6\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9e\3\2")
        buf.write(u"\2\2\u01fa\u01fb\t\4\2\2\u01fbg\3\2\2\2\u01fc\u01fd\t")
        buf.write(u"\5\2\2\u01fdi\3\2\2\2\u01fe\u01ff\6\66\3\2\u01ff\u0200")
        buf.write(u"\7e\2\2\u0200k\3\2\2\2\u0201\u0202\6\67\4\2\u0202\u0203")
        buf.write(u"\7e\2\2\u0203m\3\2\2\2\u0204\u0208\7\f\2\2\u0205\u0208")
        buf.write(u"\7\2\2\3\u0206\u0208\68\5\2\u0207\u0204\3\2\2\2\u0207")
        buf.write(u"\u0205\3\2\2\2\u0207\u0206\3\2\2\2\u0208o\3\2\2\2\u0209")
        buf.write(u"\u020a\7\2\2\3\u020aq\3\2\2\2\60sz\u0085\u008d\u0094")
        buf.write(u"\u009f\u00a4\u00b6\u00d9\u00dd\u00e1\u00eb\u00ef\u0105")
        buf.write(u"\u0109\u010f\u0115\u0127\u012b\u012d\u0134\u013a\u013f")
        buf.write(u"\u0156\u0168\u0174\u0178\u017c\u017f\u0182\u0187\u018c")
        buf.write(u"\u0191\u0197\u019b\u019e\u01a7\u01bd\u01c2\u01c8\u01d1")
        buf.write(u"\u01d9\u01e9\u01f3\u01f8\u0207")
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Do))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 112
                self.sourceElements()


            self.state = 115
            self.match(ECMAScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Do))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self._errHandler.report_error(self, re)
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
            self.state = 131
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

            elif token in [ECMAScriptParser.Do, ECMAScriptParser.For, ECMAScriptParser.While]:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.iterationStatement()

            elif token in [ECMAScriptParser.Return]:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.returnStatement()

            elif token in [ECMAScriptParser.T__0]:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.mcuSleepStatement()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 133
            self.match(ECMAScriptParser.T__0)
            self.state = 134
            self.arguments()
            self.state = 135
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 137
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 139
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Do))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 138
                self.statementList()


            self.state = 141
            self.match(ECMAScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 144 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 143
                self.statement()
                self.state = 146 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Do))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 148
            self.match(ECMAScriptParser.Var)
            self.state = 149
            self.variableDeclarationList()
            self.state = 150
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 152
            self.variableDeclaration()
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 153
                    self.match(ECMAScriptParser.Comma)
                    self.state = 154
                    self.variableDeclaration() 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 160
            self.match(ECMAScriptParser.Identifier)
            self.state = 162
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 161
                self.initialiser()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 164
            self.match(ECMAScriptParser.Assign)
            self.state = 165
            self.singleExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 167
            self.match(ECMAScriptParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 169
            if not (self._input.LA(1) != self.OpenBrace) and (self._input.LA(1) != self.Function):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "(self._input.LA(1) != self.OpenBrace) and (self._input.LA(1) != self.Function)")
            self.state = 170
            self.expressionSequence()
            self.state = 171
            self.match(ECMAScriptParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 173
            self.match(ECMAScriptParser.If)
            self.state = 174
            self.match(ECMAScriptParser.OpenParen)
            self.state = 175
            self.expressionSequence()
            self.state = 176
            self.match(ECMAScriptParser.CloseParen)
            self.state = 177
            self.statement()
            self.state = 180
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 178
                self.match(ECMAScriptParser.Else)
                self.state = 179
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
        def expressionSequence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,i)

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
            self.state = 259
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(ECMAScriptParser.Do)
                self.state = 183
                self.statement()
                self.state = 184
                self.match(ECMAScriptParser.While)
                self.state = 185
                self.match(ECMAScriptParser.OpenParen)
                self.state = 186
                self.expressionSequence()
                self.state = 187
                self.match(ECMAScriptParser.CloseParen)
                self.state = 188
                self.eos()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(ECMAScriptParser.While)
                self.state = 191
                self.match(ECMAScriptParser.OpenParen)
                self.state = 192
                self.expressionSequence()
                self.state = 193
                self.match(ECMAScriptParser.CloseParen)
                self.state = 194
                self.statement()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.SimpleForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.match(ECMAScriptParser.For)
                self.state = 197
                self.match(ECMAScriptParser.OpenParen)
                self.state = 198
                self.match(ECMAScriptParser.Var)
                self.state = 199
                self.match(ECMAScriptParser.Identifier)
                self.state = 200
                self.match(ECMAScriptParser.Assign)
                self.state = 201
                self.expressionSequence()
                self.state = 202
                self.match(ECMAScriptParser.SemiColon)
                self.state = 203
                self.match(ECMAScriptParser.Identifier)
                self.state = 204
                self.match(ECMAScriptParser.LessThan)
                self.state = 205
                self.expressionSequence()
                self.state = 206
                self.match(ECMAScriptParser.SemiColon)
                self.state = 207
                self.match(ECMAScriptParser.Identifier)
                self.state = 208
                self.match(ECMAScriptParser.PlusPlus)
                self.state = 209
                self.match(ECMAScriptParser.CloseParen)
                self.state = 210
                self.statement()
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.match(ECMAScriptParser.For)
                self.state = 213
                self.match(ECMAScriptParser.OpenParen)
                self.state = 215
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 214
                    self.expressionSequence()


                self.state = 217
                self.match(ECMAScriptParser.SemiColon)
                self.state = 219
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 218
                    self.expressionSequence()


                self.state = 221
                self.match(ECMAScriptParser.SemiColon)
                self.state = 223
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 222
                    self.expressionSequence()


                self.state = 225
                self.match(ECMAScriptParser.CloseParen)
                self.state = 226
                self.statement()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.match(ECMAScriptParser.For)
                self.state = 228
                self.match(ECMAScriptParser.OpenParen)
                self.state = 229
                self.match(ECMAScriptParser.Var)
                self.state = 230
                self.variableDeclarationList()
                self.state = 231
                self.match(ECMAScriptParser.SemiColon)
                self.state = 233
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 232
                    self.expressionSequence()


                self.state = 235
                self.match(ECMAScriptParser.SemiColon)
                self.state = 237
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                    self.state = 236
                    self.expressionSequence()


                self.state = 239
                self.match(ECMAScriptParser.CloseParen)
                self.state = 240
                self.statement()
                pass

            elif la_ == 6:
                localctx = ECMAScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 242
                self.match(ECMAScriptParser.For)
                self.state = 243
                self.match(ECMAScriptParser.OpenParen)
                self.state = 244
                self.singleExpression()
                self.state = 245
                self.match(ECMAScriptParser.In)
                self.state = 246
                self.expressionSequence()
                self.state = 247
                self.match(ECMAScriptParser.CloseParen)
                self.state = 248
                self.statement()
                pass

            elif la_ == 7:
                localctx = ECMAScriptParser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 250
                self.match(ECMAScriptParser.For)
                self.state = 251
                self.match(ECMAScriptParser.OpenParen)
                self.state = 252
                self.match(ECMAScriptParser.Var)
                self.state = 253
                self.variableDeclaration()
                self.state = 254
                self.match(ECMAScriptParser.In)
                self.state = 255
                self.expressionSequence()
                self.state = 256
                self.match(ECMAScriptParser.CloseParen)
                self.state = 257
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 261
            self.match(ECMAScriptParser.Continue)
            self.state = 263
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 262
                self.match(ECMAScriptParser.Identifier)


            self.state = 265
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 267
            self.match(ECMAScriptParser.Break)
            self.state = 269
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 268
                self.match(ECMAScriptParser.Identifier)


            self.state = 271
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 273
            self.match(ECMAScriptParser.Return)
            self.state = 275
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 274
                self.expressionSequence()


            self.state = 277
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 279
            self.match(ECMAScriptParser.With)
            self.state = 280
            self.match(ECMAScriptParser.OpenParen)
            self.state = 281
            self.expressionSequence()
            self.state = 282
            self.match(ECMAScriptParser.CloseParen)
            self.state = 283
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 285
            self.match(ECMAScriptParser.Switch)
            self.state = 286
            self.match(ECMAScriptParser.OpenParen)
            self.state = 287
            self.expressionSequence()
            self.state = 288
            self.match(ECMAScriptParser.CloseParen)
            self.state = 289
            self.caseBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 291
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 293
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Case:
                self.state = 292
                self.caseClauses()


            self.state = 299
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Default:
                self.state = 295
                self.defaultClause()
                self.state = 297
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.Case:
                    self.state = 296
                    self.caseClauses()




            self.state = 301
            self.match(ECMAScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 304 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 303
                self.caseClause()
                self.state = 306 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.Case):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 308
            self.match(ECMAScriptParser.Case)
            self.state = 309
            self.expressionSequence()
            self.state = 310
            self.match(ECMAScriptParser.Colon)
            self.state = 312
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Do))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 311
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 314
            self.match(ECMAScriptParser.Default)
            self.state = 315
            self.match(ECMAScriptParser.Colon)
            self.state = 317
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Do))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 316
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 319
            self.match(ECMAScriptParser.Identifier)
            self.state = 320
            self.match(ECMAScriptParser.Colon)
            self.state = 321
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 323
            self.match(ECMAScriptParser.Throw)
            self.state = 324
            self.expressionSequence()
            self.state = 325
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 340
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(ECMAScriptParser.Try)
                self.state = 328
                self.block()
                self.state = 329
                self.catchProduction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(ECMAScriptParser.Try)
                self.state = 332
                self.block()
                self.state = 333
                self.finallyProduction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.match(ECMAScriptParser.Try)
                self.state = 336
                self.block()
                self.state = 337
                self.catchProduction()
                self.state = 338
                self.finallyProduction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 342
            self.match(ECMAScriptParser.Catch)
            self.state = 343
            self.match(ECMAScriptParser.OpenParen)
            self.state = 344
            self.match(ECMAScriptParser.Identifier)
            self.state = 345
            self.match(ECMAScriptParser.CloseParen)
            self.state = 346
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 348
            self.match(ECMAScriptParser.Finally)
            self.state = 349
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 351
            self.match(ECMAScriptParser.Debugger)
            self.state = 352
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 354
            self.match(ECMAScriptParser.Function)
            self.state = 355
            self.match(ECMAScriptParser.Identifier)
            self.state = 356
            self.match(ECMAScriptParser.OpenParen)
            self.state = 358
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Identifier:
                self.state = 357
                self.formalParameterList()


            self.state = 360
            self.match(ECMAScriptParser.CloseParen)
            self.state = 361
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 362
            self.functionBody()
            self.state = 363
            self.match(ECMAScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 365
            self.match(ECMAScriptParser.Identifier)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 366
                self.match(ECMAScriptParser.Comma)
                self.state = 367
                self.match(ECMAScriptParser.Identifier)
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 374
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.OpenBrace) | (1 << ECMAScriptParser.SemiColon) | (1 << ECMAScriptParser.Do))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.If - 64)))) != 0):
                self.state = 373
                self.sourceElements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 376
            self.match(ECMAScriptParser.OpenBracket)
            self.state = 378
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 377
                self.elementList()


            self.state = 381
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 380
                self.match(ECMAScriptParser.Comma)


            self.state = 384
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 383
                self.elision()


            self.state = 386
            self.match(ECMAScriptParser.CloseBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 389
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 388
                self.elision()


            self.state = 391
            self.singleExpression()
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 392
                    self.match(ECMAScriptParser.Comma)
                    self.state = 394
                    _la = self._input.LA(1)
                    if _la==ECMAScriptParser.Comma:
                        self.state = 393
                        self.elision()


                    self.state = 396
                    self.singleExpression() 
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 403 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 402
                self.match(ECMAScriptParser.Comma)
                self.state = 405 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.Comma):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 407
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 409
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 408
                self.propertyNameAndValueList()


            self.state = 412
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 411
                self.match(ECMAScriptParser.Comma)


            self.state = 414
            self.match(ECMAScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 416
            self.propertyAssignment()
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 417
                    self.match(ECMAScriptParser.Comma)
                    self.state = 418
                    self.propertyAssignment() 
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 443
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.propertyName()
                self.state = 425
                self.match(ECMAScriptParser.Colon)
                self.state = 426
                self.singleExpression()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.getter()
                self.state = 429
                self.match(ECMAScriptParser.OpenParen)
                self.state = 430
                self.match(ECMAScriptParser.CloseParen)
                self.state = 431
                self.match(ECMAScriptParser.OpenBrace)
                self.state = 432
                self.functionBody()
                self.state = 433
                self.match(ECMAScriptParser.CloseBrace)
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 435
                self.setter()
                self.state = 436
                self.match(ECMAScriptParser.OpenParen)
                self.state = 437
                self.propertySetParameterList()
                self.state = 438
                self.match(ECMAScriptParser.CloseParen)
                self.state = 439
                self.match(ECMAScriptParser.OpenBrace)
                self.state = 440
                self.functionBody()
                self.state = 441
                self.match(ECMAScriptParser.CloseBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 448
            token = self._input.LA(1)
            if token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral, ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try, ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield, ECMAScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.identifierName()

            elif token in [ECMAScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.match(ECMAScriptParser.StringLiteral)

            elif token in [ECMAScriptParser.DecimalLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 447
                self.numericLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 450
            self.match(ECMAScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 452
            self.match(ECMAScriptParser.OpenParen)
            self.state = 454
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.DecimalLiteral or _la==ECMAScriptParser.Identifier:
                self.state = 453
                self.argumentList()


            self.state = 456
            self.match(ECMAScriptParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 458
            self.singleExpression()
            self.state = 463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 459
                self.match(ECMAScriptParser.Comma)
                self.state = 460
                self.singleExpression()
                self.state = 465
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 466
            self.singleExpression()
            self.state = 471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 467
                    self.match(ECMAScriptParser.Comma)
                    self.state = 468
                    self.singleExpression() 
                self.state = 473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 487
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.MethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.match(ECMAScriptParser.Identifier)
                self.state = 475
                self.match(ECMAScriptParser.Dot)
                self.state = 476
                self.identifierName()
                self.state = 477
                self.arguments()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.FunctionExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.match(ECMAScriptParser.Identifier)
                self.state = 480
                self.arguments()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 481
                self.match(ECMAScriptParser.Identifier)
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 482
                self.literal()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.ParenthesizedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 483
                self.match(ECMAScriptParser.OpenParen)
                self.state = 484
                self.expressionSequence()
                self.state = 485
                self.match(ECMAScriptParser.CloseParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 489
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.MultiplyAssign) | (1 << ECMAScriptParser.DivideAssign) | (1 << ECMAScriptParser.ModulusAssign) | (1 << ECMAScriptParser.PlusAssign) | (1 << ECMAScriptParser.MinusAssign) | (1 << ECMAScriptParser.LeftShiftArithmeticAssign) | (1 << ECMAScriptParser.RightShiftArithmeticAssign) | (1 << ECMAScriptParser.RightShiftLogicalAssign) | (1 << ECMAScriptParser.BitAndAssign) | (1 << ECMAScriptParser.BitXorAssign) | (1 << ECMAScriptParser.BitOrAssign))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 491
            self.numericLiteral()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 493
            self.match(ECMAScriptParser.DecimalLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 497
            token = self._input.LA(1)
            if token in [ECMAScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(ECMAScriptParser.Identifier)

            elif token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral, ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try, ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
                self.reservedWord()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 502
            token = self._input.LA(1)
            if token in [ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try]:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.keyword()

            elif token in [ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.futureReservedWord()

            elif token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 501
                _la = self._input.LA(1)
                if not(_la==ECMAScriptParser.NullLiteral or _la==ECMAScriptParser.BooleanLiteral):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 504
            _la = self._input.LA(1)
            if not(((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & ((1 << (ECMAScriptParser.Break - 57)) | (1 << (ECMAScriptParser.Do - 57)) | (1 << (ECMAScriptParser.Instanceof - 57)) | (1 << (ECMAScriptParser.Typeof - 57)) | (1 << (ECMAScriptParser.Case - 57)) | (1 << (ECMAScriptParser.Else - 57)) | (1 << (ECMAScriptParser.New - 57)) | (1 << (ECMAScriptParser.Var - 57)) | (1 << (ECMAScriptParser.Catch - 57)) | (1 << (ECMAScriptParser.Finally - 57)) | (1 << (ECMAScriptParser.Return - 57)) | (1 << (ECMAScriptParser.Void - 57)) | (1 << (ECMAScriptParser.Continue - 57)) | (1 << (ECMAScriptParser.For - 57)) | (1 << (ECMAScriptParser.Switch - 57)) | (1 << (ECMAScriptParser.While - 57)) | (1 << (ECMAScriptParser.Debugger - 57)) | (1 << (ECMAScriptParser.Function - 57)) | (1 << (ECMAScriptParser.This - 57)) | (1 << (ECMAScriptParser.With - 57)) | (1 << (ECMAScriptParser.Default - 57)) | (1 << (ECMAScriptParser.If - 57)) | (1 << (ECMAScriptParser.Throw - 57)) | (1 << (ECMAScriptParser.Delete - 57)) | (1 << (ECMAScriptParser.In - 57)) | (1 << (ECMAScriptParser.Try - 57)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 506
            _la = self._input.LA(1)
            if not(((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (ECMAScriptParser.Class - 83)) | (1 << (ECMAScriptParser.Enum - 83)) | (1 << (ECMAScriptParser.Extends - 83)) | (1 << (ECMAScriptParser.Super - 83)) | (1 << (ECMAScriptParser.Const - 83)) | (1 << (ECMAScriptParser.Export - 83)) | (1 << (ECMAScriptParser.Import - 83)) | (1 << (ECMAScriptParser.Implements - 83)) | (1 << (ECMAScriptParser.Let - 83)) | (1 << (ECMAScriptParser.Private - 83)) | (1 << (ECMAScriptParser.Public - 83)) | (1 << (ECMAScriptParser.Interface - 83)) | (1 << (ECMAScriptParser.Package - 83)) | (1 << (ECMAScriptParser.Protected - 83)) | (1 << (ECMAScriptParser.Static - 83)) | (1 << (ECMAScriptParser.Yield - 83)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 508
            if not self._input.LT(1).getText().startsWith("get"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._input.LT(1).getText().startsWith(\"get\")")
            self.state = 509
            self.match(ECMAScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 511
            if not self._input.LT(1).getText().startsWith("set"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._input.LT(1).getText().startsWith(\"set\")")
            self.state = 512
            self.match(ECMAScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 517
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(ECMAScriptParser.SemiColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(ECMAScriptParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 516
                if not self._input.LT(1).type == self.CloseBrace:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self._input.LT(1).type == self.CloseBrace")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
            self.state = 519
            self.match(ECMAScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.report_error(self, re)
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
         



