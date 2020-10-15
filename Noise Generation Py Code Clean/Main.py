
import numpy as np
import pandas as pd
import glob
import wfdb
import tester_utils
import process_runner


if __name__ == '__main__':
    
    half_removal_interval_length = 25
    
    ############################## Example Data ############################################
    ecg_path    = './Data/example/ecg/'
    rpeak_path  = './Data/example/rpeaks/'
    fs          = 200
    
    ecg_file    = glob.glob(ecg_path + "/*.xlsx")
    rpeak_file  = glob.glob(rpeak_path + "/*.xlsx")
    
    df_ecg = pd.read_excel(ecg_file[0])
    ecg_signal = df_ecg.values
    ecg_signal = ecg_signal[:,0]
    
    df_rpeak = pd.read_excel(rpeak_file[0])
    rpeaks = df_rpeak.values
    rpeaks = rpeaks[:,0]
    
    gen_artif = process_runner.process_run(ecg_signal, rpeaks, fs, half_removal_interval_length)
        
    ################################ MITDB Data ###########################################
    # ecg_db_path = './Data/mitdb/'
    # fs = 360
    # db_length = len(glob.glob1('./Data/mitdb/',"*.dat"))
    
    # for index, name in enumerate(glob.glob1('./Data/mitdb/',"*.dat")):
    #     name = name[:-4]
    #     print("file name: "+name + "  -->  " + str(index) + " from " + str(db_length))
    #     # read dataset
    #     record = wfdb.rdrecord(ecg_db_path + name)
    #     record = np.transpose(record.p_signal)
    #     ann = wfdb.rdann(ecg_db_path + name,'atr')
               
    #     # clean dataset        
    #     ecg_signal = record[0]
    #     rpeaks = tester_utils.sort_MIT_annotations(ann)

    #     # Generate Noise
    #     gen_artif = process_runner.process_run(ecg_signal, rpeaks, fs, half_removal_interval_length)
