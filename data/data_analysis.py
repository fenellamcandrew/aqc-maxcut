import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Read dataset
df = pd.read_csv("d_runs.csv", index_col=1)
################################################################################
# Filtering data
df = df[df['metrics.max entanglement'].notnull()]
print('Number of experiments completed: ' + str(len(df['status'])))

for i in range(1,101):
    print('instance' + str(i) + '=' + str(len(df[df['params.instance index']==i])))

df_one = df[df['params.graph type']=='unique_soln']

'''
################################################################################
# Comparing to probability of success
all_max_ent_psucc_n = sns.relplot(x='metrics.max entanglement', y='metrics.prob success', col='params.T', hue='params.n_qubits', data=df)
all_max_ent_psucc_n.savefig("figs/all_max_ent_psucc_n.png")

all_max_ent_psucc_type = sns.relplot(x='metrics.max entanglement', y='metrics.prob success', col='params.T', hue='params.Graph type', data=df)
all_max_ent_psucc_type.savefig("figs/all_max_ent_psucc_type.png")

max_ent_psucc = sns.relplot(x='metrics.max entanglement',y='metrics.prob success', col='params.n_qubits',col_wrap=3, hue='params.Graph type',data=df)
max_ent_psucc.savefig("figs/max_ent_psucc.png")
max_gent_psucc = sns.relplot(x='metrics.max ground entanglement',y='metrics.prob success', col='params.n_qubits',col_wrap=3, hue='params.Graph type',data=df)
max_gent_psucc.savefig("figs/max_gent_psucc.png")

pr_one = sns.relplot(x='metrics.max entanglement', y='metrics.prob success', hue='params.n_qubits', data=df_one)
pr_one.savefig("figs/pr_one.png")
pr_many = sns.relplot(x='metrics.max entanglement', y='metrics.prob success', hue='params.n_qubits', data=df_many)
pr_many.savefig("figs/pr_many.png")

################################################################################
# Counting Experiments
count_qubits = plt.figure()
sns.countplot(x='params.n_qubits', data=df)
count_qubits.savefig("figs/count_qubits.png")

count_Tqubits = plt.figure()
sns.countplot(x='params.n_qubits', hue='params.T', data=df)
count_Tqubits.savefig("figs/count_Tqubits")

count_type = plt.figure()
sns.countplot(x='params.Graph type', data=df)
count_type.savefig("figs/count_type")

################################################################################
# Average values (lineplots)
av_ent_qubits, axs = plt.subplots(ncols=2, figsize=(18,10))
sns.lineplot(x='params.n_qubits',y='metrics.max entanglement', estimator=np.mean, data=df, ax=axs[0])
sns.lineplot(x='params.n_qubits',y='metrics.max entanglement', estimator=np.median, data=df, ax=axs[1])
av_ent_qubits.savefig("figs/av_ent_qubits")
av_psucc_qubits, axs = plt.subplots(ncols=2, figsize=(18,10))
sns.lineplot(x='params.n_qubits', y='metrics.prob success', hue='params.Graph type', estimator=np.mean, data=df, ax=axs[0])
sns.lineplot(x='params.n_qubits', y='metrics.prob success', hue='params.Graph type', estimator=np.median, data=df, ax=axs[1])
av_psucc_qubits.savefig("figs/av_psucc_qubits")

################################################################################
# Looking at specific graph characteristics
df['chrom_div_nedges'] = df['params.Chromatic number']/df['params.n_edges']
chrom_edge_psucc = sns.relplot(x='chrom_div_nedges', y='metrics.prob success', col='params.T', hue='params.n_qubits', data=df)
chrom_edge_psucc.savefig('figs/graph_chars/chrom_edge_prsucc.png')

chrom_edge_ent = sns.relplot(x='chrom_div_nedges', y='metrics.max entanglement', col='params.T', hue='params.n_qubits', data=df)
chrom_edge_ent.savefig('figs/graph_chars/chrom_edge_ent.png')

df['chrom/av nodes deg'] = df['params.Chromatic number']/df['params.average node degree']
chrom_div_av_node_psucc = sns.relplot(x='chrom/av nodes deg', y='metrics.prob success', col='params.T', hue='params.n_qubits', data=df)
chrom_div_av_node_ent = sns.relplot(x='chrom/av nodes deg', y='metrics.max entanglement', col='params.T', hue='params.n_qubits', data=df)
chrom_div_av_node_psucc.savefig('figs/graph_chars/chrom_div_av_node_psucc.png')
chrom_div_av_node_ent.savefig('figs/graph_chars/chrom_div_av_node_ent.png')


df['tri/alg_conn'] = df['params.triangles']/df['params.algebraic connectivity']
tri_div_algc_psucc = sns.relplot(x='tri/alg_conn', y='metrics.prob success', col='params.T', hue='params.n_qubits', data=df)
tri_div_algc_ent = sns.relplot(x='tri/alg_conn', y='metrics.max entanglement', col='params.T', hue='params.n_qubits', data=df)
tri_div_algc_psucc.savefig('figs/graph_chars/tri_div_algc_psucc.png')
tri_div_algc_ent.savefig('figs/graph_chars/tri_div_algc_ent.png')

df_many['chrom_div_nedges'] = df_many['params.Chromatic number']/df_many['params.n_qubits']
sns.relplot(x='chrom_div_nedges', y='metrics.prob success', col='params.T', hue='params.n_qubits', data=df_many)

df_one['chrom_div_nedges'] = df_one['params.Chromatic number']/df_one['params.n_qubits']
sns.relplot(x='chrom_div_nedges', y='metrics.prob success', col='params.T', hue='params.n_qubits', data=df_one)
'''
'''
df_one_10 = df_one[df_one['params.n_qubits']==10]
sns.relplot(x='metrics.max entanglement',y='metrics.prob success',col='params.T',hue='params.Chromatic number',data=df_one_10)

plt.show()
'''
