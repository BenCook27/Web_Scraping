import requests
import pandas as pd
from bs4 import BeautifulSoup


URL = 'https://www.thegoodguys.com.au/computers-tablets-and-gaming/desktop-and-laptop/laptops?page=1'
html = requests.get(URL)

soup = BeautifulSoup(html.content, 'html.parser')

products = soup.find_all('div', class_='product-tile')


product_data = []
for product in products:
    name = product.find('h4', class_='product-tile-name').text.strip()
    price = product.find('span', class_='pricepoint-price').text.strip().replace('\n', '').replace('\t', '').replace('+', '')
    hyperlink = product.find('a').get('href')

    data = name, price, hyperlink
    product_data.append(data)


print(product_data)

df = pd.DataFrame(product_data, columns=['Product Name', 'Price', 'Hyperlink'])
df.to_csv('Good_guys_scraper_data.csv', index=False)
