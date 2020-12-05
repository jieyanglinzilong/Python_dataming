import pandas as pd
import statsmodels.api  as sm
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
filename = "../../data/各项评分.xls"
data = pd.read_excel(filename)
print(data)
print(data.iloc[:, 4:5])
#推荐率小于92%视为不合格的酒店
data.loc[data.comment_recommend < 0.92, 'comment_recommend'] = 0
data.loc[data.comment_recommend >= 0.92, 'comment_recommend'] = 1
#提取特征变量
x = data.drop(columns='comment_recommend')
y = data['comment_recommend']
x_train, x_test,y_train, y_test= train_test_split(x, y, test_size=0.2, random_state=1 )
modle = LogisticRegression(random_state=1, max_iter=1000)
modle.fit(x_train, y_train)
y_pred = modle.predict(x_test)
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
print(a)
score = accuracy_score(y_pred, y_test)
print(score)
#print('各项系数'+modle.coef_)
#print('常数项'+modle.intercept_)
#使用roc评价模型准确度
y_predproba = modle.predict_proba(x_test)
print(y_predproba)
print(classification_report(y_test, y_pred))
fpr, tpr, thres = roc_curve(y_test, y_predproba[:, 1])
a1 = pd.DataFrame()
a1['阈值'] = list(thres)
a1['假报警率'] = list(fpr)
a1['命中率'] = list(tpr)
print(a1)
plt.plot(fpr, tpr)
plt.title('ROC')
plt.xlabel('FDR')
plt.ylabel('TPR')
plt.savefig('ROC.png')
plt.show()