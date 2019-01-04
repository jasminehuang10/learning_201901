import csv
from matplotlib import pyplot as plt

filename="sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)

    #打印文件开头及其位置
    for index,column_header in enumerate(header_row):
        print(index,column_header)

    #提取并读取数据-最高温和最低温
    highs,lows=[],[]
    for row in reader:
        high=int(row[1])
        highs.append(high)
        low=int(row[3])
        lows.append(low)

    dates=[date for date in range(1,32)]

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)

#设置图形格式
plt.title("Daily high and low temperatures,July 2014",fontsize=24)
plt.xlabel("",fontsize=16)
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.savefig("Daily high and low temperatures,July 2014.png")