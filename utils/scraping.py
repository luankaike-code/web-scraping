from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.text import Text
from utils.log import Log

class Scraping:
	def __init__(self, **args):
		self.driver = self.__create_driver(**args)

	def __create_driver(self, browser='Chrome', **_) -> WebDriver:
		browser = Text.capitalize(browser)

		if not hasattr(webdriver, browser):
			Log.warn(f'O browser: "{browser}" não existe. Mudando para usar o Chrome')
			browser = 'Chrome'
		
		oi = webdriver.Chrome()
		oi.add_cookie
		return getattr(webdriver, browser)()

	def go(self, url: str):
		self.driver.get(url)

	def find_element(self, by, query):
		return self.driver.find_element(by, query)

	def scrolled_page(self, y: int):
		ActionChains(self.driver)\
				.scroll_by_amount(0, y)\
				.perform()
