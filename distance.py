import numpy as np
from datetime import datetime

d_meters = []   #FRB distance in meters

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

#Generate 100,000 FRB distances
for i in range(100000):
    d_meters.append(distance())

arr_d = np.array(d_meters)
time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")
np.savetxt(time_now+"_distance.txt",arr_d)
