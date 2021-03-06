import numpy as np
import matplotlib.pyplot as plt

#-----------------------------Plot---------------------------------------

def generate_fluence_plot(dirname):
    radio_fluence  = np.loadtxt(f"{dirname}/fluence.txt")
    fig = plt.gcf()
    fig.set_size_inches(8,6)
    plt.hist(radio_fluence, bins = 500, alpha = 0.5, color = 'orange')
    plt.xlabel(r"$Radio\ Fluence\ [\frac{erg}{cm^2}]$", fontsize = 15,)
    plt.ylabel("Number of FRBs",fontsize = 15)
    plt.grid(True)
    plt.yscale("Log")

    plt.savefig(f'{dirname}/Radio Fluence Analysis.png')
#-----------------------------------------------------------------------
