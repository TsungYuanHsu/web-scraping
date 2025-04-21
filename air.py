import requests
import pprint
import re

r = requests.get('https://airtw.moenv.gov.tw/json/camera_ddl_pic/camera_ddl_pic_2025042120.json')
if r.status_code == 200:
    print('Connection is ok')
    data = r.json()
    # name_aqi = [d for d in data if '富貴角' in d['Name']] [0] ['Name']
    # result = re.search(r'AQI=(\d+)', name_aqi).group(1)
    # # group(): return what regex can recognize
    # # group(1): return the first capture item
    # print(result)
    for d in data:
        try:
            location = re.search(r'(.+)\(AQI=(\d+)', d['Name']).group(1)
            aqi = re.search(r'(.+)\(AQI=(\d+)', d['Name']).group(2)
        except AttributeError:
            continue
        print(location, aqi)

