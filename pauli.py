import numpy as np
import math
import cmath

# Pauli X
def pX():
    return np.array([[0, 1],
                    [1, 0]])
# Pauli X operating on qubit i
def pXi(i,state):
    state[i] = np.dot(pX(),state[i])
    return state

# Pauli Y
def pY():
    return np.array([[0, complex(0,-1)],
                    [complex(0,1), 0]])
# Pauli Y operating on qubit i
def pYi(i,state):
    state[i] = np.dot(pY(),state[i])
    return state

# Pauli Z
def pZ():
    return np.array([[1, 0],
                    [0, -1]])
# Paulis Z operating on qubit i
def pZi(i,state):
    state[i] = np.dot(pZ(),state[i])
    return state
# Hadamard Matrix
def pH():
    return (1/np.sqrt(2))*np.array([[1, 1],
                                    [1, -1]])

# |0> State
def s0():
    return np.array([[1],[0]])
# |1> State
def s1():
    return np.array([[0],[1]])
# |+> State
def plus():
    return np.dot(pH(),s0())
# |-> State
def minus():
    return np.dot(pH(),s1())

def pT():
    return np.array([[1, 0],
                    [0, math.e**(complex(0,1)*math.pi/4)]])
