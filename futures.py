# Crawl 5 day data from https://www.taifex.com.tw/cht/3/futContractsDate

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def crawl(date):
    r = requests.get('https://www.taifex.com.tw/cht/3/futContractsDate?queryDate={}%2F{}%2F{}'.format(date.year, date.month, date.day))
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        print('Collecting data for:', date)
    else:
        print('Connection error')

date = datetime.now()
collect_daycount = 0

while collect_daycount < 5:
    crawl(date)
    collect_daycount += 1
    date = date - timedelta(days=1)




