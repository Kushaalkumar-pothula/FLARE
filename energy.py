import numpy as np
from datetime import datetime

energy = [] #Giant flare energy in ergs

#------------------Giant flare energy------------------
@jit(nopython = True)
def flare_energy():
    """
    Return a random value of giant flare energy, in the range
    10^38 erg to 10^47 erg.
    - Args: None.
    - Returns: Random giant flare energy value in ergs.
    """
    f_energy = np.random.uniform(1e38,1e47)
    return f_energy
    
#-------------------------------------------------------

#Generate 100,000 giant flares
for i in range(100000):
    energy.append(flare_energy())
 
arr_e = np.array(energy)

time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")
np.savetxt(time_now+"_energy.txt",arr_e)
