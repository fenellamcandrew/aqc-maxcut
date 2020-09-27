from statistics import mean
from random import choice
from random import sample

import networkx as nx
import matplotlib.pyplot as plt
import statistics as st
import scipy
import numpy as np

class MyGraph(nx.Graph):
    def __init__(self, num_nodes, target_deg, target_wght, max_wght=5):
        super().__init__()
        self.num_nodes = num_nodes
        self.target_deg = target_deg
        self.target_wght = target_wght
        self.max_wght = max_wght
        self.add_nodes_from(range(self.num_nodes))
        while self.avg_deg() < self.target_deg:
            n1, n2 = sample(self.nodes(), 2)
            self.add_edge(n1, n2, weight=1)
        while self.avg_wght() < self.target_wght:
            n1, n2 = choice(list(self.edges()))
            if self[n1][n2]['weight'] < self.max_wght:
                self[n1][n2]['weight'] += 1

    def avg_deg(self):
        return self.number_of_edges() * 2 / self.num_nodes

    def avg_wght(self):
        wghts = []
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                try:
                    wghts.append(self[i][j]['weight'])
                except KeyError:
                    pass
        return mean(wghts)

count = 0
while count < 20:
    G = MyGraph(9, 2, 1)
    degrees = [val for (node, val) in G.degree()]
    var = st.variance(degrees)
    if (nx.is_connected(G)) and (var > 4.5):
        lapl = sorted(nx.normalized_laplacian_spectrum(G),reverse=True)
        print(var, np.log(lapl[0]/lapl[1]))
        plt.figure()
        nx.draw(G)
        count = count + 1

plt.show()
