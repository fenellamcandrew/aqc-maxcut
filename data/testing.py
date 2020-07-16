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
psucc_t = sheet.col_values(header.index('metrics.biggest psucc change time'),start_rowx=1)
n_soln = sheet.col_values(header.index('params.Number of solutions'),start_rowx=1)
solns_found = sheet.col_values(header.index('metrics.number of solutions found'),start_rowx=1)
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
        del psucc_t[count]
        del n_soln[count]
        del solns_found[count]
        del t_step[count]
        del T[count]
        del planarity[count]
    else:
        count = count + 1

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

plt.plot(range(7,13), av_ent_d, label="Dense")
plt.plot(range(7,13), av_ent_s, label="Sparse")
plt.xlabel("n_qubits")
plt.ylabel("average entanglement")
plt.legend()
plt.show()
