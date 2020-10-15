from mxnet import nd
x = nd.arange(12)
#print(x)
x = x.reshape(3,4)
#print(x)
y = nd.zeros((2,3,4))
#print(y)
z = nd.ones((2, 8, 9))
#print(z)
z *= 3
#print(z)
k = nd.normal(0, 1, shape=(2, 3, 4))
#print(k)
k = k + y
#print(k)
#k = k/y
#print(k.exp())
a = nd.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
#b = nd.array([1, 2, 3, 4], [ 5, 6, 7, 8], [9, 10, 11, 12])
#a = nd.dot(b, a.T)
b = nd.arange(12)
b = b.reshape((4, 3))
#print(b.shape)
#print(a.shape)
#print(b)
e = b.T
#print(b)
#print(b.shape)
#矩阵的转置乘法
c = nd.dot(a, e)

#c = nd.dot(a, b)
#print(c)
#b = b.T
#b = nd.dot(a, b.T)
#print(a)
print(a)
print(b)
#矩阵连接
d = nd.concat(a, b, dim=0)
print(d)
f = d.sum()
print(f)
#转为标量
g = f.norm().asscalar()
print(g)