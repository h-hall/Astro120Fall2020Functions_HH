#!/usr/bin/env python
# coding: utf-8

# # **Astro 160 Fall 2020 Essential Pieces of Code v.1**
# ## *Hunter Hall — hall@berkeley.edu — October 21, 2020*

# ##### *These are simply taken from some of my lab assignments during the Fall of 2019. Feel free to make any edits you'd like to them, but when doing so, please make a new cell below the original code so that we can see why we edited the original as we did. - Hunter*

# In[1]:


#Import all important packages
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

#This make plots inline
get_ipython().run_line_magic('matplotlib', 'inline')
#This increases image resolution
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# # 1.0 **Importing .txt or .csv Files**
# ## *Linked below are files from Hunter's 2019 datasets from Labs 1 and 2 that are used in this example — note that the glob function wasn't necessarily used in Lab 1, but that it still works for .csv and .txt files:* 
# https://drive.google.com/file/d/1ZeIZHzrKRpZVqp-3zwkk0u72AKEZX2AN/view?usp=sharing

# ## 1.1 Importing One File

# In[2]:


#Define a variable that navigates to the csv file

lab1_data_path = 'example_data/lab1_pmt_data/lab1_data_10k_.8b_1r.csv'


# In[3]:


#Define a variable that represents the thing we want to assign our csv data to 

lab1_data = np.loadtxt(lab1_data_path,delimiter=',',dtype='int32') #In this np.loadtxt command, we must set a delimiter=',' as this is a CSV file, and we must specify the data type as a 32-bit integer


# In[4]:


#Check to see if the data from csv file you've imported makes sense — for Lab 1, we should get an array with two columns in which the first represents the Channel Number of the PMT and the second represents the time-stamps

#Let's print out indicators about our data
#--------------------------------------#
print(type(lab1_data)) #Check to make sure that the class is an array
print(np.shape(lab1_data)) #Check to make sure that the dimensions of the data makes sense
print(lab1_data) #Check to make sure that the values of the data make sense
#--------------------------------------#


# In[5]:


#Now, let's go from the imported array to useful data


#Obtains an array of useful data
#--------------------------------------#
time_step = lab1_data[:,1] #This step gets rid of the first column since we don't care about the Channel Number
#--------------------------------------#


#Let's print out indicators about our data
#--------------------------------------#
print(type(time_step)) #Check to make sure that the class is an array
print(np.shape(time_step)) #Check to make sure that the dimensions of the data makes sense
print(time_step) #Check to make sure these time-step values make sense from our data
#--------------------------------------#


# In[6]:


#Merging all steps above into one cell


#Navigate to raw data
#--------------------------------------#
lab1_data_path = 'example_data/lab1_pmt_data/lab1_data_10k_.8b_1r.csv'
#--------------------------------------#


#Import data
#--------------------------------------#
lab1_data = np.loadtxt(lab1_data_path,delimiter=',',dtype='int32')
#--------------------------------------#


#Obtains an array of useful data
#--------------------------------------#
time_step = lab1_data[:,1]
#--------------------------------------#


#Displays the final output we've made
#--------------------------------------#
time_step
#--------------------------------------#


# ## 1.2 Importing Multiple Files with *glob*

# In[7]:


#Instead of importing and manipulating data step-by-step like in 1.1, we will define a function to do multiple steps

def get_signal(file_path):
    pixel = [] #This represents the pixels of the 1D CCD used in Lab 2
    signal = [] #This represents the signal/intensities of each pixel in the 1D CCD used in Lab 2
    for file in glob.glob(file_path): #Here, we implement the glob.glob feature to unpack all .txt files in the lab2_neon_data folder
        pixNum, s = np.genfromtxt(file, dtype=(float), skip_header=17, skip_footer=1, unpack=True) #If we open one of the neon.txt files in a text editor, we can see it has a header that is 17 lines long, and a footer that is one line long, so we exclude those in the np.genfromtxt command
        signal.append(s)
        pixel = np.arange(0,2048) #This range is set as there are 2048 pixels in the CCD
    return(pixel, signal) #This will make the function output an array of pixels and an array of corresponding signals


# In[8]:


#Now we will run the function from the previous cell using neon data from Lab 2 which was provided in the dataset download link at the start of this notebook

lab2_file_path = 'example_data/lab2_neon_data/*.txt' #Define a variable that navigates to the folder where all of the neon.txt files are located

pixel, signal = get_signal(lab2_file_path) #This will output an array of pixels and an array of corresponding signals for each file in the neon dataset


# In[9]:


#What we really want though is an averaged signal for each pixel across the entire neon dataset, so in order to do this we will take the mean of the pixel-by-pixel signals across each file in the dataset

