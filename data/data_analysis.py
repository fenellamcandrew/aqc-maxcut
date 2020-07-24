import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Read dataset
df = pd.read_csv('runs.csv', index_col=0)

# Recommended way
sns.relplot(x='min energy gap', y='prob success', col='n_qubits', col_wrap=2, hue='Graph type', data=df)
sns.relplot(x='max entanglement', y='prob success', col='n_qubits', col_wrap=2, hue='Graph type', data=df)
#sns.relplot(x='min energy gap', y='max entanglement', col='n_qubits', col_wrap=2, hue='Graph type', data=df)
#sns.relplot(x='Density', y='prob success', col='n_qubits', col_wrap=2, data=df)

sns.lmplot(x='n_qubits', y='prob success', data=df)

fig, axs = plt.subplots(ncols=2)
sns.lineplot(x='n_qubits',y='max entanglement', hue='Graph type', estimator=np.mean, data=df, ax=axs[0])
sns.lineplot(x='n_qubits',y='max entanglement', hue='Graph type', estimator=np.median, data=df, ax=axs[1])
fig, axs = plt.subplots(ncols=2)
sns.lineplot(x='n_qubits', y='prob success', hue='Graph type', estimator=np.mean, data=df, ax=axs[0])
sns.lineplot(x='n_qubits', y='prob success', hue='Graph type', estimator=np.median, data=df, ax=axs[1])

df_2 = df[df['Number of solutions']==1] # Filtering data so only contains ones where n_solns=1

sns.lmplot(x='min energy gap',y='prob success',hue='n_qubits',fit_reg=False,legend=True,legend_out=True,data=df_2)

plt.figure()
sns.boxplot(x='n_qubits',y='prob success',data=df)

df_3 = df_2[df_2['Graph type']=='high_density']

sns.lmplot(x='Density',y='min energy gap',hue='n_qubits',fit_reg=False,data=df_3)

df_4 = df[df['Number of solutions']>1]
df_2['Solution type'] = 'Unique solution'
df_4['Solution type'] = 'Multiple solutions'
df_5 = pd.concat([df_2, df_4])
sns.relplot(x='max entanglement', y='prob success', data=df_5, hue='Solution type')

sns.relplot(x='max entanglement', y='prob success', data=df_2, hue='n_qubits')

plt.show()
