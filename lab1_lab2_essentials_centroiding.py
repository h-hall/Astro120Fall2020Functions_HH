#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import all important packages
import numpy as np


# In[2]:


def centroiding(signal_peaks_index, signal_data): # For this function, the first input is the array of peak indeces that was produced in our peak finding function
    CCD_PIXELS = 2048
    pixel = np.arange(0, CCD_PIXELS)
    n_peaks = len(signal_peaks_index)
    centroids = np.zeros((n_peaks,)) # Pixel coordinates for all the centroids
    FWHM = np.zeros((n_peaks,)) # Full-width-half-max signal values for each centroid
    for i in range(n_peaks): # We are using the pixel indeces from our original peak finding function
        peak = signal_peaks_index[i]
        half_max = signal_data[peak] / 2.
        FWHM[i] = (half_max)

        xmin = np.nonzero(signal_data[peak:0:-1] <= half_max)[0][0]
        xmax = np.nonzero(signal_data[peak:-1] <= half_max)[0][0]
        x_range = pixel[peak - xmin:peak + xmax].copy()
        I_range = signal_data[peak - xmin:peak + xmax].copy()
        I_total = np.sum(I_range) # Avoid duplicate calculation
        x_com = np.sum(x_range * I_range / I_total) # x_com stands for X Center of Mass
        centroids[i] = (x_com)
    return centroids, FWHM

