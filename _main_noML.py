import numpy as np
import networkx as nx
import random as rn
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import yaml
import mlflow
import argparse
import os
# Written files
from schrodinger import *
from pauli import *
from energy_calc import *
from Sahni import *

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

# Creating tmp file to store figs
if os.path.exists('tmp'):
    if os.path.exists('tmp/fig1.png'):
        os.remove('tmp/fig1.png')
    if os.path.exists('tmp/fig2.png'):
        os.remove('tmp/fig2.png')
    if os.path.exists('tmp/fig3.png'):
        os.remove('tmp/fig3.png')
    os.rmdir('tmp')
os.mkdir('tmp')

# PARSING ARGS IN TERMINAL
parser = argparse.ArgumentParser()
# Adding command line argument
parser.add_argument('--run_path', type=str)
# Parse your arguments
args = parser.parse_args()
# Extract into variable
run_path = args.run_path

print("Reading yaml file\n")
with open(run_path) as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)

params = doc["initialise"]["params"]
n_qubits = params["n_qubits"]
graph_type = params["graph_type"]
t_step = params["t_step"]
T = params["time_T"]
instance_index = params["instance_index"]

file_path = "instances/{graph_type}/n={n_qubits}/{n_qubits}_{graph_type}{instance_index}.txt".format(
    graph_type = graph_type,
    n_qubits = n_qubits,
    instance_index = instance_index
)
t_step = float(t_step)
T = int(T)

# READ GRAPH FROM FILE
f = open(file_path,"r")
g = f.readline()    # this will be a string
ge = eval(g)     # this will be the contents of the string; that is, the dictionary
G = nx.node_link_graph(ge)  # this will turn the dictionary back into a graph
n = G.number_of_nodes()
m = G.number_of_edges()

# MLFLOW:
# Creating initial state, which is just equal superposition over all
# possible states

state_curr = 1
for i in range(0,n):
    state_curr = np.kron(state_curr, minus())
t = 0 # start time
# Initial and Problem Hamiltonians based off our generated graph
ent = []
energy = []
min_gap = []
ground_ent = []
Hb = init_hamil(G)
Hp = prob_hamil(G)
T = 25

#states = []
#state1 = magnitudes(state_curr)
#states = states + [state1]
print("Starting evolution\n")
while t <= T: # Terminate when t/T = 1
    energies = energyCalcs(t,T,Hb,Hp)
    energy = energy + [energies["e_gap"]]
    ground_ent = ground_ent + [energies["g_ent"]]
    min_gap = min_gap + [abs((energies["e_gap"])[0]-(energies["e_gap"])[1])]

    # Finding stat_curr for current time step
    state_curr = schrodinger_solver(state_curr, t_step, t, T, Hb, Hp)
    #state_curr1 = magnitudes(state_curr)
    #states = states + [state_curr1]
    ent = ent + [entanglementCalc(n,state_curr)]
    t = t + t_step

state_curr = magnitudes(state_curr)

print("Creating figures\n")
# For the time being, have truncated the values to avoiding rounding errors
for i in range(0,len(state_curr)):
    state_curr[i] = truncate(state_curr[i], 10)

fig, ax = plt.subplots()

fig1 = plt.figure(1)
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
fig2 = plt.figure(figsize = (10,7))
plt.subplot(2,2,1)
x_axis1 = []
num1 = 0
for i in range(0,len(ent)):
    x_axis1 = x_axis1 + [num1]
    num1 = num1 + t_step
    #plt.plot(np.arange(0, T, t_step).tolist(), ent)
    #plt.plot(np.arange(0, T+t_step, t_step).tolist(), ent)
plt.plot(x_axis1, ent)
plt.title('Entanglement')

# Plotting picture of graph
plt.subplot(2,2,(3,4))
if nx.check_planarity(G):
    pos = nx.planar_layout(G)
nx.draw(G,with_labels=True)
#nx.draw(G,with_labels=True)

# Plotting energy graph of eigenvalues
plt.subplot(2,2,2)
x_axis2 = []
num2 = 0
for j in range(0,len(energy)):
    x_axis2 = x_axis2 + [num2]
    num2 = num2 + t_step
    #plt.plot(np.arange(0, T, t_step).tolist(), energy, 'b')
    #plt.plot(np.arange(0, T+t_step, t_step).tolist(), energy, 'b')
plt.plot(x_axis2, energy, 'b')
plt.title('Energy')
plt.ylabel('Eigenvalues')

# Plotting graph of ground state entropy
fig3 = plt.figure(3)
x_axis3 = []
num3 = 0
for k in range(0,len(ground_ent)):
    x_axis3 = x_axis3 + [num3]
    num3 = num3 + t_step
    #plt.plot(np.arange(0, T, t_step).tolist(), energy, 'b')
    #plt.plot(np.arange(0, T+t_step, t_step).tolist(), energy, 'b')
plt.plot(x_axis3, ground_ent)
plt.title('Ground State Entropy')
plt.ylabel('Entropy')

# P(Success) - Makes more sense with USA, but just hang with me
classical_soln = Sahni(G) # Classical solution
for i in range(0,len(prob_state)):
    if classical_soln==bin[i]:
        soln_prob = prob_state[i]
        break
print(soln_prob)
print(min(min_gap))
fig1.savefig("tmp/fig1.png")
fig2.savefig("tmp/fig2.png")
fig3.savefig("tmp/fig3.png")

# Deleting tmp file storing figs
#os.remove('tmp/fig1.png')
#os.remove('tmp/fig2.png')
#os.rmdir('tmp')
