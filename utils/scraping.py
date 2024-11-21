from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from utils.text import Text
from utils.log import Log

class Scraping:
	def __init__(self, **args):
		self.__driver = self.__create_driver(**args)
		self.By = By
		self.Keys = Keys

	def __create_driver(self, browser='Chrome', **_) -> WebDriver:
		browser = Text.capitalize(browser)

		if not hasattr(webdriver, browser):
			Log.warn(f'O browser: "{browser}" não existe. Mudando para usar o Chrome')
			browser = 'Chrome'
		
		oi = webdriver.Chrome()
		oi.add_cookie
		return getattr(webdriver, browser)()

	def go(self, url: str):
		self.__driver.get(url)

	def find_element(self, by: type[By], query: str) -> WebElement:
		return self.__driver.find_element(by, query)

	def scrolled_page(self, y: int):
		ActionChains(self.__driver)\
				.scroll_by_amount(0, y)\
				.perform()

	def click(self, by: type[By], query: str) -> None:
		self.find_element(self, by, query).click()