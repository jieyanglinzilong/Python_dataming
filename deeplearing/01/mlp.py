import d2lzh as d2l
from mxnet import gluon, init
from mxnet.gluon import loss as gloss, nn
net = nn.Sequential()
net.add(nn.Dense(256, activation='relu'), nn.Dense(10))
net.initialize(init.Normal(sigma=0.01))
bath = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(bath)
loss = gloss.SoftmaxCrossEntropyLoss()
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.5})
num = 5
d2l.train_ch3(net, train_iter, test_iter, loss, num, bath, None, None, trainer)
