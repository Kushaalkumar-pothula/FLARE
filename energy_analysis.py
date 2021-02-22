from datetime import datetime
time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")

import numpy as np
energy_data  = np.loadtxt(time_now+"_energy.txt")

#-----------------------------Plot---------------------------------------
import matplotlib.pyplot as plt

fig = plt.gcf()
fig.set_size_inches(8,6)
plt.hist(energy_data, bins = 500, alpha = 0.5, color = 'orange')
plt.xlabel(r"$Energy\ [=erg]$", fontsize = 15,)
plt.ylabel("Number of FRBs",fontsize = 15)
plt.grid(True)
plt.yscale("Log")

time_now_2 = datetime.now().strftime("%Y-%m-%d-%H-%M")
plt.savefig(time_now_2+"_energy_analysis.png")
#-----------------------------------------------------------------------