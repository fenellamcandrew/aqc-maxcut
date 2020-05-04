import yaml
import networkx as nx

with open(r'params/ready/t_step0.010000__time_T1__instance_index1.000000__n_qubits11.000000__graph_typeDense.yml') as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)

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
