import requests
from bs4 import BeautifulSoup

def raspagem():
	page = requests.get("http://g1.globo.com/ultimas-noticias.html")
	soup = BeautifulSoup(page.text, "html.parser")

	news = [soup.find(class_="feed-post-link")]

	for show_news in news:
		text = (str(show_news.contents[0]) + "\n" + str(show_news.get("href")))

	print(text)

def mostar():
	return raspagem()

mostar()