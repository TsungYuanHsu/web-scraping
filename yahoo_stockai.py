import requests
import pprint

r = requests.get('https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;period=d;symbols=%5B%2200762.TW%22%5D?bkt=TW-Stock-Desktop-NewTechCharts-Rampup&device=desktop&ecma=modern&feature=enableGAMAds%2CenableGAMEdgeToEdge%2CenableEvPlayer%2CenableHighChart&intl=tw&lang=zh-Hant-TW&partner=none&prid=6831potk09u12&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.4.529&returnMeta=true')
print(r.status_code)
data = r.json()
pprint.pprint(r.json())

