import pandas as pd
from sklearn.decomposition import  PCA
inputpath = 'D:/python/数据规约/data/principal_component.xls'
outputpath = 'D:/python/数据规约/data/pca.xls'
data = pd.read_excel(inputpath, header=None)
pca = PCA(3)
pca.fit(data)
print(pca.explained_variance_ratio_)
lowd = pca.transform(data)
pd.DataFrame(lowd).to_excel(outputpath)
print(lowd)