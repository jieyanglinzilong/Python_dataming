import pandas as pd
import numpy as np
from mxnet import autograd, nd
from mxnet.gluon import data as gdata
import matplotlib.pyplot as plt
file = '笔记本电脑.xlsx'

data = pd.read_excel(file)
x, y = data.shape

num = pd.DataFrame(np.arange(x*y).reshape(x, y))
#num.columns=['价格', ' 售价']

#x = num.iloc[:, 0]
#y= num.iloc[:,1]
#num.columns=['价格', ' 售价', '销售额']
#print(data.describe())
#print(type(num))
Data = pd.DataFrame(np.arange(x).reshape(x,1))
print(Data.shape)
print(num.shape)
Data = data['价格'].mul(data['dealcnt'])
data.insert(3,'零售额', Data)
#print(data.iloc[:, 3:4])
num = data.iloc[2:, [1, 2, 3]]
num.columns = ['价格', ' 售价', '销售额']
dataset = gdata.ArrayDataset(num)
print(type(num))


