# Generated from Jac.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from JacParser import JacParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\"")
        buf.write("\u00ca\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3")
        buf.write("\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\6\34")
        buf.write("\u009f\n\34\r\34\16\34\u00a0\3\35\6\35\u00a4\n\35\r\35")
        buf.write("\16\35\u00a5\3\36\3\36\7\36\u00aa\n\36\f\36\16\36\u00ad")
        buf.write("\13\36\3\36\3\36\3\37\5\37\u00b2\n\37\3\37\3\37\7\37\u00b6")
        buf.write("\n\37\f\37\16\37\u00b9\13\37\3 \3 \7 \u00bd\n \f \16 ")
        buf.write("\u00c0\13 \3 \3 \3!\6!\u00c5\n!\r!\16!\u00c6\3!\3!\2\2")
        buf.write("\"\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"\3\2\5\3\2")
        buf.write("\f\f\3\2$$\4\2\13\13\"\"\2\u00d0\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\3C\3\2\2\2")
        buf.write("\5F\3\2\2\2\7L\3\2\2\2\tR\3\2\2\2\13[\3\2\2\2\ra\3\2\2")
        buf.write("\2\17i\3\2\2\2\21q\3\2\2\2\23u\3\2\2\2\25w\3\2\2\2\27")
        buf.write("y\3\2\2\2\31{\3\2\2\2\33}\3\2\2\2\35\177\3\2\2\2\37\u0081")
        buf.write("\3\2\2\2!\u0083\3\2\2\2#\u0085\3\2\2\2%\u0087\3\2\2\2")
        buf.write("\'\u0089\3\2\2\2)\u008b\3\2\2\2+\u008d\3\2\2\2-\u0090")
        buf.write("\3\2\2\2/\u0093\3\2\2\2\61\u0095\3\2\2\2\63\u0098\3\2")
        buf.write("\2\2\65\u009a\3\2\2\2\67\u009e\3\2\2\29\u00a3\3\2\2\2")
        buf.write(";\u00a7\3\2\2\2=\u00b1\3\2\2\2?\u00ba\3\2\2\2A\u00c4\3")
        buf.write("\2\2\2CD\7k\2\2DE\7h\2\2E\4\3\2\2\2FG\7y\2\2GH\7j\2\2")
        buf.write("HI\7k\2\2IJ\7n\2\2JK\7g\2\2K\6\3\2\2\2LM\7d\2\2MN\7t\2")
        buf.write("\2NO\7g\2\2OP\7c\2\2PQ\7m\2\2Q\b\3\2\2\2RS\7e\2\2ST\7")
        buf.write("q\2\2TU\7p\2\2UV\7v\2\2VW\7k\2\2WX\7p\2\2XY\7w\2\2YZ\7")
        buf.write("g\2\2Z\n\3\2\2\2[\\\7r\2\2\\]\7t\2\2]^\7k\2\2^_\7p\2\2")
        buf.write("_`\7v\2\2`\f\3\2\2\2ab\7t\2\2bc\7g\2\2cd\7c\2\2de\7f\2")
        buf.write("\2ef\7k\2\2fg\7p\2\2gh\7v\2\2h\16\3\2\2\2ij\7t\2\2jk\7")
        buf.write("g\2\2kl\7c\2\2lm\7f\2\2mn\7u\2\2no\7v\2\2op\7t\2\2p\20")
        buf.write("\3\2\2\2qr\7f\2\2rs\7g\2\2st\7h\2\2t\22\3\2\2\2uv\7-\2")
        buf.write("\2v\24\3\2\2\2wx\7/\2\2x\26\3\2\2\2yz\7,\2\2z\30\3\2\2")
        buf.write("\2{|\7\61\2\2|\32\3\2\2\2}~\7\'\2\2~\34\3\2\2\2\177\u0080")
        buf.write("\7*\2\2\u0080\36\3\2\2\2\u0081\u0082\7+\2\2\u0082 \3\2")
        buf.write("\2\2\u0083\u0084\7}\2\2\u0084\"\3\2\2\2\u0085\u0086\7")
        buf.write("\177\2\2\u0086$\3\2\2\2\u0087\u0088\7?\2\2\u0088&\3\2")
        buf.write("\2\2\u0089\u008a\7.\2\2\u008a(\3\2\2\2\u008b\u008c\7<")
        buf.write("\2\2\u008c*\3\2\2\2\u008d\u008e\7?\2\2\u008e\u008f\7?")
        buf.write("\2\2\u008f,\3\2\2\2\u0090\u0091\7#\2\2\u0091\u0092\7?")
        buf.write("\2\2\u0092.\3\2\2\2\u0093\u0094\7@\2\2\u0094\60\3\2\2")
        buf.write("\2\u0095\u0096\7@\2\2\u0096\u0097\7?\2\2\u0097\62\3\2")
        buf.write("\2\2\u0098\u0099\7>\2\2\u0099\64\3\2\2\2\u009a\u009b\7")
        buf.write(">\2\2\u009b\u009c\7?\2\2\u009c\66\3\2\2\2\u009d\u009f")
        buf.write("\4c|\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a18\3\2\2\2\u00a2\u00a4")
        buf.write("\4\62;\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6:\3\2\2\2\u00a7")
        buf.write("\u00ab\7%\2\2\u00a8\u00aa\n\2\2\2\u00a9\u00a8\3\2\2\2")
        buf.write("\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3")
        buf.write("\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af")
        buf.write("\b\36\2\2\u00af<\3\2\2\2\u00b0\u00b2\7\17\2\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b7\7\f\2\2\u00b4\u00b6\7\"\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3")
        buf.write("\2\2\2\u00b8>\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00be")
        buf.write("\7$\2\2\u00bb\u00bd\n\3\2\2\u00bc\u00bb\3\2\2\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\u00c1\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c2\7")
        buf.write("$\2\2\u00c2@\3\2\2\2\u00c3\u00c5\t\4\2\2\u00c4\u00c3\3")
        buf.write("\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\b!\2\2\u00c9")
        buf.write("B\3\2\2\2\n\2\u00a0\u00a5\u00ab\u00b1\u00b7\u00be\u00c6")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class JacLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    WHILE = 2
    BREAK = 3
    CONTINUE = 4
    PRINT = 5
    READINT = 6
    READSTR = 7
    DEF = 8
    PLUS = 9
    MINUS = 10
    TIMES = 11
    OVER = 12
    REM = 13
    OP_PAR = 14
    CL_PAR = 15
    OP_CUR = 16
    CL_CUR = 17
    ATTRIB = 18
    COMMA = 19
    COLON = 20
    EQ = 21
    NE = 22
    GT = 23
    GE = 24
    LT = 25
    LE = 26
    NAME = 27
    NUMBER = 28
    COMMENT = 29
    NL = 30
    STRING = 31
    SPACE = 32

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'while'", "'break'", "'continue'", "'print'", "'readint'", 
            "'readstr'", "'def'", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
            "')'", "'{'", "'}'", "'='", "','", "':'", "'=='", "'!='", "'>'", 
            "'>='", "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>",
            "IF", "WHILE", "BREAK", "CONTINUE", "PRINT", "READINT", "READSTR", 
            "DEF", "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", "CL_PAR", 
            "OP_CUR", "CL_CUR", "ATTRIB", "COMMA", "COLON", "EQ", "NE", 
            "GT", "GE", "LT", "LE", "NAME", "NUMBER", "COMMENT", "NL", "STRING", 
            "SPACE" ]

    ruleNames = [ "IF", "WHILE", "BREAK", "CONTINUE", "PRINT", "READINT", 
                  "READSTR", "DEF", "PLUS", "MINUS", "TIMES", "OVER", "REM", 
                  "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", "COMMA", 
                  "COLON", "EQ", "NE", "GT", "GE", "LT", "LE", "NAME", "NUMBER", 
                  "COMMENT", "NL", "STRING", "SPACE" ]

    grammarFileName = "Jac.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class JacDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: JacLexer = lexer
            
        def pull_token(self):
            return super(JacLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.JacDenter(self, self.NL, JacParser.INDENT, JacParser.DEDENT, False)
        return self.denter.next_token()


