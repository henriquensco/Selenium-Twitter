from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

class Twitter():
	def __init__(self):
		self.driver = webdriver.Chrome('./chromedriver')
		self.driver.get("https://twitter.com/login")

	def login(self):
		write_email = self.driver.find_element_by_class_name("js-username-field")
		write_email.send_keys("") # Email de Login do Twitter

		write_pass = self.driver.find_element_by_class_name("js-password-field")

		write_pass.send_keys("") # Senha de Acesso do Twitter

		write_pass.send_keys(Keys.RETURN)

	def scrap(self):
		page = requests.get("http://g1.globo.com/ultimas-noticias.html")
		soup = BeautifulSoup(page.text, "html.parser")

		news = [soup.find(class_="feed-post-link")]

		for show_news in news:
			text = (str(show_news.contents[0]) + "\n" + str(show_news.get("href")) + "\n" + str("Selenium and Twitter"))

		return text

	def twitar(self):
		post = self.scrap()

		twitar = self.driver.find_element_by_name("tweet")
		twitar.send_keys("{}".format(post))
		send_tweet = self.driver.find_element_by_class_name("tweet-action")
		return send_tweet.click()

Twi = Twitter()
Twi.login()
Twi.twitar()
