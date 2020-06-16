from pauli import *
import numpy as np

# Finds tensor product of some assortment of Is and 2 Zs, with Zs in positions
# i and j
# eg. i = 0, j = 2, n = 5 => zz(i,j,n) = ZIZII
def zz(i,j,n):
    prod = 1
    for k in range(0,n):
        if (k==i) or (k==j):
            prod = np.kron(prod,pZ())
        else:
            prod = np.kron(prod, np.identity(2))
    return prod

# Putting small bias on qubit i so we don't have a symmetric PDF at the end
# [DOESN'T WORK YET]
def bias(i,n):
    curr = 1
    for k in range(0,n):
        if (k==i):
            curr = np.kron(curr,pZ())
        else:
            curr = np.kron(curr,np.identity(2))
    return curr

# Creates Problem Hamiltonian give graph G
def prob_hamil(G,bias_num):
    Hp = []
    nV = G.number_of_nodes()
    I = np.identity(2**nV)
    for edge in G.edges():
        curr = zz(edge[0],edge[1],nV)
        curr = (I - curr)
        Hp = [curr] + Hp
    Hp = (1/2)*sum(Hp) + bias_num*bias(0,nV)
    return Hp
