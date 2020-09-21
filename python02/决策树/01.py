import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz
from six import StringIO
filename ='D:/PythonProject/python02/决策树/data/sales_data.xls '
data = pd.read_excel(filename, index_col = u'序号');
#数据是类别标签，要将它转换为数据
#用1来表示“好”、“是”、“高”这三个属性，用-1来表示“坏”、“否”、“低”
data[u'销量'][(data[u'销量']=='高')]= "1"
data[u'是否有促销'][(data[u'是否有促销']=='是')]= "1"
data[u'天气'][(data[u'天气']=='好')]= "1"
data[data != "1"] = -1
data=pd.DataFrame(data, dtype="int")
print(data)
x = data.iloc[:,:3].values
y = data.iloc[:,3].values
dtc=DTC(criterion='entropy')
dtc.fit(x, y)

with open('tree.dot', 'w') as f:
    f =export_graphviz(dtc, out_file=f)
    f.close()