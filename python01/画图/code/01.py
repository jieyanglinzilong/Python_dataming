import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = '../data/笔记本电脑.xlsx'

data = pd.read_excel(file)
x, y = data.shape
num = pd.DataFrame(np.arange(x*y).reshape(x, y))
num = data.iloc[2:, [1, 2]]
x = num.iloc[:, 0]
y= num.iloc[:,1]
print(data.describe())