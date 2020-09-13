#序列数据的基本操做
from sympy import false

s1 = (1, 2, 3,4,5)
c = sum(s1)
#最小
print(min(s1))
#最大
print(max(s1))
#长度
print(len(s1))
#总结
print(sum(s1))
#序列查找
print(s1[1])
#切片操作
print(s1[1:3])
#连接操作
s2 = (7, 8, 9, 10)
s1 = s1 + s2
print(s1)
#复制操作
s1 = s1 * 2
print(s1)
#查看是否存在
print(1 in s1)
#排序
print(sorted(s1))
#查看是否存在
print(any(s1))
print(any([1, 2, 3]))
print(any([false]))
#序列的拆分
data = (1, '徐岚', (90, 80, 85))
id, name, score = data
print(score)
#使用临时变量
_, b, c= score
print(b)
#使用变量
a , *b, c = range(10)
print(b)
#元组创建
a = tuple([1, 2, 3])