import numpy as np
from datetime import datetime

time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")
energy_data  = np.loadtxt(time_now+"_energy.txt")
distance_data  = np.loadtxt(time_now+"_distance.txt")

#------------------Fluence values----------------------
def fluence_calc(d,e):
    """
    Return calculated value of FRB fluence, for giant flares 
    occurring within the range of FRB distances.
    Args: 
    - d: distance to the source
    - e: energy
    Returns: FRB fluence value in erg/cm^2
    """
    #Convert flare energy to joules
    fluence_val = (e/(4*np.pi*((d*100)**2)))
    return fluence_val
#------------------------------------------------------

fluence = list(map(fluence_calc, distance_data, energy_data))

time_now_2 = datetime.now().strftime("%Y-%m-%d-%H-%M")

arr_f = np.array(fluence)
np.savetxt(time_now_2+"_fluence.txt", arr_f)
