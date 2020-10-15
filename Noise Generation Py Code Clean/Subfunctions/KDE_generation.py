
"""
Step 3 code

This code generate a new noise signal with KDE estimated residue distribution, 
using the same feature (LPC coefficients in our work). The output is the
generated noise.

Inputs (from Step 2):
1. err_pdf: KDE estimated residue density with gaussian / epanechnikov kernel
2. lpc_coef: coefficients of AR(3) filter
3. ori_artif: the original noise signal with the the first element shifted to 0

"""

from scipy import signal
import numpy as np
from matplotlib import pyplot as plt

def KDE_generation(kde_err, lpc_coef, ori_artif):
    
    gen_artif = signal.lfilter(np.array([1.0]), lpc_coef, kde_err) #pass the KDE sample to the same LPC coefficients
    
    # Comparison plot: original noise and KDE generated noise
    plt.figure()
    ax1 = plt.subplot(211)
    ax1.plot(ori_artif,color='blue') 
    plt.grid()
    plt.ylabel('original artifact', fontsize=16)
    #plt.xlabel('Sample (n)')
    
    ax2 = plt.subplot(212, sharex=ax1)
    ax2.plot(gen_artif,color='blue')   
    plt.grid()
    plt.ylabel('KDE generated artifact', fontsize=16)
    plt.xlabel('Sample (n)')
    
    return gen_artif
