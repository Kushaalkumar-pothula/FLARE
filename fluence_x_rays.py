import numpy as np
from datetime import datetime

time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")
radio_fluence  = np.loadtxt(time_now+"_fluence.txt")

#------------------Fluence values----------------------
def fluence_x_ray_calc(f):
    """
    Return calculated value of FRB's X-ray counterpart fluence, 
    for giant flares occurring within the range of FRB distances.
    Args: 
    - f: Radio frequency fluence
    Returns: F
      FRB X-ray counterpart fluence value in erg/cm^2
    """
    fluence_x = (f/(2e-5))
    return fluence_x
#------------------------------------------------------

fluence_x_rays = list(map(fluence_x_ray_calc, radio_fluence))

#---------------------Plotting-------------------------
import matplotlib.pyplot as plt

fig = plt.gcf()
fig.set_size_inches(8,6)

plt.hist(fluence_x_rays, bins = 500, alpha = 0.5, color = 'red')

plt.xlabel(r"$X-ray\ Fluence\ [\frac{erg}{cm^2}]$", fontsize = 15,)
plt.ylabel("Number of FRBs",fontsize = 15)
plt.grid(True)
plt.yscale("Log")

time_now_2 = datetime.now().strftime("%Y-%m-%d-%H-%M")
plt.savefig(time_now_2+"X-ray Fluence.png")
#----------------------------------------------------
