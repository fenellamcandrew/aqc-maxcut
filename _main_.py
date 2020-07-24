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
from entanglement import *
from energy_gap import *
from Sahni import *
from energy_calc import *
from brute_maxcut import *

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

# Calculate psucess (given classical solution add up the corresponding
# probabilities in the quantum state PDF)
def psuccess(classical_soln, prob_state):
    psucc = 0
    for soln in classical_soln:
        for i in range(0,len(prob_state)):
            if soln==bin[i]:
                psucc = psucc + prob_state[i]
    return psucc

# Creating tmp file to store figs
if os.path.exists('tmp'):
    if os.path.exists('tmp/fig1.png'):
        os.remove('tmp/fig1.png')
    if os.path.exists('tmp/fig2.png'):
        os.remove('tmp/fig2.png')
    if os.path.exists('tmp/fig3.png'):
        os.remove('tmp/fig3.png')
    if os.path.exists('tmp/fig4.png'):
        os.remove('tmp/fig4.png')
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
#run_path = 'params/ready/' + run_path

print("\nReading yaml file\n")
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
density = 2*m/(n*(n-1)) # calculating density
degrees = [val for (node, val) in G.degree()] # node degrees
is_planar = nx.check_planarity(G) # checking is graph is planar
algConnect = nx.algebraic_connectivity(G) # reflects how connected a graph is
d = nx.diameter(G)
av_shortest_path = nx.average_shortest_path_length(G)
radius = nx.radius(G) # minimum eccentricity
av_cluster = nx.average_clustering(G)

# calculating chromatic number
G1 = nx.algorithms.coloring.greedy_color(G)
colours = [G1[i] for i in range(n)]
chromatic_num = max(colours)-min(colours)+1


# MLFLOW
mlflow.set_tracking_uri(doc["experiment"]["tracking-uri"])
mlflow.set_experiment(doc["experiment"]["name"])
with mlflow.start_run():
    # log parameters for mlflow
    mlflow.log_param("n_qubits", n)
    mlflow.log_param("n_edges", m)
    mlflow.log_param("t_step", t_step)
    mlflow.log_param("T", T)
    mlflow.log_param("Graph type", graph_type)
    mlflow.log_param("Density", density)
    mlflow.log_param("Planar", is_planar[0])
    mlflow.log_param("Chromatic number", chromatic_num)
    mlflow.log_param("min node degree", min(degrees))
    mlflow.log_param("max node degree", max(degrees))
    mlflow.log_param("average node degree", sum(degrees)/len(degrees))
    mlflow.log_param("algebraic connectivity", algConnect)
    mlflow.log_param("average shortest path", av_shortest_path)
    mlflow.log_param("diameter", d)
    mlflow.log_param("radius", radius)
    mlflow.log_param("average clustering", av_cluster)

    mlflow.log_artifact(run_path)

# Creating initial state, which is just equal superposition over all
# possible states
    print('Calculating classical solution\n')
    classical_soln = bruteMAX(G) # Classical solution
    if len(classical_soln) == 2:
        soln_type = 'unique solution'
        bias = 1
    else:
        soln_type = 'multiple solutions'
        bias = 0

    mlflow.log_param("Number of solutions", int(len(classical_soln)/2))
    mlflow.log_param("Solution type", soln_type)

    state_curr = 1
    for i in range(0,n):
        state_curr = np.kron(state_curr, minus())
    t = 0 # start time
