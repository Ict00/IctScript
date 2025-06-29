"""Abstract Syntax Tree classes for Howdy Script programming language"""

class XoNumber:
    def __init__(self, value):
        self.value = value


class XoVariable:
    def __init__(self, name):
        self.name = name


class XoBinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class XoAssign:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class XoEcho:
    def __init__(self, expr):
        self.expr = expr


class XoProgram:
    def __init__(self, statements):
        self.statements = statements
