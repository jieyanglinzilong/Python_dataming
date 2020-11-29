#二元一次线性回归模型
from sklearn.linear_model import LinearRegression
from matplotlib import  pyplot as plt
import pandas as pd
filename = '../data/汇总.xls'
data = pd.read_excel(filename)
print(data.head(5))

#删除包含缺失值的行
data.dropna(inplace=True)
#缺失值填充
data.fillna(0)
x = data[['real']]
y = data[['价格']]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(x, y)
plt.xlabel('评分')
plt.ylabel('价格')
#在show前面调用，避免形成空图片
plt.savefig('评分与价格一元回归.jpg')
plt.show()
regr = LinearRegression()

regr.fit(x, y)

#系数  截距
print(str(regr.coef_[0]), str(regr.intercept_))