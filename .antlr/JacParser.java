// Generated from /home/joaolaurino/Documents/University/Compilers/jac-compiler/Jac.g4 by ANTLR 4.9.2

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


import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JacParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, WHILE=2, BREAK=3, CONTINUE=4, PRINT=5, READINT=6, READSTR=7, DEF=8, 
		PLUS=9, MINUS=10, TIMES=11, OVER=12, REM=13, OP_PAR=14, CL_PAR=15, OP_CUR=16, 
		CL_CUR=17, ATTRIB=18, COMMA=19, COLON=20, EQ=21, NE=22, GT=23, GE=24, 
		LT=25, LE=26, NAME=27, NUMBER=28, COMMENT=29, NL=30, STRING=31, SPACE=32, 
		INDENT=33, DEDENT=34;
	public static final int
		RULE_program = 0, RULE_main = 1, RULE_function = 2, RULE_statement = 3, 
		RULE_st_print = 4, RULE_st_attrib = 5, RULE_st_if = 6, RULE_st_break = 7, 
		RULE_st_continue = 8, RULE_st_while = 9, RULE_st_call = 10, RULE_comparison_if = 11, 
		RULE_comparison_while = 12, RULE_expression = 13, RULE_term = 14, RULE_factor = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main", "function", "statement", "st_print", "st_attrib", 
			"st_if", "st_break", "st_continue", "st_while", "st_call", "comparison_if", 
			"comparison_while", "expression", "term", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'while'", "'break'", "'continue'", "'print'", "'readint'", 
			"'readstr'", "'def'", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", 
			"'{'", "'}'", "'='", "','", "':'", "'=='", "'!='", "'>'", "'>='", "'<'", 
			"'<='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "WHILE", "BREAK", "CONTINUE", "PRINT", "READINT", "READSTR", 
			"DEF", "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", "CL_PAR", "OP_CUR", 
			"CL_CUR", "ATTRIB", "COMMA", "COLON", "EQ", "NE", "GT", "GE", "LT", "LE", 
			"NAME", "NUMBER", "COMMENT", "NL", "STRING", "SPACE", "INDENT", "DEDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Jac.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public JacParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			if 1:
			        print('.source Test.src')
			        print('.class  public Test')
			        print('.super  java/lang/Object\n')
			        print('.method public <init>()V')
			        print('    aload_0')
			        print('    invokenonvirtual java/lang/Object/<init>()V')
			        print('    return')
			        print('.end method\n')
			    
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DEF) {
				{
				{
				setState(33);
				function();
				}
				}
				setState(38);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(39);
			main();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			if 1:
			        print('.method public static main([Ljava/lang/String;)V\n')
			    
			setState(43); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(42);
				statement();
				}
				}
				setState(45); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << PRINT) | (1L << NAME) | (1L << NL))) != 0) );
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
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public Token NAME;
		public TerminalNode DEF() { return getToken(JacParser.DEF, 0); }
		public TerminalNode NAME() { return getToken(JacParser.NAME, 0); }
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public TerminalNode COLON() { return getToken(JacParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(JacParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(JacParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			match(DEF);
			setState(50);
			((FunctionContext)_localctx).NAME = match(NAME);
			setState(51);
			match(OP_PAR);
			setState(52);
			match(CL_PAR);
			setState(53);
			match(COLON);
			if 1:
			        if (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null) not in declared_table:
			            declared_table.append((((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null))
			        else:
			            sys.stderr.write('Error: function ' + (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null) + ' already declared\n')
			            exit(1)

			        print('.method public static ' + (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null) + '()V')
			    
			setState(55);
			match(INDENT);
			setState(57); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(56);
				statement();
				}
				}
				setState(59); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << PRINT) | (1L << NAME) | (1L << NL))) != 0) );
			setState(61);
			match(DEDENT);
			if 1:
			        print('    return')
			        if (len(symbol_table) > 0):
			            print('.limit locals ' + str(len(symbol_table)))
			        print('.limit stack ' + str(stack_max))
			        print('.end method')
			        resetcounters()
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public St_printContext st_print() {
			return getRuleContext(St_printContext.class,0);
		}
		public St_attribContext st_attrib() {
			return getRuleContext(St_attribContext.class,0);
		}
		public St_ifContext st_if() {
			return getRuleContext(St_ifContext.class,0);
		}
		public St_whileContext st_while() {
			return getRuleContext(St_whileContext.class,0);
		}
		public St_breakContext st_break() {
			return getRuleContext(St_breakContext.class,0);
		}
		public St_continueContext st_continue() {
			return getRuleContext(St_continueContext.class,0);
		}
		public St_callContext st_call() {
			return getRuleContext(St_callContext.class,0);
		}
		public TerminalNode NL() { return getToken(JacParser.NL, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement);
		try {
			setState(72);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(64);
				st_print();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(65);
				st_attrib();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(66);
				st_if();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(67);
				st_while();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(68);
				st_break();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(69);
				st_continue();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(70);
				st_call();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(71);
				match(NL);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_printContext extends ParserRuleContext {
		public ExpressionContext e1;
		public ExpressionContext e2;
		public TerminalNode PRINT() { return getToken(JacParser.PRINT, 0); }
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(JacParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(JacParser.COMMA, i);
		}
		public St_printContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_print; }
	}

	public final St_printContext st_print() throws RecognitionException {
		St_printContext _localctx = new St_printContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_st_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(PRINT);
			setState(75);
			match(OP_PAR);
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READINT) | (1L << READSTR) | (1L << OP_PAR) | (1L << NAME) | (1L << NUMBER) | (1L << STRING))) != 0)) {
				{
				if 1:
				        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
				    
				setState(77);
				((St_printContext)_localctx).e1 = expression();
				if 1:
				        if ((St_printContext)_localctx).e1.type == 'i':
				            emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
				        elif ((St_printContext)_localctx).e1.type == 's':
				            emit('    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
				        else:
				            sys.stderr.write('************ HELP ************\n')
				            exit(1)
				    
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(79);
					match(COMMA);
					if 1:
					        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
					    
					setState(81);
					((St_printContext)_localctx).e2 = expression();
					if 1:
					        if ((St_printContext)_localctx).e2.type == 'i':
					            emit('    invokevirtual java/io/PrintStream/print(I)V\n', -2)
					        elif ((St_printContext)_localctx).e2.type == 's':
					            emit('    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
					        else:
					            sys.stderr.write('************ HELP ************\n')
					            exit(1)
					    
					}
					}
					setState(88);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(91);
			match(CL_PAR);
			if 1:
			        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
			        emit('    invokevirtual java/io/PrintStream/println()V\n', -1)
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_attribContext extends ParserRuleContext {
		public Token NAME;
		public ExpressionContext expression;
		public TerminalNode NAME() { return getToken(JacParser.NAME, 0); }
		public TerminalNode ATTRIB() { return getToken(JacParser.ATTRIB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public St_attribContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_attrib; }
	}

	public final St_attribContext st_attrib() throws RecognitionException {
		St_attribContext _localctx = new St_attribContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_st_attrib);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			((St_attribContext)_localctx).NAME = match(NAME);
			setState(95);
			match(ATTRIB);
			setState(96);
			((St_attribContext)_localctx).expression = expression();
			if 1:
			        if (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) not in symbol_table:
			            symbol_table.append((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null))
			            symbol_type.append(((St_attribContext)_localctx).expression.type)
			            used_table.append(False)

			        if ((St_attribContext)_localctx).expression.type == 'i':
			            emit('    istore ' +  str(symbol_table.index((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null))), +1)
			        elif ((St_attribContext)_localctx).expression.type == 's':
			            emit('    astore ' +  str(symbol_table.index((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null))), +1)
			        else:   
			            sys.stderr.write('*HELP NAME ATTRIB*')
			            exit(1)
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_ifContext extends ParserRuleContext {
		public Comparison_ifContext cmp;
		public TerminalNode IF() { return getToken(JacParser.IF, 0); }
		public TerminalNode COLON() { return getToken(JacParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(JacParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(JacParser.DEDENT, 0); }
		public Comparison_ifContext comparison_if() {
			return getRuleContext(Comparison_ifContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public St_ifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_if; }
	}

	public final St_ifContext st_if() throws RecognitionException {
		St_ifContext _localctx = new St_ifContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_st_if);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(IF);
			setState(100);
			((St_ifContext)_localctx).cmp = comparison_if();
			setState(101);
			match(COLON);
			if 1:
			        global if_max
			        emit(((St_ifContext)_localctx).cmp.type + '  NOT_IF_' + str(if_max), -2)
			        local_if = if_max
			        if_max += 1
			    
			setState(103);
			match(INDENT);
			setState(105); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(104);
				statement();
				}
				}
				setState(107); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << PRINT) | (1L << NAME) | (1L << NL))) != 0) );
			setState(109);
			match(DEDENT);
			if 1:
			        print('NOT_IF_' + str(local_if) + ':')
			        if_counter()
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_breakContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(JacParser.BREAK, 0); }
		public St_breakContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_break; }
	}

	public final St_breakContext st_break() throws RecognitionException {
		St_breakContext _localctx = new St_breakContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_st_break);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(BREAK);
			if 1:
			        if len(inside_while) == 0:
			            sys.stderr.write('**ERROR** break outside while\n')
			            exit(1)
			        emit('goto END_WHILE_' + str(while_max -1), 0)
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_continueContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(JacParser.CONTINUE, 0); }
		public St_continueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_continue; }
	}

	public final St_continueContext st_continue() throws RecognitionException {
		St_continueContext _localctx = new St_continueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_st_continue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(CONTINUE);
			if 1:
			        if len(inside_while) == 0:
			            sys.stderr.write('**ERROR** continue outside while\n')
			            exit(1)
			        emit('goto BEGIN_WHILE_' + str(while_max - 1), 0)
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_whileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(JacParser.WHILE, 0); }
		public Comparison_whileContext comparison_while() {
			return getRuleContext(Comparison_whileContext.class,0);
		}
		public TerminalNode COLON() { return getToken(JacParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(JacParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(JacParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public St_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_while; }
	}

	public final St_whileContext st_while() throws RecognitionException {
		St_whileContext _localctx = new St_whileContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_st_while);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(WHILE);
			if 1:
			        global while_max
			        local_while = while_max
			        print('BEGIN_WHILE_' + str(local_while) + ':')  
			        inside_while.append(local_while) 
			    
			setState(120);
			comparison_while();
			if 1:
			        while_max += 1
			    
			setState(122);
			match(COLON);
			setState(123);
			match(INDENT);
			setState(125); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(124);
				statement();
				}
				}
				setState(127); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << PRINT) | (1L << NAME) | (1L << NL))) != 0) );
			setState(129);
			match(DEDENT);
			if 1:
			        emit('goto BEGIN_WHILE_' + str(local_while), 0)
			        print('END_WHILE_' + str(local_while) + ':')
			        inside_while.pop()
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_callContext extends ParserRuleContext {
		public Token NAME;
		public TerminalNode NAME() { return getToken(JacParser.NAME, 0); }
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public St_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_call; }
	}

	public final St_callContext st_call() throws RecognitionException {
		St_callContext _localctx = new St_callContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_st_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			((St_callContext)_localctx).NAME = match(NAME);
			setState(133);
			match(OP_PAR);
			setState(134);
			match(CL_PAR);
			if 1:
			        print('    invokestatic Test/' + (((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null) + '()V')
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Comparison_ifContext extends ParserRuleContext {
		public  type;
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(JacParser.EQ, 0); }
		public TerminalNode NE() { return getToken(JacParser.NE, 0); }
		public TerminalNode GT() { return getToken(JacParser.GT, 0); }
		public TerminalNode GE() { return getToken(JacParser.GE, 0); }
		public TerminalNode LT() { return getToken(JacParser.LT, 0); }
		public TerminalNode LE() { return getToken(JacParser.LE, 0); }
		public Comparison_ifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison_if; }
	}

	public final Comparison_ifContext comparison_if() throws RecognitionException {
		Comparison_ifContext _localctx = new Comparison_ifContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_comparison_if);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			expression();
			setState(138);
			((Comparison_ifContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQ) | (1L << NE) | (1L << GT) | (1L << GE) | (1L << LT) | (1L << LE))) != 0)) ) {
				((Comparison_ifContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(139);
			expression();
			if 1:
			        if (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.EQ:
			            _localctx.type = 'if_icmpne'
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.NE:
			            _localctx.type = 'if_icmpeq'
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.GT:
			            _localctx.type = 'if_icmple'
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.GE:
			            _localctx.type = 'if_icmplt'
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.LT:
			            _localctx.type = 'if_icmpge'
			        elif (((Comparison_ifContext)_localctx).op!=null?((Comparison_ifContext)_localctx).op.getType():0) == JacParser.LE:
			            _localctx.type = 'if_icmpgt'
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Comparison_whileContext extends ParserRuleContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(JacParser.EQ, 0); }
		public TerminalNode NE() { return getToken(JacParser.NE, 0); }
		public TerminalNode GT() { return getToken(JacParser.GT, 0); }
		public TerminalNode GE() { return getToken(JacParser.GE, 0); }
		public TerminalNode LT() { return getToken(JacParser.LT, 0); }
		public TerminalNode LE() { return getToken(JacParser.LE, 0); }
		public Comparison_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison_while; }
	}

	public final Comparison_whileContext comparison_while() throws RecognitionException {
		Comparison_whileContext _localctx = new Comparison_whileContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_comparison_while);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			expression();
			setState(143);
			((Comparison_whileContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQ) | (1L << NE) | (1L << GT) | (1L << GE) | (1L << LT) | (1L << LE))) != 0)) ) {
				((Comparison_whileContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(144);
			expression();
			if 1:
			        if (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.EQ:
			            emit('if_icmpne END_WHILE_'+str(while_max), -2)
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.NE:
			            emit('if_icmpeq END_WHILE_'+str(while_max), -2)
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.GT:
			            emit('if_icmple END_WHILE_'+str(while_max), -2)
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.GE:
			            emit('if_icmplt END_WHILE_'+str(while_max), -2)
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.LT:
			            emit('if_icmpge END_WHILE_'+str(while_max), -2)
			        elif (((Comparison_whileContext)_localctx).op!=null?((Comparison_whileContext)_localctx).op.getType():0) == JacParser.LE:
			            emit('if_icmpgt END_WHILE_'+str(while_max), -2)
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public  type;
		public TermContext t1;
		public Token op;
		public TermContext t2;
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(JacParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(JacParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(JacParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(JacParser.MINUS, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			((ExpressionContext)_localctx).t1 = term();
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(148);
				((ExpressionContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
					((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(149);
				((ExpressionContext)_localctx).t2 = term();
				if 1:
				        if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == JacParser.PLUS:
				            emit('    iadd', -1)
				        else:
				            emit('    isub', -1)
				    
				}
				}
				setState(156);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			if 1:
			        _localctx.type = ((ExpressionContext)_localctx).t1.type
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public  type;
		public FactorContext f1;
		public Token op;
		public FactorContext f2;
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> TIMES() { return getTokens(JacParser.TIMES); }
		public TerminalNode TIMES(int i) {
			return getToken(JacParser.TIMES, i);
		}
		public List<TerminalNode> OVER() { return getTokens(JacParser.OVER); }
		public TerminalNode OVER(int i) {
			return getToken(JacParser.OVER, i);
		}
		public List<TerminalNode> REM() { return getTokens(JacParser.REM); }
		public TerminalNode REM(int i) {
			return getToken(JacParser.REM, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			((TermContext)_localctx).f1 = factor();
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) {
				{
				{
				setState(160);
				((TermContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) ) {
					((TermContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(161);
				((TermContext)_localctx).f2 = factor();
				if 1:
				        if   (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == JacParser.TIMES:
				            emit('    imul', -1)
				        elif (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == JacParser.OVER:
				            emit('    idiv', -1)
				        else:
				            emit('    irem', -1)
				    
				}
				}
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			if 1:
			        _localctx.type = ((TermContext)_localctx).f1.type
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public  type;
		public Token NUMBER;
		public Token STRING;
		public ExpressionContext e;
		public Token NAME;
		public TerminalNode NUMBER() { return getToken(JacParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(JacParser.STRING, 0); }
		public TerminalNode OP_PAR() { return getToken(JacParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(JacParser.CL_PAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NAME() { return getToken(JacParser.NAME, 0); }
		public TerminalNode READINT() { return getToken(JacParser.READINT, 0); }
		public TerminalNode READSTR() { return getToken(JacParser.READSTR, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_factor);
		try {
			setState(190);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(171);
				((FactorContext)_localctx).NUMBER = match(NUMBER);
				if 1:
				        emit('    ldc ' + str((((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null)), +1)
				        _localctx.type = 'i'
				    
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(173);
				((FactorContext)_localctx).STRING = match(STRING);
				if 1:
				        emit('    ldc ' + str((((FactorContext)_localctx).STRING!=null?((FactorContext)_localctx).STRING.getText():null)), +1)
				        _localctx.type = 's'
				    
				}
				break;
			case OP_PAR:
				enterOuterAlt(_localctx, 3);
				{
				setState(175);
				match(OP_PAR);
				setState(176);
				((FactorContext)_localctx).e = expression();
				setState(177);
				match(CL_PAR);
				if 1:
				        _localctx.type = ((FactorContext)_localctx).e.type
				    
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 4);
				{
				setState(180);
				((FactorContext)_localctx).NAME = match(NAME);
				if 1:
				        if (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) not in symbol_table:
				            sys.stderr.write('Variable ' + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + ' is not defined\n')
				            sys.exit(1)
				        elif symbol_type[symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))] == 'i':
				            emit('    iload ' +  str(symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))), +1)
				            used_table[symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))] = True
				            _localctx.type = symbol_type[symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))]
				        elif symbol_type[symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))] == 's':
				            emit('    aload ' +  str(symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))), +1)
				            used_table[symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))] = True
				            _localctx.type = symbol_type[symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))]
				    
				}
				break;
			case READINT:
				enterOuterAlt(_localctx, 5);
				{
				setState(182);
				match(READINT);
				setState(183);
				match(OP_PAR);
				setState(184);
				match(CL_PAR);
				if 1:
				        emit('    invokestatic Runtime/readInt()I', +1)
				        _localctx.type = 'i'
				    
				}
				break;
			case READSTR:
				enterOuterAlt(_localctx, 6);
				{
				setState(186);
				match(READSTR);
				setState(187);
				match(OP_PAR);
				setState(188);
				match(CL_PAR);
				if 1:
				        emit('    invokestatic Runtime/readString()Ljava/lang/String;', +1)
				        _localctx.type = 's'
				    
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$\u00c3\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\7"+
		"\2%\n\2\f\2\16\2(\13\2\3\2\3\2\3\3\3\3\6\3.\n\3\r\3\16\3/\3\3\3\3\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\6\4<\n\4\r\4\16\4=\3\4\3\4\3\4\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\5\5K\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\7\6W\n\6\f\6\16\6Z\13\6\5\6\\\n\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\6\bl\n\b\r\b\16\bm\3\b\3\b\3\b\3\t\3\t\3\t\3\n"+
		"\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\6\13\u0080\n\13\r\13\16\13"+
		"\u0081\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16"+
		"\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\7\17\u009b\n\17\f\17\16\17\u009e"+
		"\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\7\20\u00a7\n\20\f\20\16\20\u00aa"+
		"\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c1\n\21\3\21\2\2\22\2"+
		"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2\5\3\2\27\34\3\2\13\f\3\2\r\17"+
		"\2\u00c7\2\"\3\2\2\2\4+\3\2\2\2\6\63\3\2\2\2\bJ\3\2\2\2\nL\3\2\2\2\f`"+
		"\3\2\2\2\16e\3\2\2\2\20r\3\2\2\2\22u\3\2\2\2\24x\3\2\2\2\26\u0086\3\2"+
		"\2\2\30\u008b\3\2\2\2\32\u0090\3\2\2\2\34\u0095\3\2\2\2\36\u00a1\3\2\2"+
		"\2 \u00c0\3\2\2\2\"&\b\2\1\2#%\5\6\4\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&"+
		"\'\3\2\2\2\')\3\2\2\2(&\3\2\2\2)*\5\4\3\2*\3\3\2\2\2+-\b\3\1\2,.\5\b\5"+
		"\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\62\b\3\1"+
		"\2\62\5\3\2\2\2\63\64\7\n\2\2\64\65\7\35\2\2\65\66\7\20\2\2\66\67\7\21"+
		"\2\2\678\7\26\2\289\b\4\1\29;\7#\2\2:<\5\b\5\2;:\3\2\2\2<=\3\2\2\2=;\3"+
		"\2\2\2=>\3\2\2\2>?\3\2\2\2?@\7$\2\2@A\b\4\1\2A\7\3\2\2\2BK\5\n\6\2CK\5"+
		"\f\7\2DK\5\16\b\2EK\5\24\13\2FK\5\20\t\2GK\5\22\n\2HK\5\26\f\2IK\7 \2"+
		"\2JB\3\2\2\2JC\3\2\2\2JD\3\2\2\2JE\3\2\2\2JF\3\2\2\2JG\3\2\2\2JH\3\2\2"+
		"\2JI\3\2\2\2K\t\3\2\2\2LM\7\7\2\2M[\7\20\2\2NO\b\6\1\2OP\5\34\17\2PX\b"+
		"\6\1\2QR\7\25\2\2RS\b\6\1\2ST\5\34\17\2TU\b\6\1\2UW\3\2\2\2VQ\3\2\2\2"+
		"WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2[N\3\2\2\2[\\\3\2\2"+
		"\2\\]\3\2\2\2]^\7\21\2\2^_\b\6\1\2_\13\3\2\2\2`a\7\35\2\2ab\7\24\2\2b"+
		"c\5\34\17\2cd\b\7\1\2d\r\3\2\2\2ef\7\3\2\2fg\5\30\r\2gh\7\26\2\2hi\b\b"+
		"\1\2ik\7#\2\2jl\5\b\5\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2no\3\2"+
		"\2\2op\7$\2\2pq\b\b\1\2q\17\3\2\2\2rs\7\5\2\2st\b\t\1\2t\21\3\2\2\2uv"+
		"\7\6\2\2vw\b\n\1\2w\23\3\2\2\2xy\7\4\2\2yz\b\13\1\2z{\5\32\16\2{|\b\13"+
		"\1\2|}\7\26\2\2}\177\7#\2\2~\u0080\5\b\5\2\177~\3\2\2\2\u0080\u0081\3"+
		"\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083"+
		"\u0084\7$\2\2\u0084\u0085\b\13\1\2\u0085\25\3\2\2\2\u0086\u0087\7\35\2"+
		"\2\u0087\u0088\7\20\2\2\u0088\u0089\7\21\2\2\u0089\u008a\b\f\1\2\u008a"+
		"\27\3\2\2\2\u008b\u008c\5\34\17\2\u008c\u008d\t\2\2\2\u008d\u008e\5\34"+
		"\17\2\u008e\u008f\b\r\1\2\u008f\31\3\2\2\2\u0090\u0091\5\34\17\2\u0091"+
		"\u0092\t\2\2\2\u0092\u0093\5\34\17\2\u0093\u0094\b\16\1\2\u0094\33\3\2"+
		"\2\2\u0095\u009c\5\36\20\2\u0096\u0097\t\3\2\2\u0097\u0098\5\36\20\2\u0098"+
		"\u0099\b\17\1\2\u0099\u009b\3\2\2\2\u009a\u0096\3\2\2\2\u009b\u009e\3"+
		"\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f\3\2\2\2\u009e"+
		"\u009c\3\2\2\2\u009f\u00a0\b\17\1\2\u00a0\35\3\2\2\2\u00a1\u00a8\5 \21"+
		"\2\u00a2\u00a3\t\4\2\2\u00a3\u00a4\5 \21\2\u00a4\u00a5\b\20\1\2\u00a5"+
		"\u00a7\3\2\2\2\u00a6\u00a2\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2"+
		"\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab"+
		"\u00ac\b\20\1\2\u00ac\37\3\2\2\2\u00ad\u00ae\7\36\2\2\u00ae\u00c1\b\21"+
		"\1\2\u00af\u00b0\7!\2\2\u00b0\u00c1\b\21\1\2\u00b1\u00b2\7\20\2\2\u00b2"+
		"\u00b3\5\34\17\2\u00b3\u00b4\7\21\2\2\u00b4\u00b5\b\21\1\2\u00b5\u00c1"+
		"\3\2\2\2\u00b6\u00b7\7\35\2\2\u00b7\u00c1\b\21\1\2\u00b8\u00b9\7\b\2\2"+
		"\u00b9\u00ba\7\20\2\2\u00ba\u00bb\7\21\2\2\u00bb\u00c1\b\21\1\2\u00bc"+
		"\u00bd\7\t\2\2\u00bd\u00be\7\20\2\2\u00be\u00bf\7\21\2\2\u00bf\u00c1\b"+
		"\21\1\2\u00c0\u00ad\3\2\2\2\u00c0\u00af\3\2\2\2\u00c0\u00b1\3\2\2\2\u00c0"+
		"\u00b6\3\2\2\2\u00c0\u00b8\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c1!\3\2\2\2"+
		"\r&/=JX[m\u0081\u009c\u00a8\u00c0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}