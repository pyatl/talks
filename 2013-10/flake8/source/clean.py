MAPPING = {
    'a': 'A',
}

LIST = [
    'a',
    'b',
]

# This comment is a very long line, which causes problems for people
# who program Python on punch cards.

parser_errors = [
    (__name__, 1, 1, 'message'),
]

errors = [
    'Parse error at %s:%s "%s" (%s)' %
    (filename, num, line, err)
    for filename, num, line, err in parser_errors
]


# This is something you might do in an __init__.py
from .submodule import public_function  # noqa


def f(*args):
    print(args)

f(1, 2, 3,
  4, 5, 6)
