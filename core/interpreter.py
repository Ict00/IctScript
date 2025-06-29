"""Interpreter for Howdy Script programming language."""

from core.ast import (
    XoAssign,
    XoBinOp,
    XoEcho,
    XoNumber,
    XoProgram,
    XoVariable,
)

class Interpreter:
    def __init__(self):
        self.env = {} # vars storage


    def eval(self, node):
        if isinstance(node, XoProgram):
            return self._eval_program(node)
        elif isinstance(node, XoAssign):
            return self._eval_assign(node)
        elif isinstance(node, XoEcho):
            return self._eval_echo(node)
        elif isinstance(node, XoNumber):
            return self._eval_number(node)
        elif isinstance(node, XoVariable):
            return self._eval_variable(node)
        elif isinstance(node, XoBinOp):
            return self._eval_binop(node)
        else:
            raise TypeError(f"Unknown node type: {type(node).__name__}")


    def _eval_program(self, node):
        for stmt in node.statements:
            self.eval(stmt)


    def _eval_assign(self, node):
        value = self.eval(node.expr)
        self.env[node.name] = value


    def _eval_echo(self, node):
        value = self.eval(node.expr)
        print(value)


    def _eval_number(self, node):
        return node.value


    def _eval_variable(self, node):
        if node.name in self.env:
            return self.env[node.name]
        raise NameError(f"Variable '{node.name}' is not defined")


    def _eval_binop(self, node):
        left = self.eval(node.left)
        right = self.eval(node.right)

        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

        if node.op in operators:
            return operators[node.op](left, right)
        else:
            raise ValueError(f"Unknown operator: {node.op}")
