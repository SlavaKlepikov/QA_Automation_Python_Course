from bs4 import BeautifulSoup
import requests


def main_function(page_url):
    next_page_url = page_url
    counter = 0
    while True:
        counter += 1
        r = requests.get(next_page_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        next_page_link = soup.find("li", {"class": "next"})
        if not next_page_link:
            break
        next_page_url = page_url + next_page_link.a["href"]
    return counter


if __name__ == "__main__":
    url = "https://quotes.toscrape.com"
    pages_count = main_function(url)
    print(f"Number of pages: {pages_count}")



