import numpy as np

# Finds eigenvalues of Hs at current time
def min_energies(eig_vals):
    #svd = np.linalg.svd(Hs, full_matrices=True, compute_uv=True)
    #eigs = svd[1]
    #eigs = [i ** 2 for i in svd[1]]
    eigs = sorted(eig_vals)
    return eigs[:10]