signal_avg_neon = np.mean(signal,axis=0) #axis=0 makes the mean move through each file in the dataset


# In[10]:


#Now, let's check to make sure our results make sense

#Let's print out indicators about our data
#--------------------------------------#
print(type(signal_avg_neon)) #Check to make sure that the class is an array
print(np.shape(signal_avg_neon)) #Check to make sure that the dimensions of your data makes sense — in this case we should 2048 values as there should be a value for each of the 2048 pixels in the CCD
print(signal_avg_neon) #Check to make sure that the values of the data make sense
#--------------------------------------#


#Let's plot it to make sure it looks like the correct spectrum too
#--------------------------------------#
plt.figure()
plt.rcParams['figure.figsize'] = [10,5]
plt.rcParams.update({'font.size': 12})
plt.plot(pixel,signal_avg_neon)
plt.title('Neon (Raw Data)')
plt.xlabel('Pixel Number')
plt.ylabel('Raw Signal [ADU]')
plt.show()
#--------------------------------------#


# In[11]:


#Merging all steps above into one cell


#Function
#--------------------------------------#
def get_signal(file_path):
    pixel = []
    signal = []
    for file in glob.glob(file_path): 
        pixNum, s = np.genfromtxt(file, dtype=(float), skip_header=17, skip_footer=1, unpack=True)
        signal.append(s)
        pixel = np.arange(0,2048)
    return(pixel, signal)
#--------------------------------------#


#Navigate to raw data
#--------------------------------------#
lab2_file_path = 'example_data/lab2_neon_data/*.txt'
#--------------------------------------#


#Import data by executing function
#--------------------------------------#
pixel, signal = get_signal(lab2_file_path)
#--------------------------------------#


#Average files in the dataset
#--------------------------------------#
signal_avg_neon = np.mean(signal,axis=0)
#--------------------------------------#

#Plotting
#--------------------------------------#
plt.figure()
plt.rcParams['figure.figsize'] = [10,5]
plt.rcParams.update({'font.size': 12})
plt.plot(pixel,signal_avg_neon)
plt.title('Neon (Raw Data)')
plt.xlabel('Pixel Number')
plt.ylabel('Raw Signal [ADU]')
plt.show()
#--------------------------------------#


# # 2.0 **Peak Finding and Centroiding**
# ## *The data used in this section is the same data from section 1.0* 

# ## 2.1 1D Peak Finding Algorithm

# In[12]:


#We are going to use the same neon spectrum from the previous section, so let's re-run the final cell from the previous section to make sure we are starting with the fresh unchanged raw data


#Everything below is identical to the final cell from the previous section
#-------------------------------------------------------------------------#


#Function
#--------------------------------------#
def get_signal(file_path):
    pixel = []
    signal = []
    for file in glob.glob(file_path): 
        pixNum, s = np.genfromtxt(file, dtype=(float), skip_header=17, skip_footer=1, unpack=True)
        signal.append(s)
        pixel = np.arange(0,2048)
    return(pixel, signal)
#--------------------------------------#


#Navigate to raw data
#--------------------------------------#
lab2_file_path = 'example_data/lab2_neon_data/*.txt'
#--------------------------------------#


#Import data by executing function
#--------------------------------------#
pixel, signal = get_signal(lab2_file_path)
#--------------------------------------#


#Average files in the dataset
#--------------------------------------#
signal_avg_neon = np.mean(signal,axis=0)
#--------------------------------------#

#Plotting
#--------------------------------------#
plt.figure()
plt.rcParams['figure.figsize'] = [10,5]
plt.rcParams.update({'font.size': 12})
plt.plot(pixel,signal_avg_neon)
plt.title('Neon (Raw Data)')
plt.xlabel('Pixel Number')
plt.ylabel('Raw Signal [ADU]')
plt.show()
#--------------------------------------#


# In[13]:


#Now, we want to write some code that will give us the signal values of the peaks in the neon raw spectrum

threshold_neon =  200 #We don't want ALL of the peaks in the spectrum, because there are many small peaks that we don't necessarily need to use for the wavelength solution or spectroscopy later. So we set a minimum signal threshold, in this case 200 ADU, to only return the peaks that are above this threshold instead of all peaks in the spectrum.
peaks_neon = []
peaks_index_neon = [] #x positions of the peaks, or rather, their index
for i in range(len(signal_avg_neon)-1): #len(signal)-1 because you will be checking the value after than your last i 
    if (threshold_neon <= signal_avg_neon[i]) and (signal_avg_neon[i-1] <= signal_avg_neon[i]) and (signal_avg_neon[i] >= signal_avg_neon[i+1]):  #three conditions to be a peak 
        peaks_neon.append(signal_avg_neon[i])
        peaks_index_neon.append(i)


