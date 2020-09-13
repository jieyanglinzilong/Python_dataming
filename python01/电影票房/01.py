import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyhbd.ttc")
file = "D:/python/电影票房/10231_20190831.xlsx";
data = pd.read_excel(file,index_col=u'日期')
print(data.describe())
#print(data)
print(data[u'当日票房(万美元)'].corr(data[u'上映天数']))
print(data[u'累计票房(万美元)'].corr(data[u'上映天数']))
#研究爆款电影对总票房的贡献
data1=data[u'累计票房(万美元)'].sort_values()
data2=data1.tail(800)
sum =data2.sum()
el = data1.sum()
colors = {'yellowgreen', 'lightskyblue'}
labels = '爆款票房', '非爆款'
size1 =(int)((sum/el)*100)
print(sum/el)
print("*"*70,size1)
size2=100-size1
size = [size1, size2]
explode = (0.1, 0)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(size, explode=explode, labels=labels,colors=colors,shadow=True,startangle=90,autopct='%1.1f%%')
plt.axis('equal')
plt.show()