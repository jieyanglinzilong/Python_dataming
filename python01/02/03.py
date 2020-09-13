s1 = "abcdfg"
#计算长度
len(s1)
print(len(s1))
print(max(s1))
#切片取第四位开始
print(s1[3:])
#设置字符串编码
s2 = 'abdfrfr'
b1 = s2.encode(encoding='cp936')
print(s2)
print(b1.decode(encoding='cp936'))