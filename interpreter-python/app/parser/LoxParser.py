class LoxParser:
	def __init__(self, filepath) -> None:
		f = open(filepath)
		self.file_contents = f.read()
		f.close()
  
	def start(self):
		for line in self.file_contents:
			print(line)
