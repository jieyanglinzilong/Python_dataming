#导入必要的库
import os

import xlrd
from numpy import shape
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
import pandas as pd
filename ='D:/PythonProject/python02/决策树/data/sales_data.xls '
data = pd.read_excel(filename)
header = data.columns.values;
print(header)

"""""
data[u'销量'][(data[u'销量']=='高')]= "1"
data[u'是否有促销'][(data[u'是否有促销']=='是')]= "1"
data[u'天气'][(data[u'天气']=='好')]= "1"
data[data != "1"] = -1
data = pd.DataFrame(data, dtype="int")
x = data.iloc[:,:3].values
y = data.iloc[:,3].values
"""
lables = []    #用于存储标记实例，也就是本例中的是否购入电脑
feature = []   #用于存储特征
data1 = xlrd.open_workbook(os.path.join('D:/PythonProject/python02/决策树/data', 'sales_data.xls'))
table = data1.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    if i == 0:
        continue
    num = table.row_values(i)

    num= num[4]
    print(num)

    lables.append(num)
    features = {}
    for each in range(1, len(table.row_values(i))- 1):
       features[header[each]] = table.row_values(i)[each]
    feature.append(features)

"""
#reader返回的值是csv文件中每行的列表，将每行读取的值作为列表返回
for row in data:
    lables.append(row[len(row)-1])
    features = {}
    for each in range(1,len(row)-1):
        print(row)
        features[header[each]] = row[each]
    feature.append(features)
   # print(feature)
"""
#print(feature)
#print(lables)
vec = DictVectorizer()
x = vec.fit_transform(feature).toarray()

print('特征提取后的X'+'\n'+str(x))
# print(headers)
lab = preprocessing.LabelBinarizer()
print(lables)
y = lab.fit_transform(lables)

print('Y'+'\n'+str(y))
result = tree.DecisionTreeClassifier(criterion='entropy')
result.fit(x,y)
with open('tree1.dot', 'w') as f:
    f = tree.export_graphviz(result,out_file=f,feature_names=vec.get_feature_names())
print(shape(x))
print(shape(y))