import requests 
from bs4 import BeautifulSoup

page = 1

while True:
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    if response.status_code != 200:
        break

    
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    for article in soup.find_all("article", class_="product_pod"):
        book_name = article.h3.a["title"]
        book_price = article.find("p", class_= "price_color").get_text(strip=True)
        availability = article.find("p", class_= "instock availability").get_text(strip=True)
        print(book_name)
        print(book_price)
        print(availability)  
        print()
    
    page += 1