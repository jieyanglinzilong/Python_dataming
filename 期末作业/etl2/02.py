import pandas as pd
filename = '../data/汇总.xls'
data = pd.read_excel(filename)
print(data)