from utils.scraping import Scraping
from utils.text import Text
from sites.olx.types import *

class Olx(Scraping):
	def __init__(self, **args):
		super().__init__(**args)

	def prepare_page_items(self):
		self.click(self.By.XPATH, XPaths.btn_view_grid)

	def get_url(self, category:CategorysOlx='', uf:UFs='', params: dict | ParamsUrlOlx = {}) -> str:
		def strcond(str_l: str, var: any) -> str:
			return str_l+str(var) if var else ''
		
		url_base = 'https://www.olx.com.br/'+category+strcond('/estado-', uf)

		url_params = '?'+'&'.join([strcond(k+'=', v) for k, v in params.items()])
		
		return url_base+url_params
