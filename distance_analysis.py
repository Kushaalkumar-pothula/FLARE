from datetime import datetime
time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")

import numpy as np
distance_data  = np.loadtxt(time_now+"_distance.txt")

#-----------------------------Plot---------------------------------------
import matplotlib.pyplot as plt

fig = plt.gcf()
fig.set_size_inches(8,6)
plt.hist(distance_data, bins = 500, alpha = 0.5, color = 'green')
plt.xlabel(r"$Distance\ [m]$", fontsize = 15,)
plt.ylabel("Number of FRBs",fontsize = 15)
plt.grid(True)
plt.yscale("Log")

time_now_2 = datetime.now().strftime("%Y-%m-%d-%H-%M")
plt.savefig(time_now_2+"_distance_analysis.png")
#-----------------------------------------------------------------------