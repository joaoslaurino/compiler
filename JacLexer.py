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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2%")
        buf.write("\u00e0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\6\37\u00b5\n\37\r\37\16")
        buf.write("\37\u00b6\3 \6 \u00ba\n \r \16 \u00bb\3!\3!\7!\u00c0\n")
        buf.write("!\f!\16!\u00c3\13!\3!\3!\3\"\5\"\u00c8\n\"\3\"\3\"\7\"")
        buf.write("\u00cc\n\"\f\"\16\"\u00cf\13\"\3#\3#\7#\u00d3\n#\f#\16")
        buf.write("#\u00d6\13#\3#\3#\3$\6$\u00db\n$\r$\16$\u00dc\3$\3$\2")
        buf.write("\2%\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%\3\2")
        buf.write("\5\3\2\f\f\3\2$$\4\2\13\13\"\"\2\u00e6\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\3I\3\2\2\2\5L\3\2\2\2\7Q")
        buf.write("\3\2\2\2\tW\3\2\2\2\13]\3\2\2\2\rf\3\2\2\2\17l\3\2\2\2")
        buf.write("\21t\3\2\2\2\23|\3\2\2\2\25\u0080\3\2\2\2\27\u0084\3\2")
        buf.write("\2\2\31\u008b\3\2\2\2\33\u008d\3\2\2\2\35\u008f\3\2\2")
        buf.write("\2\37\u0091\3\2\2\2!\u0093\3\2\2\2#\u0095\3\2\2\2%\u0097")
        buf.write("\3\2\2\2\'\u0099\3\2\2\2)\u009b\3\2\2\2+\u009d\3\2\2\2")
        buf.write("-\u009f\3\2\2\2/\u00a1\3\2\2\2\61\u00a3\3\2\2\2\63\u00a6")
        buf.write("\3\2\2\2\65\u00a9\3\2\2\2\67\u00ab\3\2\2\29\u00ae\3\2")
        buf.write("\2\2;\u00b0\3\2\2\2=\u00b4\3\2\2\2?\u00b9\3\2\2\2A\u00bd")
        buf.write("\3\2\2\2C\u00c7\3\2\2\2E\u00d0\3\2\2\2G\u00da\3\2\2\2")
        buf.write("IJ\7k\2\2JK\7h\2\2K\4\3\2\2\2LM\7g\2\2MN\7n\2\2NO\7u\2")
        buf.write("\2OP\7g\2\2P\6\3\2\2\2QR\7y\2\2RS\7j\2\2ST\7k\2\2TU\7")
        buf.write("n\2\2UV\7g\2\2V\b\3\2\2\2WX\7d\2\2XY\7t\2\2YZ\7g\2\2Z")
        buf.write("[\7c\2\2[\\\7m\2\2\\\n\3\2\2\2]^\7e\2\2^_\7q\2\2_`\7p")
        buf.write("\2\2`a\7v\2\2ab\7k\2\2bc\7p\2\2cd\7w\2\2de\7g\2\2e\f\3")
        buf.write("\2\2\2fg\7r\2\2gh\7t\2\2hi\7k\2\2ij\7p\2\2jk\7v\2\2k\16")
        buf.write("\3\2\2\2lm\7t\2\2mn\7g\2\2no\7c\2\2op\7f\2\2pq\7k\2\2")
        buf.write("qr\7p\2\2rs\7v\2\2s\20\3\2\2\2tu\7t\2\2uv\7g\2\2vw\7c")
        buf.write("\2\2wx\7f\2\2xy\7u\2\2yz\7v\2\2z{\7t\2\2{\22\3\2\2\2|")
        buf.write("}\7f\2\2}~\7g\2\2~\177\7h\2\2\177\24\3\2\2\2\u0080\u0081")
        buf.write("\7k\2\2\u0081\u0082\7p\2\2\u0082\u0083\7v\2\2\u0083\26")
        buf.write("\3\2\2\2\u0084\u0085\7t\2\2\u0085\u0086\7g\2\2\u0086\u0087")
        buf.write("\7v\2\2\u0087\u0088\7w\2\2\u0088\u0089\7t\2\2\u0089\u008a")
        buf.write("\7p\2\2\u008a\30\3\2\2\2\u008b\u008c\7-\2\2\u008c\32\3")
        buf.write("\2\2\2\u008d\u008e\7/\2\2\u008e\34\3\2\2\2\u008f\u0090")
        buf.write("\7,\2\2\u0090\36\3\2\2\2\u0091\u0092\7\61\2\2\u0092 \3")
        buf.write("\2\2\2\u0093\u0094\7\'\2\2\u0094\"\3\2\2\2\u0095\u0096")
        buf.write("\7*\2\2\u0096$\3\2\2\2\u0097\u0098\7+\2\2\u0098&\3\2\2")
        buf.write("\2\u0099\u009a\7}\2\2\u009a(\3\2\2\2\u009b\u009c\7\177")
        buf.write("\2\2\u009c*\3\2\2\2\u009d\u009e\7?\2\2\u009e,\3\2\2\2")
        buf.write("\u009f\u00a0\7.\2\2\u00a0.\3\2\2\2\u00a1\u00a2\7<\2\2")
        buf.write("\u00a2\60\3\2\2\2\u00a3\u00a4\7?\2\2\u00a4\u00a5\7?\2")
        buf.write("\2\u00a5\62\3\2\2\2\u00a6\u00a7\7#\2\2\u00a7\u00a8\7?")
        buf.write("\2\2\u00a8\64\3\2\2\2\u00a9\u00aa\7@\2\2\u00aa\66\3\2")
        buf.write("\2\2\u00ab\u00ac\7@\2\2\u00ac\u00ad\7?\2\2\u00ad8\3\2")
        buf.write("\2\2\u00ae\u00af\7>\2\2\u00af:\3\2\2\2\u00b0\u00b1\7>")
        buf.write("\2\2\u00b1\u00b2\7?\2\2\u00b2<\3\2\2\2\u00b3\u00b5\4c")
        buf.write("|\2\u00b4\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7>\3\2\2\2\u00b8\u00ba")
        buf.write("\4\62;\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc@\3\2\2\2\u00bd")
        buf.write("\u00c1\7%\2\2\u00be\u00c0\n\2\2\2\u00bf\u00be\3\2\2\2")
        buf.write("\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5")
        buf.write("\b!\2\2\u00c5B\3\2\2\2\u00c6\u00c8\7\17\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00cd\7\f\2\2\u00ca\u00cc\7\"\2\2\u00cb\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3")
        buf.write("\2\2\2\u00ceD\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d4")
        buf.write("\7$\2\2\u00d1\u00d3\n\3\2\2\u00d2\u00d1\3\2\2\2\u00d3")
        buf.write("\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d7\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\7")
        buf.write("$\2\2\u00d8F\3\2\2\2\u00d9\u00db\t\4\2\2\u00da\u00d9\3")
        buf.write("\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\b$\2\2\u00df")
        buf.write("H\3\2\2\2\n\2\u00b6\u00bb\u00c1\u00c7\u00cd\u00d4\u00dc")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class JacLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    WHILE = 3
    BREAK = 4
    CONTINUE = 5
    PRINT = 6
    READINT = 7
    READSTR = 8
    DEF = 9
    INT = 10
    RETURN = 11
    PLUS = 12
    MINUS = 13
    TIMES = 14
    OVER = 15
    REM = 16
    OP_PAR = 17
    CL_PAR = 18
    OP_CUR = 19
    CL_CUR = 20
    ATTRIB = 21
    COMMA = 22
    COLON = 23
    EQ = 24
    NE = 25
    GT = 26
    GE = 27
    LT = 28
    LE = 29
    NAME = 30
    NUMBER = 31
    COMMENT = 32
    NL = 33
    STRING = 34
    SPACE = 35

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'while'", "'break'", "'continue'", "'print'", 
            "'readint'", "'readstr'", "'def'", "'int'", "'return'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'{'", "'}'", "'='", 
            "','", "':'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "WHILE", "BREAK", "CONTINUE", "PRINT", "READINT", 
            "READSTR", "DEF", "INT", "RETURN", "PLUS", "MINUS", "TIMES", 
            "OVER", "REM", "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", 
            "COMMA", "COLON", "EQ", "NE", "GT", "GE", "LT", "LE", "NAME", 
            "NUMBER", "COMMENT", "NL", "STRING", "SPACE" ]

    ruleNames = [ "IF", "ELSE", "WHILE", "BREAK", "CONTINUE", "PRINT", "READINT", 
                  "READSTR", "DEF", "INT", "RETURN", "PLUS", "MINUS", "TIMES", 
                  "OVER", "REM", "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", 
                  "ATTRIB", "COMMA", "COLON", "EQ", "NE", "GT", "GE", "LT", 
                  "LE", "NAME", "NUMBER", "COMMENT", "NL", "STRING", "SPACE" ]

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


