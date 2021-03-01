import numpy as np
import os
import matplotlib.pyplot as plt

#------------------------------File IO (input)------------------------------
i = -1
if os.path.exists("flare_fluence_result%s.txt" % i):
    pass
else:
    i +=1

radio_fluence = np.loadtxt("flare_fluence_result%s.txt" % i)
#---------------------------------------------------------------------------


#-----------------------------Plot---------------------------------------
fig = plt.gcf()
fig.set_size_inches(8,6)
plt.hist(radio_fluence, bins = 500, alpha = 0.5, color = 'orange')
plt.xlabel(r"$Radio\ Fluence\ [\frac{erg}{cm^2}]$", fontsize = 15,)
plt.ylabel("Number of FRBs",fontsize = 15)
plt.grid(True)
plt.yscale("Log")

plt.savefig("fluence_analysis_result%s.png" % i)
#-----------------------------------------------------------------------
