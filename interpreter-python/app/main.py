import sys
from app.scanner import LoxScanner, TokenType
from app.parser import LoxParser


def main():
	if len(sys.argv) < 3:
		print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
		exit(1)

	command = sys.argv[1]
	filename = sys.argv[2]

	match command:
		case "tokenize":
			scanner = LoxScanner(filepath=filename)
			tokens = scanner.start()
   
			have_err_scan = False
			for token in tokens:
				match token["token_type"]:
					case TokenType.SCAN_ERROR:
						have_err_scan = True
						print(f"[line {token['line_num']}] Error: {token['error']}", file=sys.stderr)
					case TokenType.RESERVED_WORD:
						print(f"{token['value'].upper()} {token['message']}")
					case default:
						print(f"{token['token_type'].name} {token['message']}")

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
