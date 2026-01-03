import requests
from bs4 import BeautifulSoup

page = 1

while True:
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)

    if response.status_code != 200:
        break

    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote" )

    for quote in quotes:
        text = quote.get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)
        print(text)
        print(f"by {author}")
        print()
    
    page += 1  