import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from EvalVisitor import EvalVisitor
from Skyline import Skyline

input_stream = InputStream(input('? '))

lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()

visitor = EvalVisitor()
result = visitor.visit(tree)

print(result.buildings)
