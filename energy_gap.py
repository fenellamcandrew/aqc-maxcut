import numpy as np

# Finds eigenvalues of Hs at current time
def energy_calc(t, T, Hb, Hp):
    Hs = ham(t, T, Hb, Hp)
    #svd = np.linalg.svd(Hs, full_matrices=True, compute_uv=True)
    #eigs = svd[1]
    #eigs = [i ** 2 for i in svd[1]]
    eigs = sorted(np.linalg.eig(Hs)[0])
    return eigs[:10]

def ham(t, T, Hb, Hp):
    return (1-t/T)*Hb + (t/T)*Hp
