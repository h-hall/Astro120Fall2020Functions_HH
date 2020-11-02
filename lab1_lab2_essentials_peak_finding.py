#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import all important packages
import numpy as np


# In[2]:


def peak_finding(signal_threshold_minimum, signal_data):
    signal_peaks = []
    signal_peaks_index = [] # x positions of the peaks, or rather, their index

    for i in range(len(signal_data) - 1): #len(signal)-1 because you will be checking the value after than your last i 
        if (signal_threshold_minimum <= signal_data[i]) \
            and (signal_data[i - 1] <= signal_data[i]) \
            and (signal_data[i] >= signal_data[i + 1]):  #three conditions to be a peak 
            
            signal_peaks.append(signal_data[i])
            signal_peaks_index.append(i)
    return signal_peaks_index, signal_peaks
