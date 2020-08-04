import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Read dataset
df = pd.read_csv("d_runs.csv", index_col=0)
print(len(df['metrics.max entanglement'])-df['metrics.max entanglement'].isnull().sum())
print(df['metrics.max entanglement'].isnull())

################################################################################
# Filtering data
df = df[(df['status']=='FAILED') | (df['status']=='FINISHED')]
print('Number of experiments completed: ' + str(len(df['status'])))
'''
df_one = df[df['params.Graph type']=='unique_soln']
df_many = df[df['params.Graph type']=='multiple_soln']

df_2 = df[df['params.Number of solutions']==2]
df_3 = df[df['params.Number of solutions']==3]
df_4 = df[df['params.Number of solutions']==4]
df_5 = df[df['params.Number of solutions']==5]
df_more = df[df['params.Number of solutions']>5]


################################################################################
# Comparing to probability of success
all_max_ent_psucc = sns.relplot(x='metrics.max entanglement', y='metrics.prob success', hue='params.Density', data=df)
all_max_ent_psucc.savefig("figs/all_max_ent_psucc.png")

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

count_t_step_qubits = plt.figure()
sns.countplot(x='params.n_qubits', hue='params.t_step', data=df)
count_t_step_qubits.savefig("figs/count_t_step_qubits")

count_type = plt.figure()
sns.countplot(x='params.Graph type', data=df)
count_type.savefig("figs/count_type")

################################################################################
# Average values (lineplots)
av_ent_qubits, axs = plt.subplots(ncols=2, figsize=(18,10))
sns.lineplot(x='params.n_qubits',y='metrics.max entanglement', hue='params.Graph type', estimator=np.mean, data=df, ax=axs[0])
sns.lineplot(x='params.n_qubits',y='metrics.max entanglement', hue='params.Graph type', estimator=np.median, data=df, ax=axs[1])
av_ent_qubits.savefig("figs/av_ent_qubits")
av_psucc_qubits, axs = plt.subplots(ncols=2, figsize=(18,10))
sns.lineplot(x='params.n_qubits', y='metrics.prob success', hue='params.Graph type', estimator=np.mean, data=df, ax=axs[0])
sns.lineplot(x='params.n_qubits', y='metrics.prob success', hue='params.Graph type', estimator=np.median, data=df, ax=axs[1])
av_psucc_qubits.savefig("figs/av_psucc_qubits")

################################################################################
# Comparing with entanglement
# Unique Solution
path = 'figs/unique_soln/'
av_node_v_ent = sns.relplot(x='params.average node degree', y='metrics.max entanglement', col='params.n_qubits', col_wrap=3, data=df_one)
av_node_v_ent.savefig(path + "av_node_v_ent.png")

av_clust_v_ent = sns.relplot(x='params.average clustering', y='metrics.max entanglement', col='params.n_qubits', col_wrap=3, data=df_one)
av_clust_v_ent.savefig(path + "av_clust_v_ent.png")

av_short_path_v_ent = sns.relplot(x='params.average shortest path', y='metrics.max entanglement', col='params.n_qubits', col_wrap=3, data=df_one)
av_short_path_v_ent.savefig(path + "av_short_path_v_ent.png")

alg_connect_v_ent = sns.relplot(x='params.algebraic connectivity', y='metrics.max entanglement', col='params.n_qubits', col_wrap=3, data=df_one)
alg_connect_v_ent.savefig(path + "alg_connect_v_ent.png")

# Multiple Solutions
path = 'figs/many_soln/'
av_node_v_ent = sns.relplot(x='params.average node degree', y='metrics.max entanglement', col='params.n_qubits', col_wrap=3, data=df_many)
av_node_v_ent.savefig(path + "av_node_v_ent.png")

av_clust_v_ent = sns.relplot(x='params.average clustering', y='metrics.max entanglement', col='params.n_qubits', col_wrap=3, data=df_many)
av_clust_v_ent.savefig(path + "av_clust_v_ent.png")

av_short_path_v_ent = sns.relplot(x='params.average shortest path', y='metrics.max entanglement', col='params.n_qubits', col_wrap=3, data=df_many)
av_short_path_v_ent.savefig(path + "av_short_path_v_ent.png")

alg_connect_v_ent = sns.relplot(x='params.algebraic connectivity', y='metrics.max entanglement', col='params.n_qubits', col_wrap=3, data=df_many)
alg_connect_v_ent.savefig(path + "alg_connect_v_ent.png")
'''
'''
sns.relplot(x='metrics.max entanglement', y='metrics.prob success', hue='params.max node degree', data=df_many, legend='full')
sns.relplot(x='metrics.max entanglement', y='metrics.prob success', hue='params.max node degree', data=df_one, legend='full')

sns.relplot(x='metrics.max entanglement', y='metrics.prob success', hue='params.Planar', data=df_many, legend='full')
sns.relplot(x='metrics.max entanglement', y='metrics.prob success', hue='params.Planar', data=df_one, legend='full')

df_more['params.Number of solutions'] = '>5'
df_new = pd.concat([df_2, df_3, df_4, df_5, df_more])
sns.relplot(x='metrics.max entanglement', y='metrics.prob success', hue='params.Number of solutions', data=df_new, legend='full')
plt.show()
'''