# In[14]:


#Next, we want to confirm that the peak finding function worked, so we will print out the peak signal values, their pixel locations, and then plot them over the original spectrum to see if everything lines up

#Let's print out indicators about our data
#--------------------------------------#
print(np.hstack((np.vstack(peaks_index_neon),np.vstack(peaks_neon)))) #This prints out two columns with the first representing the pixel location of the peak and the second representing the signal value at that peak
#Output will be in the format below:
#Pixel number, signal 
#--------------------------------------#


#Let's plot the spectrum as well as a scatter plot of our peaks to make sure it looks like the correct
#--------------------------------------#
plt.figure()
plt.rcParams['figure.figsize'] = [10,5]
plt.rcParams.update({'font.size': 12})
plt.plot(pixel, signal_avg_neon)
plt.scatter(peaks_index_neon, peaks_neon, color='red', marker='o', label='Peaks')
plt.title('Neon (Raw Data)')
plt.xlabel('Pixel Number')
plt.ylabel('Raw Signal [ADU]')
plt.legend()
plt.show()
#--------------------------------------#


# ## 2.2 1D Centroiding
# ### *Tutorial I followed during 2019 to help make my Lab 2 centroiding function:* 
# https://prappleizer.github.io/Tutorials/Centroiding/centroiding_tutorial.html

# In[15]:


#We want to write some code for the neon data that will give us the x-coordinate/pixel position of the centroids of our primary peaks. We will be using the peak finding code from section 2.1 for the initial pixel position guesses, so make sure that has been run before this cell.

centroids_neon = [] #Pixel coordinates for all the centroids
FWHM = [] #Full-width-half-max signal values for each centroid
for i in peaks_index_neon: #We are using the pixel indeces from our original peak finding function
    half_max = signal_avg_neon[i]/2.
    xmin = np.where(signal_avg_neon[i:0:-1] <= half_max)[0][0]
    xmax = np.where(signal_avg_neon[i:-1] <= half_max)[0][0]
    x_range = pixel[i-xmin:i+xmax]
    I_range = signal_avg_neon[i-xmin:i+xmax]
    x_range = np.array(x_range)
    I_range = np.array(I_range)
    x_com = np.sum(x_range*I_range / np.sum(I_range)) #x_com stands for X Center of Mass, which is the x-coordinate of our centroid, since a centroid is a center of mass
    centroids_neon.append(x_com)
    FWHM.append(half_max)


# In[16]:


#Similarly to the peak finding code, we want to confirm that the centroiding code worked, so we will print out the FWHM signal values, their new CENTROID locations, and then plot them over the original spectrum to see if everything lines up

#Let's print out indicators about our data
#--------------------------------------#
print(np.hstack((np.vstack(centroids_neon),np.vstack(FWHM)))) #This prints out two columns with the first representing the pixel location of the peak and the second representing the signal value at that peak
#Output will be in the format below:
#Centroid x-coordinate/pixel, FWHM signal value 
#--------------------------------------#


#Let's plot the spectrum as well as vertical bars on our centroid x-coordinates/pixels to make sure it looks like the correct
#-------------------------------------------------------------------------#


#This will plot the vertical lines on the centroid x-coordinates
#--------------------------------------#
def plot_vert(x): 
    '''
    Just plots vertical lines, in green dashes
    '''
    plt.axvline(x, color='green', ls='-.')
    
for i in centroids_neon[1:]: #Call our plotting function on every centroid except the first
    plot_vert(i)
#--------------------------------------#


#Let's plot the spectrum as well as the vertical centroid locations to make sure it looks like the correct
#--------------------------------------#
min_pixel = 1300 #Here, I am setting the minimum and maximum pixels that I want to view in the plot, since the neon peaks will be easier to see in this pixel range
max_pixel = 2000

plt.rcParams['figure.figsize'] = [10,5]
plt.rcParams.update({'font.size': 12})
plt.axvline(centroids_neon[0],color='green',ls='-.',label='Centroid') #Reserve the first so I don't have a million "centroid" labels
plt.plot(pixel[min_pixel:max_pixel], signal_avg_neon[min_pixel:max_pixel]) #Plot the actual spectrum
plt.scatter(centroids_neon, FWHM, color='red', marker='o', label='FWHM')
plt.title('Neon (Raw Data)')
plt.xlabel('Pixel Number')
plt.ylabel('Raw Signal [ADU]')
plt.legend()
plt.show()
#--------------------------------------#
#-------------------------------------------------------------------------#

