import numpy as np
from itertools import permutations
from pauli import *
import math

# Funciton to calucate entanglement for current state
# utilizes the theory from Schmidt Decomposition
def entanglementCalc(n, state_curr):

    # Reshapes our current state to a matrix so we can computer singular
    # values
    if n%2 == 0: # if n is EVEN then matrix is dimension 2^(n/2) X 2^(n/2)
        m = int(2**(n/2))
        state_curr = state_curr.reshape(m, m)
    else: # if n is ODD then matrix is dimension 2^((n-1)/2) X 2^((n+1)/2)
        m1 = int(2**((n-1)/2))
        m2 = int(2**((n+1)/2))
        state_curr = state_curr.reshape(m1, m2)

    svd = np.linalg.svd(state_curr, full_matrices=True, compute_uv=True)

    # Computes shannon entropy
    shanEntr = 0
    for i in svd[1]:
        if i == 0:
            continue
        shanEntr = shanEntr + (i**2)*math.log((i**2),2.0)
    return -shanEntr
