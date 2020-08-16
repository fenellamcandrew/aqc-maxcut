import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.clique import graph_number_of_cliques
from networkx.algorithms.wiener import wiener_index
import seaborn as sns

sns.set()

# Read dataset
df = pd.read_csv('d_runs.csv', index_col=0)
# Filtering data
df = df[df['metrics.max entanglement'].notnull()]
print('Number of experiments completed: ' + str(len(df['status'])))

df = df[df['params.Graph type']=='unique_soln']

df = df[df['params.n_qubits']==9]
print('Number of experiments completed: ' + str(len(df['status'])))

ent = []
matching = []
lapl_ev = []
cliques = []
wiener = []

print('\nCalculating new data')
for i in range(len(df)):
    instance = df['params.instance index'][i]
    graph = df['params.Graph type'][i]
    n = df['params.n_qubits'][i]
    file = str(n) + "_" + str(graph) + str(instance) + ".txt"
    file_path = "instances/" + str(graph) + "/n=" + str(n) + "/" + file
    f = open(file_path,"r")
    g = f.readline()    # this will be a string
    ge = eval(g)     # this will be the contents of the string; that is, the dictionary
    G = nx.node_link_graph(ge)  # this will turn the dictionary back into a graph
    ent = ent + [df['metrics.max entanglement'][i]]

    max_lap = (sorted((nx.normalized_laplacian_spectrum(G)),reverse=True))[0]
    max_2_lapl = (sorted((nx.normalized_laplacian_spectrum(G)),reverse=True))[1]
    lapl_ev = lapl_ev + [np.log(max_lap/max_2_lapl)]

    cliques = cliques + [graph_number_of_cliques(G)]
    wiener = wiener + [wiener_index(G)]

print('\nAdding new data')
df['lapl_ev'] = lapl_ev
df['cliques'] = cliques
df['wiener'] = wiener
'''
print('\nPlotting')
n_clique_ent = sns.relplot(x='cliques',y='metrics.max entanglement', hue='params.n_qubits', col='params.T', data=df)
n_clique_psucc = sns.relplot(x='cliques',y='metrics.prob success', hue='params.n_qubits', col='params.T', data=df)
n_clique_ent.savefig('figs/graph_chars/n_clique_ent')
n_clique_psucc.savefig('figs/graph_chars/n_clique_psucc')

wiener_ind_ent = sns.relplot(x='wiener',y='metrics.max entanglement', hue='params.n_qubits', col='params.T', data=df)
wiener_ind_psucc = sns.relplot(x='wiener',y='metrics.prob success', hue='params.n_qubits', col='params.T', data=df)
wiener_ind_ent.savefig('figs/graph_chars/wiener_ind_ent.png')
wiener_ind_psucc.savefig('figs/graph_chars/wiener_ind_psucc.png')

df = df[df['lapl_ev'] > -6]
lapl_ev_ent = sns.relplot(x='lapl_ev',y='metrics.max entanglement', hue='params.n_qubits', col='params.T', data=df)
lapl_ev_psucc = sns.relplot(x='lapl_ev',y='metrics.prob success', hue='params.n_qubits', col='params.T', data=df)
lapl_ev_ent.savefig('figs/graph_chars/lapl_ev_ent')
lapl_ev_psucc.savefig('figs/graph_chars/lapl_ev_psucc')
'''

sns.relplot(x='metrics.max entanglement', y='metrics.prob success', col='params.T', hue='lapl_ev',data=df)
print(df)

plt.show()
