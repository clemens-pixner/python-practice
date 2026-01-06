import requests
from bs4 import BeautifulSoup

prices = []
page = 1

while True:
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    if response.status_code != 200:
        break

    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article", class_="product_pod")
    
    if not articles:
        break

    for article in articles:
        name = article.h3.a["title"]
        price_text = article.find("p", class_="price_color").text
        price_float = float(price_text[1:])
        prices.append(price_float)

    page += 1

avg_p = sum(prices) / len(prices)
print(f"Average book price: £{avg_p} ")
