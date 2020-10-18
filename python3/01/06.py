import random
from IPython import display

from matplotlib import pyplot as plt
from mxnet import autograd, nd

def data_iter(batch_size, features, labels):
    """Iterate through a data set."""
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        j = nd.array(indices[i: min(i + batch_size, num_examples)])
        yield features.take(j), labels.take(j)
