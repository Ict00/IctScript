from core.ast import (
    IctAssign,
    IctBinOp,
    IctEcho,
    IctNumber,
    IctProgram,
    IctVariable
)

def print_ast(node, indent=0):
    prefix = '  ' * indent

    match node:
        case IctProgram(statements):
            print(f'{prefix}IctProgram')
            for stmt in statements:
                print_ast(stmt, indent + 1)

        case IctAssign(name, expr):
            print(f'{prefix}IctAssign {name}')
            print_ast(expr, indent + 1)

        case IctEcho(expr):
            print(f'{prefix}IctEcho')
            print_ast(expr, indent + 1)

        case IctBinOp(left, op, right):
            print(f'{prefix}IctBinOp {op}')
            print_ast(left, indent + 1)
            print_ast(right, indent + 1)

        case IctNumber(value):
            print(f'{prefix}IctNumber {value}')

        case IctVariable(name):
            print(f'{prefix}IctVariable {name}')

        case _:
            print(f'{prefix}Unknown node: {node}')


