single_pattern = {
    "(": "LEFT_PAREN",
    ")": "RIGHT_PAREN",
    "{": "LEFT_BRACE",
    "}": "RIGHT_BRACE",
    "*": "STAR",
    "+": "PLUS",
    ".": "DOT",
    ",": "COMMA",
    ";": "SEMICOLON",
    "-": "MINUS"
}

double_operators_pattern = {
    "=": {
        "second": "=",
        "match_first": "EQUAL",
        "match_all": "EQUAL_EQUAL"
    },
    "!": {
        "second": "=",
        "match_first": "BANG",
        "match_all": "BANG_EQUAL"
    },
    "<": {
        "second": "=",
        "match_first": "LESS",
        "match_all": "LESS_EQUAL"
    },
    ">": {
        "second": "=",
        "match_first": "GREATER",
        "match_all": "GREATER_EQUAL"
    }
}

reserved_words = ["and", "class", "else", "false", "for", "fun", "if", "nil", "or", "print", "return", "super", "this", "true", "var", "while"]
