from mxnet import nd
import numpy as np
"""""
#广播机制
a = nd.arange(12).reshape((12, 1))
b = nd.arange(6).reshape((1, 6))
c = a+b
print(c)
"""
#索引机制 与numpy无差别
a = nd.arange(24).reshape(4, 6)
print(a)
print(a[0:2, :])
b = nd.arange(24).reshape(4,6)
#增加了内存开销
before = id(b)
b = b + a
print(id(b) == before)
#减少内存开销1
before = id(b)
b += a
print(id(b) == before)
#减少内存开销2
before = id(b)
b = nd.elemwise_add(a, b, out=b)
print(id(b) == before)
#numpy和ndarry的互换
p = np.ones((2, 3))
d = nd.array(p)
print(d)
e = d.asnumpy()
print(e)