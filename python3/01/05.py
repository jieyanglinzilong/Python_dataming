import random

from IPython import display

from matplotlib import pyplot as plt
from mxnet import autograd, nd
num = 2
num_example = 1000
true_w = [2, -3.4]
true_b = 4.2
fea = nd.random.normal(scale=1, shape=(num_example, num))
labes = true_w[0] * fea[:, 0] + true_w[1] * fea[:, 1] + true_b
labes += nd.random.normal(scale=0.01, shape=labes.shape)
def use_svg():
    display.set_matplotlib_formats('svg')
def set_figsize( figsize=(3.5, 2.5)):
    use_svg()
    plt.rcParams['figure.figsize'] = figsize
set_figsize()
plt.scatter(fea[:, 1].asnumpy(), labes.asnumpy(), 1);
def data_iter(batch_size, features, labels):
    """Iterate through a data set."""
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        j = nd.array(indices[i: min(i + batch_size, num_examples)])
        yield features.take(j), labels.take(j)
bath = 3
for x, y in data_iter(bath, fea,labes):
    print(x, y)
    break
w = nd.random.normal(scale=0.01,shape=(2, 1))
b = nd.zeros(shape=(1, ))
w.attach_grad()
b.attach_grad()
def linreg(x, w, b):
    return nd.dot(x,w)+b
def squard_loss(y_hat, y):
    return (y_hat - y.reshape(y_hat.shape))**2/2
def sgd(params, lr, bath):
    for param in params:
        param[:] = param - lr*param.grad/bath
lr = 0.03
num_epoch = 3
net =linreg
loss =squard_loss
for epoch in range(num_epoch):
    for x,y in data_iter(bath, fea, labes):
        with autograd.record():
            l = loss(net(x, w, b), y)
        l.backward()
        sgd([w, b],lr, bath)
    train_l=loss(net(fea,w,b), labes)
    print(epoch+1, train_l.mean().asnumpy())
