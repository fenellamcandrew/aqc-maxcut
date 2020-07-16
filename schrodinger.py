import numpy as np
import cmath
from scipy.linalg import expm
from init_hamil import *
from prob_hamil import *

# Applies the hamiltonian at time t to our current state to return
# the newly formed state
def schrodinger_solver(state_curr, t_step, t, T, Hb, Hp):
    H1 = ham(Hb, Hp, t, T)
    H2 = ham(Hb, Hp, t+t_step, T)
    Hs = (H1+H2)/2
    thingy = expm(np.complex(0,-1)*Hs*t_step)
    state = np.dot(thingy,state_curr)
    return norm(state)

# Function to determine current Hamiltonian from adiabatic equation
def ham(Hb,Hp,t,T):
    return (1-t/T)*Hb + (t/T)*Hp

# Returns the norm of an array containing complex numbers INCORRECT
def normBAD(array):
    for i in range(0,len(array)):
        array[i] = abs(array[i].real + array[i].imag)
    return (array/sum(array)).real

def norm(array): # Should be correct
    sum = 0
    #newArray = []
    for i in range(0,len(array)):
        sum = sum + ((array[i].real)**2 + (array[i].imag)**2)
        #newArray = newArray + [np.sqrt(abs((array[i].real)**2 + (array[i].imag)**2))]
    return (array/(np.sqrt(sum)))
