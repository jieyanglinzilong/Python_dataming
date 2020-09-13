# coding=utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager
#初始化字体
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyhbd.ttc")


#另外一种设置字体的方式
#my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
#设置x轴
x = range(0, 120)
#设置y轴的长度
y = [random.randint(20,35) for i in range(120)]
#设置图片的大小和像素
plt.figure(figsize=(20,8),dpi=80)
print(type(x))
print(type(y))
plt.plot(x,y)

#调整x轴的刻度
#_x =list(x)[::6]

_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
#取步长，数字和字符串一一对应，数据的长度一样
#plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font) #rotaion旋转的度数

#添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)
#设置步长 设置旋转45度 设置字体
plt.xticks(list(x)[::3],_xtick_labels[::3], rotation=45, fontproperties=my_font)
plt.show()
