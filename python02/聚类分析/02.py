import pandas as pd
from sklearn.cluster import KMeans
inputfile='D:\PythonProject\python02\聚类分析\data\一模成绩分析.xlsx'
data = pd.read_excel(inputfile, index_col='排名')
k = 10
time = 1000
data_zs = 1.0*(data-data.mean())/data.std()
model = KMeans(n_clusters=k, n_jobs=4,max_iter=4)
model.fit(data_zs)
r1 = pd.Series(model.labels_).value_counts()
r2 = pd.DataFrame(model.cluster_centers_)
r = pd.concat([r2, r1],axis=1)
r.columns = list(data.columns) + [u'类别'] #重命名表头
print(r)
r= r.loc[:,r.notnull().any(axis=0)]
def density_plot(data): #自定义作图函数
  import matplotlib.pyplot as plt
  plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
  plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
  p = data.plot(kind='kde', linewidth = 2, subplots = True, sharex = False)
  [p[i].set_ylabel(u'密度') for i in range(k)]
  plt.legend()
  return plt

pic_output = 'D:\PythonProject\python02\聚类分析\data\pl' #概率密度图文件名前缀
for i in range(k):
  density_plot(data[r[u'类别']==i]).savefig(u'%s%s.png' %(pic_output, i))



