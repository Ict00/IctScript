"""Interpreter for Howdy Script programming language."""
#VARS = {"": ""}

class Interpreter:
    def __init__(self):
        self.env = {} # vars storage

    def eval(self, node):
        if func := getattr(node, '_eval'):
            return func(self, node)
        else:
            raise TypeError(f"Unknown node type: {type(node).__name__}")
