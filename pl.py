import sys
from tokens import *
from lexer import *


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python3 pl.py <filename>')
    filename = sys.argv[1]
    print(filename)

    with open(filename) as file:
        source = file.read()
        print(source)

        print('LEXER:')
        tokens = Lexer(source).tokenize()
        for token in tokens:
            print(token)
