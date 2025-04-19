# Crawl stock price from https://tw.stock.yahoo.com/quote/2330.TW

import requests
from bs4 import BeautifulSoup


r = requests.get('https://tw.stock.yahoo.com/quote/2330.TW')
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')


ul = soup.find('ul', class_='D(f) Fld(c) Flw(w) H(192px) Mx(-16px)')
li = ul.find_all('li')[1]

# Find 開盤 price
price = li.find_all('span')[1].text
print(price)

# Use find_next to find next result from li tag
print(li.find_next('li'))


