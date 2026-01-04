import requests
from bs4 import BeautifulSoup

def extract_rating(article):
    RATING_MAP = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    rating_tag = article.find("p", class_="star-rating")
    rating_word = rating_tag["class"][1]
    return RATING_MAP[rating_word]


page = 1


while True:
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    if response.status_code != 200:
        break
    
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        book_name = article.h3.a["title"]
        rating = extract_rating(article)
        print(book_name)
        print(f"rating: {rating} out of 5 stars")
        print()

    page += 1

    print(f"page: {page}\n")
    