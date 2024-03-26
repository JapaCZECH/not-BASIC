from src.nodes.nodes import *
from src.lexer.classlex import *
from src.tok.classtok import *
from pos import *
from GLOBAL.CONST import *
from src.errors.errors import *
from src.parser.parseres import *
from src.parser.parser import *
from src.rtres import *
from src.interpreter.interpreter import *
from src.errors.context import Context
from GLOBAL.symbol_table import global_symbol_table

def run(fn, text):
  # Generate tokens
  lexer = Lexer(fn, text)
  tokens, error = lexer.make_tokens()
  if error: return None, error
  
  # Generate AST
  parser = Parser(tokens)
  ast = parser.parse()
  if ast.error: return None, ast.error

  # Run program
  interpreter = Interpreter()
  context = Context('<program>')
  context.symbol_table = global_symbol_table
  result = interpreter.visit(ast.node, context)

  return result.value, result.error