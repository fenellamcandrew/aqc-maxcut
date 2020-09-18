import numpy as np
from itertools import permutations
from pauli import *
import networkx as nx
import matplotlib.pyplot as plt
import math
import yaml
import pandas as pd
from brute_maxcut import *

# DO NOT DELETE!!! DON'T BE STUPID FENELLA!!!

#dir = "/Users/fenella/Documents/Uni/Research/Code/Instances/Sparse"
#f = open(r"/Users/fenella/Documents/Uni/Research/Code/Instances/Sparse" + "/n=15/15_Sparse1.txt","r")
#g = f.readline()    # this will be a string
#ge = eval(g)     # this will be the contents of the string; that is, the dictionary
#G = nx.node_link_graph(ge)  # this will turn the dictionary back into a graph
#n = G.number_of_nodes()
#m = G.number_of_edges()
#nx.draw(G)
#plt.show()

########################################################################
'''
def normTest(array): # Should be correct
    sum = 0
    #newArray = []
    for i in range(0,len(array)):
        sum = sum + abs((array[i].real)**2 + (array[i].imag)**2)
        #newArray = newArray + [np.sqrt(abs((array[i].real)**2 + (array[i].imag)**2))]
    return (array/(np.sqrt(sum)))

def normFinal(array):
    sum = 0
    newArray = []
    for i in range(0,len(array)):
        sum = sum + abs((array[i].real)**2 + (array[i].imag)**2)
        newArray = newArray + [np.sqrt(abs((array[i].real)**2 + (array[i].imag)**2))]
    return (newArray/(np.sqrt(sum)))

# Create sparse 8 node graph
G1 = nx.Graph()
G1 = nx.gnm_random_graph(8,10)

# Create dense 8 node graph
G2 = nx.Graph()
G2 = nx.gnm_random_graph(8,22)

# Create structured 8 node graph (average degree is 4)
nodes = [0,1,2,3,4,5,6,7]
edges = [(0,1),(0,3),(0,5),(0,6),(1,4),(1,6),(1,7),(2,3),(2,5),(2,6),(2,7), \
         (3,4),(3,7),(4,5),(4,7),(5,6)]

G3 = nx.Graph()
G3.add_nodes_from(nodes)
G3.add_edges_from(edges)
'''
########################################################################
#graphs = [G1, G2, G3]
#path = "/Users/fenella/Documents/Uni/Research/Code/Instances/Simple Examples/"
#count = 0
#list = ['Sparse', 'Dense', 'Deg4']
#for G in graphs:
#    name = list[count] + ".txt"
#    f = open(path + name,"w+")
#    print(nx.node_link_data(G),file=f)
#    f.flush()
#    f.close()
#    count = count + 1

#plt.figure(1)
#nx.draw(G1,with_labels=True)
#plt.figure(2)
#nx.draw(G2,with_labels=True)
#plt.figure(3)
#nx.draw(G3,with_labels=True)
#plt.show()

########################################################################
'''
def squareElems(array):
    newArray = []
    for i in range(0,len(array)):
        newArray = newArray + [array[i]**2]
    return newArray

GPlanar = nx.gnm_random_graph(3,3)
GNonPlanar = nx.complete_graph(7)

print(nx.algorithms.planarity.check_planarity(GPlanar, counterexample=True))
print(nx.algorithms.planarity.check_planarity(GNonPlanar, counterexample=True))
'''
########################################################################
'''
state = np.kron(plus(), plus())
state = normTest(state)
print(state)
state = np.dot(np.kron(pT(),pH()),state)
state = normTest(state)
print(state)
state = np.dot(np.kron(pH(),np.identity(2)),state)
state = normFinal(state)
print(state)
'''

########################################################################
# SAVE FOR _main_.py file
#for i in range(0,len(states)):
#    plt.figure(i+1)
#    state_curr_A = states[len(states)-(i+1)]
## Finding the max values in PDF, so we don't have to label every value
## Will only label xaxis of the highest peaks (makes it neater)
#    x = np.arange(0,2**n,1)
#    length = len(str(format(x[-1],'b'))) # Length of final binary value
#    bin = []
#    for i in x:
#        bin = bin + [format(i,'b').zfill(length)] # Converting all values to binary values

