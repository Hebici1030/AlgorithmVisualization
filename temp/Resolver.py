import datetime
import datetime as dt
import matplotlib.pyplot as plt
ax =[]
ay =[]
with open("C:\\Users\\Hasee\\Desktop\\新建文本文档 (2).txt",encoding="utf-8") as file:
    for item in file:
        if item == '':
            break
        data = dt.datetime.strptime(item[0:-1], "%Y年%m月%d日")
        temp = data.year.__str__()+"-"+data.month.__str__()+"-"+data.day.__str__()
        str = dt.datetime.strptime(temp, "%Y-%m-%d")
        if str not in ax:
            ax.append(str)
            ay.append(1)
        else:
            index = ax.index(str)
            ay[index] +=1
print(len(ax))
print(len(ay))
print(ax)
print(ay)
from matplotlib.ticker import FuncFormatter
plt.rcParams['figure.figsize']=(12.8, 7.2)
fig, tax = plt.subplots()
tax.plot(ax, ay)
import matplotlib.dates as mdates
xfmt = mdates.DateFormatter('%y-%m-%d')
tax.xaxis.set_major_formatter(xfmt)
plt.ylabel(u'搜索量（次）',fontproperties='SimHei',rotation=90)
plt.xlabel(u'时间（日）',fontproperties='SimHei')
plt.xlim([datetime.date(2021,1,1),datetime.date(2021,1,30)])
plt.ylim([0,7])
plt.title(u'2021.1-2023.1疫情微博热搜搜索量',fontproperties='SimHei')
tax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
tax.get_yaxis().get_major_formatter().set_scientific(False)
fig.subplots_adjust(left=0.08, bottom=0.5, right=0.99, top=0.95)
plt.gcf().autofmt_xdate()
plt.grid(True)
plt.show()
# dates = [dt.datetime.strptime(date, "%Y-%m-%d") for date in tempAx]