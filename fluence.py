import numpy as np

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

def generate_fluence(dirname):
    energy_data  = np.loadtxt(f'{dirname}/energy.txt')
    distance_data  = np.loadtxt(f'{dirname}/distance.txt')
    
    fluence = list(map(fluence_calc, distance_data, energy_data))

    arr_f = np.array(fluence)
    np.savetxt(f'{dirname}/fluence.txt', arr_f)
