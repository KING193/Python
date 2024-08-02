# WEB SCRAPING-2
import requests
import bs4

goodreads_website = requests.get("https://www.goodreads.com/quotes?page=2")
html = goodreads_website.text

html_parser = bs4.BeautifulSoup(html, "html.parser")
quotes = html_parser.findAll("div", attrs={"class": "quoteText"})

for quote in quotes:
	print(quote.text)

print(len(quotes))