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
        buf.write(u"i\u01ec\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3")
        buf.write(u"\2\5\2r\n\2\3\2\3\2\3\3\6\3w\n\3\r\3\16\3x\3\4\3\4\3")
        buf.write(u"\5\3\5\3\5\5\5\u0080\n\5\3\6\3\6\5\6\u0084\n\6\3\6\3")
        buf.write(u"\6\3\7\6\7\u0089\n\7\r\7\16\7\u008a\3\b\3\b\3\b\3\b\3")
        buf.write(u"\t\3\t\3\n\3\n\5\n\u0095\n\n\3\13\3\13\3\13\3\f\3\f\3")
        buf.write(u"\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write(u"\u00a7\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00ba")
        buf.write(u"\n\17\3\17\3\17\5\17\u00be\n\17\3\17\3\17\5\17\u00c2")
        buf.write(u"\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00cc")
        buf.write(u"\n\17\3\17\3\17\5\17\u00d0\n\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\5\17\u00e6\n\17\3\20\3\20\5")
        buf.write(u"\20\u00ea\n\20\3\20\3\20\3\21\3\21\5\21\u00f0\n\21\3")
        buf.write(u"\21\3\21\3\22\3\22\5\22\u00f6\n\22\3\22\3\22\3\23\3\23")
        buf.write(u"\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write(u"\25\3\25\5\25\u0108\n\25\3\25\3\25\5\25\u010c\n\25\5")
        buf.write(u"\25\u010e\n\25\3\25\3\25\3\26\6\26\u0113\n\26\r\26\16")
        buf.write(u"\26\u0114\3\27\3\27\3\27\3\27\5\27\u011b\n\27\3\30\3")
        buf.write(u"\30\3\30\5\30\u0120\n\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write(u"\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\5\33\u0137\n\33\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3")
        buf.write(u"\37\3\37\3\37\5\37\u0149\n\37\3\37\3\37\3\37\3\37\3\37")
        buf.write(u"\3 \3 \3 \7 \u0153\n \f \16 \u0156\13 \3!\5!\u0159\n")
        buf.write(u"!\3\"\3\"\5\"\u015d\n\"\3\"\5\"\u0160\n\"\3\"\5\"\u0163")
        buf.write(u"\n\"\3\"\3\"\3#\5#\u0168\n#\3#\3#\3#\5#\u016d\n#\3#\7")
        buf.write(u"#\u0170\n#\f#\16#\u0173\13#\3$\6$\u0176\n$\r$\16$\u0177")
        buf.write(u"\3%\3%\5%\u017c\n%\3%\5%\u017f\n%\3%\3%\3&\3&\3&\7&\u0186")
        buf.write(u"\n&\f&\16&\u0189\13&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u019e")
        buf.write(u"\n\'\3(\3(\3(\5(\u01a3\n(\3)\3)\3*\3*\5*\u01a9\n*\3*")
        buf.write(u"\3*\3+\3+\3+\7+\u01b0\n+\f+\16+\u01b3\13+\3,\3,\3,\7")
        buf.write(u",\u01b8\n,\f,\16,\u01bb\13,\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\5-\u01c8\n-\3.\3.\3/\3/\5/\u01ce\n/\3\60\3\60")
        buf.write(u"\3\61\3\61\5\61\u01d4\n\61\3\62\3\62\3\62\5\62\u01d9")
        buf.write(u"\n\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3")
        buf.write(u"\66\3\67\3\67\3\67\5\67\u01e8\n\67\38\38\38\2\29\2\4")
        buf.write(u"\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write(u"\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\6\3\2*\64\3\2\65\66")
        buf.write(u"\3\2:S\3\2Tc\u01ed\2q\3\2\2\2\4v\3\2\2\2\6z\3\2\2\2\b")
        buf.write(u"\177\3\2\2\2\n\u0081\3\2\2\2\f\u0088\3\2\2\2\16\u008c")
        buf.write(u"\3\2\2\2\20\u0090\3\2\2\2\22\u0092\3\2\2\2\24\u0096\3")
        buf.write(u"\2\2\2\26\u0099\3\2\2\2\30\u009b\3\2\2\2\32\u009f\3\2")
        buf.write(u"\2\2\34\u00e5\3\2\2\2\36\u00e7\3\2\2\2 \u00ed\3\2\2\2")
        buf.write(u"\"\u00f3\3\2\2\2$\u00f9\3\2\2\2&\u00ff\3\2\2\2(\u0105")
        buf.write(u"\3\2\2\2*\u0112\3\2\2\2,\u0116\3\2\2\2.\u011c\3\2\2\2")
        buf.write(u"\60\u0121\3\2\2\2\62\u0125\3\2\2\2\64\u0136\3\2\2\2\66")
        buf.write(u"\u0138\3\2\2\28\u013e\3\2\2\2:\u0141\3\2\2\2<\u0144\3")
        buf.write(u"\2\2\2>\u014f\3\2\2\2@\u0158\3\2\2\2B\u015a\3\2\2\2D")
        buf.write(u"\u0167\3\2\2\2F\u0175\3\2\2\2H\u0179\3\2\2\2J\u0182\3")
        buf.write(u"\2\2\2L\u019d\3\2\2\2N\u01a2\3\2\2\2P\u01a4\3\2\2\2R")
        buf.write(u"\u01a6\3\2\2\2T\u01ac\3\2\2\2V\u01b4\3\2\2\2X\u01c7\3")
        buf.write(u"\2\2\2Z\u01c9\3\2\2\2\\\u01cd\3\2\2\2^\u01cf\3\2\2\2")
        buf.write(u"`\u01d3\3\2\2\2b\u01d8\3\2\2\2d\u01da\3\2\2\2f\u01dc")
        buf.write(u"\3\2\2\2h\u01de\3\2\2\2j\u01e1\3\2\2\2l\u01e7\3\2\2\2")
        buf.write(u"n\u01e9\3\2\2\2pr\5\4\3\2qp\3\2\2\2qr\3\2\2\2rs\3\2\2")
        buf.write(u"\2st\7\2\2\3t\3\3\2\2\2uw\5\6\4\2vu\3\2\2\2wx\3\2\2\2")
        buf.write(u"xv\3\2\2\2xy\3\2\2\2y\5\3\2\2\2z{\5\b\5\2{\7\3\2\2\2")
        buf.write(u"|\u0080\5\n\6\2}\u0080\5\26\f\2~\u0080\5\"\22\2\177|")
        buf.write(u"\3\2\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080\t\3\2\2\2\u0081")
        buf.write(u"\u0083\7\t\2\2\u0082\u0084\5\f\7\2\u0083\u0082\3\2\2")
        buf.write(u"\2\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086")
        buf.write(u"\7\n\2\2\u0086\13\3\2\2\2\u0087\u0089\5\b\5\2\u0088\u0087")
        buf.write(u"\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write(u"\u008b\3\2\2\2\u008b\r\3\2\2\2\u008c\u008d\7A\2\2\u008d")
        buf.write(u"\u008e\5\20\t\2\u008e\u008f\5l\67\2\u008f\17\3\2\2\2")
        buf.write(u"\u0090\u0091\5\22\n\2\u0091\21\3\2\2\2\u0092\u0094\7")
        buf.write(u"d\2\2\u0093\u0095\5\24\13\2\u0094\u0093\3\2\2\2\u0094")
        buf.write(u"\u0095\3\2\2\2\u0095\23\3\2\2\2\u0096\u0097\7\r\2\2\u0097")
        buf.write(u"\u0098\5X-\2\u0098\25\3\2\2\2\u0099\u009a\7\13\2\2\u009a")
        buf.write(u"\27\3\2\2\2\u009b\u009c\6\r\2\2\u009c\u009d\5V,\2\u009d")
        buf.write(u"\u009e\7\13\2\2\u009e\31\3\2\2\2\u009f\u00a0\7O\2\2\u00a0")
        buf.write(u"\u00a1\7\7\2\2\u00a1\u00a2\5V,\2\u00a2\u00a3\7\b\2\2")
        buf.write(u"\u00a3\u00a6\5\b\5\2\u00a4\u00a5\7?\2\2\u00a5\u00a7\5")
        buf.write(u"\b\5\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write(u"\33\3\2\2\2\u00a8\u00a9\7;\2\2\u00a9\u00aa\5\b\5\2\u00aa")
        buf.write(u"\u00ab\7I\2\2\u00ab\u00ac\7\7\2\2\u00ac\u00ad\5V,\2\u00ad")
        buf.write(u"\u00ae\7\b\2\2\u00ae\u00af\5l\67\2\u00af\u00e6\3\2\2")
        buf.write(u"\2\u00b0\u00b1\7I\2\2\u00b1\u00b2\7\7\2\2\u00b2\u00b3")
        buf.write(u"\5V,\2\u00b3\u00b4\7\b\2\2\u00b4\u00b5\5\b\5\2\u00b5")
        buf.write(u"\u00e6\3\2\2\2\u00b6\u00b7\7G\2\2\u00b7\u00b9\7\7\2\2")
        buf.write(u"\u00b8\u00ba\5V,\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3")
        buf.write(u"\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\7\13\2\2\u00bc")
        buf.write(u"\u00be\5V,\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write(u"\u00be\u00bf\3\2\2\2\u00bf\u00c1\7\13\2\2\u00c0\u00c2")
        buf.write(u"\5V,\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write(u"\u00c3\3\2\2\2\u00c3\u00c4\7\b\2\2\u00c4\u00e6\5\b\5")
        buf.write(u"\2\u00c5\u00c6\7G\2\2\u00c6\u00c7\7\7\2\2\u00c7\u00c8")
        buf.write(u"\7A\2\2\u00c8\u00c9\5\20\t\2\u00c9\u00cb\7\13\2\2\u00ca")
        buf.write(u"\u00cc\5V,\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2")
        buf.write(u"\u00cc\u00cd\3\2\2\2\u00cd\u00cf\7\13\2\2\u00ce\u00d0")
        buf.write(u"\5V,\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write(u"\u00d1\3\2\2\2\u00d1\u00d2\7\b\2\2\u00d2\u00d3\5\b\5")
        buf.write(u"\2\u00d3\u00e6\3\2\2\2\u00d4\u00d5\7G\2\2\u00d5\u00d6")
        buf.write(u"\7\7\2\2\u00d6\u00d7\5X-\2\u00d7\u00d8\7R\2\2\u00d8\u00d9")
        buf.write(u"\5V,\2\u00d9\u00da\7\b\2\2\u00da\u00db\5\b\5\2\u00db")
        buf.write(u"\u00e6\3\2\2\2\u00dc\u00dd\7G\2\2\u00dd\u00de\7\7\2\2")
        buf.write(u"\u00de\u00df\7A\2\2\u00df\u00e0\5\22\n\2\u00e0\u00e1")
        buf.write(u"\7R\2\2\u00e1\u00e2\5V,\2\u00e2\u00e3\7\b\2\2\u00e3\u00e4")
        buf.write(u"\5\b\5\2\u00e4\u00e6\3\2\2\2\u00e5\u00a8\3\2\2\2\u00e5")
        buf.write(u"\u00b0\3\2\2\2\u00e5\u00b6\3\2\2\2\u00e5\u00c5\3\2\2")
        buf.write(u"\2\u00e5\u00d4\3\2\2\2\u00e5\u00dc\3\2\2\2\u00e6\35\3")
        buf.write(u"\2\2\2\u00e7\u00e9\7F\2\2\u00e8\u00ea\7d\2\2\u00e9\u00e8")
        buf.write(u"\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write(u"\u00ec\5l\67\2\u00ec\37\3\2\2\2\u00ed\u00ef\7:\2\2\u00ee")
        buf.write(u"\u00f0\7d\2\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write(u"\u00f0\u00f1\3\2\2\2\u00f1\u00f2\5l\67\2\u00f2!\3\2\2")
        buf.write(u"\2\u00f3\u00f5\7D\2\2\u00f4\u00f6\5V,\2\u00f5\u00f4\3")
        buf.write(u"\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write(u"\u00f8\5l\67\2\u00f8#\3\2\2\2\u00f9\u00fa\7M\2\2\u00fa")
        buf.write(u"\u00fb\7\7\2\2\u00fb\u00fc\5V,\2\u00fc\u00fd\7\b\2\2")
        buf.write(u"\u00fd\u00fe\5\b\5\2\u00fe%\3\2\2\2\u00ff\u0100\7H\2")
        buf.write(u"\2\u0100\u0101\7\7\2\2\u0101\u0102\5V,\2\u0102\u0103")
        buf.write(u"\7\b\2\2\u0103\u0104\5(\25\2\u0104\'\3\2\2\2\u0105\u0107")
        buf.write(u"\7\t\2\2\u0106\u0108\5*\26\2\u0107\u0106\3\2\2\2\u0107")
        buf.write(u"\u0108\3\2\2\2\u0108\u010d\3\2\2\2\u0109\u010b\5.\30")
        buf.write(u"\2\u010a\u010c\5*\26\2\u010b\u010a\3\2\2\2\u010b\u010c")
        buf.write(u"\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u0109\3\2\2\2\u010d")
        buf.write(u"\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7\n\2")
        buf.write(u"\2\u0110)\3\2\2\2\u0111\u0113\5,\27\2\u0112\u0111\3\2")
        buf.write(u"\2\2\u0113\u0114\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115")
        buf.write(u"\3\2\2\2\u0115+\3\2\2\2\u0116\u0117\7>\2\2\u0117\u0118")
        buf.write(u"\5V,\2\u0118\u011a\7\17\2\2\u0119\u011b\5\f\7\2\u011a")
        buf.write(u"\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b-\3\2\2\2\u011c")
        buf.write(u"\u011d\7N\2\2\u011d\u011f\7\17\2\2\u011e\u0120\5\f\7")
        buf.write(u"\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120/\3\2")
        buf.write(u"\2\2\u0121\u0122\7d\2\2\u0122\u0123\7\17\2\2\u0123\u0124")
        buf.write(u"\5\b\5\2\u0124\61\3\2\2\2\u0125\u0126\7P\2\2\u0126\u0127")
        buf.write(u"\5V,\2\u0127\u0128\5l\67\2\u0128\63\3\2\2\2\u0129\u012a")
        buf.write(u"\7S\2\2\u012a\u012b\5\n\6\2\u012b\u012c\5\66\34\2\u012c")
        buf.write(u"\u0137\3\2\2\2\u012d\u012e\7S\2\2\u012e\u012f\5\n\6\2")
        buf.write(u"\u012f\u0130\58\35\2\u0130\u0137\3\2\2\2\u0131\u0132")
        buf.write(u"\7S\2\2\u0132\u0133\5\n\6\2\u0133\u0134\5\66\34\2\u0134")
        buf.write(u"\u0135\58\35\2\u0135\u0137\3\2\2\2\u0136\u0129\3\2\2")
        buf.write(u"\2\u0136\u012d\3\2\2\2\u0136\u0131\3\2\2\2\u0137\65\3")
        buf.write(u"\2\2\2\u0138\u0139\7B\2\2\u0139\u013a\7\7\2\2\u013a\u013b")
        buf.write(u"\7d\2\2\u013b\u013c\7\b\2\2\u013c\u013d\5\n\6\2\u013d")
        buf.write(u"\67\3\2\2\2\u013e\u013f\7C\2\2\u013f\u0140\5\n\6\2\u0140")
        buf.write(u"9\3\2\2\2\u0141\u0142\7J\2\2\u0142\u0143\5l\67\2\u0143")
        buf.write(u";\3\2\2\2\u0144\u0145\7K\2\2\u0145\u0146\7d\2\2\u0146")
        buf.write(u"\u0148\7\7\2\2\u0147\u0149\5> \2\u0148\u0147\3\2\2\2")
        buf.write(u"\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b")
        buf.write(u"\7\b\2\2\u014b\u014c\7\t\2\2\u014c\u014d\5@!\2\u014d")
        buf.write(u"\u014e\7\n\2\2\u014e=\3\2\2\2\u014f\u0154\7d\2\2\u0150")
        buf.write(u"\u0151\7\f\2\2\u0151\u0153\7d\2\2\u0152\u0150\3\2\2\2")
        buf.write(u"\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155")
        buf.write(u"\3\2\2\2\u0155?\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0159")
        buf.write(u"\5\4\3\2\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write(u"A\3\2\2\2\u015a\u015c\7\5\2\2\u015b\u015d\5D#\2\u015c")
        buf.write(u"\u015b\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f\3\2\2")
        buf.write(u"\2\u015e\u0160\7\f\2\2\u015f\u015e\3\2\2\2\u015f\u0160")
        buf.write(u"\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u0163\5F$\2\u0162")
        buf.write(u"\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2")
        buf.write(u"\2\u0164\u0165\7\6\2\2\u0165C\3\2\2\2\u0166\u0168\5F")
        buf.write(u"$\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169")
        buf.write(u"\3\2\2\2\u0169\u0171\5X-\2\u016a\u016c\7\f\2\2\u016b")
        buf.write(u"\u016d\5F$\2\u016c\u016b\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write(u"\u016d\u016e\3\2\2\2\u016e\u0170\5X-\2\u016f\u016a\3")
        buf.write(u"\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write(u"\u0172\3\2\2\2\u0172E\3\2\2\2\u0173\u0171\3\2\2\2\u0174")
        buf.write(u"\u0176\7\f\2\2\u0175\u0174\3\2\2\2\u0176\u0177\3\2\2")
        buf.write(u"\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178G\3\2")
        buf.write(u"\2\2\u0179\u017b\7\t\2\2\u017a\u017c\5J&\2\u017b\u017a")
        buf.write(u"\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2\u017d")
        buf.write(u"\u017f\7\f\2\2\u017e\u017d\3\2\2\2\u017e\u017f\3\2\2")
        buf.write(u"\2\u017f\u0180\3\2\2\2\u0180\u0181\7\n\2\2\u0181I\3\2")
        buf.write(u"\2\2\u0182\u0187\5L\'\2\u0183\u0184\7\f\2\2\u0184\u0186")
        buf.write(u"\5L\'\2\u0185\u0183\3\2\2\2\u0186\u0189\3\2\2\2\u0187")
        buf.write(u"\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188K\3\2\2\2\u0189")
        buf.write(u"\u0187\3\2\2\2\u018a\u018b\5N(\2\u018b\u018c\7\17\2\2")
        buf.write(u"\u018c\u018d\5X-\2\u018d\u019e\3\2\2\2\u018e\u018f\5")
        buf.write(u"h\65\2\u018f\u0190\7\7\2\2\u0190\u0191\7\b\2\2\u0191")
        buf.write(u"\u0192\7\t\2\2\u0192\u0193\5@!\2\u0193\u0194\7\n\2\2")
        buf.write(u"\u0194\u019e\3\2\2\2\u0195\u0196\5j\66\2\u0196\u0197")
        buf.write(u"\7\7\2\2\u0197\u0198\5P)\2\u0198\u0199\7\b\2\2\u0199")
        buf.write(u"\u019a\7\t\2\2\u019a\u019b\5@!\2\u019b\u019c\7\n\2\2")
        buf.write(u"\u019c\u019e\3\2\2\2\u019d\u018a\3\2\2\2\u019d\u018e")
        buf.write(u"\3\2\2\2\u019d\u0195\3\2\2\2\u019eM\3\2\2\2\u019f\u01a3")
        buf.write(u"\5`\61\2\u01a0\u01a3\7e\2\2\u01a1\u01a3\5^\60\2\u01a2")
        buf.write(u"\u019f\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a1\3\2\2")
        buf.write(u"\2\u01a3O\3\2\2\2\u01a4\u01a5\7d\2\2\u01a5Q\3\2\2\2\u01a6")
        buf.write(u"\u01a8\7\7\2\2\u01a7\u01a9\5T+\2\u01a8\u01a7\3\2\2\2")
        buf.write(u"\u01a8\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab")
        buf.write(u"\7\b\2\2\u01abS\3\2\2\2\u01ac\u01b1\5X-\2\u01ad\u01ae")
        buf.write(u"\7\f\2\2\u01ae\u01b0\5X-\2\u01af\u01ad\3\2\2\2\u01b0")
        buf.write(u"\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2")
        buf.write(u"\2\u01b2U\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b9\5X")
        buf.write(u"-\2\u01b5\u01b6\7\f\2\2\u01b6\u01b8\5X-\2\u01b7\u01b5")
        buf.write(u"\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write(u"\u01ba\3\2\2\2\u01baW\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc")
        buf.write(u"\u01bd\7d\2\2\u01bd\u01be\7\20\2\2\u01be\u01bf\5`\61")
        buf.write(u"\2\u01bf\u01c0\5R*\2\u01c0\u01c8\3\2\2\2\u01c1\u01c2")
        buf.write(u"\7d\2\2\u01c2\u01c8\5R*\2\u01c3\u01c4\7\7\2\2\u01c4\u01c5")
        buf.write(u"\5V,\2\u01c5\u01c6\7\b\2\2\u01c6\u01c8\3\2\2\2\u01c7")
        buf.write(u"\u01bc\3\2\2\2\u01c7\u01c1\3\2\2\2\u01c7\u01c3\3\2\2")
        buf.write(u"\2\u01c8Y\3\2\2\2\u01c9\u01ca\t\2\2\2\u01ca[\3\2\2\2")
        buf.write(u"\u01cb\u01ce\t\3\2\2\u01cc\u01ce\5^\60\2\u01cd\u01cb")
        buf.write(u"\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ce]\3\2\2\2\u01cf\u01d0")
        buf.write(u"\7\67\2\2\u01d0_\3\2\2\2\u01d1\u01d4\7d\2\2\u01d2\u01d4")
        buf.write(u"\5b\62\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4")
        buf.write(u"a\3\2\2\2\u01d5\u01d9\5d\63\2\u01d6\u01d9\5f\64\2\u01d7")
        buf.write(u"\u01d9\t\3\2\2\u01d8\u01d5\3\2\2\2\u01d8\u01d6\3\2\2")
        buf.write(u"\2\u01d8\u01d7\3\2\2\2\u01d9c\3\2\2\2\u01da\u01db\t\4")
        buf.write(u"\2\2\u01dbe\3\2\2\2\u01dc\u01dd\t\5\2\2\u01ddg\3\2\2")
        buf.write(u"\2\u01de\u01df\6\65\3\2\u01df\u01e0\7d\2\2\u01e0i\3\2")
        buf.write(u"\2\2\u01e1\u01e2\6\66\4\2\u01e2\u01e3\7d\2\2\u01e3k\3")
        buf.write(u"\2\2\2\u01e4\u01e8\7\13\2\2\u01e5\u01e8\7\2\2\3\u01e6")
        buf.write(u"\u01e8\6\67\5\2\u01e7\u01e4\3\2\2\2\u01e7\u01e5\3\2\2")
        buf.write(u"\2\u01e7\u01e6\3\2\2\2\u01e8m\3\2\2\2\u01e9\u01ea\7\2")
        buf.write(u"\2\3\u01eao\3\2\2\2\60qx\177\u0083\u008a\u0094\u00a6")
        buf.write(u"\u00b9\u00bd\u00c1\u00cb\u00cf\u00e5\u00e9\u00ef\u00f5")
        buf.write(u"\u0107\u010b\u010d\u0114\u011a\u011f\u0136\u0148\u0154")
        buf.write(u"\u0158\u015c\u015f\u0162\u0167\u016c\u0171\u0177\u017b")
        buf.write(u"\u017e\u0187\u019d\u01a2\u01a8\u01b1\u01b9\u01c7\u01cd")
        buf.write(u"\u01d3\u01d8\u01e7")
        return buf.getvalue()


class ECMAScriptParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'['", u"']'", 
                     u"'('", u"')'", u"'{'", u"'}'", u"';'", u"','", u"'='", 
                     u"'?'", u"':'", u"'.'", u"'++'", u"'--'", u"'+'", u"'-'", 
                     u"'~'", u"'!'", u"'*'", u"'/'", u"'%'", u"'>>'", u"'<<'", 
                     u"'>>>'", u"'<'", u"'>'", u"'<='", u"'>='", u"'=='", 
                     u"'!='", u"'==='", u"'!=='", u"'&'", u"'^'", u"'|'", 
                     u"'&&'", u"'||'", u"'*='", u"'/='", u"'%='", u"'+='", 
                     u"'-='", u"'<<='", u"'>>='", u"'>>>='", u"'&='", u"'^='", 
                     u"'|='", u"'null'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
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

    symbolicNames = [ u"<INVALID>", u"RegularExpressionLiteral", u"LineTerminator", 
                      u"OpenBracket", u"CloseBracket", u"OpenParen", u"CloseParen", 
                      u"OpenBrace", u"CloseBrace", u"SemiColon", u"Comma", 
                      u"Assign", u"QuestionMark", u"Colon", u"Dot", u"PlusPlus", 
                      u"MinusMinus", u"Plus", u"Minus", u"BitNot", u"Not", 
                      u"Multiply", u"Divide", u"Modulus", u"RightShiftArithmetic", 
                      u"LeftShiftArithmetic", u"RightShiftLogical", u"LessThan", 
                      u"MoreThan", u"LessThanEquals", u"GreaterThanEquals", 
                      u"Equals", u"NotEquals", u"IdentityEquals", u"IdentityNotEquals", 
                      u"BitAnd", u"BitXOr", u"BitOr", u"And", u"Or", u"MultiplyAssign", 
                      u"DivideAssign", u"ModulusAssign", u"PlusAssign", 
                      u"MinusAssign", u"LeftShiftArithmeticAssign", u"RightShiftArithmeticAssign", 
                      u"RightShiftLogicalAssign", u"BitAndAssign", u"BitXorAssign", 
                      u"BitOrAssign", u"NullLiteral", u"BooleanLiteral", 
                      u"DecimalLiteral", u"HexIntegerLiteral", u"OctalIntegerLiteral", 
                      u"Break", u"Do", u"Instanceof", u"Typeof", u"Case", 
                      u"Else", u"New", u"Var", u"Catch", u"Finally", u"Return", 
                      u"Void", u"Continue", u"For", u"Switch", u"While", 
                      u"Debugger", u"Function", u"This", u"With", u"Default", 
                      u"If", u"Throw", u"Delete", u"In", u"Try", u"Class", 
                      u"Enum", u"Extends", u"Super", u"Const", u"Export", 
                      u"Import", u"Implements", u"Let", u"Private", u"Public", 
                      u"Interface", u"Package", u"Protected", u"Static", 
                      u"Yield", u"Identifier", u"StringLiteral", u"WhiteSpaces", 
                      u"MultiLineComment", u"SingleLineComment", u"UnexpectedCharacter" ]

    RULE_program = 0
    RULE_sourceElements = 1
    RULE_sourceElement = 2
    RULE_statement = 3
    RULE_block = 4
    RULE_statementList = 5
    RULE_variableStatement = 6
    RULE_variableDeclarationList = 7
    RULE_variableDeclaration = 8
    RULE_initialiser = 9
    RULE_emptyStatement = 10
    RULE_expressionStatement = 11
    RULE_ifStatement = 12
    RULE_iterationStatement = 13
    RULE_continueStatement = 14
    RULE_breakStatement = 15
    RULE_returnStatement = 16
    RULE_withStatement = 17
    RULE_switchStatement = 18
    RULE_caseBlock = 19
    RULE_caseClauses = 20
    RULE_caseClause = 21
    RULE_defaultClause = 22
    RULE_labelledStatement = 23
    RULE_throwStatement = 24
    RULE_tryStatement = 25
    RULE_catchProduction = 26
    RULE_finallyProduction = 27
    RULE_debuggerStatement = 28
    RULE_functionDeclaration = 29
    RULE_formalParameterList = 30
    RULE_functionBody = 31
    RULE_arrayLiteral = 32
    RULE_elementList = 33
    RULE_elision = 34
    RULE_objectLiteral = 35
    RULE_propertyNameAndValueList = 36
    RULE_propertyAssignment = 37
    RULE_propertyName = 38
    RULE_propertySetParameterList = 39
    RULE_arguments = 40
    RULE_argumentList = 41
    RULE_expressionSequence = 42
    RULE_singleExpression = 43
    RULE_assignmentOperator = 44
    RULE_literal = 45
    RULE_numericLiteral = 46
    RULE_identifierName = 47
    RULE_reservedWord = 48
    RULE_keyword = 49
    RULE_futureReservedWord = 50
    RULE_getter = 51
    RULE_setter = 52
    RULE_eos = 53
    RULE_eof = 54

    ruleNames =  [ u"program", u"sourceElements", u"sourceElement", u"statement", 
                   u"block", u"statementList", u"variableStatement", u"variableDeclarationList", 
                   u"variableDeclaration", u"initialiser", u"emptyStatement", 
                   u"expressionStatement", u"ifStatement", u"iterationStatement", 
                   u"continueStatement", u"breakStatement", u"returnStatement", 
                   u"withStatement", u"switchStatement", u"caseBlock", u"caseClauses", 
                   u"caseClause", u"defaultClause", u"labelledStatement", 
                   u"throwStatement", u"tryStatement", u"catchProduction", 
                   u"finallyProduction", u"debuggerStatement", u"functionDeclaration", 
                   u"formalParameterList", u"functionBody", u"arrayLiteral", 
                   u"elementList", u"elision", u"objectLiteral", u"propertyNameAndValueList", 
                   u"propertyAssignment", u"propertyName", u"propertySetParameterList", 
                   u"arguments", u"argumentList", u"expressionSequence", 
                   u"singleExpression", u"assignmentOperator", u"literal", 
                   u"numericLiteral", u"identifierName", u"reservedWord", 
                   u"keyword", u"futureReservedWord", u"getter", u"setter", 
                   u"eos", u"eof" ]

    EOF = Token.EOF
    RegularExpressionLiteral=1
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
    OctalIntegerLiteral=55
    Break=56
    Do=57
    Instanceof=58
    Typeof=59
    Case=60
    Else=61
    New=62
    Var=63
    Catch=64
    Finally=65
    Return=66
    Void=67
    Continue=68
    For=69
    Switch=70
    While=71
    Debugger=72
    Function=73
    This=74
    With=75
    Default=76
    If=77
    Throw=78
    Delete=79
    In=80
    Try=81
    Class=82
    Enum=83
    Extends=84
    Super=85
    Const=86
    Export=87
    Import=88
    Implements=89
    Let=90
    Private=91
    Public=92
    Interface=93
    Package=94
    Protected=95
    Static=96
    Yield=97
    Identifier=98
    StringLiteral=99
    WhiteSpaces=100
    MultiLineComment=101
    SingleLineComment=102
    UnexpectedCharacter=103

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
            self.state = 111
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (ECMAScriptParser.OpenBrace - 7)) | (1 << (ECMAScriptParser.SemiColon - 7)) | (1 << (ECMAScriptParser.Return - 7)))) != 0):
                self.state = 110
                self.sourceElements()


            self.state = 113
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
            self.state = 116 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 115
                self.sourceElement()
                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (ECMAScriptParser.OpenBrace - 7)) | (1 << (ECMAScriptParser.SemiColon - 7)) | (1 << (ECMAScriptParser.Return - 7)))) != 0)):
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
            self.state = 120
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


        def emptyStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.EmptyStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ReturnStatementContext,0)


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
            self.state = 125
            token = self._input.LA(1)
            if token in [ECMAScriptParser.OpenBrace]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.block()

            elif token in [ECMAScriptParser.SemiColon]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.emptyStatement()

            elif token in [ECMAScriptParser.Return]:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.returnStatement()

            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 129
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (ECMAScriptParser.OpenBrace - 7)) | (1 << (ECMAScriptParser.SemiColon - 7)) | (1 << (ECMAScriptParser.Return - 7)))) != 0):
                self.state = 128
                self.statementList()


            self.state = 131
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
        self.enterRule(localctx, 10, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 133
                self.statement()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (ECMAScriptParser.OpenBrace - 7)) | (1 << (ECMAScriptParser.SemiColon - 7)) | (1 << (ECMAScriptParser.Return - 7)))) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(ECMAScriptParser.Var)
            self.state = 139
            self.variableDeclarationList()
            self.state = 140
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

        def variableDeclaration(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationContext,0)


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
        self.enterRule(localctx, 14, self.RULE_variableDeclarationList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.variableDeclaration()
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
        self.enterRule(localctx, 16, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ECMAScriptParser.Identifier)
            self.state = 146
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 145
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
        self.enterRule(localctx, 18, self.RULE_initialiser)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ECMAScriptParser.Assign)
            self.state = 149
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
        self.enterRule(localctx, 20, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
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
        self.enterRule(localctx, 22, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            if not (self._input.LA(1) != self.OpenBrace) and (self._input.LA(1) != self.Function):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "(self._input.LA(1) != self.OpenBrace) and (self._input.LA(1) != self.Function)")
            self.state = 154
            self.expressionSequence()
            self.state = 155
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
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ECMAScriptParser.If)
            self.state = 158
            self.match(ECMAScriptParser.OpenParen)
            self.state = 159
            self.expressionSequence()
            self.state = 160
            self.match(ECMAScriptParser.CloseParen)
            self.state = 161
            self.statement()
            self.state = 164
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Else:
                self.state = 162
                self.match(ECMAScriptParser.Else)
                self.state = 163
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
        self.enterRule(localctx, 26, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 227
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(ECMAScriptParser.Do)
                self.state = 167
                self.statement()
                self.state = 168
                self.match(ECMAScriptParser.While)
                self.state = 169
                self.match(ECMAScriptParser.OpenParen)
                self.state = 170
                self.expressionSequence()
                self.state = 171
                self.match(ECMAScriptParser.CloseParen)
                self.state = 172
                self.eos()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(ECMAScriptParser.While)
                self.state = 175
                self.match(ECMAScriptParser.OpenParen)
                self.state = 176
                self.expressionSequence()
                self.state = 177
                self.match(ECMAScriptParser.CloseParen)
                self.state = 178
                self.statement()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.match(ECMAScriptParser.For)
                self.state = 181
                self.match(ECMAScriptParser.OpenParen)
                self.state = 183
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.Identifier:
                    self.state = 182
                    self.expressionSequence()


                self.state = 185
                self.match(ECMAScriptParser.SemiColon)
                self.state = 187
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.Identifier:
                    self.state = 186
                    self.expressionSequence()


                self.state = 189
                self.match(ECMAScriptParser.SemiColon)
                self.state = 191
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.Identifier:
                    self.state = 190
                    self.expressionSequence()


                self.state = 193
                self.match(ECMAScriptParser.CloseParen)
                self.state = 194
                self.statement()
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.match(ECMAScriptParser.For)
                self.state = 196
                self.match(ECMAScriptParser.OpenParen)
                self.state = 197
                self.match(ECMAScriptParser.Var)
                self.state = 198
                self.variableDeclarationList()
                self.state = 199
                self.match(ECMAScriptParser.SemiColon)
                self.state = 201
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.Identifier:
                    self.state = 200
                    self.expressionSequence()


                self.state = 203
                self.match(ECMAScriptParser.SemiColon)
                self.state = 205
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.Identifier:
                    self.state = 204
                    self.expressionSequence()


                self.state = 207
                self.match(ECMAScriptParser.CloseParen)
                self.state = 208
                self.statement()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.match(ECMAScriptParser.For)
                self.state = 211
                self.match(ECMAScriptParser.OpenParen)
                self.state = 212
                self.singleExpression()
                self.state = 213
                self.match(ECMAScriptParser.In)
                self.state = 214
                self.expressionSequence()
                self.state = 215
                self.match(ECMAScriptParser.CloseParen)
                self.state = 216
                self.statement()
                pass

            elif la_ == 6:
                localctx = ECMAScriptParser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 218
                self.match(ECMAScriptParser.For)
                self.state = 219
                self.match(ECMAScriptParser.OpenParen)
                self.state = 220
                self.match(ECMAScriptParser.Var)
                self.state = 221
                self.variableDeclaration()
                self.state = 222
                self.match(ECMAScriptParser.In)
                self.state = 223
                self.expressionSequence()
                self.state = 224
                self.match(ECMAScriptParser.CloseParen)
                self.state = 225
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
        self.enterRule(localctx, 28, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ECMAScriptParser.Continue)
            self.state = 231
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 230
                self.match(ECMAScriptParser.Identifier)


            self.state = 233
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
        self.enterRule(localctx, 30, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(ECMAScriptParser.Break)
            self.state = 237
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 236
                self.match(ECMAScriptParser.Identifier)


            self.state = 239
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
        self.enterRule(localctx, 32, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ECMAScriptParser.Return)
            self.state = 243
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 242
                self.expressionSequence()


            self.state = 245
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
        self.enterRule(localctx, 34, self.RULE_withStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ECMAScriptParser.With)
            self.state = 248
            self.match(ECMAScriptParser.OpenParen)
            self.state = 249
            self.expressionSequence()
            self.state = 250
            self.match(ECMAScriptParser.CloseParen)
            self.state = 251
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
        self.enterRule(localctx, 36, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ECMAScriptParser.Switch)
            self.state = 254
            self.match(ECMAScriptParser.OpenParen)
            self.state = 255
            self.expressionSequence()
            self.state = 256
            self.match(ECMAScriptParser.CloseParen)
            self.state = 257
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
        self.enterRule(localctx, 38, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 261
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Case:
                self.state = 260
                self.caseClauses()


            self.state = 267
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Default:
                self.state = 263
                self.defaultClause()
                self.state = 265
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.Case:
                    self.state = 264
                    self.caseClauses()




            self.state = 269
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
        self.enterRule(localctx, 40, self.RULE_caseClauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 271
                self.caseClause()
                self.state = 274 
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
        self.enterRule(localctx, 42, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ECMAScriptParser.Case)
            self.state = 277
            self.expressionSequence()
            self.state = 278
            self.match(ECMAScriptParser.Colon)
            self.state = 280
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (ECMAScriptParser.OpenBrace - 7)) | (1 << (ECMAScriptParser.SemiColon - 7)) | (1 << (ECMAScriptParser.Return - 7)))) != 0):
                self.state = 279
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
        self.enterRule(localctx, 44, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(ECMAScriptParser.Default)
            self.state = 283
            self.match(ECMAScriptParser.Colon)
            self.state = 285
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (ECMAScriptParser.OpenBrace - 7)) | (1 << (ECMAScriptParser.SemiColon - 7)) | (1 << (ECMAScriptParser.Return - 7)))) != 0):
                self.state = 284
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
        self.enterRule(localctx, 46, self.RULE_labelledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(ECMAScriptParser.Identifier)
            self.state = 288
            self.match(ECMAScriptParser.Colon)
            self.state = 289
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
        self.enterRule(localctx, 48, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(ECMAScriptParser.Throw)
            self.state = 292
            self.expressionSequence()
            self.state = 293
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
        self.enterRule(localctx, 50, self.RULE_tryStatement)
        try:
            self.state = 308
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(ECMAScriptParser.Try)
                self.state = 296
                self.block()
                self.state = 297
                self.catchProduction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(ECMAScriptParser.Try)
                self.state = 300
                self.block()
                self.state = 301
                self.finallyProduction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(ECMAScriptParser.Try)
                self.state = 304
                self.block()
                self.state = 305
                self.catchProduction()
                self.state = 306
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
        self.enterRule(localctx, 52, self.RULE_catchProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(ECMAScriptParser.Catch)
            self.state = 311
            self.match(ECMAScriptParser.OpenParen)
            self.state = 312
            self.match(ECMAScriptParser.Identifier)
            self.state = 313
            self.match(ECMAScriptParser.CloseParen)
            self.state = 314
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
        self.enterRule(localctx, 54, self.RULE_finallyProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ECMAScriptParser.Finally)
            self.state = 317
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
        self.enterRule(localctx, 56, self.RULE_debuggerStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ECMAScriptParser.Debugger)
            self.state = 320
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
        self.enterRule(localctx, 58, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(ECMAScriptParser.Function)
            self.state = 323
            self.match(ECMAScriptParser.Identifier)
            self.state = 324
            self.match(ECMAScriptParser.OpenParen)
            self.state = 326
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Identifier:
                self.state = 325
                self.formalParameterList()


            self.state = 328
            self.match(ECMAScriptParser.CloseParen)
            self.state = 329
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 330
            self.functionBody()
            self.state = 331
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
        self.enterRule(localctx, 60, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(ECMAScriptParser.Identifier)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 334
                self.match(ECMAScriptParser.Comma)
                self.state = 335
                self.match(ECMAScriptParser.Identifier)
                self.state = 340
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
        self.enterRule(localctx, 62, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (ECMAScriptParser.OpenBrace - 7)) | (1 << (ECMAScriptParser.SemiColon - 7)) | (1 << (ECMAScriptParser.Return - 7)))) != 0):
                self.state = 341
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
        self.enterRule(localctx, 64, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(ECMAScriptParser.OpenBracket)
            self.state = 346
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 345
                self.elementList()


            self.state = 349
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 348
                self.match(ECMAScriptParser.Comma)


            self.state = 352
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 351
                self.elision()


            self.state = 354
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
        self.enterRule(localctx, 66, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 356
                self.elision()


            self.state = 359
            self.singleExpression()
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 360
                    self.match(ECMAScriptParser.Comma)
                    self.state = 362
                    _la = self._input.LA(1)
                    if _la==ECMAScriptParser.Comma:
                        self.state = 361
                        self.elision()


                    self.state = 364
                    self.singleExpression() 
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 68, self.RULE_elision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 370
                self.match(ECMAScriptParser.Comma)
                self.state = 373 
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
        self.enterRule(localctx, 70, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(ECMAScriptParser.OpenBrace)
            self.state = 377
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 376
                self.propertyNameAndValueList()


            self.state = 380
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 379
                self.match(ECMAScriptParser.Comma)


            self.state = 382
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
        self.enterRule(localctx, 72, self.RULE_propertyNameAndValueList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.propertyAssignment()
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 385
                    self.match(ECMAScriptParser.Comma)
                    self.state = 386
                    self.propertyAssignment() 
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self.enterRule(localctx, 74, self.RULE_propertyAssignment)
        try:
            self.state = 411
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.propertyName()
                self.state = 393
                self.match(ECMAScriptParser.Colon)
                self.state = 394
                self.singleExpression()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.getter()
                self.state = 397
                self.match(ECMAScriptParser.OpenParen)
                self.state = 398
                self.match(ECMAScriptParser.CloseParen)
                self.state = 399
                self.match(ECMAScriptParser.OpenBrace)
                self.state = 400
                self.functionBody()
                self.state = 401
                self.match(ECMAScriptParser.CloseBrace)
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 403
                self.setter()
                self.state = 404
                self.match(ECMAScriptParser.OpenParen)
                self.state = 405
                self.propertySetParameterList()
                self.state = 406
                self.match(ECMAScriptParser.CloseParen)
                self.state = 407
                self.match(ECMAScriptParser.OpenBrace)
                self.state = 408
                self.functionBody()
                self.state = 409
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
        self.enterRule(localctx, 76, self.RULE_propertyName)
        try:
            self.state = 416
            token = self._input.LA(1)
            if token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral, ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try, ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield, ECMAScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.identifierName()

            elif token in [ECMAScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.match(ECMAScriptParser.StringLiteral)

            elif token in [ECMAScriptParser.DecimalLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 415
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
        self.enterRule(localctx, 78, self.RULE_propertySetParameterList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
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
        self.enterRule(localctx, 80, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(ECMAScriptParser.OpenParen)
            self.state = 422
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.OpenParen or _la==ECMAScriptParser.Identifier:
                self.state = 421
                self.argumentList()


            self.state = 424
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
        self.enterRule(localctx, 82, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.singleExpression()
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 427
                self.match(ECMAScriptParser.Comma)
                self.state = 428
                self.singleExpression()
                self.state = 433
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
        self.enterRule(localctx, 84, self.RULE_expressionSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.singleExpression()
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 435
                    self.match(ECMAScriptParser.Comma)
                    self.state = 436
                    self.singleExpression() 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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



    def singleExpression(self):

        localctx = ECMAScriptParser.SingleExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_singleExpression)
        try:
            self.state = 453
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.MethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(ECMAScriptParser.Identifier)
                self.state = 443
                self.match(ECMAScriptParser.Dot)
                self.state = 444
                self.identifierName()
                self.state = 445
                self.arguments()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.FunctionExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.match(ECMAScriptParser.Identifier)
                self.state = 448
                self.arguments()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.ParenthesizedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 449
                self.match(ECMAScriptParser.OpenParen)
                self.state = 450
                self.expressionSequence()
                self.state = 451
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
        self.enterRule(localctx, 88, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
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

        def NullLiteral(self):
            return self.getToken(ECMAScriptParser.NullLiteral, 0)

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
        self.enterRule(localctx, 90, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 459
            token = self._input.LA(1)
            if token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                _la = self._input.LA(1)
                if not(_la==ECMAScriptParser.NullLiteral or _la==ECMAScriptParser.BooleanLiteral):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [ECMAScriptParser.DecimalLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
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
        self.enterRule(localctx, 92, self.RULE_numericLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
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
        self.enterRule(localctx, 94, self.RULE_identifierName)
        try:
            self.state = 465
            token = self._input.LA(1)
            if token in [ECMAScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.match(ECMAScriptParser.Identifier)

            elif token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral, ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try, ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
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
        self.enterRule(localctx, 96, self.RULE_reservedWord)
        self._la = 0 # Token type
        try:
            self.state = 470
            token = self._input.LA(1)
            if token in [ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.keyword()

            elif token in [ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.futureReservedWord()

            elif token in [ECMAScriptParser.NullLiteral, ECMAScriptParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 469
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
        self.enterRule(localctx, 98, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not(((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & ((1 << (ECMAScriptParser.Break - 56)) | (1 << (ECMAScriptParser.Do - 56)) | (1 << (ECMAScriptParser.Instanceof - 56)) | (1 << (ECMAScriptParser.Typeof - 56)) | (1 << (ECMAScriptParser.Case - 56)) | (1 << (ECMAScriptParser.Else - 56)) | (1 << (ECMAScriptParser.New - 56)) | (1 << (ECMAScriptParser.Var - 56)) | (1 << (ECMAScriptParser.Catch - 56)) | (1 << (ECMAScriptParser.Finally - 56)) | (1 << (ECMAScriptParser.Return - 56)) | (1 << (ECMAScriptParser.Void - 56)) | (1 << (ECMAScriptParser.Continue - 56)) | (1 << (ECMAScriptParser.For - 56)) | (1 << (ECMAScriptParser.Switch - 56)) | (1 << (ECMAScriptParser.While - 56)) | (1 << (ECMAScriptParser.Debugger - 56)) | (1 << (ECMAScriptParser.Function - 56)) | (1 << (ECMAScriptParser.This - 56)) | (1 << (ECMAScriptParser.With - 56)) | (1 << (ECMAScriptParser.Default - 56)) | (1 << (ECMAScriptParser.If - 56)) | (1 << (ECMAScriptParser.Throw - 56)) | (1 << (ECMAScriptParser.Delete - 56)) | (1 << (ECMAScriptParser.In - 56)) | (1 << (ECMAScriptParser.Try - 56)))) != 0)):
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
        self.enterRule(localctx, 100, self.RULE_futureReservedWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            _la = self._input.LA(1)
            if not(((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & ((1 << (ECMAScriptParser.Class - 82)) | (1 << (ECMAScriptParser.Enum - 82)) | (1 << (ECMAScriptParser.Extends - 82)) | (1 << (ECMAScriptParser.Super - 82)) | (1 << (ECMAScriptParser.Const - 82)) | (1 << (ECMAScriptParser.Export - 82)) | (1 << (ECMAScriptParser.Import - 82)) | (1 << (ECMAScriptParser.Implements - 82)) | (1 << (ECMAScriptParser.Let - 82)) | (1 << (ECMAScriptParser.Private - 82)) | (1 << (ECMAScriptParser.Public - 82)) | (1 << (ECMAScriptParser.Interface - 82)) | (1 << (ECMAScriptParser.Package - 82)) | (1 << (ECMAScriptParser.Protected - 82)) | (1 << (ECMAScriptParser.Static - 82)) | (1 << (ECMAScriptParser.Yield - 82)))) != 0)):
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
        self.enterRule(localctx, 102, self.RULE_getter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            if not self._input.LT(1).getText().startsWith("get"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._input.LT(1).getText().startsWith(\"get\")")
            self.state = 477
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
        self.enterRule(localctx, 104, self.RULE_setter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            if not self._input.LT(1).getText().startsWith("set"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._input.LT(1).getText().startsWith(\"set\")")
            self.state = 480
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
        self.enterRule(localctx, 106, self.RULE_eos)
        try:
            self.state = 485
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.match(ECMAScriptParser.SemiColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.match(ECMAScriptParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
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
        self.enterRule(localctx, 108, self.RULE_eof)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
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
        self._predicates[11] = self.expressionStatement_sempred
        self._predicates[51] = self.getter_sempred
        self._predicates[52] = self.setter_sempred
        self._predicates[53] = self.eos_sempred
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
         



