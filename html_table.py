# Crawl table data from https://www.w3schools.com/html/html_tables.asp

import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.w3schools.com/html/html_tables.asp')
# print(r.status_code)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('table')
# print(table)

list = []
for tr in table.find_all('tr'):
    if tr.find_all('th'):
        Company, Contact, Country = [th.text for th in tr.find_all('th')]
        column = [Company, Contact, Country]
    elif tr.find_all('td'):
        Company, Contact, Country = [td.text for td in tr.find_all('td')]
        list.append([Company, Contact, Country])


df = pd.DataFrame(list, columns=column)
df.to_excel('html_table.xlsx')
df.to_html('html_table.html')

