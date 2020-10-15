
"""
Step 1 code

Note: This code remove R-peaks in the original signal, thus the remaining signal is mostly
noise, which is the basis of modelling. To use this code, we need to first identify the correct locations of R-peaks.
In our work, we did simultaneous recording with gel electrode
from heart (high quality) and we've identified the R-peak locations in the heart
(reference) signal. 

Meaning of inputs: 
1. signal: the recorded raw ECG
2. peak_true: true R-peak locations (indices)
3. fs: sampling frequency
4. half_removal_interval_length = l (ms): the interval that we want to remove
around the R-peak, i.e. the signal in [R-peak - l, R-peak + l] is
replaced by [R-peak - 3l, R-peak - l]. The R-peak infomation is replaced
by noise. In our work, we choose a small value l=25ms to reduce
information loss. If the user want to make sure that the whole QRS is removed,
l=50ms is appropriate as well.

"""

#import numpy as np

def R_peak_removal(signal, peak_true, fs, half_removal_interval_length):
    
    half_remove_sample_num = int(half_removal_interval_length * fs / 1000)
    # number of samples in the half removal interval, i.e. removal interval 
    # is [peak_true_index - half_remove_sample_num:peak_true +
    # half_remove_sample_num].half_removal_interval_length (in sec) =  half_remove_sample_num/sampling fq
    # so half_remove_sample_num =
    # half_removal_interval_length (in ms) * sampling fq / 1000
    
    removed_sig = signal
    
    for j in range(1, len(peak_true)): 
        removed_sig[peak_true[j]-half_remove_sample_num:peak_true[j]+half_remove_sample_num] = signal[peak_true[j]-(3*half_remove_sample_num)-1:peak_true[j]-half_remove_sample_num-1]
        # replace the signal around peaks by previous noise.
    
    print("Completed Rpeak removal.")
    
    return removed_sig



    