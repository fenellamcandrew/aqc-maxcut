import networkx as nx
from itertools import combinations, chain
import matplotlib.pyplot as plt
# This code calculates the Cheeger Constant using a brute force approach.
# It's an NP-Hard problem, so this is the best we can do (sad face).

def cheeger_num(V1,V2,G):
    dA = 0
    for v in V1:
        for u in V2:
            if G.has_edge(v,u):
                dA = dA + 1
    d1 = 0
    for i in V1:
        d1 = d1 + G.degree[i]
    d2 = 0
    for j in V2:
        d2 = d2 + G.degree[j]
    A = min(d1,d2)
    return dA/A

# Returns all combinations of splitting the list x into two sublists and returns
# it as a list of tuples.
def all_combinations(x):
    listt = []
    subsets = [v for a in range(len(x)) for v in combinations(x, a)]
    for i in range(int(len(subsets)/2 + 1)):
        new = list(chain(subsets[i])), [e for e in x if e not in subsets[i]]
        listt = listt + [new]
    return listt

def brute_CHEEGER(G):
    n = nx.number_of_nodes(G)
    # Creates all possible cut combinations
    combs = all_combinations(list(range(0,n)))
    # First loop through all the cuts and return the size of the cut
    cheegs = []
    for curr in combs:
        tup_list = list(curr)
        if (len(tup_list[0])==0) or (len(tup_list[1])==0):
            continue
        curr_cut = cheeger_num(tup_list[0],tup_list[1],G)
        cheegs = cheegs + [curr_cut]
    return min(cheegs)

# Example from paper 'The_first_two_largest_eigenvalues_of_Laplacian_spe.pdf'
'''
eg_edges = [(0,1),(0,2),(0,4),(1,2),(2,3),(3,4)]
G = nx.Graph(eg_edges)
print(brute_CHEEGER(G))
'''
