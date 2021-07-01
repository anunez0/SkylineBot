# Generated from .\Skyline.g by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#start.
    def visitStart(self, ctx:SkylineParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#identifier.
    def visitIdentifier(self, ctx:SkylineParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skyline.
    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#priority1.
    def visitPriority1(self, ctx:SkylineParser.Priority1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#priority2.
    def visitPriority2(self, ctx:SkylineParser.Priority2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#priority3.
    def visitPriority3(self, ctx:SkylineParser.Priority3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#priority4.
    def visitPriority4(self, ctx:SkylineParser.Priority4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#building.
    def visitBuilding(self, ctx:SkylineParser.BuildingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#composed.
    def visitComposed(self, ctx:SkylineParser.ComposedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#random.
    def visitRandom(self, ctx:SkylineParser.RandomContext):
        return self.visitChildren(ctx)



del SkylineParser