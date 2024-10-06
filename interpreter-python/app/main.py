import sys
from app.scanner.LoxScanner import LoxScanner
from app.parser.LoxParser import LoxParser

def main():
	if len(sys.argv) < 3:
		print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
		exit(1)

	command = sys.argv[1]
	filename = sys.argv[2]

	match command:
		case "tokenize":
			scanner = LoxScanner(filepath=filename)
			have_err_scan = scanner.start()
   
			print("EOF  null")
			exit(0 if not have_err_scan else 65)
		case "parse":
			parser = LoxParser(filepath=filename)
			parser.start()
			exit(0)
		case default:
			print(f"Unknown command: {command}", file=sys.stderr)
			exit(1)

if __name__ == "__main__":
	main()
