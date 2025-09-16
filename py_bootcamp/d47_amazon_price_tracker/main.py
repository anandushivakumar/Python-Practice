from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/instant_pot/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

response = requests.get(URL, headers = header)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')

price_whole = soup.find('span', class_="a-price-whole")
# print(price_whole.getText()) # type: ignore

price_decimal = soup.find('span', class_="a-price-fraction")
# print(price_decimal.getText()) # type: ignore

price = price_whole.getText() + price_decimal.getText() # type: ignore
price_float = float(price)
print(price_float)

# sending the email to user is not implemented