import os

from etl1.change01 import change
from etl1.jieba01 import create_word_cloud

i = 1
newlist = []
for filename in os.listdir('../data'):
    change(filename)
create_word_cloud("pinup")

#data

