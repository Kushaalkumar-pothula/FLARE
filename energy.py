import numpy as np

#------------------Giant flare energy------------------
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

def generate_energy(dirname):
    #Generate 100,000 giant flares
    energy = [flare_energy() for _ in range(100000)]
    
    arr_e = np.array(energy)
    np.savetxt(f'{dirname}/energy.txt', arr_e)
