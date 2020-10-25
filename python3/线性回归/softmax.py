import d2lzh as d2l
from mxnet import gluon, init
from mxnet.gluon import loss as gloss, nn
bathsize = 256
trainer_iter, test_iter = d2l.load_data_fashion_mnist(bathsize)
net = nn.Sequential()
net.add(nn.Dense(10))
net.initialize(init.Normal(sigma=0.01))
loss = gloss.SoftmaxCELoss()
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.05})
num = 5
d2l.train_ch3(net, trainer_iter, test_iter,loss, num, bathsize, None, None, trainer)
for x, y in test_iter:
    break
truelabes = d2l.get_fashion_mnist_labels(y.asnumpy())
falselabes = d2l.get_fashion_mnist_labels(net(x).argmax(axis =1 ).asnumpy())
title = [true+'\n'+ pred for true,pred in zip(truelabes,falselabes)]
d2l.show_fashion_mnist(x[0:9], title[0:9])