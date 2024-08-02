# WEB SCRAPING

#pip install requests
#pip install bs4

# https://www.goodreads.com/quotes
import requests
import bs4

goodreads_website = requests.get("https://www.goodreads.com/quotes")
html = goodreads_website.text # or goodreads_website.content

html_parser = bs4.BeautifulSoup(html, "html.parser")
quote = html_parser.find("div", attrs={"class": "quoteText"}).text
print(quote)