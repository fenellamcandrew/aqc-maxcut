import numpy as np
import matplotlib.pyplot as plt
import xlrd

loc = "d_runs.xls"

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

header = sheet.row_values(0) # Name of columns

# Put each column of data into a list
status = sheet.col_values(header.index('status'),start_rowx=1)
density = sheet.col_values(header.index('params.Density'),start_rowx=1)
type = sheet.col_values(header.index('params.Graph type'),start_rowx=1)
ent = sheet.col_values(header.index('metrics.max entanglement'),start_rowx=1)
n = sheet.col_values(header.index('params.n_qubits'),start_rowx=1)
psucc = sheet.col_values(header.index('metrics.prob success'),start_rowx=1)
psucc_t = sheet.col_values(header.index('metrics.biggest psucc change time'),start_rowx=1)
n_soln = sheet.col_values(header.index('params.Number of solutions'),start_rowx=1)
solns_found = sheet.col_values(header.index('metrics.number of solutions found'),start_rowx=1)
e_gap = sheet.col_values(header.index('metrics.min energy gap'),start_rowx=1)
t_step = sheet.col_values(header.index('params.t_step'),start_rowx=1)
T = sheet.col_values(header.index('params.T'),start_rowx=1)
planarity = sheet.col_values(header.index('params.Planar'),start_rowx=1)

# Filter data so it's only completed runs
count = 0
while count < len(status):
    if status[count] != "FINISHED":
        del status[count]
        del density[count]
        del type[count]
        del ent[count]
        del n[count]
        del psucc[count]
        del psucc_t[count]
        del n_soln[count]
        del solns_found[count]
        del e_gap[count]
        del t_step[count]
        del T[count]
        del planarity[count]
    else:
        count = count + 1

size = sum([1 for i in range(len(status)) if (n[i]==12) and (type[i]=='Sparse')])
print(size)

# Dense/Sparse - average entanglement vs number of qubits
av_ent_d = [[0]]*len(range(7,13))
av_ent_s = [[0]]*len(range(7,13))
for i in range(7,13):
    count_d = 0
    count_s = 0
    for j in range(len(ent)):
        if (type[j] == "Dense") and (n[j]==i):
            av_ent_d[i-7] = av_ent_d[i-7] + [ent[j]]
        if (type[j] == "Sparse") and (n[j]==i):
            av_ent_s[i-7] = av_ent_s[i-7] + [ent[j]]

for i in range(7,13):
    av_ent_d[i-7] = sum(av_ent_d[i-7])/len(av_ent_d[i-7])
    av_ent_s[i-7] = sum(av_ent_s[i-7])/len(av_ent_s[i-7])

plt.figure(1)
plt.plot(range(7,13), av_ent_d, label="Dense")
plt.plot(range(7,13), av_ent_s, label="Sparse")
plt.xlabel("n_qubits")
plt.ylabel("average entanglement")
plt.legend()

# Planar/Non Planar - average entanglement vs number of qubits
av_ent_plan = [[0]]*len(range(7,13))
av_ent_nplan = [[0]]*len(range(7,13))
for i in range(7,13):
    count_d = 0
    count_s = 0
    for j in range(len(ent)):
        if (planarity[j] == True) and (n[j]==i):
            av_ent_plan[i-7] = av_ent_plan[i-7] + [ent[j]]
        if (planarity[j] == False) and (n[j]==i):
            av_ent_nplan[i-7] = av_ent_nplan[i-7] + [ent[j]]

for i in range(7,13):
    av_ent_plan[i-7] = sum(av_ent_plan[i-7])/len(av_ent_plan[i-7])
    av_ent_nplan[i-7] = sum(av_ent_nplan[i-7])/len(av_ent_nplan[i-7])

plt.figure(2)
plt.plot(range(7,13), av_ent_plan, label="Planar")
plt.plot(range(7,13), av_ent_nplan, label="Non Planar")
plt.xlabel("n_qubits")
plt.ylabel("average entanglement")
plt.legend()

