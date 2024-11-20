from utils.scraping import Scraping

web = Scraping(browser="Firefox")
web.go('https://olx.com.br')
for i in range(10):
	web.scrolled_page(100*(i+1))
