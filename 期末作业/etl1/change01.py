import pandas as pd
import xlrd
def strs(row):
 values = ""
 for i in range(len(row)):
  if i == len(row) - 1:
   values = values + str(row[i])
  else:
   values = values + str(row[i])
 return values
def change(filename):
 filename = '../data/'+filename
 sqlfile = open("pinup.txt", "a")
 data = xlrd.open_workbook(filename)
 table = data.sheets()[0]  # 表头
 nrows = table.nrows  # 行数
 ncols = table.ncols  # 列数
 colnames = table.row_values(1)
 print(ncols)
 print(colnames)
 for ronum in range(1, nrows):  # 控制显示第几行，即去除行标题之类的
   row = table.cell_value(rowx=ronum, colx=2)  # 只需要修改你要读取的列数-1
   row = str(row)
   values = strs(row)  # 调用函数，将行数据拼接成字符串
   sqlfile.writelines(values + "\n")
 sqlfile.close()
change("成都.xlsx")