from sites.olx.olx import Olx, XPaths

class Inova(Olx):
	def __init__(self):
		super().__init__(browser='firefox')
		self.start_scraping()
	
	def start_scraping(self):
		t = self.get_url('imoveis','ac', params={'ps': 100, 'pe': '1000', 'sp': 5, 'f': 'c'})
		print(t)