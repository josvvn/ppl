from tokens import *

class Lexer:
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.curr = 0
        self.line = 1
        self.tokens = []

    def add_token(self, token_type):
        self.tokens.append(Token(token_type, self.source[self.start:self.curr]))

    def tokenize(self):
        while self.curr < len(self.source):
            self.start = self.curr
            ch = self.advance()
            if ch == '+': self.add_token(TOK_PLUS)
            if ch == '-': self.add_token(TOK_MINUS)
        return self.tokens

    # advances the 'curr' pointer
    def advance(self):
        ch = self.source [self.curr]
        self.curr = self.curr + 1
        return ch # consumes the character

    # just peeks the current character
    def peek(self):
        return self.source[self.curr] # does not consume the character

    # looks at the next character in the source
    def lookahead(self, n = 1):
        return self.source[self.curr + n] # does not consume the character
    
    # check if the 'curr' character matches an 'expectation'
    def match(self, expected):
        if self.source[self.curr] != expected:
            return False
        self.curr = self.curr + 1
        return True # consumes the character only if the match is true
