import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt
from matplotlib import font_manager
catering_sale = '笔记本电脑.xlsx'
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyhbd.ttc")
data = pd.read_excel(catering_sale,  usecols=[1])
data1=pd.read_excel(catering_sale,usecols=[2])

data = data[(data[u'价格']>400)&(data[u'价格']<15000)]
statists = data.describe()
statists.loc['var'] = statists.loc['std']/statists.loc['mean']
print(statists)
#print(data1)

#print("第一" ,data1.loc[1])
n = data1.values.tolist()
n2 = np.array(data1)
n4=np.array(data)

n3= n2.tolist()
info = list()
k=1
#销量
for i in n3:
 j=k+1
 string = ''.join(str(n3[k:j]))
 string =re.findall(r"\d+",string)
 m = list(map(int,string))
 info.append(m)
 k=k+1
k=1
#print(info)
info1=list()
#gn=pd.DataFrame(info1,info)


#价格

for i in n4:
 j=k+1
 string = ''.join(str(n4[k:j]))
 string = re.findall(r"\d+", string)
 g = list(map(int,string))
 info1.append(g)
 k=k+1
#print(len(info))
#print(len(info1))
ln=len(info)-len(info1)
print(type(ln))
print(ln)
for z in range(ln):
  info1.append(0)
#print(type(info1))
#print(type(info))
#print(info[0])
#print(info1[0])
#while z<len(info1):
 # l={info1[z]:info[z]}
#print(l)
print(len(info)-len(info1))
x=range(len(info1))
info = list(map())
plt.plot(x, info)
print("*****")
#设置x轴刻度
_xtick_labels = ["{}元".format(i) for i in x]
plt.xticks(x[:500],_xtick_labels[:500],fontproperties=my_font)
#绘制网格
plt.grid(alpha=0.4,linestyle=':', color="#F08080")

#添加图例
plt.legend(prop=my_font,loc="upper left")

#展示
plt.show()
