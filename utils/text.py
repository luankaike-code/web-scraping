class Text:
	@staticmethod
	def capitalize(string: str) -> str:
		return string.lower().capitalize()

	@staticmethod
	def fromText(string: any) -> str:
		if string == None:
			return ''
		return str(string)