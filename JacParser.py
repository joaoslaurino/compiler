# Generated from Jac.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import sys;
symbol_table = []
symbol_type = []
type_table = []
used_table = []
inside_while = []
declared_table = []
function_table = []
param_table = []


stack_cur = 0 
stack_max = 0
if_max = 1
while_max = 1
arg_max = 0

has_error = False
function_error = False
has_return = False

type = 'V'

def emit(bytecode, delta):
    global stack_cur, stack_max
    stack_cur += delta
    if stack_cur > stack_max:
        stack_max = stack_cur
    print('    ' + bytecode + '    ; delta=' + str(delta))

def if_counter():
    global if_max
    if_max += 1

def reset_counters():
    global stack_cur, stack_max, if_max, while_max, symbol_table, symbol_type, used_table, has_return, type
    stack_cur = 0
    stack_max = 0
    symbol_table = []
    symbol_type = []
    used_table = []
    has_return = False
    type = 'V'
    if_max = 1
    while_max = 1

def update_error():
    global has_error
    has_error = True



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("\u010d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\7\2+\n\2\f\2\16\2.\13\2\3\2\3\2\3\3")
        buf.write("\3\3\6\3\64\n\3\r\3\16\3\65\3\3\3\3\3\4\3\4\3\4\3\4\5")
        buf.write("\4>\n\4\3\4\3\4\3\4\3\4\3\4\5\4E\n\4\3\4\7\4H\n\4\f\4")
        buf.write("\16\4K\13\4\3\4\3\4\7\4O\n\4\f\4\16\4R\13\4\3\4\7\4U\n")
        buf.write("\4\f\4\16\4X\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\7\5a\n\5")
        buf.write("\f\5\16\5d\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6o\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7{\n")
        buf.write("\7\f\7\16\7~\13\7\5\7\u0080\n\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\6\t\u0090\n\t\r\t\16")
        buf.write("\t\u0091\3\t\3\t\3\t\3\t\3\t\3\t\6\t\u009a\n\t\r\t\16")
        buf.write("\t\u009b\5\t\u009e\n\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\6\f\u00b0\n\f\r\f")
        buf.write("\16\f\u00b1\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u00ba\n\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00ca\n\17\f\17\16\17\u00cd\13\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\7\22\u00de\n\22\f\22\16\22\u00e1\13\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\7\23\u00ea\n\23\f")
        buf.write("\23\16\23\u00ed\13\23\3\23\3\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00fd\n\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u010b\n\24\3\24\2\2\25\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&\2\5\3\2\32\37\3\2\16\17\3\2\20")
        buf.write("\22\2\u011a\2(\3\2\2\2\4\61\3\2\2\2\69\3\2\2\2\b[\3\2")
        buf.write("\2\2\nn\3\2\2\2\fp\3\2\2\2\16\u0084\3\2\2\2\20\u0089\3")
        buf.write("\2\2\2\22\u00a2\3\2\2\2\24\u00a5\3\2\2\2\26\u00a8\3\2")
        buf.write("\2\2\30\u00b6\3\2\2\2\32\u00be\3\2\2\2\34\u00c2\3\2\2")
        buf.write("\2\36\u00ce\3\2\2\2 \u00d3\3\2\2\2\"\u00d8\3\2\2\2$\u00e4")
        buf.write("\3\2\2\2&\u010a\3\2\2\2(,\b\2\1\2)+\5\6\4\2*)\3\2\2\2")
        buf.write("+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-/\3\2\2\2.,\3\2\2\2/\60")
        buf.write("\5\4\3\2\60\3\3\2\2\2\61\63\b\3\1\2\62\64\5\n\6\2\63\62")
        buf.write("\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66")
        buf.write("\67\3\2\2\2\678\b\3\1\28\5\3\2\2\29:\7\13\2\2:;\7 \2\2")
        buf.write(";=\7\23\2\2<>\5\b\5\2=<\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@")
        buf.write("\7\24\2\2@A\7\31\2\2AD\b\4\1\2BC\7\f\2\2CE\b\4\1\2DB\3")
        buf.write("\2\2\2DE\3\2\2\2EI\3\2\2\2FH\7&\2\2GF\3\2\2\2HK\3\2\2")
        buf.write("\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LP\b\4\1\2M")
        buf.write("O\5\n\6\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QV\3")
        buf.write("\2\2\2RP\3\2\2\2SU\7\'\2\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2")
        buf.write("\2VW\3\2\2\2WY\3\2\2\2XV\3\2\2\2YZ\b\4\1\2Z\7\3\2\2\2")
        buf.write("[\\\7 \2\2\\b\b\5\1\2]^\7\30\2\2^_\7 \2\2_a\b\5\1\2`]")
        buf.write("\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\t\3\2\2\2db\3")
        buf.write("\2\2\2eo\5\f\7\2fo\5\16\b\2go\5\20\t\2ho\5\26\f\2io\5")
        buf.write("\22\n\2jo\5\24\13\2ko\5\30\r\2lo\5\32\16\2mo\7#\2\2ne")
        buf.write("\3\2\2\2nf\3\2\2\2ng\3\2\2\2nh\3\2\2\2ni\3\2\2\2nj\3\2")
        buf.write("\2\2nk\3\2\2\2nl\3\2\2\2nm\3\2\2\2o\13\3\2\2\2pq\7\b\2")
        buf.write("\2q\177\7\23\2\2rs\b\7\1\2st\5\"\22\2t|\b\7\1\2uv\7\30")
        buf.write("\2\2vw\b\7\1\2wx\5\"\22\2xy\b\7\1\2y{\3\2\2\2zu\3\2\2")
        buf.write("\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\u0080\3\2\2\2~|\3\2")
        buf.write("\2\2\177r\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081\3\2\2")
        buf.write("\2\u0081\u0082\7\24\2\2\u0082\u0083\b\7\1\2\u0083\r\3")
        buf.write("\2\2\2\u0084\u0085\7 \2\2\u0085\u0086\7\27\2\2\u0086\u0087")
        buf.write("\5\"\22\2\u0087\u0088\b\b\1\2\u0088\17\3\2\2\2\u0089\u008a")
        buf.write("\7\3\2\2\u008a\u008b\5\36\20\2\u008b\u008c\7\31\2\2\u008c")
        buf.write("\u008d\b\t\1\2\u008d\u008f\7&\2\2\u008e\u0090\5\n\6\2")
        buf.write("\u008f\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u008f\3")
        buf.write("\2\2\2\u0091\u0092\3\2\2\2\u0092\u009d\3\2\2\2\u0093\u0094")
        buf.write("\7\'\2\2\u0094\u0095\7\4\2\2\u0095\u0096\7\31\2\2\u0096")
        buf.write("\u0097\7&\2\2\u0097\u0099\b\t\1\2\u0098\u009a\5\n\6\2")
        buf.write("\u0099\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u0099\3")
        buf.write("\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u0093")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00a0\b\t\1\2\u00a0\u00a1\7\'\2\2\u00a1\21\3\2\2\2\u00a2")
        buf.write("\u00a3\7\6\2\2\u00a3\u00a4\b\n\1\2\u00a4\23\3\2\2\2\u00a5")
        buf.write("\u00a6\7\7\2\2\u00a6\u00a7\b\13\1\2\u00a7\25\3\2\2\2\u00a8")
        buf.write("\u00a9\7\5\2\2\u00a9\u00aa\b\f\1\2\u00aa\u00ab\5 \21\2")
        buf.write("\u00ab\u00ac\b\f\1\2\u00ac\u00ad\7\31\2\2\u00ad\u00af")
        buf.write("\7&\2\2\u00ae\u00b0\5\n\6\2\u00af\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7\'\2\2\u00b4\u00b5\b")
        buf.write("\f\1\2\u00b5\27\3\2\2\2\u00b6\u00b7\7 \2\2\u00b7\u00b9")
        buf.write("\7\23\2\2\u00b8\u00ba\5\34\17\2\u00b9\u00b8\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\7\24\2")
        buf.write("\2\u00bc\u00bd\b\r\1\2\u00bd\31\3\2\2\2\u00be\u00bf\7")
        buf.write("\r\2\2\u00bf\u00c0\5\"\22\2\u00c0\u00c1\b\16\1\2\u00c1")
        buf.write("\33\3\2\2\2\u00c2\u00c3\b\17\1\2\u00c3\u00c4\5\"\22\2")
        buf.write("\u00c4\u00cb\b\17\1\2\u00c5\u00c6\7\30\2\2\u00c6\u00c7")
        buf.write("\5\"\22\2\u00c7\u00c8\b\17\1\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write("\u00c5\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\35\3\2\2\2\u00cd\u00cb\3\2")
        buf.write("\2\2\u00ce\u00cf\5\"\22\2\u00cf\u00d0\t\2\2\2\u00d0\u00d1")
        buf.write("\5\"\22\2\u00d1\u00d2\b\20\1\2\u00d2\37\3\2\2\2\u00d3")
        buf.write("\u00d4\5\"\22\2\u00d4\u00d5\t\2\2\2\u00d5\u00d6\5\"\22")
        buf.write("\2\u00d6\u00d7\b\21\1\2\u00d7!\3\2\2\2\u00d8\u00df\5$")
        buf.write("\23\2\u00d9\u00da\t\3\2\2\u00da\u00db\5$\23\2\u00db\u00dc")
        buf.write("\b\22\1\2\u00dc\u00de\3\2\2\2\u00dd\u00d9\3\2\2\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\b")
        buf.write("\22\1\2\u00e3#\3\2\2\2\u00e4\u00eb\5&\24\2\u00e5\u00e6")
        buf.write("\t\4\2\2\u00e6\u00e7\5&\24\2\u00e7\u00e8\b\23\1\2\u00e8")
        buf.write("\u00ea\3\2\2\2\u00e9\u00e5\3\2\2\2\u00ea\u00ed\3\2\2\2")
        buf.write("\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ee\3")
        buf.write("\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\b\23\1\2\u00ef")
        buf.write("%\3\2\2\2\u00f0\u00f1\7!\2\2\u00f1\u010b\b\24\1\2\u00f2")
        buf.write("\u00f3\7$\2\2\u00f3\u010b\b\24\1\2\u00f4\u00f5\7\23\2")
        buf.write("\2\u00f5\u00f6\5\"\22\2\u00f6\u00f7\7\24\2\2\u00f7\u00f8")
        buf.write("\b\24\1\2\u00f8\u010b\3\2\2\2\u00f9\u00fa\7 \2\2\u00fa")
        buf.write("\u00fc\7\23\2\2\u00fb\u00fd\5\34\17\2\u00fc\u00fb\3\2")
        buf.write("\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff")
        buf.write("\7\24\2\2\u00ff\u010b\b\24\1\2\u0100\u0101\7 \2\2\u0101")
        buf.write("\u010b\b\24\1\2\u0102\u0103\7\t\2\2\u0103\u0104\7\23\2")
        buf.write("\2\u0104\u0105\7\24\2\2\u0105\u010b\b\24\1\2\u0106\u0107")
        buf.write("\7\n\2\2\u0107\u0108\7\23\2\2\u0108\u0109\7\24\2\2\u0109")
        buf.write("\u010b\b\24\1\2\u010a\u00f0\3\2\2\2\u010a\u00f2\3\2\2")
        buf.write("\2\u010a\u00f4\3\2\2\2\u010a\u00f9\3\2\2\2\u010a\u0100")
        buf.write("\3\2\2\2\u010a\u0102\3\2\2\2\u010a\u0106\3\2\2\2\u010b")
        buf.write("\'\3\2\2\2\27,\65=DIPVbn|\177\u0091\u009b\u009d\u00b1")
        buf.write("\u00b9\u00cb\u00df\u00eb\u00fc\u010a")
        return buf.getvalue()


class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'break'", 
                     "'continue'", "'print'", "'readint'", "'readstr'", 
                     "'def'", "'int'", "'return'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'('", "')'", "'{'", "'}'", "'='", "','", 
                     "':'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "BREAK", "CONTINUE", 
                      "PRINT", "READINT", "READSTR", "DEF", "INT", "RETURN", 
                      "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", 
                      "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", "COMMA", "COLON", 
                      "EQ", "NE", "GT", "GE", "LT", "LE", "NAME", "NUMBER", 
                      "COMMENT", "NL", "STRING", "SPACE", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_function = 2
    RULE_parameters = 3
    RULE_statement = 4
    RULE_st_print = 5
    RULE_st_attrib = 6
    RULE_st_if = 7
    RULE_st_break = 8
    RULE_st_continue = 9
    RULE_st_while = 10
    RULE_st_call = 11
    RULE_st_return = 12
    RULE_arguments = 13
    RULE_comparison_if = 14
    RULE_comparison_while = 15
    RULE_expression = 16
    RULE_term = 17
    RULE_factor = 18

    ruleNames =  [ "program", "main", "function", "parameters", "statement", 
                   "st_print", "st_attrib", "st_if", "st_break", "st_continue", 
                   "st_while", "st_call", "st_return", "arguments", "comparison_if", 
                   "comparison_while", "expression", "term", "factor" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    BREAK=4
    CONTINUE=5
    PRINT=6
    READINT=7
    READSTR=8
    DEF=9
    INT=10
    RETURN=11
    PLUS=12
    MINUS=13
    TIMES=14
    OVER=15
    REM=16
    OP_PAR=17
    CL_PAR=18
    OP_CUR=19
    CL_CUR=20
    ATTRIB=21
    COMMA=22
    COLON=23
    EQ=24
    NE=25
    GT=26
    GE=27
    LT=28
    LE=29
    NAME=30
    NUMBER=31
    COMMENT=32
    NL=33
    STRING=34
    SPACE=35
    INDENT=36
    DEDENT=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(JacParser.MainContext,0)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.FunctionContext)
            else:
                return self.getTypedRuleContext(JacParser.FunctionContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_program




    def program(self):

        localctx = JacParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    print('.source Test.src')
                    print('.class  public Test')
                    print('.super  java/lang/Object\n')
                    print('.method public <init>()V')
                    print('    aload_0')
                    print('    invokenonvirtual java/lang/Object/<init>()V')
                    print('    return')
                    print('.end method\n')
                
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.DEF:
                self.state = 39
                self.function()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_main




    def main(self):

        localctx = JacParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    print('.method public static main([Ljava/lang/String;)V\n')
                
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.statement()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.PRINT) | (1 << JacParser.RETURN) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    global has_error
                    print('    return')
                    if (len(symbol_table) > 0):
                        print('.limit locals ' + str(len(symbol_table)))
                    print('.limit stack ' + str(stack_max))
                    print('.end method')
                    print('\n; symbol_table:', symbol_table)
                    print('; symbol_type:', symbol_type)
                    print('; used_table:', used_table)
                    if has_error == True:
                        exit(1)
                    if (False in used_table):
                        sys.stderr.write('Warning: unused variables: ' + str([symbol_table[i] for i in range(len(used_table)) if not used_table[i]]) + '\n')        
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def DEF(self):
            return self.getToken(JacParser.DEF, 0)

        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def COLON(self):
            return self.getToken(JacParser.COLON, 0)

        def parameters(self):
            return self.getTypedRuleContext(JacParser.ParametersContext,0)


        def INT(self):
            return self.getToken(JacParser.INT, 0)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.INDENT)
            else:
                return self.getToken(JacParser.INDENT, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.DEDENT)
            else:
                return self.getToken(JacParser.DEDENT, i)

        def getRuleIndex(self):
            return JacParser.RULE_function




    def function(self):

        localctx = JacParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(JacParser.DEF)
            self.state = 56
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 57
            self.match(JacParser.OP_PAR)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JacParser.NAME:
                self.state = 58
                self.parameters()


            self.state = 61
            self.match(JacParser.CL_PAR)
            self.state = 62
            self.match(JacParser.COLON)
            if 1:
                    global type, function_table, param_table, symbol_table, has_return
                
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JacParser.INT:
                self.state = 64
                self.match(JacParser.INT)
                if 1:
                        type = 'I'
                    


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.INDENT:
                self.state = 68
                self.match(JacParser.INDENT)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    I = ''
                    for j in range(0, len(symbol_table)):
                        I = I + 'I'
                    param_table.append(len(symbol_table))
                    if (None if localctx._NAME is None else localctx._NAME.text)+type not in function_table:
                        print('.method public static ' + (None if localctx._NAME is None else localctx._NAME.text) + '(' + I + ')' + type)
                        function_table.append((None if localctx._NAME is None else localctx._NAME.text) + type)
                    else:
                        sys.stderr.write('Error in function: "' + (None if localctx._NAME is None else localctx._NAME.text) + '" is already declared\n')
                        update_error()
                
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 75
                    self.statement() 
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.DEDENT:
                self.state = 81
                self.match(JacParser.DEDENT)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    #sys.stderr.write('Type = ' + str(type) + '\n')
                    #sys.stderr.write('has_return = ' + str(has_return) + '\n')
                    if type == 'I' and has_return == False:
                        sys.stderr.write('Error in function: "' + (None if localctx._NAME is None else localctx._NAME.text) + '" must return a integer value\n')
                        update_error()
                    print('return')
                    if (len(symbol_table) > 0):
                        print('.limit locals ' + str(len(symbol_table)))
                    print('.limit stack ' + str(stack_max))
                    print('.end method\n')
                    reset_counters()
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.NAME)
            else:
                return self.getToken(JacParser.NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.COMMA)
            else:
                return self.getToken(JacParser.COMMA, i)

        def getRuleIndex(self):
            return JacParser.RULE_parameters




    def parameters(self):

        localctx = JacParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            localctx._NAME = self.match(JacParser.NAME)
            if 1:
                    symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                    used_table.append(False)
                    symbol_type.append('i')
                
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.COMMA:
                self.state = 91
                self.match(JacParser.COMMA)
                self.state = 92
                localctx._NAME = self.match(JacParser.NAME)
                if 1:
                        if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                            sys.stderr.write('Error in parameter: names must be unique\n')
                            update_error()
                        else:
                            symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                            used_table.append(False)
                            symbol_type.append('i')
                    
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def st_print(self):
            return self.getTypedRuleContext(JacParser.St_printContext,0)


        def st_attrib(self):
            return self.getTypedRuleContext(JacParser.St_attribContext,0)


        def st_if(self):
            return self.getTypedRuleContext(JacParser.St_ifContext,0)


        def st_while(self):
            return self.getTypedRuleContext(JacParser.St_whileContext,0)


        def st_break(self):
            return self.getTypedRuleContext(JacParser.St_breakContext,0)


        def st_continue(self):
            return self.getTypedRuleContext(JacParser.St_continueContext,0)


        def st_call(self):
            return self.getTypedRuleContext(JacParser.St_callContext,0)


        def st_return(self):
            return self.getTypedRuleContext(JacParser.St_returnContext,0)


        def NL(self):
            return self.getToken(JacParser.NL, 0)

        def getRuleIndex(self):
            return JacParser.RULE_statement




    def statement(self):

        localctx = JacParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.st_print()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.st_attrib()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.st_if()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.st_while()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 103
                self.st_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 104
                self.st_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 105
                self.st_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 106
                self.st_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 107
                self.match(JacParser.NL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def PRINT(self):
            return self.getToken(JacParser.PRINT, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JacParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.COMMA)
            else:
                return self.getToken(JacParser.COMMA, i)

        def getRuleIndex(self):
            return JacParser.RULE_st_print




    def st_print(self):

        localctx = JacParser.St_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_st_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(JacParser.PRINT)
            self.state = 111
            self.match(JacParser.OP_PAR)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.READSTR) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER) | (1 << JacParser.STRING))) != 0):
                if 1:
                        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 113
                localctx.e1 = self.expression()
                if 1:
                        if localctx.e1.type == 'i':
                            emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
                        elif localctx.e1.type == 's':
                            emit('    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                        else:
                            sys.stderr.write('************ HELP ************\n')
                            exit(1)
                    
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JacParser.COMMA:
                    self.state = 115
                    self.match(JacParser.COMMA)
                    if 1:
                            emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                        
                    self.state = 117
                    localctx.e2 = self.expression()
                    if 1:
                            if localctx.e2.type == 'i':
                                emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
                            elif localctx.e2.type == 's':
                                emit('    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                            else:
                                sys.stderr.write('************ HELP ************\n')
                                exit(1)
                        
                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 127
            self.match(JacParser.CL_PAR)
            if 1:
                    emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    emit('    invokevirtual java/io/PrintStream/println()V\n', -1)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_attribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token
            self._expression = None # ExpressionContext

        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def ATTRIB(self):
            return self.getToken(JacParser.ATTRIB, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_st_attrib




    def st_attrib(self):

        localctx = JacParser.St_attribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 131
            self.match(JacParser.ATTRIB)
            self.state = 132
            localctx._expression = self.expression()
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                        symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                        symbol_type.append(localctx._expression.type)
                        used_table.append(False)
                    if symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] == 'i':
                        if symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] != localctx._expression.type:
                            sys.stderr.write('Error in attribution: integer variable "' + (None if localctx._NAME is None else localctx._NAME.text) + '" must receive a integer expression\n')
                            update_error()
                        elif localctx._expression.type == 'error' or localctx._expression.type == 's':
                            sys.stderr.write('Error in attribution: integer variable "' + (None if localctx._NAME is None else localctx._NAME.text) + '" cannot receive a string expression\n')
                            update_error()
                        elif localctx._expression.type == 'i':
                            emit('    istore ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), -1)
                        else:
                            sys.stderr.write('Error in expression: invalid type of expression\n')
                            update_error()
                    elif symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] == 's':
                        if symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] != localctx._expression.type:
                            sys.stderr.write('Error in attribution: string variable "' + (None if localctx._NAME is None else localctx._NAME.text) + '" must receive a string expression\n')
                            update_error()
                        elif localctx._expression.type == 'error' or localctx._expression.type == 'i':
                            sys.stderr.write('Error in attribution: string variable "' + (None if localctx._NAME is None else localctx._NAME.text) + '" cannot receive a integer expression\n')
                            update_error()
                        elif localctx._expression.type == 's':
                            emit('    astore ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), -1)
                        else:
                            sys.stderr.write('Error in expression: invalid type of expression\n')
                            update_error()
                    elif symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] == 'void':
                        sys.stderr.write('Error in atribuition: a void function does not return a value\n')
                        update_error()
                    else:
                        sys.stderr.write('Error in expression: invalid type of token\n')
                        update_error()
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cmp = None # Comparison_ifContext

        def IF(self):
            return self.getToken(JacParser.IF, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.COLON)
            else:
                return self.getToken(JacParser.COLON, i)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.INDENT)
            else:
                return self.getToken(JacParser.INDENT, i)

        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.DEDENT)
            else:
                return self.getToken(JacParser.DEDENT, i)

        def comparison_if(self):
            return self.getTypedRuleContext(JacParser.Comparison_ifContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(JacParser.ELSE, 0)

        def getRuleIndex(self):
            return JacParser.RULE_st_if




    def st_if(self):

        localctx = JacParser.St_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(JacParser.IF)
            self.state = 136
            localctx.cmp = self.comparison_if()
            self.state = 137
            self.match(JacParser.COLON)
            if 1:
                    global if_max
                    has_else = False
                    emit(localctx.cmp.type + ' NOT_IF_' + str(if_max), -2)
                    local_if = if_max
                    if_max += 1
                
            self.state = 139
            self.match(JacParser.INDENT)
            self.state = 141 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 140
                self.statement()
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.PRINT) | (1 << JacParser.RETURN) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 145
                self.match(JacParser.DEDENT)
                self.state = 146
                self.match(JacParser.ELSE)
                self.state = 147
                self.match(JacParser.COLON)
                self.state = 148
                self.match(JacParser.INDENT)
                if 1:
                        has_else = True
                        print('goto END_ELSE_' + str(local_if))
                        print('NOT_IF_' + str(local_if) + ':')
                        if_counter()
                    
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 150
                    self.statement()
                    self.state = 153 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.PRINT) | (1 << JacParser.RETURN) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                        break



            if 1:
                    if has_else:
                        print('END_ELSE_' + str(local_if) + ':')
                    else:
                        print('NOT_IF_' + str(local_if) + ':')
                    if_counter()
                
            self.state = 158
            self.match(JacParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(JacParser.BREAK, 0)

        def getRuleIndex(self):
            return JacParser.RULE_st_break




    def st_break(self):

        localctx = JacParser.St_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_st_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(JacParser.BREAK)
            if 1:
                    if len(inside_while) == 0:
                        sys.stderr.write('**ERROR** break outside while\n')
                        exit(1)
                    emit('goto END_WHILE_' + str(while_max -1), 0)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(JacParser.CONTINUE, 0)

        def getRuleIndex(self):
            return JacParser.RULE_st_continue




    def st_continue(self):

        localctx = JacParser.St_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_st_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(JacParser.CONTINUE)
            if 1:
                    if len(inside_while) == 0:
                        sys.stderr.write('**ERROR** continue outside while\n')
                        exit(1)
                    emit('goto BEGIN_WHILE_' + str(while_max - 1), 0)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(JacParser.WHILE, 0)

        def comparison_while(self):
            return self.getTypedRuleContext(JacParser.Comparison_whileContext,0)


        def COLON(self):
            return self.getToken(JacParser.COLON, 0)

        def INDENT(self):
            return self.getToken(JacParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(JacParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_st_while




    def st_while(self):

        localctx = JacParser.St_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_st_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(JacParser.WHILE)
            if 1:
                    global while_max
                    local_while = while_max
                    print('BEGIN_WHILE_' + str(local_while) + ':')  
                    inside_while.append(local_while) 
                
            self.state = 168
            self.comparison_while()
            if 1:
                    while_max += 1
                
            self.state = 170
            self.match(JacParser.COLON)
            self.state = 171
            self.match(JacParser.INDENT)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.statement()
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.PRINT) | (1 << JacParser.RETURN) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            self.state = 177
            self.match(JacParser.DEDENT)
            if 1:
                    emit('goto BEGIN_WHILE_' + str(local_while), 0)
                    print('END_WHILE_' + str(local_while) + ':')
                    inside_while.pop()
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def arguments(self):
            return self.getTypedRuleContext(JacParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_st_call




    def st_call(self):

        localctx = JacParser.St_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_st_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 181
            self.match(JacParser.OP_PAR)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.READSTR) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER) | (1 << JacParser.STRING))) != 0):
                self.state = 182
                self.arguments()


            self.state = 185
            self.match(JacParser.CL_PAR)
            if 1:
                    global function_table, arg_max, function_error, has_return
                    I = ''
                    if (None if localctx._NAME is None else localctx._NAME.text)+'I' in function_table or (None if localctx._NAME is None else localctx._NAME.text)+'V' in function_table :
                        if (None if localctx._NAME is None else localctx._NAME.text)+'I' in function_table:
                            currentType = 'I'
                        else:
                            currentType = 'V'
                        if function_error == True:
                            if currentType == 'I':
                                sys.stderr.write('Error in function call: function "' + (None if localctx._NAME is None else localctx._NAME.text) + '" needs to return a value\n')
                            else:
                                sys.stderr.write('Error in function call: all arguments must be integer\n')
                            update_error()
                        if param_table[function_table.index((None if localctx._NAME is None else localctx._NAME.text)+currentType)] != arg_max:
                            sys.stderr.write('Error in function call: wrong number of arguments\n')
                            update_error()

                        for j in range(0, arg_max):
                            I += 'I'
                        print('    invokestatic Test/' + (None if localctx._NAME is None else localctx._NAME.text) + '(' + I + ')' + currentType)
                    else:
                        sys.stderr.write('Error in function call: function "' + (None if localctx._NAME is None else localctx._NAME.text) + '" not declared\n')
                        update_error()
                    arg_max = 0
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e = None # ExpressionContext

        def RETURN(self):
            return self.getToken(JacParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JacParser.RULE_st_return




    def st_return(self):

        localctx = JacParser.St_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_st_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(JacParser.RETURN)
            self.state = 189
            localctx.e = self.expression()
            if 1:
                    global has_return
                    if function_table[len(function_table)-1].endswith('V'):
                        sys.stderr.write('Error in return: void function cannot return a value\n')
                        update_error()
                    else:
                        if localctx.e.type == 'i':
                            print('    ireturn')
                        else:
                            sys.stderr.write('Error in return: function must return an integer value\n')
                            update_error()
                        has_return = True    
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JacParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.COMMA)
            else:
                return self.getToken(JacParser.COMMA, i)

        def getRuleIndex(self):
            return JacParser.RULE_arguments




    def arguments(self):

        localctx = JacParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    global arg_max, function_error
                    arg_max = 0
                
            self.state = 193
            localctx.e1 = self.expression()
            if 1:
                    arg_max += 1
                    if localctx.e1.type != 'i':
                        update_error()
                        function_error = True
                
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.COMMA:
                self.state = 195
                self.match(JacParser.COMMA)
                self.state = 196
                localctx.e2 = self.expression()
                if 1:
                        arg_max += 1
                        if localctx.e2.type != 'i':
                            function_error = True
                            update_error()
                    
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.e1 = None # ExpressionContext
            self.op = None # Token
            self.e2 = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JacParser.ExpressionContext,i)


        def EQ(self):
            return self.getToken(JacParser.EQ, 0)

        def NE(self):
            return self.getToken(JacParser.NE, 0)

        def GT(self):
            return self.getToken(JacParser.GT, 0)

        def GE(self):
            return self.getToken(JacParser.GE, 0)

        def LT(self):
            return self.getToken(JacParser.LT, 0)

        def LE(self):
            return self.getToken(JacParser.LE, 0)

        def getRuleIndex(self):
            return JacParser.RULE_comparison_if




    def comparison_if(self):

        localctx = JacParser.Comparison_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comparison_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            localctx.e1 = self.expression()
            self.state = 205
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 206
            localctx.e2 = self.expression()
            if 1:
                    if localctx.e1.type != localctx.e2.type:
                        sys.stderr.write('Error in comparison: operator cannot use string type\n')
                        update_error()
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.EQ:
                        localctx.type = 'if_icmpne'
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.NE:
                        localctx.type = 'if_icmpeq'
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GT:
                        localctx.type = 'if_icmple'
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GE:
                        localctx.type = 'if_icmplt'
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LT:
                        localctx.type = 'if_icmpge'
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LE:
                        localctx.type = 'if_icmpgt'
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e1 = None # ExpressionContext
            self.op = None # Token
            self.e2 = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JacParser.ExpressionContext,i)


        def EQ(self):
            return self.getToken(JacParser.EQ, 0)

        def NE(self):
            return self.getToken(JacParser.NE, 0)

        def GT(self):
            return self.getToken(JacParser.GT, 0)

        def GE(self):
            return self.getToken(JacParser.GE, 0)

        def LT(self):
            return self.getToken(JacParser.LT, 0)

        def LE(self):
            return self.getToken(JacParser.LE, 0)

        def getRuleIndex(self):
            return JacParser.RULE_comparison_while




    def comparison_while(self):

        localctx = JacParser.Comparison_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparison_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            localctx.e1 = self.expression()
            self.state = 210
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 211
            localctx.e2 = self.expression()
            if 1:
                    if localctx.e1.type != localctx.e2.type:
                        sys.stderr.write('Error in comparison: operator cannot use string type\n')
                        update_error()
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.EQ:
                        emit('if_icmpne END_WHILE_'+str(while_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.NE:
                        emit('if_icmpeq END_WHILE_'+str(while_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GT:
                        emit('if_icmple END_WHILE_'+str(while_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GE:
                        emit('if_icmplt END_WHILE_'+str(while_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LT:
                        emit('if_icmpge END_WHILE_'+str(while_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LE:
                        emit('if_icmpgt END_WHILE_'+str(while_max), -2)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.t1 = None # TermContext
            self.op = None # Token
            self.t2 = None # TermContext

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.TermContext)
            else:
                return self.getTypedRuleContext(JacParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.PLUS)
            else:
                return self.getToken(JacParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.MINUS)
            else:
                return self.getToken(JacParser.MINUS, i)

        def getRuleIndex(self):
            return JacParser.RULE_expression




    def expression(self):

        localctx = JacParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            localctx.t1 = self.term()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.PLUS or _la==JacParser.MINUS:
                self.state = 215
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==JacParser.PLUS or _la==JacParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 216
                localctx.t2 = self.term()
                if 1: 
                        if localctx.t1.type != localctx.t2.type or localctx.t1.type != 'i' or localctx.t2.type != 'i':
                            sys.stderr.write('Error in expression: operator cannot combine different types\n')
                            update_error()
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            emit('    iadd', -1)
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.MINUS:
                            emit('    isub', -1)
                    
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    localctx.type = localctx.t1.type
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.f1 = None # FactorContext
            self.op = None # Token
            self.f2 = None # FactorContext

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.FactorContext)
            else:
                return self.getTypedRuleContext(JacParser.FactorContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.TIMES)
            else:
                return self.getToken(JacParser.TIMES, i)

        def OVER(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.OVER)
            else:
                return self.getToken(JacParser.OVER, i)

        def REM(self, i:int=None):
            if i is None:
                return self.getTokens(JacParser.REM)
            else:
                return self.getToken(JacParser.REM, i)

        def getRuleIndex(self):
            return JacParser.RULE_term




    def term(self):

        localctx = JacParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            localctx.f1 = self.factor()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0):
                self.state = 227
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 228
                localctx.f2 = self.factor()
                if 1:
                        if localctx.f1.type != localctx.f2.type or localctx.f1.type != 'i' or localctx.f2.type != 'i':
                            sys.stderr.write('Error in term: operator cannot combine different types\n')
                            update_error()
                        else:
                            if (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES:
                                emit('    imul', -1)
                            if (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:
                                emit('    idiv', -1)
                            if (0 if localctx.op is None else localctx.op.type) == JacParser.REM:
                                emit('    irem', -1)
                    
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    localctx.type = localctx.f1.type
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self._NUMBER = None # Token
            self._STRING = None # Token
            self.e = None # ExpressionContext
            self._NAME = None # Token

        def NUMBER(self):
            return self.getToken(JacParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(JacParser.STRING, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def arguments(self):
            return self.getTypedRuleContext(JacParser.ArgumentsContext,0)


        def READINT(self):
            return self.getToken(JacParser.READINT, 0)

        def READSTR(self):
            return self.getToken(JacParser.READSTR, 0)

        def getRuleIndex(self):
            return JacParser.RULE_factor




    def factor(self):

        localctx = JacParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                localctx._NUMBER = self.match(JacParser.NUMBER)
                if 1:
                        global symbol_table, function_table, function_error
                        emit('    ldc ' + str((None if localctx._NUMBER is None else localctx._NUMBER.text)), +1)
                        localctx.type = 'i'
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                localctx._STRING = self.match(JacParser.STRING)
                if 1:
                        emit('    ldc ' + str((None if localctx._STRING is None else localctx._STRING.text)), +1)
                        localctx.type = 's'
                    
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(JacParser.OP_PAR)
                self.state = 243
                localctx.e = self.expression()
                self.state = 244
                self.match(JacParser.CL_PAR)
                if 1:
                        localctx.type = localctx.e.type
                    
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                localctx._NAME = self.match(JacParser.NAME)
                self.state = 248
                self.match(JacParser.OP_PAR)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.READSTR) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER) | (1 << JacParser.STRING))) != 0):
                    self.state = 249
                    self.arguments()


                self.state = 252
                self.match(JacParser.CL_PAR)
                if 1:
                        global arg_max
                        I = ''
                        if (None if localctx._NAME is None else localctx._NAME.text)+'I' in function_table:
                            currentType = 'I'
                        else:
                            currentType = 'V'
                        if (None if localctx._NAME is None else localctx._NAME.text)+currentType in function_table:
                            if function_table[function_table.index((None if localctx._NAME is None else localctx._NAME.text)+currentType)].endswith('V'):
                                update_error()
                                function_error = True
                                localctx.type = 'void'
                            else:
                                for i in range(arg_max):
                                    I += 'I'
                                print('    invokestatic Test/' + (None if localctx._NAME is None else localctx._NAME.text) + '(' + I + ')' + currentType)
                                localctx.type = 'i'
                    
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                localctx._NAME = self.match(JacParser.NAME)
                if 1:
                        if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                            sys.stderr.write('Error in factor: Variable ' + (None if localctx._NAME is None else localctx._NAME.text) + ' is not declared\n')
                            localctx.type = 'error'
                            exit(1)
                        else:
                            if symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] == 'i':
                                emit('    iload ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), +1)
                                used_table[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] = True
                                localctx.type = symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))]
                            elif symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] == 's':
                                emit('    aload ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), +1)
                                used_table[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] = True
                                localctx.type = symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))]
                    
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 256
                self.match(JacParser.READINT)
                self.state = 257
                self.match(JacParser.OP_PAR)
                self.state = 258
                self.match(JacParser.CL_PAR)
                if 1:
                        emit('invokestatic Runtime/readInt()I', +1)
                        localctx.type = 'i'
                    
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 260
                self.match(JacParser.READSTR)
                self.state = 261
                self.match(JacParser.OP_PAR)
                self.state = 262
                self.match(JacParser.CL_PAR)
                if 1:
                        emit('invokestatic Runtime/readString()Ljava/lang/String;', +1)
                        localctx.type = 's'
                    
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





