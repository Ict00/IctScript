"""Lexical analyzer for Howdy Script programming language"""

import re
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

KEYWORDS = {'echo', 'HOWDY'}

TOKEN_SPECIFICATION = [
    ('NUMBER', r'\d+(\.\d*)?'), # числа
    ('ID', r'[a-zA-Z_][a-zA-Z_0-9]*'), # идентификаторы (переменные)
    ('OP', r'[:]=|==|!=|<=|>=|[+\-*/=<>]'), # операции (присвоение и тд)
    ('SKIP', r'[ \t]+'), # пропускать пробелы и табуляции
    ('NEWLINE', r'\n'), # новая строка
    ('LPAREN', r'\('), # открывающая скобка
    ('RPAREN', r'\)'), # закрывающая скобка
    ('MISMATCH', r'.'), # всё остальное мисмач (несовпадение)
]


def lex(code):
    # компилируем все в один шаблон
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)

    # разбиваем на токены
    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
            yield Token(kind, value)
        elif kind == 'ID':
            token_type = value.upper() if value in KEYWORDS else 'ID'
            yield Token(token_type, value)
        elif kind == 'OP':
            yield Token(kind, value)
        elif kind in ('NEWLINE', 'SKIP'):
            continue
        elif kind in ('LPAREN', 'RPAREN'):
            yield Token(kind, value)
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected character: {value!r}')
