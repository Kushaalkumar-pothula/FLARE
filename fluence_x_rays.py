import numpy as np
import matplotlib.pyplot as plt


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

def generate_fluence_xray(dirname):
	radio_fluence  = np.loadtxt(f'{dirname}/fluence.txt')
	fluence_x_rays = list(map(fluence_x_ray_calc, radio_fluence))

	#---------------------Plotting-------------------------

	fig = plt.gcf()
	fig.set_size_inches(8,6)

	plt.hist(fluence_x_rays, bins = 500, alpha = 0.5, color = 'red')

	plt.xlabel(r"$X-ray\ Fluence\ [\frac{erg}{cm^2}]$", fontsize = 15,)
	plt.ylabel("Number of FRBs",fontsize = 15)
	plt.grid(True)
	plt.yscale("Log")

	plt.savefig(f'{dirname}/X-ray Fluence.png')
	#----------------------------------------------------
