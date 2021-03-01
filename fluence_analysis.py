from datetime import datetime
time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")

import numpy as np
radio_fluence  = np.loadtxt(time_now+"_fluence.txt")

#-----------------------------Plot---------------------------------------
import matplotlib.pyplot as plt

fig = plt.gcf()
fig.set_size_inches(8,6)
plt.hist(radio_fluence, bins = 500, alpha = 0.5, color = 'orange')
plt.xlabel(r"$Radio\ Fluence\ [\frac{erg}{cm^2}]$", fontsize = 15,)
plt.ylabel("Number of FRBs",fontsize = 15)
plt.grid(True)
plt.yscale("Log")

time_now_2 = datetime.now().strftime("%Y-%m-%d-%H-%M")
plt.savefig(time_now_2+"Radio Fluence Analysis.png")
#-----------------------------------------------------------------------
