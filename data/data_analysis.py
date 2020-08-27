import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from brute_cheeger import *

sns.set()

# Read dataset
df = pd.read_csv("d_runs.csv", index_col=0)
################################################################################
# Filtering data
df = df[df['metrics.max entanglement'].notnull()]
print('Number of experiments completed: ' + str(len(df['status'])))

sns.relplot(x='params.log laplacian eig ratio',y='metrics.prob success',col='params.T',data=df)
lapl_diff = []
cheegs = []
lap = []
energy = []
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

    laplacian = nx.normalized_laplacian_matrix(G)
    lapl = nx.normalized_laplacian_spectrum(G)
    energy = energy + [sum(lapl**2)]
    max_2_lapl = (sorted(lapl,reverse=True))[1]
    max_lapl = (sorted(lapl,reverse=True))[0]
    min_lapl = (sorted(lapl))[0]
    lapl_diff = lapl_diff + [abs(max_lapl-max_2_lapl)]
    lap = lap + [abs(min_lapl-max_lapl)]
    cheegs = cheegs + [np.log(brute_CHEEGER(G))]
    '''
    n = nx.number_of_nodes(G)
    m = nx.number_of_edges(G)
    degrees = [val for (node, val) in G.degree()]

    if (min(degrees)==2) and (max(degrees)==2) and (nx.density(G)==1):
        print(abs(max_lapl-max_2_lapl)/2 < np.log(brute_CHEEGER(G)))
    else:
        print(abs(max_lapl-max_2_lapl)/2 >= np.log(brute_CHEEGER(G)))
    '''

df['lapl_diff'] = lapl_diff
df['cheeger_const'] = cheegs
df['lap'] = lap
df['energy'] = energy
sns.relplot(x='energy',y='metrics.prob success',col='params.T',data=df)

plt.show()
