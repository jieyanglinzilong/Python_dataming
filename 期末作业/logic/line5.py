#二元一次线性回归模型
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import  pyplot as plt
import pandas as pd
import statsmodels.api as sm
filename = '../data/汇总.xls'
data = pd.read_excel(filename)
print(data.head(5))

#删除包含缺失值的行
data.dropna(inplace=True)
#缺失值填充
data.fillna(0)
x = data[['count']]
y = data[['real']]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(x, y)
plt.xlabel('评论数')
plt.ylabel('评分')
#在show前面调用，避免形成空图片
plt.savefig('评分与点评数二元回归.jpg')
plt.show()
regr = PolynomialFeatures(degree=2)

x_= regr.fit_transform(x)
reg = LinearRegression()
reg.fit(x_, y)
#系数  截距
#print(str(regr.coef_[0]), str(regr.intercept_))
x2 = sm.add_constant(x)
est = sm.OLS(y, x2).fit()
print(est.summary())
#print(reg.coef)