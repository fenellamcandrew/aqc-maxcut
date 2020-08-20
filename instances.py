import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random as rn
from brute_maxcut import *

# n = 15,16,17,18,19,20 - 20 graphs for each
# 4 cases: sparse, dense, sparse weighted, dense weighted (weight in [1,9])
# density = 2E / (V (V-1) )

# IDEA
# Randomly choose a number of edges, use random graph generator, make sure graph
# is connected, not entirely needed but want it that way.
# Need each graph to be different, so need to distinguish.

# nx.is_isomorphic(G1,G2) (unweighted)
# nx.is_isomorphic(G1,G2,edge_match=em) (weighted)

def density(n,m):
    D = (2*m)/(n*(n-1))
    return D
'''
n = 12 # number of graph nodes

# Creating low density graphs of n nodes
#n = 7
count = 0
sparse_graphs = []
while count < 50:
    m = rn.randint(n-1,(n*(n-1)/2))
    if density(n,m) < 0.35:
        G = nx.gnm_random_graph(n,m) # <- Erdos-Renyi
        if nx.is_connected(G) and not(G in sparse_graphs):
            sparse_graphs = sparse_graphs + [G]
            count = count + 1

path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/low_density/n="+str(n)+"/"
count = 1
for G in sparse_graphs:
    name = str(n)+"_low_density" + str(count) + ".txt"
    f = open(path + name,"w+")
    print(nx.node_link_data(G),file=f)
    f.flush()
    f.close()
    count = count + 1

#print(sparse_graphs)
#for i in range(0,20):
#    plt.figure(i)
#    nx.draw(sparse_graphs[i],with_labels=True)
#plt.show()

# Creating medium density graphs for n nodes
#n = 7
count = 0
dense_graphs = []
while count < 50:
    m = rn.randint(n-1,(n*(n-1)/2))
    if (density(n,m) > 0.4) and (density(n,m) < 0.65):
        G = nx.gnm_random_graph(n,m) # <- Erdos-Renyi
        if nx.is_connected(G) and not(G in dense_graphs):
            dense_graphs = dense_graphs + [G]
            count = count + 1

path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/medium_density/n="+str(n)+"/"
count = 1
for G in dense_graphs:
    name = str(n)+"_medium_density" + str(count) + ".txt"
    f = open(path + name,"w+")
    print(nx.node_link_data(G),file=f)
    f.flush()
    f.close()
    count = count + 1

# Creating high density graphs for n nodes
#n = 7
count = 0
dense_graphs = []
while count < 50:
    m = rn.randint(n-1,(n*(n-1)/2))
    if density(n,m) > 0.7:
        G = nx.gnm_random_graph(n,m) # <- Erdos-Renyi
        if nx.is_connected(G) and not(G in dense_graphs):
            dense_graphs = dense_graphs + [G]
            count = count + 1

path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/high_density/n="+str(n)+"/"
count = 1
for G in dense_graphs:
    name = str(n)+"_high_density" + str(count) + ".txt"
    f = open(path + name,"w+")
    print(nx.node_link_data(G),file=f)
    f.flush()
    f.close()
    count = count + 1
'''
n = 8
count = 0
graphs = []
while count < 300:
    m = rn.randint(n-1,(n*(n-1)/2))
    G = nx.gnm_random_graph(n,m)
    solver = bruteMAX(G)
    solns = solver['cuts']
    if nx.is_connected(G) and (len(solns) == 2) and (G not in graphs):
        print(len(solns)/2, density(n,m))
        graphs = graphs + [G]
        count = count + 1

path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/unique_soln/n="+str(n)+"/"
count = 1
for G in graphs:
    name = str(n)+"_unique_soln" + str(count) + ".txt"
    f = open(path + name,"w+")
    print(nx.node_link_data(G),file=f)
    f.flush()
    f.close()
    count = count + 1
'''
path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/unique_soln_bias/n="+str(n)+"/"
count = 1
for G in graphs:
    name = str(n)+"_unique_soln_bias" + str(count) + ".txt"
    f = open(path + name,"w+")
    print(nx.node_link_data(G),file=f)
    f.flush()
    f.close()
    count = count + 1
'''