#    m = max(state_curr) # Max peak
#    maxes = [i for i, j in enumerate(state_curr_A) if j == m] # Finding all maxes
#    slice = list(np.array(bin)[maxes]) # Returning index of maxvalues

#    prob_state = squareElems(state_curr_A)

## Plotting PDF for final states, graph relating to the problem
##plt.bar(x,state_curr.transpose().tolist()[0])
#    plt.bar(x,prob_state.transpose().tolist())
#    plt.xticks(maxes, slice, rotation=90)
#    plt.title("PDF for final states")

########################################################################
'''
with open(r'params_template.yaml') as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)
    print(doc["build_hamiltonians"]["params"]["n_qubits"])
'''
'''
fig, ax = plt.subplots()
fig1 = plt.figure(1)
x = [1,2,3,4]
y = [1,2,3,4]
plt.plot(x,y)

fig2 = plt.figure(figsize = (10,7))
plt.subplot(2,2,1)
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x,y)

fig1.savefig('tmp/fig1.png')
fig2.savefig('tmp/fig2.png')
'''

########################################################################
'''
dir = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/unique_soln"
f = open(r"/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/unique_soln" + "/n=8/8_unique_soln16.txt","r")
g = f.readline()    # this will be a string
ge = eval(g)     # this will be the contents of the string; that is, the dictionary
G1 = nx.node_link_graph(ge)  # this will turn the dictionary back into a graph
n1 = G1.number_of_nodes()
m1 = G1.number_of_edges()

plt.figure()
pos1 = nx.circular_layout(G1)
nx.draw(G1,pos1,with_labels=True)

print("radius: %d" % nx.radius(G1))
print("diameter: %d" % nx.diameter(G1))
print("eccentricity: %s" % nx.eccentricity(G1))
print("center: %s" % nx.center(G1))
print("periphery: %s" % nx.periphery(G1))
print("density: %s" % nx.density(G1))

dir = "/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/unique_soln"
f = open(r"/Users/fenella/Documents/Uni/Research/aqc-maxcut/instances/unique_soln" + "/n=8/8_unique_soln48.txt","r")
g = f.readline()    # this will be a string
ge = eval(g)     # this will be the contents of the string; that is, the dictionary
G2 = nx.node_link_graph(ge)  # this will turn the dictionary back into a graph
n2 = G2.number_of_nodes()
m2 = G2.number_of_edges()

plt.figure()
pos2 = nx.circular_layout(G2)
nx.draw(G2,pos2,with_labels=True)

print("radius: %d" % nx.radius(G2))
print("diameter: %d" % nx.diameter(G2))
print("eccentricity: %s" % nx.eccentricity(G2))
print("center: %s" % nx.center(G2))
print("periphery: %s" % nx.periphery(G2))
print("density: %s" % nx.density(G2))

city = pd.DataFrame([[str(nx.center(G1)), str(nx.eccentricity(G1))], [str(nx.center(G2)), str(nx.eccentricity(G2))]], columns=['center', 'eccentricity'])
city.to_csv('temp_yaml/test.csv')
df = pd.read_csv('temp_yaml/test.csv', index_col=0)
print(df)
'''
'''
nodes = 10*[3]
Glist = []
count = 0
while count < 20:
    G = nx.random_degree_sequence_graph(nodes)
    solver = bruteMAX(G)
    solns = solver['cuts']
    if nx.is_connected(G) and (len(solns) == 2) and (G not in Glist):
        continue
    else:
        Glist = Glist + [G]
        plt.figure()
        nx.draw(G,with_labels=True)
        count = count + 1
print(G.degree())
print(Glist)
'''
G = nx.random_powerlaw_tree(9)
nx.draw(G,with_labels=True)
plt.show()
