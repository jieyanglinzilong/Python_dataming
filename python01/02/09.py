#重定向
import sys
filename1=input("输入文件名 ")
line_no = 0
with open(filename1, 'r', encoding='utf8') as f:
    f1 = open('out.txt','w')
    sys.stdout = f1
    sys.stdout = sys.__stdout__

