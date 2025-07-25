from core.lexer import lex
from core.parser import Parser
from core.inter import *
from core.ast import *

if __name__ == '__main__':
    code = open('test.ict', 'r').read()

    tokens = lex(code) # лексер
    parser = Parser(tokens)
    ast = parser.parse() # ast дерево
    
    inter = Interpreter()
    
    inter.eval(ast)
