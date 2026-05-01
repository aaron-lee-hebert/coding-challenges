from enum import Enum
from dataclasses import dataclass
from typing import Any

class TokenType(Enum):
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    LEFT_BRACKET = "["
    RIGHT_BRACKET = "]"
    COLON = ":"
    COMMA = ","
    STRING = "STRING"
    NUMBER = "NUMBER"
    EOF = "EOF"

@dataclass
class Token:
    type: TokenType
    value: Any = None