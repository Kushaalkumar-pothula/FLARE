import numpy as np

#--------------------FRB Distances-----------------------
def distance():
    """
    Return a random value of FRB distance, 
    choosen from a range of observed FRB distances.
    - Args: None.
    - Returns: FRB distance in meters
    """
    dist_m = np.random.uniform(6.4332967e24,1.6849561e26)
    return dist_m
#---------------------------------------------------------

def generate_distance(dirname):
    #Generate 100,000 FRB distances
    d_meters = [distance() for _ in range(100000)]

    arr_d = np.array(d_meters)
    np.savetxt(f'{dirname}/distance.txt', arr_d)

