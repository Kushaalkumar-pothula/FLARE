import numpy as np
import os

#------------------------------File IO (input)------------------------------
i_1 = 0
if os.path.exists("flare_distance_result%s.txt" % i_1):
    pass
else:
    i_1 += 1

distance_data = np.loadtxt("flare_distance_result%s.txt" % i_1)

i_2 = 0
if os.path.exists("flare_energy_result%s.txt" % i_2):
    pass
else:
    i_2 += 1

energy_data = np.loadtxt("flare_energy_result%s.txt" % i_2)
#---------------------------------------------------------------------------

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


#------------------------------File IO (output)-----------------------------
arr_f = np.array(fluence)

i = 0
if os.path.exists("flare_fluence_result%s.txt" % i):
    i += 1
else:
    pass


np.savetxt("flare_fluence_result%s.txt" % i, arr_f)
#---------------------------------------------------------------------------

