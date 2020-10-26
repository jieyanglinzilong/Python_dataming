from mxnet import init
from mxnet.gluon import nn
from mxnet import autograd, nd
from mxnet.gluon import  data as gdata
from mxnet import gluon
from mxnet.gluon import  loss as gloss
import numpy as np
num = 2
num_example = 1000
true_w = [2, -3.4]
true_b = 4.2
fea = nd.random.normal(scale=1, shape=(num_example, num))
labes = true_w[0] * fea[:, 0] + true_w[1] * fea[:, 1] + true_b
labes += nd.random.normal(scale=0.01, shape=labes.shape)
batch = 10
dataset = gdata.ArrayDataset(fea,labes)
data_iter = gdata.DataLoader(dataset=dataset, batch_size=batch, shuffle=True)
for x, y in data_iter:
    print(x, y)
    break
net = nn.Sequential()
net.add(nn.Dense(1))
net.initialize(init.Normal(sigma=0.01))
loss = gloss.L2Loss()
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.03})
num_epoch = 3
for epoch in range(1, num_epoch+1):
    for x, y in data_iter:
        with autograd.record():
            l = loss(net(x), y)
        l.backward()
        trainer.step(batch)
    l = loss(net(fea), labes)
    print(epoch+1, l.mean().asnumpy())
dense =net[0]
print(dense.weight.data())


