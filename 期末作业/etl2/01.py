import os
import pandas as pd
newlist = []
for filename in os.listdir('../data'):
    filename = '../data/' + filename
    data = filename = pd.read_excel(filename, usecols=[4, 5, 6])
    newlist.append(data)
outputfile = '../data/汇总.xls'
df = pd.concat(newlist)
df.to_excel(outputfile, index=False)