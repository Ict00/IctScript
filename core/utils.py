from core.ast import (
    XoAssign,
    XoBinOp,
    XoEcho,
    XoNumber,
    XoProgram,
    XoVariable
)

def print_ast(node, indent=0):
    prefix = '  ' * indent

    match node:
        case XoProgram(statements):
            print(f'{prefix}XoProgram')
            for stmt in statements:
                print_ast(stmt, indent + 1)

        case XoAssign(name, expr):
            print(f'{prefix}XoAssign {name}')
            print_ast(expr, indent + 1)

        case XoEcho(expr):
            print(f'{prefix}XoEcho')
            print_ast(expr, indent + 1)

        case XoBinOp(left, op, right):
            print(f'{prefix}XoBinOp {op}')
            print_ast(left, indent + 1)
            print_ast(right, indent + 1)

        case XoNumber(value):
            print(f'{prefix}XoNumber {value}')

        case XoVariable(name):
            print(f'{prefix}XoVariable {name}')

        case _:
            print(f'{prefix}Unknown node: {node}')
