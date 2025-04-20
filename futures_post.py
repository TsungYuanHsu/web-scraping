# Crawl data from https://www.taifex.com.tw/cht/3/futContractsDate via requests.post()

import requests
from bs4 import BeautifulSoup

payload = {
    'queryDate': '2025/04/16',
    'button': '送出查詢',
}
r = requests.post('https://www.taifex.com.tw/cht/3/futContractsDate', data=payload)
if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify())
    print('Collecting data for: 2025/04/16')
else:
    print('Connection error')
