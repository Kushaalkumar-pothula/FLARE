import numpy as np
import os

#--------------------------------Astrophysics--------------------------------
d_meters = []   #FRB distance in meters

def distance():
    """
    Return a random value of FRB distance, 
    choosen from a range of observed FRB distances.
    - Args: None.
    - Returns: FRB distance in meters
    """
    dist_m = np.random.uniform(6.4332967e24,1.6849561e26)
    return dist_m

#Generate 100,000 FRB distances
for i in range(100000):
    d_meters.append(distance())
#--------------------------------------------------------------------------


#----------------------------------File IO---------------------------------
i = -2
while os.path.exists("flare_distance_result%s.txt" % i):
    i += 1

 
arr = np.array(d_meters)
np.savetxt("flare_distance_result%s.txt" % i, arr)
#---------------------------------------------------------------------------
