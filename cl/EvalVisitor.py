if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
    from .Skyline import Skyline
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor
    from Skyline import Skyline


class EvalVisitor(SkylineVisitor):
    def __init__(self):
        self.identifiers = {}

    def visitRoot(self, ctx: SkylineParser.RootContext):
        l = [n for n in ctx.getChildren()]
        return self.visit(l[0])

    def visitStart(self, ctx: SkylineParser.StartContext):
        l = [n for n in ctx.getChildren()]
        if len(l) == 1:
            return self.visit(l[0])
        elif len(l) == 3:
            identifier = l[0].getText()
            skyline = self.visit(l[2])
            self.identifiers[identifier] = skyline
            return skyline

    def visitSkyline(self, ctx: SkylineParser.SkylineContext):
        l = [n for n in ctx.getChildren()]
        return self.visit(l[0])

    def visitPriority1(self, ctx: SkylineParser.Priority1Context):
        l = [n for n in ctx.getChildren()]
        skyline = self.visit(l[0])
        if len(l) >= 3:
            for i in range(2, len(l), 2):
                if hasattr(l[i], 'getRuleIndex'):
                    skyline.union(self.visit(l[i]))
                else:
                    if l[i - 1].getText() == '+':
                        skyline.right_shift(int(l[i].getText()))
                    else:
                        skyline.left_shift(int(l[i].getText()))
        return skyline

    def visitPriority2(self, ctx: SkylineParser.Priority2Context):
        l = [n for n in ctx.getChildren()]
        skyline = self.visit(l[0])
        if len(l) >= 3:
            for i in range(2, len(l), 2):
                if hasattr(l[i], 'getRuleIndex'):
                    skyline.intersection(self.visit(l[i]))
                else:
                    skyline.replication(int(l[i].getText()))
        return skyline

    def visitPriority3(self, ctx: SkylineParser.Priority3Context):
        l = [n for n in ctx.getChildren()]
        skyline = self.visit(l[len(l) - 1])
        if len(l) == 2:
            skyline.mirror()
        return skyline

    def visitPriority4(self, ctx: SkylineParser.Priority4Context):
        l = [n for n in ctx.getChildren()]
        if len(l) == 3:
            return self.visit(l[1])
        else:
            return self.visit(l[0])

    def visitIdentifier(self, ctx: SkylineParser.IdentifierContext):
        identifier = ctx.getText()
        return self.identifiers[identifier]

    def visitBuilding(self, ctx: SkylineParser.BuildingContext):
        l = [n for n in ctx.getChildren()]
        skyline = Skyline()
        skyline.building(int(l[1].getText()), int(l[3].getText()), int(l[5].getText()))
        return skyline

    def visitComposed(self, ctx: SkylineParser.ComposedContext):
        l = [n for n in ctx.getChildren()]
        skyline = self.visit(l[1])
        if len(l) >= 5:
            for i in range(3, len(l) - 1, 2):
                skyline.union(self.visit(l[i]))
        return skyline

    def visitRandom(self, ctx: SkylineParser.RandomContext):
        l = [n for n in ctx.getChildren()]
        skyline = Skyline()
        skyline.random(int(l[1].getText()), int(l[3].getText()), int(l[5].getText()), int(l[7].getText()), int(l[9].getText()))
        return skyline
