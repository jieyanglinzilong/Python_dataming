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
print(b.shape)
print(a.shape)
b = b.T
print(a)
print(b.shape)
c = nd.dot(a, b)

#c = nd.dot(a, b)
print(c)
#b = b.T
#b = nd.dot(a, b.T)
#print(a)