from lexer import Lexer
from tokens import TokenType

def test_empty_input_returns_eof():
    lexer = Lexer("")
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.EOF
