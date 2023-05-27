from copy import copy
import matplotlib.pyplot as plt
import datetime as dt
def y_update_scale_value(temp, position):
    result = temp//1000
    return "{}k".format(int(result))
SkipArray = ["社会","新","河北省","时事","主持人：央视新闻"]
StartIndex = 2
ax = []
ay = []
prvitem = None
end = 291
end2 =801
end3 = 199
end4 =401
end5 = 2001
with open("C:\\Users\\Hasee\\Desktop\\2021.1.1-2021.5.20.txt",encoding="utf-8") as file:
    for item in file:
        if item in SkipArray:
            continue;
        if item == end.__str__():
            ay.append(prvitem[0:-1])
            break;
        if "最后在榜时间" in item:
            ax.append(item[7:-7])
            continue
        if item == str(StartIndex.__str__()+"\n"):
            ay.append(prvitem[0:-1])
            StartIndex+=1
        else:
            prvitem = copy(item)
ax.reverse()
ay.reverse()
print(len(ax))
StartIndex = 402
with open("C:\\Users\\Hasee\\Desktop\\5-8.txt",encoding="utf-8") as file1:
    for item in file1:
        if item == end2.__str__():
            ay.append(prvitem[0:-1])
            break;
        if "最后在榜时间" in item:
            ax.append(item[7:-7])
            continue
        if item == str(StartIndex.__str__()+"\n"):
            ay.append(prvitem[0:-1])
            StartIndex+=1
        else:
            prvitem = copy(item)
ax[290:] = list(reversed(ax[290:]))
ay[290:] = list(reversed(ay[290:]))
print(len(ax))
StartIndex = 2
with open("C:\\Users\\Hasee\\Desktop\\8.15-10.28.txt",encoding="utf-8") as file1:
    for item in file1:
        if item == end3.__str__():
            ay.append(prvitem[0:-1])
            break;
        if "最后在榜时间" in item:
            ax.append(item[7:-7])
            continue
        if item == str(StartIndex.__str__()+"\n"):
            ay.append(prvitem[0:-1])
            StartIndex+=1
        else:
            prvitem = copy(item)
ax[690:] = list(reversed(ax[690:]))
ay[690:] = list(reversed(ay[690:]))
print(len(ax))
StartIndex = 2
with open("C:\\Users\\Hasee\\Desktop\\2021.5.21-2021.12.12.txt",encoding="utf-8") as file1:
    for item in file1:
        if item == end4.__str__():
            ay.append(prvitem[0:-1])
            break;
        if "最后在榜时间" in item:
            ax.append(item[7:-7])
            continue
        if item == str(StartIndex.__str__()+"\n"):
            ay.append(prvitem[0:-1])
            StartIndex+=1
        else:
            prvitem = copy(item)
ax[888:] = list(reversed(ax[888:]))
ay[888:] = list(reversed(ay[888:]))
print(len(ax))
StartIndex = 2
with open("C:\\Users\\Hasee\\Desktop\\2021.12.13-2022.12.txt",encoding="utf-8") as file2:
    for item in file2:
        if item in SkipArray:
            continue;
        if item == end5.__str__():
            ay.append(prvitem[0:-1])
            break;
        if "最后在榜时间" in item:
            ax.append(item[7:-7])
            continue
        if item == str(StartIndex.__str__()+"\n"):
            ay.append(prvitem[0:-1])
            StartIndex+=1
        else:
            prvitem = copy(item)
ax[1288:] = list(reversed(ax[1288:]))
ay[1288:] = list(reversed(ay[1288:]))
print(len(ax))
StartIndex=2
end6 = 31
with open("C:\\Users\\Hasee\\Desktop\\2023.1.txt",encoding="utf-8") as file2:
    for item in file2:
        if item in SkipArray:
            continue;
        if item == end6.__str__():
            ay.append(prvitem[0:-1])
            break;
        if "最后在榜时间" in item:
            ax.append(item[7:-7])
            continue
        if item == str(StartIndex.__str__()+"\n"):
            ay.append(prvitem[0:-1])
            StartIndex+=1
        else:
            prvitem = copy(item)
ax[3288:] = list(reversed(ax[3288:]))
ay[3288:] = list(reversed(ay[3288:]))
print(len(ax))
print(len(ay))
tempAx=[]
tempAy=[]

for i in range(len(ax)):
    if ax[i] not in tempAx:
        tempAx.append(ax[i])
        tempAy.append(int(ay[i]))
    else:
        index = tempAx.index(ax[i], 0, len(tempAx))
        tempAy[index] += int(ay[i])
tempAy[tempAy.index(max(tempAy))] = 20000000
tempAy[tempAy.index(max(tempAy))] = 20000000
from matplotlib.ticker import FuncFormatter
plt.rcParams['figure.figsize']=(12.8, 7.2)
dates = [dt.datetime.strptime(date,"%Y-%m-%d")for date in tempAx]
fig, ax = plt.subplots()
ax.plot(dates, tempAy)
import matplotlib.dates as mdates
xfmt = mdates.DateFormatter('%y-%m-%d')
ax.xaxis.set_major_formatter(xfmt)
plt.ylim([0,35000000])
plt.ylabel(u'搜索量（次）',fontproperties='SimHei',rotation=90)
plt.xlabel(u'时间（日）',fontproperties='SimHei')
plt.title(u'2021.1-2023.1疫情微博热搜搜索量',fontproperties='SimHei')
ax.xaxis.set_major_locator(mdates.DayLocator(interval=30))
ax.get_yaxis().get_major_formatter().set_scientific(False)
fig.subplots_adjust(left=0.08, bottom=0.5, right=0.99, top=0.95)
plt.gcf().autofmt_xdate()
plt.grid(True)
plt.gca().yaxis.set_major_formatter(FuncFormatter(y_update_scale_value))
plt.savefig("test1.png",format="png")
plt.show()