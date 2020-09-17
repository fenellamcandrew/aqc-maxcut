import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from brute_cheeger import *
from scipy.optimize import curve_fit

def test_func(x, a, b, c):
    return a * np.exp(b * x) + c

sns.set()

# Read dataset
df = pd.read_csv("d_runs.csv", index_col=False)
################################################################################
# Filtering data
df = df[df['metrics.max entanglement'].notnull()]
print('Number of experiments completed: ' + str(len(df['status'])))

T_list = []
lapl_list = []
for i in range(1,401):
    df_curr = df[df['params.instance index'] == i]
    if (len(df_curr) != 12):
        continue
    smallest_T_needed = 100
    for j in range(10,70,5):
        df_T = df_curr[df_curr['params.T'] == j]
        #print(df_T.iloc[0]['metrics.prob success'])
        if df_T.iloc[0]['metrics.prob success'] > 0.8:
            smallest_T_needed = j
            break
    if smallest_T_needed == 100:
        continue
    lapl_list = lapl_list + len(df_curr)*[df_T.iloc[0]['params.log laplacian eig ratio']]
    T_list = T_list + len(df_curr)*[smallest_T_needed]
plt.figure()
plt.plot(lapl_list,T_list,'o')
plt.xlabel('log laplacian eig ratio')
plt.ylabel('minimum time needed')
plt.title('Psuccess = 0.8, n = 9')

lapl_list = np.array(lapl_list)
T_list = np.array(T_list)

idx = lapl_list.argsort()[::-1]
lapl_list = lapl_list[idx]
T_list = T_list[idx]

params, pcov = curve_fit(test_func, lapl_list, T_list)
print(params)

plt.figure(figsize=(6, 4))
plt.scatter(lapl_list, T_list, label='Data')
plt.plot(lapl_list, test_func(lapl_list, *params),
         label='Fitted function')
plt.legend(loc='best')

T_list = []
lapl_list = []
for i in range(1,401):
    df_curr = df[df['params.instance index'] == i]
    if (len(df_curr) != 12):
        continue
    smallest_T_needed = 100
    for j in range(10,70,5):
        df_T = df_curr[df_curr['params.T'] == j]
        #print(df_T.iloc[0]['metrics.prob success'])
        if df_T.iloc[0]['metrics.prob success'] > 0.9:
            smallest_T_needed = j
            break
    if smallest_T_needed == 100:
        continue
    lapl_list = lapl_list + len(df_curr)*[df_T.iloc[0]['params.log laplacian eig ratio']]
    T_list = T_list + len(df_curr)*[smallest_T_needed]
plt.figure()
plt.plot(lapl_list,T_list,'o')
plt.xlabel('log laplacian eig ratio')
plt.ylabel('minimum time needed')
plt.title('Psuccess = 0.9, n = 9')

lapl_list = np.array(lapl_list)
T_list = np.array(T_list)

idx = lapl_list.argsort()[::-1]
lapl_list = lapl_list[idx]
T_list = T_list[idx]

params, pcov = curve_fit(test_func, lapl_list, T_list)
print(params)

plt.figure(figsize=(6, 4))
plt.scatter(lapl_list, T_list, label='Data')
plt.plot(lapl_list, test_func(lapl_list, *params),
         label='Fitted function')
plt.legend(loc='best')

'''
cheegs = []
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

    cheegs = cheegs + [np.log(brute_CHEEGER(G))]

    n = nx.number_of_nodes(G)
    m = nx.number_of_edges(G)
    degrees = [val for (node, val) in G.degree()]

    if (min(degrees)==2) and (max(degrees)==2) and (nx.density(G)==1):
        print(abs(max_lapl-max_2_lapl)/2 < np.log(brute_CHEEGER(G)))
    else:
        print(abs(max_lapl-max_2_lapl)/2 >= np.log(brute_CHEEGER(G)))

df['cheeger_const'] = cheegs
sns.relplot(x='cheeger_const',y='metrics.prob success',col='params.T',data=df)
'''
plt.show()
