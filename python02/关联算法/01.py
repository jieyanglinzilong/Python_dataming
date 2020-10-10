from __future__ import print_function
import pandas as pd
#导入自行编写的apriori函数
from 关联算法.apriori import find_rule

inputfile = 'D:\PythonProject\python02\关联算法\data\menu_orders.xls'
outputfile = 'D:\PythonProject\python02\关联算法\data\apriori_rules.xls' #结果文件
data = pd.read_excel(inputfile, header = None)

print(u'\n转换原始数据至0-1矩阵...')
ct = lambda x : pd.Series(1, index = x[pd.notnull(x)]) #转换0-1矩阵的过渡函数
b = map(ct, data.) #用map方式执行
data = pd.DataFrame(list(b)).fillna(0) #实现矩阵转换，空值用0填充
print(u'\n转换完毕。')
del b #删除中间变量b，节省内存

support = 0.2 #最小支持度
confidence = 0.5 #最小置信度
ms = '---' #连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

find_rule(data, support, confidence, ms).to_excel(outputfile) #保存结果