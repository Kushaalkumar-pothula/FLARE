import numpy as np
from datetime import datetime

#----------------------------Astrophysics--------------------------------

energy = [] #Giant flare energy in ergs

def flare_energy():
    """
    Return a random value of giant flare energy, in the range
    10^38 erg to 10^47 erg.
    - Args: None.
    - Returns: Random giant flare energy value in ergs.
    """
    f_energy = np.random.uniform(1e38,1e47)
    return f_energy
    

#Generate 100,000 giant flares
for i in range(100000):
    energy.append(flare_energy())
 
#--------------------------------------------------------------------------


#----------------------------------File IO---------------------------------
arr_e = np.array(energy)

i = 0
while os.path.exists("flare_energy_result%s.txt" % i):
    i += 1

 
np.savetxt("flare_energy_result%s.txt" % i, arr_e)
#---------------------------------------------------------------------------
