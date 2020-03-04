from pauli import *

# Creates the initial Hamiltonian given graph G
def init_hamil(G):
    Hb = []
    for i in range(0, G.number_of_nodes()):
        curr = 1
        for j in range(0, G.number_of_nodes()):
            if j == i:
                curr = np.kron(curr,pX())
            else:
                curr = np.kron(curr,np.identity(2))
        Hb = Hb + [(np.identity(2**G.number_of_nodes())-curr)/2]
    Hb = sum(Hb)
    return Hb
