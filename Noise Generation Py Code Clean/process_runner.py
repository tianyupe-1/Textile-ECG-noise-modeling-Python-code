
"""
Process Runner Code

Note: This code takes the initial inpus and calls all the sub-functions before returning the generated artifact

Inputs:
    1. ecg_signal: the recorded raw ECG
    2. rpeaks: true R-peak locations (indices)
    3. fs: sampling frequency
    4. half_removal_interval_length = l (ms)
"""

from Subfunctions.R_peak_removal import R_peak_removal as RpeakRemove
from Subfunctions.lpc_approx import lpc_approx as lpcApx
from Subfunctions.KDE_generation import KDE_generation as generateKDE

def process_run(ecg_signal, rpeaks, fs, half_removal_interval_length):
    
    rpk_removed_sig = RpeakRemove(ecg_signal, rpeaks, fs, half_removal_interval_length)
    rpk_removed_sig_0, lpc_pred, err, pdf_err, lpc_coef, kde_err = lpcApx(rpk_removed_sig)
    gen_artif = generateKDE(kde_err, lpc_coef, rpk_removed_sig_0)
    
    return gen_artif

