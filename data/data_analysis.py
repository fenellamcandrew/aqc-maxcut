import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from brute_cheeger import *
from scipy.optimize import curve_fit
import statistics as st
import scipy

sns.set()

# Read dataset
df_else = pd.read_csv("d_runs.csv", index_col=0)
df_ws = pd.read_csv("d_runs_ws.csv", index_col=0)
df_ncb = pd.read_csv("d_runs_ncb.csv", index_col=0)
df = pd.concat([df_else, df_ws, df_ncb],sort=True)
################################################################################
# Filtering data
df = df[df['metrics.max entanglement'].notnull()]
df = df[(df['params.T']==20) | (df['params.T']==30) | (df['params.T']==40) | (df['params.T']==50) | (df['params.T']==60)]
df = df[df['params.number of solutions']==1]
print('Number of experiments completed: ' + str(len(df['status'])))

st_dev = []
geom_mean = []
harm_mean = []
ratio_min_min = []
ratio_max_min = []
skewness = []
kurt = []
large_eig = []
second_large_eig = []
curr = []
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

    n = nx.number_of_nodes(G)
    m = nx.number_of_edges(G)

    lapl = sorted(nx.normalized_laplacian_spectrum(G),reverse=True)
    lapl_small_to_big = sorted(nx.normalized_laplacian_spectrum(G))
    degrees = [val for (node, val) in G.degree()]

    st_dev = st_dev + [st.stdev(degrees)]
    geom_mean = geom_mean + [st.geometric_mean(degrees)]
    harm_mean = harm_mean + [st.harmonic_mean(degrees)]
    skewness = skewness + [scipy.stats.skew(degrees)]
    kurt = kurt + [scipy.stats.kurtosis(degrees)]
    ratio_max_min = ratio_max_min + [max(degrees)/min(degrees)]

    ratio_min_min = ratio_min_min + [lapl_small_to_big[2]/lapl_small_to_big[1]]
    large_eig = large_eig + [np.log(lapl[0])]
    second_large_eig = second_large_eig + [np.log(lapl[1])]
    curr = curr + [np.log(lapl[3])]

df['params.node_deg_stdev'] = st_dev
df['params.node_deg_geom_mean'] = geom_mean
df['params.node_deg_harm_mean'] = harm_mean
df['params.ratio_max_min_node_deg'] = ratio_max_min
df['params.node_deg_skewness'] = skewness
df['params.node_deg_kurtosis'] = kurt
df['params.log_ratio_min_Laplacian_eig'] = ratio_min_min
df['params.log_largest_eig_laplacian'] = large_eig
df['params.log_second_largest_eig_laplacian'] = second_large_eig
sns.relplot(x='params.log_ratio_min_Laplacian_eig',y='metrics.prob success',hue='params.graph type', col='params.T',data=df)
df.to_csv('data_updated.csv',index=False)
plt.show()
