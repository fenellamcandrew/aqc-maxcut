import numpy as np
import random as rn
import networkx as nx
import matplotlib.pyplot as plt

# P-Complete Approximation Problems, Sahni & Gonzales 1976

# For the time being will stay true to their naming conventions, may change
# later on

# (Step 2)
def Step2(G, SET, WT, j):
    for edge in G.edges(j):
        m = edge[1]
        if SET[m] != 0:
            WT[SET[m]-1] = WT[SET[m]-1] + 1
    return WT

# (Step 3)
def Step3(WT, dj):
    upper = min(dj+1,2)
    domain = list(range(0, upper))
    mini = WT[0]
    mindex = 0
    for i in domain:
        if WT[i] < mini:
            mini = WT[i]
            mindex = i
    return mindex

# (Step 4)
def Step4(SET,j,i):
    SET[j] = i

# (Step 5)
def Step5(G, SET, WT, SOL, j, i):
    for edge in G.edges(j):
        m = edge[1]
        if SET[m] == 0:
            continue
        if SET[m] != i+1:
            SOL = SOL + 1
        WT[SET[m]-1] = 0
    return WT, SOL

# (Step 6) Starting with the stuff from Step 1

# Generate random instance of the problem
n = rn.randint(10,12)
m = rn.randint(n,2*n)
G = nx.gnm_random_graph(n,m)

# Initial Values (Step 1)
WT = [0,0]
#SET = np.concatenate((np.array(range(1,3)), np.zeros(n-2)))
SET = [1,2] + ((n-2)*[0])
SOL = G.number_of_edges()
edgelist = list(G.edges())
SOL = edgelist.count((0,1))
j = 2

while j < n:
    WT = Step2(G, SET, WT, j)
    dj = G.degree(j)
    i = Step3(WT,dj)
    SET[j] = i+1
    WT, SOL = Step5(G, SET, WT, SOL, j, i)
    j = j + 1

set1 = [i for i in range(0,len(SET)) if SET[i]==1]
set2 = [i for i in range(0,len(SET)) if SET[i]==2]

print("Sets are:", set1, set2)
print("Value of the cut is:", SOL)
nx.draw(G, with_labels=True)
plt.show()
