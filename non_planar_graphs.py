import networkx as nx
import matplotlib.pyplot as plt

# Complete 5 node graph
K5 = nx.complete_graph(5) # cr = 1

# Utility Graph (aka K3,3)
K3_3 = nx.complete_bipartite_graph(3,3) # cr = 1

# 16-Cell graph
beta4 = nx.random_regular_graph(6,8)

# Grötzsch Graph
# - chromatic num = 4
grot_edges = [(0,1),(0,9),(0,10),(1,2),(1,5),(1,7),(2,3),(2,10),(3,4),(3,7), \
                (3,9),(4,5),(4,10),(5,6),(5,9),(6,7),(6,10),(7,8),(8,9),(8,10)]
grot = nx.Graph(grot_edges)

# Chvátal Graph
# - chromatic num = 4
chva_edges = [(0,1),(0,3),(0,4),(0,11),(1,2),(1,9),(1,10),(2,3),(2,7),(2,8), \
                (3,5),(3,6),(4,5),(4,7),(4,8),(5,9),(5,10),(6,7),(6,9),(6,10), \
                (7,11),(8,9),(8,11),(10,11)]
chva = nx.Graph(chva_edges)

# Franklin Graph
frank_edges = [(0,1),(0,3),(0,11),(1,2),(1,6),(2,3),(2,9),(3,4),(4,5),(4,7), \
                (5,6),(5,10),(6,7),(7,8),(8,9),(8,11),(9,10),(10,11)]
frank = nx.Graph(frank_edges)

# Heawood Graph
# - chromatic number = 2
heaw_edges = [(0,1),(0,9),(0,13),(1,2),(1,6),(2,3),(2,11),(3,4),(3,8),(4,5), \
                (4,13),(5,6),(6,7),(7,8),(7,12),(8,9),(9,10),(10,11),(11,12) \
                (12,13)]
heaw = nx.Graph(heaw_edges)

# Petersen Graph
petersen = nx.petersen_graph()
