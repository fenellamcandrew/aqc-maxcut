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

# Creates Problem Hamiltonian give graph G
def prob_hamil(G):
    Hp = []
    nV = G.number_of_nodes()
    I = np.identity(2**nV)
    for edge in G.edges():
        curr = zz(edge[0],edge[1],nV)
        curr = (I - curr)
        Hp = [curr] + Hp
    Hp = (1/2)*sum(Hp)
    return Hp
