from enum import Enum

class TokenType(Enum):
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    STAR = "*"
    PLUS = "+"
    DOT = "."
    COMMA = ","
    SEMICOLON = ";"
    MINUS = "-"
    EQUAL = "="
    EQUAL_EQUAL = "=="
    BANG = "!"
    BANG_EQUAL = "!="
    LESS = "<"
    LESS_EQUAL = "<="
    GREATER = ">"
    GREATER_EQUAL = ">="
    SLASH = "/"
    STRING = "STRING"
    NUMBER = "NUMBER"
    IDENTIFIER = "IDENTIFIER"
    SCAN_ERROR = "SCAN_ERROR"
    RESERVED_WORD = "RESERVED_WORD"

single_pattern = {
    "(": TokenType.LEFT_PAREN,
    ")": TokenType.RIGHT_PAREN,
    "{": TokenType.LEFT_BRACE,
    "}": TokenType.RIGHT_BRACE,
    "*": TokenType.STAR,
    "+": TokenType.PLUS,
    ".": TokenType.DOT,
    ",": TokenType.COMMA,
    ";": TokenType.SEMICOLON,
    "-": TokenType.MINUS
}

double_operators_pattern = {
    "=": {
        "second": "=",
        "match_first": TokenType.EQUAL,
        "match_all": TokenType.EQUAL_EQUAL
    },
    "!": {
        "second": "=",
        "match_first": TokenType.BANG,
        "match_all": TokenType.BANG_EQUAL
    },
    "<": {
        "second": "=",
        "match_first": TokenType.LESS,
        "match_all": TokenType.LESS_EQUAL
    },
    ">": {
        "second": "=",
        "match_first": TokenType.GREATER,
        "match_all": TokenType.GREATER_EQUAL
    }
}


reserved_words = ["and", "class", "else", "false", "for", "fun", "if", "nil", "or", "print", "return", "super", "this", "true", "var", "while"]
