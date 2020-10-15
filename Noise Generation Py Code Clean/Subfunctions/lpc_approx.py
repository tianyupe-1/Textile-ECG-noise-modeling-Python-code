

"""
Step 2 code

This code gives the noise features. The input is the noise signal (after
R-peak removal) in Step 1. We use a LPC filter (AR(3)), and other filters
can be used to replace AR(3).

Outputs:
1. removed_sig_0: the noise signal with the the first element shifted to 0
2. lpc_pred: AR(3) predicted signal
3. err: AR(3) prediction residue signal
4. pdf_err: KDE estimated residue density with epanechnikov kernel
5. lpc_coef: coefficients of AR(3) filter

"""

import librosa
from scipy import signal
import numpy as np
from matplotlib import pyplot as plt

from sklearn.neighbors import KernelDensity

def lpc_approx(removed_sig):
    
    try:        
        removed_sig = removed_sig[:,0]
    except:
        removed_sig = removed_sig
           
    removed_sig_0 = removed_sig - removed_sig[0] # shift the first element to 0
    removed_sig_0=removed_sig_0.astype(np.float) #Convert to floating point
    lpc_coef = librosa.lpc(removed_sig_0, 3) # get coefficients of AR(3) filter
    lpc_coef_filtering = -lpc_coef
    lpc_coef_filtering[0] = 0
    lpc_pred = signal.lfilter(lpc_coef_filtering,1,removed_sig_0) # AR(3) predicted signal
    
    err = np.zeros((len(lpc_pred),1))
    err[:,0] = removed_sig_0 - lpc_pred # residue signal
    
    kde = KernelDensity(kernel='gaussian').fit(err) #KDE estimated density with gaussian / epanechnikov kernel
    pdf_err = kde.score_samples(err) # score_samples returns the log of the probability density
    
    kde_err = kde.sample(n_samples=len(removed_sig_0), random_state=None) #generate a random sample residue with KDE estimation
    
    # comparison plots

    # # seperate plots
    # plt.figure(1)
    # ax1 = plt.subplot(211)
    # ax1.plot(removed_sig,color='blue') 
    # plt.grid()
    # plt.ylabel('Signal (a.u.)', fontsize=16)
    # #plt.xlabel('Sample (n)')
    
    # ax2 = plt.subplot(212, sharex=ax1)
    # ax2.plot(lpc_pred,color='blue')   
    # plt.grid()
    # plt.ylabel('Predicted LPC (a.u.)', fontsize=16)
    # plt.xlabel('Sample (n)')
    
    print("Completed LPC Approximation.")
    
    # plot together, compare original noise with AR(3) prediction
    ns = np.arange(0,len(removed_sig_0),1)
    plt.figure()
    plt.plot(ns,removed_sig_0, label='Original signal')
    plt.plot(ns,lpc_pred, label='LPC estimate')
    plt.legend()

    
    return removed_sig_0, lpc_pred, err, pdf_err, lpc_coef, kde_err
    