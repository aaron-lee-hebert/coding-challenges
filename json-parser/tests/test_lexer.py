from pathlib import Path
from lexer import Lexer
from tokens import TokenType

TEST_DATA_DIR = Path(__file__).parent / "step1"

def load_json(filename: str) -> str:
    return (TEST_DATA_DIR / filename).read_text()

def test_empty_input_returns_eof():
    lexer = Lexer(load_json("invalid.json"))
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.EOF

def test_braces():
    lexer = Lexer(load_json("valid.json"))
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.LEFT_BRACE
    assert tokens[1].type == TokenType.RIGHT_BRACE
    assert tokens[2].type == TokenType.EOF