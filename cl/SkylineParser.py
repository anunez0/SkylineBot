# Generated from .\Skyline.g by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("j\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\5\3\37\n\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\7\6,\n\6\f\6\16\6/\13\6\3\7\3\7\3\7\3\7\5\7")
        buf.write("\65\n\7\7\7\67\n\7\f\7\16\7:\13\7\3\b\5\b=\n\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tI\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\7\13W\n\13\f")
        buf.write("\13\16\13Z\13\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\2\3\3\2\4\5\2i\2\30\3\2\2\2\4\36\3\2\2\2\6\"\3\2\2")
        buf.write("\2\b$\3\2\2\2\n&\3\2\2\2\f\60\3\2\2\2\16<\3\2\2\2\20H")
        buf.write("\3\2\2\2\22J\3\2\2\2\24R\3\2\2\2\26]\3\2\2\2\30\31\5\4")
        buf.write("\3\2\31\32\7\2\2\3\32\3\3\2\2\2\33\34\5\6\4\2\34\35\7")
        buf.write("\3\2\2\35\37\3\2\2\2\36\33\3\2\2\2\36\37\3\2\2\2\37 \3")
        buf.write("\2\2\2 !\5\b\5\2!\5\3\2\2\2\"#\7\16\2\2#\7\3\2\2\2$%\5")
        buf.write("\n\6\2%\t\3\2\2\2&-\5\f\7\2\'(\7\4\2\2(,\5\f\7\2)*\t\2")
        buf.write("\2\2*,\7\17\2\2+\'\3\2\2\2+)\3\2\2\2,/\3\2\2\2-+\3\2\2")
        buf.write("\2-.\3\2\2\2.\13\3\2\2\2/-\3\2\2\2\608\5\16\b\2\61\64")
        buf.write("\7\6\2\2\62\65\5\16\b\2\63\65\7\17\2\2\64\62\3\2\2\2\64")
        buf.write("\63\3\2\2\2\65\67\3\2\2\2\66\61\3\2\2\2\67:\3\2\2\28\66")
        buf.write("\3\2\2\289\3\2\2\29\r\3\2\2\2:8\3\2\2\2;=\7\5\2\2<;\3")
        buf.write("\2\2\2<=\3\2\2\2=>\3\2\2\2>?\5\20\t\2?\17\3\2\2\2@A\7")
        buf.write("\7\2\2AB\5\b\5\2BC\7\b\2\2CI\3\2\2\2DI\5\6\4\2EI\5\22")
        buf.write("\n\2FI\5\24\13\2GI\5\26\f\2H@\3\2\2\2HD\3\2\2\2HE\3\2")
        buf.write("\2\2HF\3\2\2\2HG\3\2\2\2I\21\3\2\2\2JK\7\7\2\2KL\7\17")
        buf.write("\2\2LM\7\t\2\2MN\7\17\2\2NO\7\t\2\2OP\7\17\2\2PQ\7\b\2")
        buf.write("\2Q\23\3\2\2\2RS\7\n\2\2SX\5\22\n\2TU\7\t\2\2UW\5\22\n")
        buf.write("\2VT\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[\3\2\2\2Z")
        buf.write("X\3\2\2\2[\\\7\13\2\2\\\25\3\2\2\2]^\7\f\2\2^_\7\17\2")
        buf.write("\2_`\7\t\2\2`a\7\17\2\2ab\7\t\2\2bc\7\17\2\2cd\7\t\2\2")
        buf.write("de\7\17\2\2ef\7\t\2\2fg\7\17\2\2gh\7\r\2\2h\27\3\2\2\2")
        buf.write("\n\36+-\648<HX")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'+'", "'-'", "'*'", "'('", "')'", 
                     "','", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "NUMBER", "LETTER", "DIGIT", "WS" ]

    RULE_root = 0
    RULE_start = 1
    RULE_identifier = 2
    RULE_skyline = 3
    RULE_priority1 = 4
    RULE_priority2 = 5
    RULE_priority3 = 6
    RULE_priority4 = 7
    RULE_building = 8
    RULE_composed = 9
    RULE_random = 10

    ruleNames =  [ "root", "start", "identifier", "skyline", "priority1", 
                   "priority2", "priority3", "priority4", "building", "composed", 
                   "random" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    IDENTIFIER=12
    NUMBER=13
    LETTER=14
    DIGIT=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start(self):
            return self.getTypedRuleContext(SkylineParser.StartContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.start()
            self.state = 23
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SkylineParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = SkylineParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 25
                self.identifier()
                self.state = 26
                self.match(SkylineParser.T__0)


            self.state = 30
            self.skyline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SkylineParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = SkylineParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(SkylineParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def priority1(self):
            return self.getTypedRuleContext(SkylineParser.Priority1Context,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_skyline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline" ):
                return visitor.visitSkyline(self)
            else:
                return visitor.visitChildren(self)




    def skyline(self):

        localctx = SkylineParser.SkylineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_skyline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.priority1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Priority1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def priority2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.Priority2Context)
            else:
                return self.getTypedRuleContext(SkylineParser.Priority2Context,i)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUMBER)
            else:
                return self.getToken(SkylineParser.NUMBER, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_priority1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPriority1" ):
                return visitor.visitPriority1(self)
            else:
                return visitor.visitChildren(self)




    def priority1(self):

        localctx = SkylineParser.Priority1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_priority1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.priority2()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__1 or _la==SkylineParser.T__2:
                self.state = 41
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 37
                    self.match(SkylineParser.T__1)
                    self.state = 38
                    self.priority2()
                    pass

                elif la_ == 2:
                    self.state = 39
                    _la = self._input.LA(1)
                    if not(_la==SkylineParser.T__1 or _la==SkylineParser.T__2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 40
                    self.match(SkylineParser.NUMBER)
                    pass


                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Priority2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def priority3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.Priority3Context)
            else:
                return self.getTypedRuleContext(SkylineParser.Priority3Context,i)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUMBER)
            else:
                return self.getToken(SkylineParser.NUMBER, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_priority2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPriority2" ):
                return visitor.visitPriority2(self)
            else:
                return visitor.visitChildren(self)




    def priority2(self):

        localctx = SkylineParser.Priority2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_priority2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.priority3()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__3:
                self.state = 47
                self.match(SkylineParser.T__3)
                self.state = 50
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SkylineParser.T__2, SkylineParser.T__4, SkylineParser.T__7, SkylineParser.T__9, SkylineParser.IDENTIFIER]:
                    self.state = 48
                    self.priority3()
                    pass
                elif token in [SkylineParser.NUMBER]:
                    self.state = 49
                    self.match(SkylineParser.NUMBER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Priority3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def priority4(self):
            return self.getTypedRuleContext(SkylineParser.Priority4Context,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_priority3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPriority3" ):
                return visitor.visitPriority3(self)
            else:
                return visitor.visitChildren(self)




    def priority3(self):

        localctx = SkylineParser.Priority3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_priority3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SkylineParser.T__2:
                self.state = 57
                self.match(SkylineParser.T__2)


            self.state = 60
            self.priority4()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Priority4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SkylineParser.IdentifierContext,0)


        def building(self):
            return self.getTypedRuleContext(SkylineParser.BuildingContext,0)


        def composed(self):
            return self.getTypedRuleContext(SkylineParser.ComposedContext,0)


        def random(self):
            return self.getTypedRuleContext(SkylineParser.RandomContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_priority4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPriority4" ):
                return visitor.visitPriority4(self)
            else:
                return visitor.visitChildren(self)




    def priority4(self):

        localctx = SkylineParser.Priority4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_priority4)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(SkylineParser.T__4)
                self.state = 63
                self.skyline()
                self.state = 64
                self.match(SkylineParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.building()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.composed()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.random()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuildingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUMBER)
            else:
                return self.getToken(SkylineParser.NUMBER, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_building

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuilding" ):
                return visitor.visitBuilding(self)
            else:
                return visitor.visitChildren(self)




    def building(self):

        localctx = SkylineParser.BuildingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_building)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(SkylineParser.T__4)
            self.state = 73
            self.match(SkylineParser.NUMBER)
            self.state = 74
            self.match(SkylineParser.T__6)
            self.state = 75
            self.match(SkylineParser.NUMBER)
            self.state = 76
            self.match(SkylineParser.T__6)
            self.state = 77
            self.match(SkylineParser.NUMBER)
            self.state = 78
            self.match(SkylineParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComposedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def building(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.BuildingContext)
            else:
                return self.getTypedRuleContext(SkylineParser.BuildingContext,i)


        def getRuleIndex(self):
            return SkylineParser.RULE_composed

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposed" ):
                return visitor.visitComposed(self)
            else:
                return visitor.visitChildren(self)




    def composed(self):

        localctx = SkylineParser.ComposedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_composed)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SkylineParser.T__7)
            self.state = 81
            self.building()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__6:
                self.state = 82
                self.match(SkylineParser.T__6)
                self.state = 83
                self.building()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(SkylineParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUMBER)
            else:
                return self.getToken(SkylineParser.NUMBER, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_random

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandom" ):
                return visitor.visitRandom(self)
            else:
                return visitor.visitChildren(self)




    def random(self):

        localctx = SkylineParser.RandomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_random)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(SkylineParser.T__9)
            self.state = 92
            self.match(SkylineParser.NUMBER)
            self.state = 93
            self.match(SkylineParser.T__6)
            self.state = 94
            self.match(SkylineParser.NUMBER)
            self.state = 95
            self.match(SkylineParser.T__6)
            self.state = 96
            self.match(SkylineParser.NUMBER)
            self.state = 97
            self.match(SkylineParser.T__6)
            self.state = 98
            self.match(SkylineParser.NUMBER)
            self.state = 99
            self.match(SkylineParser.T__6)
            self.state = 100
            self.match(SkylineParser.NUMBER)
            self.state = 101
            self.match(SkylineParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





