import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random as rn

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

# Creating sparse graphs of n nodes
'''
n = 10
count = 0
sparse_graphs = []
while count < 20:
    m = rn.randint(n-1,(n*(n-1)/2))
    if density(n,m) < 0.5:
        G = nx.gnm_random_graph(n,m) # <- Erdos-Renyi
        if nx.is_connected(G) and not(G in sparse_graphs):
            sparse_graphs = sparse_graphs + [G]
            count = count + 1

path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/Sparse/n=10/"
count = 1
for G in sparse_graphs:
    name = "10_Sparse" + str(count) + ".txt"
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
'''
# Creating Dense graphs for n nodes
'''
n = 10
count = 0
dense_graphs = []
while count < 20:
    m = rn.randint(n-1,(n*(n-1)/2))
    if density(n,m) > 0.5:
        G = nx.gnm_random_graph(n,m) # <- Erdos-Renyi
        if nx.is_connected(G) and not(G in dense_graphs):
            dense_graphs = dense_graphs + [G]
            count = count + 1

path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/Dense/n=10/"
count = 1
for G in dense_graphs:
    name = "10_Dense" + str(count) + ".txt"
    f = open(path + name,"w+")
    print(nx.node_link_data(G),file=f)
    f.flush()
    f.close()
    count = count + 1
'''

# Creating single n=4 instance

n = 6
G = nx.gnm_random_graph(n,10)
while not(nx.is_connected(G)):
    G = nx.gnam_random_graph(n,10)

path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/Dense/n=6/"
name = "6_Dense1.txt"
f = open(path + name,"w+")
print(nx.node_link_data(G),file=f)
f.flush()
f.close()
