from app.scanner.constants import (
    single_pattern, double_operators_pattern, reserved_words,
    TokenType
)
from app.scanner.utils import (
	check_next_char, 
	is_identifier_char, 
	scan_string, 
	scan_numberic, 
	scan_identifier
)

class LoxScanner:
	def __init__(self, filepath) -> None:
		f = open(filepath)
		self.file_contents = f.read()
		f.close()

		self.line_num = 1
		self.have_err_scan = False

	def start(self):
		self.index = 0
		tokens = []

		while self.index < len(self.file_contents):
			c = self.file_contents[self.index]

			if c in single_pattern:
				tokens.append({
					"token_type": single_pattern[c],
					"value": c,
					"message": f"{c} null"
				})
			elif c in double_operators_pattern:
				config = double_operators_pattern[c]
				if check_next_char(self.file_contents, self.index, config['second']):
					tokens.append({
						"token_type": config['match_all'],
						"value": f"{c}{config['second']}",
						"message": f"{c}{config['second']} null"
					})
					self.index += 1
				else:
					tokens.append({
						"token_type": config['match_first'],
						"value": c,
						"message": f"{c} null"
					})
			elif c == "\n":
				self.line_num += 1
			elif c == "/":
				if check_next_char(self.file_contents, self.index, "/"):
					# Skip comments to end of line
					while self.index < len(self.file_contents) and self.file_contents[self.index] != "\n":
						self.index += 1
					# It should be new line after skipping all comment
					self.line_num += 1
				else:
					tokens.append({
						"token_type": TokenType.SLASH,
						"value": "/",
						"message": "/ null"
					})
			elif c.isspace():
				# Skip white space
				self.index += 1
				continue
			elif c == "\"":
				content, new_index = scan_string(self.index, self.file_contents)
				if content is not None:
					tokens.append({
						"token_type": TokenType.STRING,
						"value": content,
						"message": f"\"{content}\" {content}"
					})
				else:
					self.have_err_scan = True
					tokens.append({
						"token_type": TokenType.SCAN_ERROR,
						"line_num": self.line_num,
						"error": "Unterminated string."
					})
				self.index = new_index + 1
				continue
			elif c.isnumeric():
				value, new_index = scan_numberic(self.index, self.file_contents)
				tokens.append({
					"token_type": TokenType.NUMBER,
					"value": value,
					"message": f"{value} {float(value)}"
				})
				self.index = new_index
				continue
			elif is_identifier_char(c):
				identifier, new_index = scan_identifier(self.index, self.file_contents)
				if identifier in reserved_words:
					tokens.append({
						"token_type": TokenType.RESERVED_WORD,
						"value": identifier,
						"message": f"{identifier} null"
					})
				else:
					tokens.append({
						"token_type": TokenType.IDENTIFIER,
						"value": identifier,
						"message": f"{identifier} null"
					})
				self.index = new_index
				continue
			else:
				tokens.append({
					"token_type": TokenType.SCAN_ERROR,
					"line_num": self.line_num,
					"error": f"Unexpected character: {c}"
				})

			self.index += 1

		tokens.append({
			"token_type": TokenType.EOF,
			"message": "null"
		})
		return tokens

__all__ = ["LoxScanner"]
