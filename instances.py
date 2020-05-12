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
'''
n = 14
count = 0
sparse_graphs = []
while count < 20:
    m = rn.randint(n-1,(n*(n-1)/2))
    if density(n,m) < 0.5:
        G = nx.gnm_random_graph(n,m) # <- Erdos-Renyi
        if nx.is_connected(G) and not(G in sparse_graphs):
            sparse_graphs = sparse_graphs + [G]
            count = count + 1

path = "/Users/fenella/Documents/Uni/Research/Code/Instances/Sparse/n=14/"
count = 1
for G in sparse_graphs:
    name = "14_Sparse" + str(count) + ".txt"
    f = open(path + name,"w+")
    print(nx.node_link_data(G),file=f)
    f.flush()
    f.close()
    count = count + 1
'''
#print(sparse_graphs)
#for i in range(0,20):
#    plt.figure(i)
#    nx.draw(sparse_graphs[i],with_labels=True)
#plt.show()
'''
n = 16
count = 0
dense_graphs = []
while count < 20:
    m = rn.randint(n-1,(n*(n-1)/2))
    if density(n,m) > 0.5:
        G = nx.gnm_random_graph(n,m) # <- Erdos-Renyi
        if nx.is_connected(G) and not(G in dense_graphs):
            dense_graphs = dense_graphs + [G]
            count = count + 1

path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/Dense/n=16/"
count = 1
for G in dense_graphs:
    name = "16_Dense" + str(count) + ".txt"
    f = open(path + name,"w+")
    print(nx.node_link_data(G),file=f)
    f.flush()
    f.close()
    count = count + 1
'''
n = 4
G = nx.gnm_random_graph(4,3)
while not(nx.is_connected(G)):
    G = nx.gnam_random_graph(4,3)

path = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/Sparse/n=4/"
name = "4_Sparse1.txt"
f = open(path + name,"w+")
print(nx.node_link_data(G),file=f)
f.flush()
f.close()
