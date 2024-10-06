import sys

from app.scanner.constants import single_pattern, double_operators_pattern, reserved_words
from app.scanner.utils import \
	check_next_char, is_identifier_char, \
 	scan_string, scan_numberic, scan_identifier

class LoxScanner:
	def __init__(self, filepath) -> None:
		f = open(filepath)
		self.file_contents = f.read()
		f.close()

		self.line_num = 1
		self.have_err_scan = False

	def start(self):
		self.index = 0
		while self.index < len(self.file_contents):
			c = self.file_contents[self.index]
   
			if c in single_pattern:
				print(f"{single_pattern[c]} {c} null")
			elif c in double_operators_pattern:
				config = double_operators_pattern[c]
				if check_next_char(self.file_contents, self.index, config['second']):
					print(f"{config['match_all']} {c}{config['second']} null")
					self.index += 1
				else:
					print(f"{config['match_first']} {c} null")
			elif c == "\n":
				self.line_num += 1
			elif c == "/":
				if check_next_char(self.file_contents, self.index, "/"):
					# Skip comments to end of line
					while self.index < len(self.file_contents) and self.file_contents[self.index] != "\n":
						self.index += 1
	  
					# It should be new line after skip all comment
					self.line_num += 1
				else:
					print("SLASH / null")
			elif c.isspace():
				# Skip white space
				self.index += 1
				continue
			elif c == "\"":
				content, new_index = scan_string(self.index, self.file_contents)
				if content is not None:
					print(f"STRING \"{content}\" {content}")
				else:
					self.have_err_scan = True
					print(f"[line {self.line_num}] Error: Unterminated string.", file=sys.stderr)

				self.index = new_index + 1
				continue
			elif c.isnumeric():
				value, new_index = scan_numberic(self.index, self.file_contents)
				print(f"NUMBER {value} {float(value)}")
				self.index = new_index
				continue
			elif is_identifier_char(c):
				# indetifier can contains number (e.g _123a) => make sure to check the numeric case first before scan identifier.
				identifier, new_index = scan_identifier(self.index, self.file_contents)
				if identifier in reserved_words:
					print(f"{identifier.upper()} {identifier} null")
				else:
					print(f"IDENTIFIER {identifier} null")
				self.index = new_index
				continue
			else:
				print(f"[line {self.line_num}] Error: Unexpected character: {c}", file=sys.stderr)
				self.have_err_scan = True
	
			self.index += 1
  
		return self.have_err_scan

		