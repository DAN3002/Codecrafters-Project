import sys

from app.scanner.constants import single_pattern, double_operators_pattern
from app.scanner.utils import check_next_char, scan_string

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
					line_num += 1
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
					print(f"[line {self.line_num}] Error: Unterminated string.", file=sys.stderr)

				self.index = new_index
			else:
				print(f"[line {self.line_num}] Error: Unexpected character: {c}", file=sys.stderr)
				self.have_err_scan = True
	
			self.index += 1
  
		return self.have_err_scan

		