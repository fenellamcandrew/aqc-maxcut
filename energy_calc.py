import numpy as np
from energy_gap import *
from ground_entropy import *

# We only want to calculate the eigenvalues and eigenvectors once, so this Function
# calculates them and feeds them into our function energy_gap and ground_entr.
# we then return these values as a dictionary.
def energyCalcs(t, T, Hb, Hp):
    Hs = ham(t,T,Hb,Hp)
    eigs = np.linalg.eig(Hs)
    smallest_eigs = min_energies(eigs[0])
    ground_ent = ground_entr(eigs)
    vals = {
        "e_gap": smallest_eigs,
        "g_ent": ground_ent
    }
    return vals

def ham(t, T, Hb, Hp):
    return (1-t/T)*Hb + (t/T)*Hp
