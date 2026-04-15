import requests
from bs4 import BeautifulSoup
import random

def get_random_quote():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select(".quote")
    q = random.choice(quotes)

    text = q.select_one(".text").text
    author = q.select_one(".author").text

    return text, author


def get_author_wiki(author):
    search_url = f"https://en.wikipedia.org/w/index.php?search={author.replace(' ', '+')}"

    response = requests.get(search_url)

    if response.status_code != 200:
        return "No info found."

    soup = BeautifulSoup(response.text, "html.parser")

    # find first search result link
    result = soup.select_one(".mw-search-result-heading a")

    if result:
        page_url = "https://en.wikipedia.org" + result["href"]

        page = requests.get(page_url)
        soup = BeautifulSoup(page.text, "html.parser")

        paragraphs = soup.select("p")

        for p in paragraphs:
            text = p.text.strip()
            if text and len(text) > 50:
                return text[:500]

    return "No info found."