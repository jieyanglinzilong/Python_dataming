#创建列表
a = list("abc")
print(a)
#替换指定序列
a[1] = "5"
print(a)
#删除一个序列
del a[1]
print(a)
#追加
a.append("def")
print(a)
#链表的添加
a.extend(a)
print(a)
#链表的插入
a.insert(2,"kf")
print(a)
#删除指定序列的对象
a.pop(2)
print(a)
#链表的复制
s = a.copy()
print(s)
#链表的反转
s2 = a.reverse()
print(s2)
#链表排序
s3 = [2, 3, 4, 0]
s3.sort()
print(s3)