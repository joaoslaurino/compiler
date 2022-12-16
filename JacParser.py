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



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3!")
        buf.write("\u008e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\6\3!\n\3\r\3\16\3\"\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\5\5=\n\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\6\7M\n")
        buf.write("\7\r\7\16\7N\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\6")
        buf.write("\b[\n\b\r\b\16\b\\\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\7\13q\n\13\f")
        buf.write("\13\16\13t\13\13\3\f\3\f\3\f\3\f\3\f\7\f{\n\f\f\f\16\f")
        buf.write("~\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u008c\n\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\2\5\3\2\25\32\3\2\t\n\3\2\13\r\2\u008f\2\32\3\2\2\2\4")
        buf.write("\36\3\2\2\2\6+\3\2\2\2\b-\3\2\2\2\nA\3\2\2\2\fF\3\2\2")
        buf.write("\2\16S\3\2\2\2\20a\3\2\2\2\22f\3\2\2\2\24k\3\2\2\2\26")
        buf.write("u\3\2\2\2\30\u008b\3\2\2\2\32\33\b\2\1\2\33\34\5\4\3\2")
        buf.write("\34\35\7\2\2\3\35\3\3\2\2\2\36 \b\3\1\2\37!\5\6\4\2 \37")
        buf.write("\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%")
        buf.write("\b\3\1\2%\5\3\2\2\2&,\5\b\5\2\',\5\n\6\2(,\5\f\7\2),\5")
        buf.write("\16\b\2*,\7\36\2\2+&\3\2\2\2+\'\3\2\2\2+(\3\2\2\2+)\3")
        buf.write("\2\2\2+*\3\2\2\2,\7\3\2\2\2-.\7\7\2\2.<\7\16\2\2/\60\b")
        buf.write("\5\1\2\60\61\5\24\13\2\619\b\5\1\2\62\63\7\23\2\2\63\64")
        buf.write("\b\5\1\2\64\65\5\24\13\2\65\66\b\5\1\2\668\3\2\2\2\67")
        buf.write("\62\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:=\3\2\2\2")
        buf.write(";9\3\2\2\2</\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\7\17\2\2?@")
        buf.write("\b\5\1\2@\t\3\2\2\2AB\7\33\2\2BC\7\22\2\2CD\5\24\13\2")
        buf.write("DE\b\6\1\2E\13\3\2\2\2FG\7\3\2\2GH\5\20\t\2HI\b\7\1\2")
        buf.write("IJ\7\24\2\2JL\7 \2\2KM\5\6\4\2LK\3\2\2\2MN\3\2\2\2NL\3")
        buf.write("\2\2\2NO\3\2\2\2OP\3\2\2\2PQ\7!\2\2QR\b\7\1\2R\r\3\2\2")
        buf.write("\2ST\7\4\2\2TU\b\b\1\2UV\5\22\n\2VW\b\b\1\2WX\7\24\2\2")
        buf.write("XZ\7 \2\2Y[\5\6\4\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\")
        buf.write("]\3\2\2\2]^\3\2\2\2^_\7!\2\2_`\b\b\1\2`\17\3\2\2\2ab\5")
        buf.write("\24\13\2bc\t\2\2\2cd\5\24\13\2de\b\t\1\2e\21\3\2\2\2f")
        buf.write("g\5\24\13\2gh\t\2\2\2hi\5\24\13\2ij\b\n\1\2j\23\3\2\2")
        buf.write("\2kr\5\26\f\2lm\t\3\2\2mn\5\26\f\2no\b\13\1\2oq\3\2\2")
        buf.write("\2pl\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\25\3\2\2\2")
        buf.write("tr\3\2\2\2u|\5\30\r\2vw\t\4\2\2wx\5\30\r\2xy\b\f\1\2y")
        buf.write("{\3\2\2\2zv\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\27")
        buf.write("\3\2\2\2~|\3\2\2\2\177\u0080\7\34\2\2\u0080\u008c\b\r")
        buf.write("\1\2\u0081\u0082\7\16\2\2\u0082\u0083\5\24\13\2\u0083")
        buf.write("\u0084\7\17\2\2\u0084\u008c\3\2\2\2\u0085\u0086\7\33\2")
        buf.write("\2\u0086\u008c\b\r\1\2\u0087\u0088\7\b\2\2\u0088\u0089")
        buf.write("\7\16\2\2\u0089\u008a\7\17\2\2\u008a\u008c\b\r\1\2\u008b")
        buf.write("\177\3\2\2\2\u008b\u0081\3\2\2\2\u008b\u0085\3\2\2\2\u008b")
        buf.write("\u0087\3\2\2\2\u008c\31\3\2\2\2\13\"+9<N\\r|\u008b")
        return buf.getvalue()


class JacParser ( Parser ):

    grammarFileName = "Jac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'while'", "'break'", "'continue'", 
                     "'print'", "'readint'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'('", "')'", "'{'", "'}'", "'='", "','", "':'", 
                     "'=='", "'!='", "'>'", "'>='", "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>", "IF", "WHILE", "BREAK", "CONTINUE", "PRINT", 
                      "READINT", "PLUS", "MINUS", "TIMES", "OVER", "REM", 
                      "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", 
                      "COMMA", "COLON", "EQ", "NE", "GT", "GE", "LT", "LE", 
                      "NAME", "NUMBER", "COMMENT", "NL", "SPACE", "INDENT", 
                      "DEDENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_attrib = 4
    RULE_st_if = 5
    RULE_st_while = 6
    RULE_comparison_if = 7
    RULE_comparison_while = 8
    RULE_expression = 9
    RULE_term = 10
    RULE_factor = 11

    ruleNames =  [ "program", "main", "statement", "st_print", "st_attrib", 
                   "st_if", "st_while", "comparison_if", "comparison_while", 
                   "expression", "term", "factor" ]

    EOF = Token.EOF
    IF=1
    WHILE=2
    BREAK=3
    CONTINUE=4
    PRINT=5
    READINT=6
    PLUS=7
    MINUS=8
    TIMES=9
    OVER=10
    REM=11
    OP_PAR=12
    CL_PAR=13
    OP_CUR=14
    CL_CUR=15
    ATTRIB=16
    COMMA=17
    COLON=18
    EQ=19
    NE=20
    GT=21
    GE=22
    LT=23
    LE=24
    NAME=25
    NUMBER=26
    COMMENT=27
    NL=28
    SPACE=29
    INDENT=30
    DEDENT=31

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


        def EOF(self):
            return self.getToken(JacParser.EOF, 0)

        def getRuleIndex(self):
            return JacParser.RULE_program




    def program(self):

        localctx = JacParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
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
                
            self.state = 25
            self.main()
            self.state = 26
            self.match(JacParser.EOF)
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
                
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self.statement()
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            if 1:
                    print('    return')
                    if (len(symbol_table) > 0):
                        print('.limit locals ' + str(len(symbol_table)))
                    print('.limit stack ' + str(stack_max))
                    print('.end method')
                    print('\n; symbol_table:', symbol_table)
                
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


        def NL(self):
            return self.getToken(JacParser.NL, 0)

        def getRuleIndex(self):
            return JacParser.RULE_statement




    def statement(self):

        localctx = JacParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.st_print()
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.st_attrib()
                pass
            elif token in [JacParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.st_if()
                pass
            elif token in [JacParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.st_while()
                pass
            elif token in [JacParser.NL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.match(JacParser.NL)
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


    class St_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 6, self.RULE_st_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(JacParser.PRINT)
            self.state = 44
            self.match(JacParser.OP_PAR)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.READINT) | (1 << JacParser.OP_PAR) | (1 << JacParser.NAME) | (1 << JacParser.NUMBER))) != 0):
                if 1:
                        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 46
                self.expression()
                if 1:
                        emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
                    
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JacParser.COMMA:
                    self.state = 48
                    self.match(JacParser.COMMA)
                    if 1:
                            emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                        
                    self.state = 50
                    self.expression()
                    if 1:
                            emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
                        
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 60
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
        self.enterRule(localctx, 8, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            localctx._NAME = self.match(JacParser.NAME)
            self.state = 64
            self.match(JacParser.ATTRIB)
            self.state = 65
            self.expression()
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                        symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                    emit('    istore ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), +1)
                
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

        def IF(self):
            return self.getToken(JacParser.IF, 0)

        def comparison_if(self):
            return self.getTypedRuleContext(JacParser.Comparison_ifContext,0)


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
            return JacParser.RULE_st_if




    def st_if(self):

        localctx = JacParser.St_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(JacParser.IF)
            self.state = 69
            self.comparison_if()
            if 1:
                    global if_max
                    local_if = if_max
                    if_max += 1
                
            self.state = 71
            self.match(JacParser.COLON)
            self.state = 72
            self.match(JacParser.INDENT)
            self.state = 74 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 73
                self.statement()
                self.state = 76 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            self.state = 78
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
        self.enterRule(localctx, 12, self.RULE_st_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(JacParser.WHILE)
            if 1:
                    global while_max
                    local_while = while_max
                    print('BEGIN_WHILE_' + str(local_while) + ':')  
                
            self.state = 83
            self.comparison_while()
            if 1:
                    while_max += 1
                
            self.state = 85
            self.match(JacParser.COLON)
            self.state = 86
            self.match(JacParser.INDENT)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self.statement()
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.IF) | (1 << JacParser.WHILE) | (1 << JacParser.PRINT) | (1 << JacParser.NAME) | (1 << JacParser.NL))) != 0)):
                    break

            self.state = 92
            self.match(JacParser.DEDENT)
            if 1:
                    emit('goto BEGIN_WHILE_' + str(local_while), 0)
                    print('END_WHILE_' + str(local_while) + ':')
                
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
        self.enterRule(localctx, 14, self.RULE_comparison_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.expression()
            self.state = 96
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 97
            self.expression()
            if 1:
                    if (0 if localctx.op is None else localctx.op.type) == JacParser.EQ:
                        emit('if_icmpne NOT_IF_'+str(if_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.NE:
                        emit('if_icmpeq NOT_IF_'+str(if_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GT:
                        emit('if_icmple NOT_IF_'+str(if_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.GE:
                        emit('if_icmplt NOT_IF_'+str(if_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LT:
                        emit('if_icmpge NOT_IF_'+str(if_max), -2)
                    elif (0 if localctx.op is None else localctx.op.type) == JacParser.LE:
                        emit('if_icmpgt NOT_IF_'+str(if_max), -2)
                
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
        self.enterRule(localctx, 16, self.RULE_comparison_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.expression()
            self.state = 101
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.EQ) | (1 << JacParser.NE) | (1 << JacParser.GT) | (1 << JacParser.GE) | (1 << JacParser.LT) | (1 << JacParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 102
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
            self.op = None # Token

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
        self.enterRule(localctx, 18, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.term()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JacParser.PLUS or _la==JacParser.MINUS:
                self.state = 106
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==JacParser.PLUS or _la==JacParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 107
                self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == JacParser.PLUS:
                            emit('    iadd', -1)
                        else:
                            emit('    isub', -1)
                    
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.op = None # Token

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
        self.enterRule(localctx, 20, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.factor()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0):
                self.state = 116
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JacParser.TIMES) | (1 << JacParser.OVER) | (1 << JacParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117
                self.factor()
                if 1:
                        if   (0 if localctx.op is None else localctx.op.type) == JacParser.TIMES:
                            emit('    imul', -1)
                        elif (0 if localctx.op is None else localctx.op.type) == JacParser.OVER:
                            emit('    idiv', -1)
                        else:
                            emit('    irem', -1)
                    
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self._NUMBER = None # Token
            self._NAME = None # Token

        def NUMBER(self):
            return self.getToken(JacParser.NUMBER, 0)

        def OP_PAR(self):
            return self.getToken(JacParser.OP_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(JacParser.ExpressionContext,0)


        def CL_PAR(self):
            return self.getToken(JacParser.CL_PAR, 0)

        def NAME(self):
            return self.getToken(JacParser.NAME, 0)

        def READINT(self):
            return self.getToken(JacParser.READINT, 0)

        def getRuleIndex(self):
            return JacParser.RULE_factor




    def factor(self):

        localctx = JacParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JacParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                localctx._NUMBER = self.match(JacParser.NUMBER)
                if 1:
                        emit('    ldc ' + str((None if localctx._NUMBER is None else localctx._NUMBER.text)), +1)
                    
                pass
            elif token in [JacParser.OP_PAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(JacParser.OP_PAR)
                self.state = 128
                self.expression()
                self.state = 129
                self.match(JacParser.CL_PAR)
                pass
            elif token in [JacParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                localctx._NAME = self.match(JacParser.NAME)
                if 1:
                        emit('    iload ' +  str(symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))), +1)
                    
                pass
            elif token in [JacParser.READINT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.match(JacParser.READINT)
                self.state = 134
                self.match(JacParser.OP_PAR)
                self.state = 135
                self.match(JacParser.CL_PAR)
                if 1:
                        emit('    invokestatic Runtime/readInt()I', +1)
                    
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





