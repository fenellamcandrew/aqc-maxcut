import numpy as np
import networkx as nx
import random as rn
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from schrodinger import *
from pauli import *
from entanglement import *
from energy_gap import *

# Creates random graph give n vertices and m edges
def graph(n,m):
    G = nx.gnm_random_graph(n,m)
    return G

# Function that truncates number to certain number of decimal points
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def squareElems(array):
    newArray = []
    array = array.tolist()
    for i in array:
        newArray = newArray + [i[0]**2]
    return np.array(newArray)

def magnitudes(array): # Should be correct
    sum = 0
    newArray = []
    for i in range(0,len(array)):
        sum = sum + abs((array[i].real)**2 + (array[i].imag)**2)
        newArray = newArray + [np.sqrt(abs((array[i].real)**2 + (array[i].imag)**2))]
    return newArray/np.sqrt(sum)

# Creating random graph
n = rn.randint(3,5)
m = rn.randint(n-1,((n*(n-1))/2)-1)
G = graph(n,m)
while not (nx.is_connected(G)):
    G = graph(n,m)
n = 6
m = 1
G = graph(n,m)
G = nx.complete_graph(n)

# Creating initial state, which is just equal superposition over all
# possible states
state_curr = 1
for i in range(0,n):
    state_curr = np.kron(state_curr, minus())

t_step = 0.1 # Time step
T = 1000 # Total time
t = 0 # Starting time

# Initial and Problem Hamiltonians based off our generated graph
ent = []
energy = []
Hb = init_hamil(G)
Hp = prob_hamil(G)

#states = []
#state1 = magnitudes(state_curr)
#states = states + [state1]

while t <= T: # Terminate when t/T = 1
    energy = energy + [energy_calc(t, T, Hb, Hp)]
    state_curr = schrodinger_solver(state_curr, t_step, t, T, Hb, Hp)
    #state_curr1 = magnitudes(state_curr)
    #states = states + [state_curr1]
    ent = ent + [entanglementCalc(n,state_curr)]
    t = t + t_step

state_curr = magnitudes(state_curr)

# For the time being, have truncated the values to avoiding rounding errors

for i in range(0,len(state_curr)):
    state_curr[i] = truncate(state_curr[i], 10)

fig, ax = plt.subplots()

plt.figure(1)
# Finding the max values in PDF, so we don't have to label every value
# Will only label xaxis of the highest peaks (makes it neater)
x = np.arange(0,2**n,1)
length = len(str(format(x[-1],'b'))) # Length of final binary value
bin = []
for i in x:
    bin = bin + [format(i,'b').zfill(length)] # Converting all values to binary values

m = max(state_curr) # Max peak
maxes = [i for i, j in enumerate(state_curr) if j == m] # Finding all maxes
slice = list(np.array(bin)[maxes]) # Returning index of maxvalues

prob_state = squareElems(state_curr)

# Plotting PDF for final states, graph relating to the problem
#plt.bar(x,state_curr.transpose().tolist()[0])
plt.bar(x,prob_state.transpose().tolist())
plt.xticks(maxes, slice, rotation=90)
plt.title("PDF for final states")

# Plotting graph of entanglement
plt.figure(figsize = (10,7))
plt.subplot(2,2,1)
#plt.plot(np.arange(0, T+t_step, t_step).tolist(), ent)
plt.plot(np.arange(0, T, t_step).tolist(), ent)
plt.title('Entanglement')

# Plotting energy graph of eigenvalues
plt.subplot(2,2,2)
#plt.plot(np.arange(0,1+(t_step/T),t_step/T).tolist(), energy, 'b')
plt.plot(np.arange(0,1,t_step/T).tolist(), energy, 'b')
plt.title('Energy')
plt.ylabel('Eigenvalues')

# Plotting picture of graph
plt.subplot(2,2,(3,4))
nx.draw(G,with_labels=True)

plt.show()
