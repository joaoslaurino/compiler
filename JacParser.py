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

stack_cur = 0 
stack_max = 0
if_max = 1
while_max = 1

def emit(bytecode, delta):
    global stack_cur, stack_max
    stack_cur += delta
    if stack_cur > stack_max:
        stack_max = stack_cur
    print('    ' + bytecode + '    ; delta=' + str(delta))

def if_counter():
    global if_max
    if_max += 1

def resetcounters():
    global stack_cur, stack_max, if_max, while_max
    stack_cur = 0
    stack_max = 0
    if_max = 1
    while_max = 1



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$")
        buf.write("\u00c3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\7\2%\n\2\f")
        buf.write("\2\16\2(\13\2\3\2\3\2\3\3\3\3\6\3.\n\3\r\3\16\3/\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\6\4<\n\4\r\4\16\4=")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5K\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6W\n\6\f\6")
        buf.write("\16\6Z\13\6\5\6\\\n\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\6\bl\n\b\r\b\16\bm\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\6\13\u0080\n\13\r\13\16\13\u0081\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\7\17\u009b\n")
        buf.write("\17\f\17\16\17\u009e\13\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\7\20\u00a7\n\20\f\20\16\20\u00aa\13\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c1")
        buf.write("\n\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \2\5\3\2\27\34\3\2\13\f\3\2\r\17\2\u00c7\2\"\3\2\2")
        buf.write("\2\4+\3\2\2\2\6\63\3\2\2\2\bJ\3\2\2\2\nL\3\2\2\2\f`\3")
        buf.write("\2\2\2\16e\3\2\2\2\20r\3\2\2\2\22u\3\2\2\2\24x\3\2\2\2")
        buf.write("\26\u0086\3\2\2\2\30\u008b\3\2\2\2\32\u0090\3\2\2\2\34")
        buf.write("\u0095\3\2\2\2\36\u00a1\3\2\2\2 \u00c0\3\2\2\2\"&\b\2")
        buf.write("\1\2#%\5\6\4\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2")
        buf.write("\2\')\3\2\2\2(&\3\2\2\2)*\5\4\3\2*\3\3\2\2\2+-\b\3\1\2")
        buf.write(",.\5\b\5\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\62\b\3\1\2\62\5\3\2\2\2\63\64\7\n\2\2\64")
        buf.write("\65\7\35\2\2\65\66\7\20\2\2\66\67\7\21\2\2\678\7\26\2")
        buf.write("\289\b\4\1\29;\7#\2\2:<\5\b\5\2;:\3\2\2\2<=\3\2\2\2=;")
        buf.write("\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\7$\2\2@A\b\4\1\2A\7\3\2")
        buf.write("\2\2BK\5\n\6\2CK\5\f\7\2DK\5\16\b\2EK\5\24\13\2FK\5\20")
        buf.write("\t\2GK\5\22\n\2HK\5\26\f\2IK\7 \2\2JB\3\2\2\2JC\3\2\2")
        buf.write("\2JD\3\2\2\2JE\3\2\2\2JF\3\2\2\2JG\3\2\2\2JH\3\2\2\2J")
        buf.write("I\3\2\2\2K\t\3\2\2\2LM\7\7\2\2M[\7\20\2\2NO\b\6\1\2OP")
        buf.write("\5\34\17\2PX\b\6\1\2QR\7\25\2\2RS\b\6\1\2ST\5\34\17\2")
        buf.write("TU\b\6\1\2UW\3\2\2\2VQ\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3")
        buf.write("\2\2\2Y\\\3\2\2\2ZX\3\2\2\2[N\3\2\2\2[\\\3\2\2\2\\]\3")
        buf.write("\2\2\2]^\7\21\2\2^_\b\6\1\2_\13\3\2\2\2`a\7\35\2\2ab\7")
        buf.write("\24\2\2bc\5\34\17\2cd\b\7\1\2d\r\3\2\2\2ef\7\3\2\2fg\5")
        buf.write("\30\r\2gh\7\26\2\2hi\b\b\1\2ik\7#\2\2jl\5\b\5\2kj\3\2")
        buf.write("\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2no\3\2\2\2op\7$\2\2")
        buf.write("pq\b\b\1\2q\17\3\2\2\2rs\7\5\2\2st\b\t\1\2t\21\3\2\2\2")
        buf.write("uv\7\6\2\2vw\b\n\1\2w\23\3\2\2\2xy\7\4\2\2yz\b\13\1\2")
        buf.write("z{\5\32\16\2{|\b\13\1\2|}\7\26\2\2}\177\7#\2\2~\u0080")
        buf.write("\5\b\5\2\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\177\3")
        buf.write("\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\7$\2\2\u0084\u0085\b\13\1\2\u0085\25\3\2\2\2\u0086\u0087")
        buf.write("\7\35\2\2\u0087\u0088\7\20\2\2\u0088\u0089\7\21\2\2\u0089")
        buf.write("\u008a\b\f\1\2\u008a\27\3\2\2\2\u008b\u008c\5\34\17\2")
        buf.write("\u008c\u008d\t\2\2\2\u008d\u008e\5\34\17\2\u008e\u008f")
        buf.write("\b\r\1\2\u008f\31\3\2\2\2\u0090\u0091\5\34\17\2\u0091")
        buf.write("\u0092\t\2\2\2\u0092\u0093\5\34\17\2\u0093\u0094\b\16")
        buf.write("\1\2\u0094\33\3\2\2\2\u0095\u009c\5\36\20\2\u0096\u0097")
        buf.write("\t\3\2\2\u0097\u0098\5\36\20\2\u0098\u0099\b\17\1\2\u0099")
        buf.write("\u009b\3\2\2\2\u009a\u0096\3\2\2\2\u009b\u009e\3\2\2\2")
        buf.write("\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f\3")
        buf.write("\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\b\17\1\2\u00a0")
        buf.write("\35\3\2\2\2\u00a1\u00a8\5 \21\2\u00a2\u00a3\t\4\2\2\u00a3")
        buf.write("\u00a4\5 \21\2\u00a4\u00a5\b\20\1\2\u00a5\u00a7\3\2\2")
        buf.write("\2\u00a6\u00a2\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00ab\u00ac\b\20\1\2\u00ac\37\3\2\2\2\u00ad")
        buf.write("\u00ae\7\36\2\2\u00ae\u00c1\b\21\1\2\u00af\u00b0\7!\2")
        buf.write("\2\u00b0\u00c1\b\21\1\2\u00b1\u00b2\7\20\2\2\u00b2\u00b3")
        buf.write("\5\34\17\2\u00b3\u00b4\7\21\2\2\u00b4\u00b5\b\21\1\2\u00b5")
        buf.write("\u00c1\3\2\2\2\u00b6\u00b7\7\35\2\2\u00b7\u00c1\b\21\1")
        buf.write("\2\u00b8\u00b9\7\b\2\2\u00b9\u00ba\7\20\2\2\u00ba\u00bb")
        buf.write("\7\21\2\2\u00bb\u00c1\b\21\1\2\u00bc\u00bd\7\t\2\2\u00bd")
        buf.write("\u00be\7\20\2\2\u00be\u00bf\7\21\2\2\u00bf\u00c1\b\21")
        buf.write("\1\2\u00c0\u00ad\3\2\2\2\u00c0\u00af\3\2\2\2\u00c0\u00b1")
        buf.write("\3\2\2\2\u00c0\u00b6\3\2\2\2\u00c0\u00b8\3\2\2\2\u00c0")
        buf.write("\u00bc\3\2\2\2\u00c1!\3\2\2\2\r&/=JX[m\u0081\u009c\u00a8")
        buf.write("\u00c0")
        return buf.getvalue()


