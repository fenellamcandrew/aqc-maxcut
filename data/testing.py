import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.clique import graph_number_of_cliques
from networkx.algorithms.wiener import wiener_index
from scipy.sparse.linalg import eigs
from scipy.sparse.linalg import svds
import seaborn as sns

def randic(G):
    index = 0
    for edge in G.edges():
        deg_u = G.degree(edge[0])
        deg_v = G.degree(edge[1])
        index = index + (1/np.sqrt(deg_u*deg_v))
    return index

def product(listt):
    prod = 1
    for i in listt:
        if i < 1e-10:
            continue
        prod = i*prod
    return prod

def sum_inv(listt):
    summ = 0
    for i in listt[1:]:
        if i < 1e-10: # essential 0, get ridda it
            continue
        summ = summ + 1/i
    return summ
sns.set()

# Read dataset
df = pd.read_csv('d_runs.csv', index_col=0)
# Filtering data
df = df[df['metrics.max entanglement'].notnull()]
print('Number of experiments completed: ' + str(len(df['status'])))

df['max entanglement'] = df['metrics.max entanglement']
df['probability of success'] = df['metrics.prob success']

df = df[(df['params.T']==20) | (df['params.T']==30) | (df['params.T']==40) | (df['params.T']==50) | (df['params.T']==60)]
sns.relplot(x='max entanglement', y='probability of success', col='params.T', col_wrap=3, data=df)
sns.relplot(x='params.log laplacian eig ratio', y='max entanglement', col='params.T', col_wrap=3, data=df)
'''
Q_log_diff = []
lapl_log_ratio = []
N_L_diff = []
for i in range(len(df)):
    instance = df['params.instance index'][i]
    graph = df['params.graph type'][i]
    n = df['params.n_qubits'][i]
    file = str(n) + "_" + str(graph) + str(instance) + ".txt"
    file_path = "instances/" + str(graph) + "/n=" + str(n) + "/" + file
    f = open(file_path,"r")
    g = f.readline()    # this will be a string
    ge = eval(g)     # this will be the contents of the string; that is, the dictionary
    G = nx.node_link_graph(ge)  # this will turn the dictionary back into a graph

    L = nx.laplacian_matrix(G)
    Q = 2*A + L
    D = A + L
    Q = Q.asfptype()
    D = D.asfptype().toarray()

    Q_norm = (np.sqrt(np.linalg.inv(D)))*Q*(np.sqrt(D))
    eig_vals = sorted(eigs(Q_norm)[0],reverse=True)
    Q_diff = np.log(eig_vals[1]/eig_vals[2])
    Q_log_diff = Q_log_diff + [Q_diff]


df['Q_log_diff'] = Q_log_diff
df['small_N_L_diff'] = N_L_diff
sns.relplot(x='small_N_L_diff',y='metrics.prob success', col='params.T', data=df)
'''

min_l = 100
min_i = 0

max_l = 0
max_i = 0

min_c = 100
max_c = 0

largest = []

ratio = []
diff = []
trans = []
for i in range(len(df)):
    instance = df['params.instance index'][i]
    graph = df['params.graph type'][i]
    n = df['params.n_qubits'][i]
    m = df['params.n_edges'][i]
    file = str(n) + "_" + str(graph) + str(instance) + ".txt"
    file_path = "instances/" + str(graph) + "/n=" + str(n) + "/" + file
    f = open(file_path,"r")
    g = f.readline()    # this will be a string
    ge = eval(g)     # this will be the contents of the string; that is, the dictionary
    G = nx.node_link_graph(ge)  # this will turn the dictionary back into a graph
    L_norm_eigs = sorted(nx.normalized_laplacian_spectrum(G))
    largest = largest + [L_norm_eigs[-1]]
    ratio = ratio + [L_norm_eigs[-1]/L_norm_eigs[1]]
    diff = diff + [np.log(L_norm_eigs[-1]/L_norm_eigs[1])]

    trans = trans + [nx.transitivity(G)/m]

    lapl = df.iloc[i]['params.log laplacian eig ratio']
    cheeg = df.iloc[i]['params.cheeger constant']
    if lapl < min_l:
        min_l = lapl
        min_i = i
        min_c = cheeg
    if lapl > max_l:
        max_l = lapl
        max_i = i
        max_c = cheeg

print('max: '+ str(max_i) + ' ' + str(max_l) + ' ' + str(max_c))
print('min: '+ str(min_i) + ' ' + str(min_l) + ' ' + str(min_c))
path1 = 'instances/unique_soln/n=9/9_unique_soln277.txt'
path2 = 'instances/unique_soln/n=9/9_unique_soln2.txt'
f = open(path1,"r")
g = f.readline()    # this will be a string
ge = eval(g)     # this will be the contents of the string; that is, the dictionary
G1 = nx.node_link_graph(ge)  # this will turn the dictionary back into a graph
f = open(path2,"r")
g = f.readline()    # this will be a string
ge = eval(g)     # this will be the contents of the string; that is, the dictionary
G2 = nx.node_link_graph(ge)  # this will turn the dictionary back into a graph

plt.figure()
pos1 = nx.circular_layout(G1)
#pos1 = {0: np.array([1.00000000e+00, 1.98682148e-08]), 1: np.array([0.76604444, 0.64278759]), 2: np.array([0.17364823, 0.98480774]), 7: np.array([-0.50000005,  0.8660254 ]), 3: np.array([-0.9396926 ,  0.34202023]), 4: np.array([-0.9396926 , -0.34202013]), 5: np.array([-0.4999999 , -0.86602542]), 6: np.array([ 0.17364816, -0.9848077 ]), 8: np.array([ 0.76604432, -0.64278773])}
plt.title('max')
nx.draw(G1, pos1, with_labels=True)

plt.figure()
pos2 = nx.circular_layout(G2)
plt.title('min')
nx.draw(G2, pos2, with_labels=True)

df['largest'] = largest
df['ratio'] = ratio
df['diff'] = diff
df['trans'] = trans
sns.relplot(x='trans', y='metrics.prob success', col='params.T', col_wrap=3, data=df)

plt.show()
