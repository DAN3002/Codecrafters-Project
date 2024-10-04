import sys

def exit_program(code):
	print("EOF  null")
	exit(code)

def main():
	if len(sys.argv) < 3:
		print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
		exit(1)

	command = sys.argv[1]
	filename = sys.argv[2]

	if command != "tokenize":
		print(f"Unknown command: {command}", file=sys.stderr)
		exit(1)

	line_num = 1
	have_err_scan = False
	with open(filename) as file:
		file_contents = file.read()

		index = 0
		while index < len(file_contents):
			c = file_contents[index]
			if c == "(":
				print("LEFT_PAREN ( null")
			elif c == ")":
				print("RIGHT_PAREN ) null")
			elif c == "{":
				print("LEFT_BRACE { null")
			elif c == "}":
				print("RIGHT_BRACE } null")
			elif c == "*":
				print("STAR * null")
			elif c == "+":
				print("PLUS + null")
			elif c == ".":
				print("DOT . null")
			elif c == ",":
				print("COMMA , null")
			elif c == ";":
				print("SEMICOLON ; null")
			elif c == "-":
				print("MINUS - null")
			elif c == "/":
				print("SLASH / null")
			elif c == "\n":
				line_num += 1
			elif c == "=":
				if check_next_char(file_contents, index + 1, "="):
					print("EQUAL_EQUAL == null")
					index += 1
				else:
					print("EQUAL = null")
			else:
				print(f"[line {line_num}] Error: Unexpected character: {
					  c}", file=sys.stderr)
				have_err_scan = True
    
			index += 1

	exit_program(0 if not have_err_scan else 65)

def check_next_char(file_contents, index, expected_char):
	if index >= len(file_contents):
		return False

	if file_contents[index] != expected_char:
		return False

	return True

if __name__ == "__main__":
	main()
