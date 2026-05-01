from tokens import TokenType, Token

class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0

    def current_char(self):
        if self.position >= len(self.text):
            return None
        return self.text[self.position]
    
    def advance(self):
        self.position += 1

    def tokenize(self):
        tokens = []

        while self.current_char() is not None:
            char = self.current_char()

            if char == "{":
                tokens.append(Token(TokenType.LEFT_BRACE))
                self.advance()
                
            elif char == "}":
                tokens.append(Token(TokenType.RIGHT_BRACE))
                self.advance()

            else:
                raise Exception(f"Unexpected char: {char}")

        tokens.append(Token(TokenType.EOF))
        return tokens