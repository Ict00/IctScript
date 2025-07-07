from core.lexer import lex
from core.parser import Parser
from core.inter import *
from core.ast import *


def exec_ast(node):
    inter = Interpreter()

    match node:
        case IctProgram(statements):
            for stmt in statements:
                exec_ast(stmt)
        case _:
            inter.eval(node)

if __name__ == '__main__':
    code = open('test.ict', 'r').read()

    tokens = lex(code) # лексер
    parser = Parser(tokens)
    ast = parser.parse() # ast дерево
    
    inter = Interpreter()
    
    inter.eval(ast)

    #exec_ast(ast)
