"""Abstract Syntax Tree classes for Howdy Script programming language"""


class IctBase:
    def __init__(self, _eval: callable):
        self._eval = _eval


class IctNumber(IctBase):
    __match_args__ = ("value",)

    def __init__(self, value):
        super().__init__(
            _eval=lambda x, node: node.value
        )
        self.value = value


class IctVariable(IctBase):
    __match_args__ = ("name",)

    def __init__(self, name):
        def _eval(x, node):
            if node.name in x.env:
                return x.env[node.name]
            raise NameError(f"Variable '{node.name}' is not defined")

        super().__init__(
            _eval=_eval
        )
        self.name = name


class IctBinOp(IctBase):
    __match_args__ = ("left", "op", "right")

    def __init__(self, left, op, right):
        def _eval(x, node):
            _left = x.eval(node.left)
            _right = x.eval(node.right)

            operators = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b,
            }

            if node.op in operators:
                return operators[node.op](_left, _right)
            else:
                raise ValueError(f"Unknown operator: {node.op}")

        super().__init__(_eval)
        self.left = left
        self.op = op
        self.right = right


class IctAssign(IctBase):
    __match_args__ = ("name", "expr")

    def __init__(self, name, expr):
        def e(x, node):
           x.env[node.name] = x.eval(node.expr) or None
 
        super().__init__(_eval=e)
        self.name = name
        self.expr = expr


class IctEcho(IctBase):
    __match_args__ = ("expr",)

    def __init__(self, expr):
        super().__init__(
            _eval=lambda x, node: print(x.eval(node.expr))
        )
        self.expr = expr


class IctProgram(IctBase):
    __match_args__ = ("statements",)

    def __init__(self, statements):
        super().__init__(
            _eval=lambda x, node: [x.eval(stmt) for stmt in node.statements]
        )
        self.statements = statements
