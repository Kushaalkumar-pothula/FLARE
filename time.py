import numpy as np 
import matplotlib.pyplot as plt 
from datetime import datetime

#------------------FRB period------------------

def frb_period():
    """
    Return a random value of FRB timescale, in the range
    0.08 ms to 5000 ms.
    - Args: None.
    - Returns: Random FRB timescale in milliseconds.
    """
    frb_t = np.random.uniform(0.08,5000)
    return frb_t
    
#-------------------------------------------------------

#Generate 100,000 giant flares
for i in range(100000):
    time.append(frb_period())

fig = plt.gcf()
fig.set_size_inches(8,6)

plt.hist(np.log(time), bins = 105, alpha = 0.5, color = 'blue')

plt.xlabel(r"$log(FRB\ Timescale) [ms]$", fontsize = 15,)
plt.ylabel("Number of FRBs",fontsize = 15)

plt.grid(True)
plt.yscale("Log")

time_now  = datetime.now().strftime("%Y-%m-%d-%H-%M")

arr_t = np.array(time)
np.savetxt(time_now+"_FRB period.txt", arr_t)
plt.savefig(time_now+"_FRB period analysis.png")