# Initial and Problem Hamiltonians based off our generated graph
    ent = []
    energy = []
    min_gap = []
    ground_ent = []
    p_succ = []
    biggest_psucc_diff = [0,0]

    print('Building Hamiltonians\n')
    Hb = init_hamil(G)
    Hp = prob_hamil(G,bias)

    x = np.arange(0,2**n,1)
    length = len(str(format(x[-1],'b'))) # Length of final binary value
    bin = []
    for i in x:
        bin = bin + [format(i,'b').zfill(length)] # Converting all values to binary values

    # Current probability of success
    psucc_curr = psuccess(classical_soln,squareElems(magnitudes(state_curr)))

    print("Starting evolution\n")
    while t <= T: # Terminate when t/T = 1
        energies = energyCalcs(t,T,Hb,Hp)
        energy = energy + [energies["e_gap"]] # Energy gap list
        ground_ent = ground_ent + [energies["g_ent"]] # Entropy of ground state
        min_gap = min_gap + [abs((energies["e_gap"])[0]-(energies["e_gap"])[1])] # Minimum energy gap

        new_state = schrodinger_solver(state_curr, t_step, t, T, Hb, Hp)

        # Kepping track of time when the largest jump in psuccess happens
        psucc_new = psuccess(classical_soln,squareElems(magnitudes(new_state)))
        if biggest_psucc_diff[0] < abs(psucc_new-psucc_curr):
            biggest_psucc_diff[0] = abs(psucc_new-psucc_curr)
            biggest_psucc_diff[1] = t

        psucc_curr = psucc_new

        p_succ = p_succ + [psucc_curr] #

        state_curr = new_state
    #state_curr1 = magnitudes(state_curr)
    #states = states + [state_curr1]
        ent = ent + [entanglementCalc(n,state_curr)]
        t = t + t_step

    state_curr = magnitudes(state_curr)

    print("Creating figures\n")
# For the time being, have truncated the values to avoiding rounding errors
    for i in range(0,len(state_curr)):
        state_curr[i] = np.round(state_curr[i],10)
        #state_curr[i] = truncate(state_curr[i], 10)

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
    if bias == 1:
        solns_found = len(maxes)
    else:
        solns_found = len(maxes)/2

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
    plt.xlabel("T")

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
    plt.xlabel("T")

# Plotting picture of graph
    plt.subplot(2,2,(3,4))
    nx.draw(G,with_labels=True)

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
    plt.xlabel('T')

# PLOTTING PSUCCESS, BUT PROBABLY UNINTERESTING
    fig4 = plt.figure(4)
    x_axis4 = []
    num4 = 0
    for k in range(0,len(p_succ)):
        x_axis4 = x_axis4 + [num4]
        num4 = num4 + t_step
    plt.plot(x_axis4, p_succ)
    plt.title("Probability Success")
    plt.ylabel("probability success")
    plt.xlabel("T")

# P(Success) - just hang with me
    #classical_soln = bruteMAX(G) # Classical solution
    psucc = 0
    for soln in classical_soln:
        for i in range(0,len(prob_state)):
            if soln==bin[i]:
                psucc = psucc + prob_state[i]

    fig1.savefig("tmp/fig1.png")
    fig2.savefig("tmp/fig2.png")
    fig3.savefig("tmp/fig3.png")
    fig4.savefig("tmp/fig4.png")

    print('Logging MLFlow data\n')

# log metrics for mlflow
    mlflow.log_metric("max entanglement",max(ent))
    mlflow.log_metric("min energy gap",min(min_gap))
    mlflow.log_metric("prob success",psucc)
    mlflow.log_metric("biggest psucc change",biggest_psucc_diff[0])
    mlflow.log_metric("biggest psucc change time", biggest_psucc_diff[1])
    mlflow.log_metric("number of solutions found", solns_found)
    mlflow.log_metric("max ground entanglement",max(ground_ent))

# lof artifacts for mlflow (graphs and run_path)
    mlflow.log_artifact("tmp/fig1.png")
    mlflow.log_artifact("tmp/fig2.png")
    mlflow.log_artifact("tmp/fig3.png")
    mlflow.log_artifact("tmp/fig4.png")


# Deleting tmp file storing figs
os.remove('tmp/fig1.png')
os.remove('tmp/fig2.png')
os.remove('tmp/fig3.png')
os.remove('tmp/fig4.png')
os.rmdir('tmp')
