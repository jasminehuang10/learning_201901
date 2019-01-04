


#json下载
'''
from urllib.request import urlopen
import json

json_url="https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017" \
         ".json"
response=urlopen(json_url)
#读取数据
req=response.read()
#将数据写入文件
with open("btc_close_2017_urllib.json","wb") as f:
    f.write(req)
#加载json格式
file_urllib=json.loads(req)
print(file_urllib)


import requests

json_url="https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017" \
         ".json"
req=requests.get(json_url)

with open("btc_close_2017_urllib.json","w") as f:
    f.write(req.text)

file_requests=req.json()'''

import json
from datetime import datetime
import math


#将数据加载到一个列表中
filename="btc_close_2017_urllib.json"
with open(filename) as f:
    btc_data=json.load(f)

dates=[]
months=[]
weeks=[]
weekdays=[]
close=[]

for btc_dict in btc_data:
    dates.append(btc_dict["date"])
    months.append(int(btc_dict["month"]))
    weeks.append(int(btc_dict["week"]))
    weekdays.append(btc_dict["weekday"])
    close.append(int(float(btc_dict["close"])))

import pygal
line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title="收盘价（¥）"
#line_chart.xml_filters=dates
#N=20
#line_chart._x_labels_major=dates[::N]
line_chart.x_labels=dates
close_log=[math.log10(_) for _ in close]
line_chart.add("收盘价（¥）",close_log)
line_chart.render_to_file('收盘价折线图.svg')

with open("收盘价Dashboard.html","w",encoding="utf8") as html_file:
    html_file.write("<html><head><title>收盘价Dashboard</title><metacharset='utf"
                    "-8'></head><body>\n")
    for svg in ["收盘价折线图.svg"]:
        html_file.write("<object type='image/svg+xml' data='{0}' "
                        "height=500></object>\n".format(svg))
        html_file.write("</body></html>")


















