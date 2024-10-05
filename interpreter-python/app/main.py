import sys
from app.scanner.LoxScanner import LoxScanner

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

	scanner = LoxScanner(filepath=filename)
	have_err_scan = scanner.start()

	exit_program(0 if not have_err_scan else 65)

if __name__ == "__main__":
	main()
