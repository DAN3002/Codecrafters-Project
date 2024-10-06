from app.scanner import LoxScanner

class LoxParser:
	def __init__(self, filepath) -> None:
		self.filepath = filepath
  
	def start(self):
		scanner = LoxScanner(filepath=self.filepath)
		tokens = scanner.start()
	
		for token in tokens:
			print(token['value'])

__all__ = "LoxParser"
