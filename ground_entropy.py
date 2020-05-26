import numpy as np
from entanglement import *
import math

# Calculates the entropy of the ground state, we call on our function
# entanglementCalc to do so.
def ground_entr(eigs):
    # Eigenvales
    eig_vals = eigs[0]
    # Matrix of eigenvectors where the rows are the eigenvectors
    eig_vecs = eigs[1]
    # Sort eigenvectors in terms of smallest eigenvalue to largest, and take the
    # eigenvector associated with the smallest eigenvalue
    eig_vals_sorted = np.sort(eig_vals)
    eig_vecs_sorted = eig_vecs[:, eig_vals.argsort()]
    # Number of qubits (as state is length 2^n)
    n = math.log(len(eig_vecs_sorted[0]),2.0)
    ground_ent = entanglementCalc(n, (eig_vecs_sorted[:,0]))
    return ground_ent
