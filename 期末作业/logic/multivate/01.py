#多元回归 分析获得客户评价对推荐人数的影响
import pandas as pd
import statsmodels.api  as sm
from sklearn.linear_model import LinearRegression
filename = "../../data/各项评分.xls"
data = pd.read_excel(filename)
print(data.describe())
x = data[['location', 'service', 'fac', 'health']]
y = data[['comment_recommend']]
regr = LinearRegression()
regr.fit(x, y)
print('各项系数'+str(regr.coef_))
print('常数项'+str(regr.intercept_))
x2 = sm.add_constant(x)
est = sm.OLS(y, x2).fit()
print(est.summary())