class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'while'", "'break'", "'continue'", 
                     "'print'", "'readint'", "'readstr'", "'def'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'{'", "'}'", 
                     "'='", "','", "':'", "'=='", "'!='", "'>'", "'>='", 
                     "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>", "IF", "WHILE", "BREAK", "CONTINUE", "PRINT", 
                      "READINT", "READSTR", "DEF", "PLUS", "MINUS", "TIMES", 
                      "OVER", "REM", "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", 
                      "ATTRIB", "COMMA", "COLON", "EQ", "NE", "GT", "GE", 
                      "LT", "LE", "NAME", "NUMBER", "COMMENT", "NL", "STRING", 
                      "SPACE", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_function = 2
    RULE_statement = 3
    RULE_st_print = 4
    RULE_st_attrib = 5
    RULE_st_if = 6
    RULE_st_break = 7
    RULE_st_continue = 8
    RULE_st_while = 9
    RULE_st_call = 10
    RULE_comparison_if = 11
    RULE_comparison_while = 12
    RULE_expression = 13
    RULE_term = 14
    RULE_factor = 15

    ruleNames =  [ "program", "main", "function", "statement", "st_print", 
                   "st_attrib", "st_if", "st_break", "st_continue", "st_while", 
                   "st_call", "comparison_if", "comparison_while", "expression", 
                   "term", "factor" ]

    EOF = Token.EOF
    IF=1
    WHILE=2
    BREAK=3
    CONTINUE=4
    PRINT=5
    READINT=6
    READSTR=7
    DEF=8
    PLUS=9
    MINUS=10
    TIMES=11
    OVER=12
    REM=13
    OP_PAR=14
    CL_PAR=15
    OP_CUR=16
    CL_CUR=17
    ATTRIB=18
    COMMA=19
    COLON=20
    EQ=21
    NE=22
    GT=23
    GE=24
    LT=25
    LE=26
    NAME=27
    NUMBER=28
    COMMENT=29
    NL=30
    STRING=31
    SPACE=32
    INDENT=33
    DEDENT=34

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
                
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.DEF:
                self.state = 33
                self.function()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
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
                
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.statement()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    print('    return')
                    if (len(symbol_table) > 0):
                        print('.limit locals ' + str(len(symbol_table)))
                    print('.limit stack ' + str(stack_max))
                    print('.end method')
                    print('\n; symbol_table:', symbol_table)
                    print('; symbol_type:', symbol_type)
                    print('; used_table:', used_table)
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
            return JacParser.RULE_function




    def function(self):

        localctx = JacParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(JacParser.DEF)
            self.state = 50
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 51
            self.match(JacParser.OP_PAR)
            self.state = 52
            self.match(JacParser.CL_PAR)
            self.state = 53
            self.match(JacParser.COLON)
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) not in declared_table:
                        declared_table.append((None if localctx._NAME is None else localctx._NAME.text))
                    else:
                        sys.stderr.write('Error: function ' + (None if localctx._NAME is None else localctx._NAME.text) + ' already declared\n')
                        exit(1)

                    print('.method public static ' + (None if localctx._NAME is None else localctx._NAME.text) + '()V')
                
            self.state = 55
            self.match(JacParser.INDENT)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.statement()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            self.state = 61
            self.match(JacParser.DEDENT)
            if 1:
                    print('    return')
                    if (len(symbol_table) > 0):
                        print('.limit locals ' + str(len(symbol_table)))
                    print('.limit stack ' + str(stack_max))
                    print('.end method')
                    resetcounters()
                
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


        def NL(self):
            return self.getToken(JacParser.NL, 0)

        def getRuleIndex(self):
            return JacParser.RULE_statement




    def statement(self):

        localctx = JacParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.st_print()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.st_attrib()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.st_if()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.st_while()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.st_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.st_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 70
                self.st_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 71
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
        self.enterRule(localctx, 8, self.RULE_st_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(JacParser.PRINT)
            self.state = 75
            self.match(JacParser.OP_PAR)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.READSTR) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER) | (1 << JacParser.STRING))) != 0):
                if 1:
                        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 77
                localctx.e1 = self.expression()
                if 1:
                        if localctx.e1.type == 'i':
                            emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
                        elif localctx.e1.type == 's':
                            emit('    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                        else:
                            sys.stderr.write('************ HELP ************\n')
                            exit(1)
                    
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JacParser.COMMA:
                    self.state = 79
                    self.match(JacParser.COMMA)
                    if 1:
                            emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                        
                    self.state = 81
                    localctx.e2 = self.expression()
                    if 1:
                            if localctx.e2.type == 'i':
                                emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
                            elif localctx.e2.type == 's':
                                emit('    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                            else:
                                sys.stderr.write('************ HELP ************\n')
                                exit(1)
                        
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 91
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
        self.enterRule(localctx, 10, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 95
            self.match(JacParser.ATTRIB)
            self.state = 96
            localctx._expression = self.expression()
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                        symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                        symbol_type.append(localctx._expression.type)
                        used_table.append(False)
                    if localctx._expression.type == 'i':
                        emit('    istore ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), +1)
                    elif localctx._expression.type == 's':
                        emit('    astore ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), +1)
                    else:
                        sys.stderr.write('*HELP NAME ATTRIB*')
                        exit(1)
                
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

        def COLON(self):
            return self.getToken(JacParser.COLON, 0)

        def INDENT(self):
            return self.getToken(JacParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(JacParser.DEDENT, 0)

        def comparison_if(self):
            return self.getTypedRuleContext(JacParser.Comparison_ifContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JacParser.StatementContext)
            else:
                return self.getTypedRuleContext(JacParser.StatementContext,i)


        def getRuleIndex(self):
            return JacParser.RULE_st_if




    def st_if(self):

        localctx = JacParser.St_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(JacParser.IF)
            self.state = 100
            localctx.cmp = self.comparison_if()
            self.state = 101
            self.match(JacParser.COLON)
            if 1:
                    global if_max
                    emit(localctx.cmp.type + '  NOT_IF_' + str(if_max), -2)
                    local_if = if_max
                    if_max += 1
                
            self.state = 103
            self.match(JacParser.INDENT)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.statement()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            self.state = 109
            self.match(JacParser.DEDENT)
            if 1:
                    print('NOT_IF_' + str(local_if) + ':')
                    if_counter()
                
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
        self.enterRule(localctx, 14, self.RULE_st_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
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
        self.enterRule(localctx, 16, self.RULE_st_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
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
        self.enterRule(localctx, 18, self.RULE_st_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(JacParser.WHILE)
            if 1:
                    global while_max
                    local_while = while_max
                    print('BEGIN_WHILE_' + str(local_while) + ':')  
                    inside_while.append(local_while) 
                
            self.state = 120
            self.comparison_while()
            if 1:
                    while_max += 1
                
            self.state = 122
            self.match(JacParser.COLON)
            self.state = 123
            self.match(JacParser.INDENT)
            self.state = 125 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 124
                self.statement()
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.BREAK) | (1 << JacParser.CONTINUE) | (1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            self.state = 129
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

        def getRuleIndex(self):
            return JacParser.RULE_st_call




    def st_call(self):

        localctx = JacParser.St_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_st_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 133
            self.match(JacParser.OP_PAR)
            self.state = 134
            self.match(JacParser.CL_PAR)
            if 1:
                    print('    invokestatic Test/' + (None if localctx._NAME is None else localctx._NAME.text) + '()V')
                
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
            self.op = None # Token

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
        self.enterRule(localctx, 22, self.RULE_comparison_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.expression()
            self.state = 138
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 139
            self.expression()
            if 1:
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
            self.op = None # Token

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
        self.enterRule(localctx, 24, self.RULE_comparison_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.expression()
            self.state = 143
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 144
            self.expression()
            if 1:
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
        self.enterRule(localctx, 26, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            localctx.t1 = self.term()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.PLUS or _la==JacParser.MINUS:
                self.state = 148
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==JacParser.PLUS or _la==JacParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 149
                localctx.t2 = self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            emit('    iadd', -1)
                        else:
                            emit('    isub', -1)
                    
                self.state = 156
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
        self.enterRule(localctx, 28, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            localctx.f1 = self.factor()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0):
                self.state = 160
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 161
                localctx.f2 = self.factor()
                if 1:
                        if   (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES:
                            emit('    imul', -1)
                        elif (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:
                            emit('    idiv', -1)
                        else:
                            emit('    irem', -1)
                    
                self.state = 168
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

        def READINT(self):
            return self.getToken(JacParser.READINT, 0)

        def READSTR(self):
            return self.getToken(JacParser.READSTR, 0)

        def getRuleIndex(self):
            return JacParser.RULE_factor




    def factor(self):

        localctx = JacParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                localctx._NUMBER = self.match(JacParser.NUMBER)
                if 1:
                        emit('    ldc ' + str((None if localctx._NUMBER is None else localctx._NUMBER.text)), +1)
                        localctx.type = 'i'
                    
                pass
            elif token in [JacParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                localctx._STRING = self.match(JacParser.STRING)
                if 1:
                        emit('    ldc ' + str((None if localctx._STRING is None else localctx._STRING.text)), +1)
                        localctx.type = 's'
                    
                pass
            elif token in [JacParser.OP_PAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.match(JacParser.OP_PAR)
                self.state = 176
                localctx.e = self.expression()
                self.state = 177
                self.match(JacParser.CL_PAR)
                if 1:
                        localctx.type = localctx.e.type
                    
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                localctx._NAME = self.match(JacParser.NAME)
                if 1:
                        if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                            sys.stderr.write('Variable ' + (None if localctx._NAME is None else localctx._NAME.text) + ' is not defined\n')
                            sys.exit(1)
                        elif symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] == 'i':
                            emit('    iload ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), +1)
                            used_table[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] = True
                            localctx.type = symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))]
                        elif symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] == 's':
                            emit('    aload ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), +1)
                            used_table[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))] = True
                            localctx.type = symbol_type[symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))]
                    
                pass
            elif token in [JacParser.READINT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.match(JacParser.READINT)
                self.state = 183
                self.match(JacParser.OP_PAR)
                self.state = 184
                self.match(JacParser.CL_PAR)
                if 1:
                        emit('    invokestatic Runtime/readInt()I', +1)
                        localctx.type = 'i'
                    
                pass
            elif token in [JacParser.READSTR]:
                self.enterOuterAlt(localctx, 6)
                self.state = 186
                self.match(JacParser.READSTR)
                self.state = 187
                self.match(JacParser.OP_PAR)
                self.state = 188
                self.match(JacParser.CL_PAR)
                if 1:
                        emit('    invokestatic Runtime/readString()Ljava/lang/String;', +1)
                        localctx.type = 's'
                    
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





