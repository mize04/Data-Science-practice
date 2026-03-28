import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
titles=[]
prices=[]


# find book titles
book_titles = [book.h3.a["title"] for book in soup.find_all("article", class_="product_pod")]
for title in book_titles:
    titles.append(title.strip())
# find book prices
book_prices = soup.find_all("p", class_="price_color")
for price in book_prices:
    prices.append(price.text.strip())
# find book star ratings

print(len(book_titles))
print(len(titles))
print(len(prices))

# create a DataFrame
df = pd.DataFrame({"Title": titles, "Price": prices, })       
print(df.head(20))
