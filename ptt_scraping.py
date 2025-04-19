# Crawl title data from https://disp.cc/b/PttHot

import requests
from bs4 import BeautifulSoup

r = requests.get('https://disp.cc/b/PttHot')  # Build the connection with website
print(r)  # <Response [200]> means connection is ok
print(r.text)  # return page source code


# Get the title from the PttHot
soup = BeautifulSoup(r.text, 'html.parser')  # Create the instance. Input target content and parser

soups = soup.find_all('span', class_='titleColor')  # Use find_all to find information within span tag and titleColor class
print([s.text for s in soups])

# Get the link of the title: find href (hyper reference)
soup = BeautifulSoup(r.text, 'html.parser')
spans = soup.find_all('span', class_='listTitle')  # L34, nowrap, and listTitle are all class
for span in spans:
    base_url = 'https://disp.cc'
    title_url = span.find('a').get('href')
    if title_url == '/b/PttHot/59l9':
        continue
    url = base_url + title_url
    title = span.text
    print(f'{title}\n{url}')


spans = soup.select('span.listTitle')
for span in spans:
    base_url = 'https://disp.cc'
    title_url = span.find('a').get('href')
    if title_url == '/b/PttHot/59l9':
        continue
    url = base_url + title_url
    title = span.text
    print(f'{title}\n{url}')
