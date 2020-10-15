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
plt.scatter(fea[:, 1].asnumpy(), labes.asnumpy(), 1)

