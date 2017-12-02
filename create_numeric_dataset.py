#%%

import pandas as pd
import numpy as np

#%%

from sklearn import preprocessing

names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
         'marital-status', 'occupation', 'relationship', 'race', 'sex', 
         'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'class']
data = pd.read_csv('CensusIncome/CencusIncome.test.txt', encoding='utf8', sep=', ', names=names, na_values='?')
data = data.fillna(data.mean())
data = data.fillna(data.mode().iloc[0, :])

#%%

X = data.iloc[:,0:14].values
categorical_indices = [1,2,3,5,6,7,8,9,13] 
numeric_indices = [x for x in list(range(14)) if x not in categorical_indices]
X = X[:, numeric_indices]

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)

#%%

y = data.iloc[:, 14].values
y = y != '<=50K.'
y = y.astype(int)

#%%

file = open('dataset_standard_numeric', 'w')
file.write('{}\n'.format(len(X)))
for i in range(len(X)):
    file.write(' '.join([str(x) for x in X[i,:]]))
    file.write(' {}'.format(y[i]))
    file.write('\n')
file.close()

#%%

# Optional
# from sklearn.manifold import TSNE

# tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
# tsne_results = tsne.fit_transform(X)

# from matplotlib import pyplot as plt
# plt.scatter(tsne_results[:, 0], tsne_results[:, 1], c=y)
# plt.show()