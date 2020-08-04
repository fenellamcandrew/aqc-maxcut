import networkx as nx
from itertools import combinations, chain

# Returns size of the cut given vertices split into two distinct vertex sets
def cut_size(V1,V2,G):
    cut = 0
    for v in V1:
        for u in V2:
            if G.has_edge(v,u):
                cut = cut + 1
    return cut

# Returns all combinations of splitting the list x into two sublists and returns
# it as a list of tuples.
def all_combinations(x):
    listt = []
    subsets = [v for a in range(len(x)) for v in combinations(x, a)]
    for i in range(int(len(subsets)/2 + 1)):
        new = list(chain(subsets[i])), [e for e in x if e not in subsets[i]]
        listt = listt + [new]
    return listt

# Returns all of the cuts as binary values ('101' and '010' represent the same
# cut).
def bruteMAX(G):
    n = nx.number_of_nodes(G)
    # Creates all possible cut combinations
    combs = all_combinations(list(range(0,n)))
    # First loop through all the cuts and return the size of the cut
    cuts = []
    for curr in combs:
        tup_list = list(curr)
        curr_cut = cut_size(tup_list[0],tup_list[1],G)
        cuts = cuts + [curr_cut]
    # Determine size of maximum possible cute
    max_size = max(cuts)
    # Create list of all possible maxcuts
    max_cuts = []
    for i in range(0,len(cuts)):
        if cuts[i]==max_size:
            max_cuts = max_cuts + [combs[i]]
    # Represent answers as binary values
    bin_cuts = []
    for i in max_cuts:
        bin1 = ''
        bin2 = ''
        for j in range(0,n):
            if j in list(i)[0]:
                bin1 = bin1 + '0'
                bin2 = bin2 + '1'
            else:
                bin1 = bin1 + '1'
                bin2 = bin2 + '0'
        bin_cuts = bin_cuts + [bin1] + [bin2]
    vals = {
        "cut_size": max_size,
        "cuts": bin_cuts
    }
    return vals
