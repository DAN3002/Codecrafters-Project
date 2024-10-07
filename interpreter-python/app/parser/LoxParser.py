from app.scanner import LoxScanner, TokenType

class LoxParser:
	def __init__(self, filepath) -> None:
		self.filepath = filepath
  
	def start(self):
		scanner = LoxScanner(filepath=self.filepath)
		tokens = scanner.start()
	
		for token in tokens:
			match token['token_type']:
				case TokenType.NUMBER:
					print(float(token['value']))
				case default:
					print(token['value'])

__all__ = "LoxParser"
