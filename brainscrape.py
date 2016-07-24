# BrainyQuote Web Scraper (By Keyword)
# Alaina Kafkes

import requests
from bs4 import BeautifulSoup
example_key = "lemons"

def getQuotes(keyword=example_key):
    """
    Given a keyword, uses Requests & BeautifulSoup to obtain (quote, author) tuples from BrainyQuote.
    """
    # Initialize lists
    quoteArray = []
    authorArray = []
    
    # Obtain BrainyQuote page html
    base_url = "http://www.brainyquote.com/quotes/keywords/"
    url = base_url + keyword + ".html"
    response_data = requests.get(url).text[:]
    soup = BeautifulSoup(response_data, 'html.parser')

    # Populate quoteArray
    for item in soup.find_all("span", class_="bqQuoteLink"):
        quoteArray.append(item.get_text().rstrip())

    # Populate authorArray
    for item in soup.find_all("div", class_="bq-aut"):
        authorArray.append(item.get_text())

    # Create list of tuples of the form (quote, author)
    return zip(quoteArray, authorArray)
