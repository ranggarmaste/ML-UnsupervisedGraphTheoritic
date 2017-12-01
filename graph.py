import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from scipy.spatial.distance import euclidean, cdist
import math
from tqdm import tqdm

#%%

# Load the data
data = []
with open('dataset1') as rf:
    next(rf)
    for row in rf:
        data.append(tuple(float(x) for x in row.strip().split(' ')))

N = len(data)
data = np.array(data)

X = data[:, 0:6]
y = data[:, 6]

#%%

# Calculating hopkins statistic
m = 100
Xs = X[np.random.choice(N, m)]
Xr = np.random.random((100, 6))

dxs = np.sort(cdist(Xs, X, 'euclidean'), axis=1)[:, 1]
dxr = np.min(cdist(Xr, X, 'euclidean'), axis=1)

sdxs = np.sum(dxs)
sdxr = np.sum(dxr)

hopkins = sdxr / (sdxr + sdxs)
hopkins

#%%

# Load the mst
ixs = []
jxs = []
ws = []
with open('dataset2') as rf:
    next(rf)
    next(rf)
    for row in rf:
        i, j, w = row.strip().split(' ')
        ixs.append(int(i))
        jxs.append(int(j))
        ws.append(float(w))

largest_edges = [(ixs[i], jxs[i], ws[i]) for i in sorted(range(N-1), key=lambda i: ws[i], reverse=True)]

graph = coo_matrix((ws, (ixs, jxs)), shape=(N, N)).todok()

#%%

def entropy(nsel, selector):
    N = len(selector)
    ne = 0
    for s in range(nsel):
        p = np.sum(selector == s)/N
        ne += p * math.log2(p)
    return -ne

def mutual_information(nclus, cluster_labels, nclass, class_labels):
    mi = 0
    N = len(cluster_labels)
    for i in range(nclus):
        for j in range(nclass):
            intersect = np.sum((cluster_labels == i) * (class_labels == j))
            if intersect > 0:
                mi += (intersect/N) * math.log2(N * intersect / (np.sum(cluster_labels == i) * np.sum(class_labels == j)))

    return mi

#%%

def evaluate_graph_clusters(g):
    nc, labels = connected_components(g)

    purity = sum(max(np.sum((labels == l) * (y == c)) for c in range(2)) for l in range(nc))/N
    nc_no_outliers = np.sum(np.bincount(labels) > 1)
    nmi = mutual_information(nc, labels, 2, y) / ((entropy(nc, labels) + entropy(2, y)) / 2)

    return (nc, nc_no_outliers, purity, nmi)

#%%

base = 10

igraph = graph.copy()
results = []
cdis = []
for lei in tqdm(range(20000)):
    i, j, w = largest_edges[lei]

    del igraph[i, j]

    if (lei + 1) % (base**math.floor(math.log(lei + 1, base))) == 0:
        results.append(evaluate_graph_clusters(igraph))

for r in results:
    print(*r)

#%%

igraph = graph.copy()

for i, j, w in largest_edges:
    if w < 0.2: break
    del igraph[i, j]

r2 = evaluate_graph_clusters(igraph)
print(*r2)
