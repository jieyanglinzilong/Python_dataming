import d2lzh as d2l
from mxnet import autograd, gluon, init, nd
from mxnet.gluon import data as gdata,  loss as gloss, nn
import numpy as py
import pandas as pd
train_data = pd.read_csv('./data/kaggle_house_pred_train.csv')
test_data = pd.read_csv('./data/kaggle_house_pred_train.csv')
all_fea = pd.concat((train_data.iloc[:, 1:-1], test_data.iloc[:, 1:]))
num_fea = all_fea.dtypes[all_fea.dtypes!='object'].index
all_fea[num_fea]= all_fea[num_fea].apply(lambda x: (x - x.mean())/(x.std()))
all_fea =pd.get_dummies(all_fea, dummy_na=True)
n_train = train_data.shape[0]
train_fea = nd.array(all_fea[:n_train].values)
test_fea = nd.array(all_fea[:n_train].values)
train_labels = nd.array(train_data.SalePrice.values).reshape((-1 ,1 ))
loss = gloss.L2Loss()
def get_net():
    net = nn.Sequential()
    net.add(nn.Dense(1))
    net.initialize()
    return  net
def log_rmse(net, fea, labels):
    cli = nd.clip(net(fea), 1, float('inf'))
    rmse = nd.sqrt(2*loss(cli.log(),labels.log()).mean())
    return rmse.asscalar()
def train(net, train_fea, train_labels, test_fea, test_labels, num_epoch ,leaing_rate, weight, batch_size):
    train_ls, test_ls= [], []
    train_iter = gdata.DataLoader(gdata.ArrayDataset(train_fea, train_labels), batch_size, shuffle=True)
    trainer = gluon.Trainer(net.collect_params(),'adam', {'learing_rate':leaing_rate, 'wd':weight})
    for epoch in range(num_epoch):
        for x, y in train_iter:
            with autograd.record():
                l = loss(net(x), y)
            l.backward()
            trainer.step(batch_size)
        train_ls.append(log_rmse(net, train_fea, train_labels))
        if test_labels is not None:
           test_ls.append(log_rmse(net, train_fea, test_labels))
    return train_ls, test_ls
def get_k(k, i, x, y):
    assert k>1
    fold_size = x.shape[0]
    x_train, y_train =None ,None
    for j in range(k):
        idx = slice(j*fold_size,(j+1)*fold_size)
        x_part, y_part = x[idx,:], y[idx, :]

