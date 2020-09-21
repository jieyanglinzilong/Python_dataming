import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
inputpath = 'D:/PythonProject/python02\逻辑回归/data/bankloan.xls'
data = pd.read_excel(inputpath)
x = data.iloc[:, :8].values
y = data.iloc[:, 8].values
lr = LR(solver='liblinear')
lr = lr.fit(x, y)
print('模型的平均准确度为：%s' % lr.score(x, y))