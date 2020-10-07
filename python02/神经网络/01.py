#-*- coding: utf-8 -*-
#使用神经网络算法预测销量高低
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import pandas as pd
from cmplot import *
#参数初始化
from numpy import shape
from 决策树.data.cm_plot import cm_plot
inputfile = 'D:/PythonProject/python02/决策树/data/sales_data.xls '
data = pd.read_excel(inputfile, index_col = u'序号') #导入数据
header = data.columns.values;
print(header)
data[u'销量'][(data[u'销量']=='高')]= "1"
data[u'是否有促销'][(data[u'是否有促销']=='是')]= "1"
data[u'天气'][(data[u'天气']=='好')]= "1"
data[u'是否周末'][(data[u'是否周末']=='是')] = "1"
print(data)
data[data != "1"] = 0
data = pd.DataFrame(data, dtype="int")
print(data)
x = data.iloc[:,:3]
y = data.iloc[:,3]
model = Sequential()
model.add(Dense(30, Activation('relu'), input_dim=3))
#model.add)
model.add(Dense(1, Activation('sigmoid'), 3))
#model.add(Dense(input_dim=10, output_dim = 1))
#model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid函数作为激活函数

model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#编译模型。由于我们做的是二元分类，所以我们指定损失函数为binary_crossentropy，以及模式为binary
#另外常见的损失函数还有mean_squared_error、categorical_crossentropy等，请阅读帮助文件。
#求解方法我们指定用adam，还有sgd、rmsprop等可选

model.fit(x, y, epochs=1000, batch_size =3) #训练模型，学习一千次
print(shape(y))
print(shape(x))
print(x)
print(y)
yp = model.predict_classes(x).reshape(len(y)) #分类预测
print(yp)
cm_plot(y, yp).show() #显示混淆矩阵可视化结果