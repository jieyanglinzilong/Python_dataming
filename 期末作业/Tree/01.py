import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
filename = "../data/各项评分.xls"
data = pd.read_excel(filename)
#推荐率小于92%视为不合格的酒店
data.loc[data.comment_recommend < 0.92, 'comment_recommend'] = 0
data.loc[data.comment_recommend >= 0.92, 'comment_recommend'] = 1
x = data.drop(columns='comment_recommend')
y = data['comment_recommend']
x_train, x_test,y_train, y_test= train_test_split(x, y, test_size=0.2, random_state=1)
model = DecisionTreeClassifier(max_depth=4, random_state=1)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
print(a)
#准确度
score = accuracy_score(y_pred, y_test)
print(score)
#预测推荐和不推荐
y_pred_proba = model.predict_proba(x_test)
b = pd.DataFrame(y_pred_proba, columns=['不推荐', '推荐'])
print(b)
#模型评估
fpr, tpr, thres = roc_curve(y_test, y_pred_proba[:, 1])
a = pd.DataFrame()
a['阈值'] = list(thres)
a['假报警'] = list(fpr)
a['命中率'] = list(tpr)
print(a)
#获取特征重要性
fea  = x.columns
importances = model.feature_importances_
#以二维表格显示
importances_df = pd.DataFrame()
importances_df['特征名称'] = fea
importances_df['特征重要性'] = importances
importances_df.sort_values('特征重要性', ascending=False)
print(importances_df)