# Dense/Sparse - Probability of success vs number of qubits
psucc_d = [psucc[i] for i in range(len(psucc)) if type[i]=='Dense']
n_d = [n[i] for i in range(len(psucc)) if type[i]=='Dense']
psucc_s = [psucc[i] for i in range(len(psucc)) if type[i]=='Sparse']
n_s = [n[i] for i in range(len(psucc)) if type[i]=='Sparse']

plt.figure(3)
plt.plot(n_s, psucc_s, 'o', label="Sparse")
plt.plot(n_d, psucc_d, 'o', label="Dense")
plt.xlabel("n_qubits")
plt.ylabel("probability success")
plt.legend()

# Planar/Non Planar - Probability of success vs number of qubits
psucc_plan = [psucc[i] for i in range(len(psucc)) if planarity[i]==True]
n_plan = [n[i] for i in range(len(psucc)) if planarity[i]==True]
psucc_nplan = [psucc[i] for i in range(len(psucc)) if planarity[i]==False]
n_nplan = [n[i] for i in range(len(psucc)) if planarity[i]==False]

plt.figure(4)
plt.plot(n_plan, psucc_plan, 'o', label="Planar")
plt.plot(n_nplan, psucc_nplan, 'o', label="Non Planar")
plt.xlabel("n_qubits")
plt.ylabel("probability success")
plt.legend()

# Planar/Non Planar - average probability of success vs number of qubits
av_psucc_plan = [0]*len(range(7,13))
av_psucc_nplan = [0]*len(range(7,13))
for j in range(7,13):
    psucc_plan = [psucc[i] for i in range(len(psucc)) if (planarity[i]==True) and (n[i]==j)]
    psucc_nplan = [psucc[i] for i in range(len(psucc)) if (planarity[i]==False) and (n[i]==j)]
    len_plan = len(psucc_plan)
    len_nplan = len(psucc_nplan)
    if len_plan == 0: len_plan = 1
    if len_nplan == 0: len_nplan = 1
    av_psucc_plan[j-7] = sum(psucc_plan)/len_plan
    av_psucc_nplan[j-7] = sum(psucc_nplan)/len_nplan

plt.figure(5)
plt.plot(range(7,13), av_psucc_plan, label="Planar")
plt.plot(range(7,13), av_psucc_nplan, label="Non Planar")
plt.xlabel("n_qubits")
plt.ylabel("average probability success")
plt.legend()

# different T, same t, energy gap vs number of qubits
fig = plt.figure(figsize = (10,7))
fig.suptitle("t=0.1")
t = 0.1
Ts = [100,200,300,400]
for i in Ts:
    energy = [e_gap[j] for j in range(len(e_gap)) if (n_soln[j]==1) and (T[j]==i) and (t_step[j]==t)]
    ns = [n[j] for j in range(len(e_gap)) if (n_soln[j]==1) and (T[j]==i) and (t_step[j]==t)]
    plt.subplot(2,2,int(i/100))
    plt.plot(ns, energy, 'o', label=str(i))
    plt.xlabel("n_qubits")
    plt.ylabel("energy gap")
    plt.legend()

fig = plt.figure(figsize = (10,7))
fig.suptitle("t=0.2")
t = 0.2
Ts = [100,200,300,400]
for i in Ts:
    energy = [e_gap[j] for j in range(len(e_gap)) if (n_soln[j]==1) and (T[j]==i) and (t_step[j]==t)]
    ns = [n[j] for j in range(len(e_gap)) if (n_soln[j]==1) and (T[j]==i) and (t_step[j]==t)]
    plt.subplot(2,2,int(i/100))
    plt.plot(ns, energy, 'o', label=str(i))
    plt.xlabel("n_qubits")
    plt.ylabel("energy gap")
    plt.legend()

plt.show()
