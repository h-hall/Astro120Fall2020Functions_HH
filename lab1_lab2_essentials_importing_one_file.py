#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import all important packages
import numpy as np


# In[2]:


# Navigate to raw data
#--------------------------------------#
lab1_data_path = 'example_data/lab1_pmt_data/lab1_data_10k_.8b_1r.csv'
#--------------------------------------#


# Import data
#--------------------------------------#
DELIMITER = ','
DTYPE = 'int32'

lab1_data = np.loadtxt(lab1_data_path, delimiter=DELIMITER, dtype=DTYPE)
#--------------------------------------#

