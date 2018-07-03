from time import sleep
import numpy as np
from tsfresh.feature_extraction.feature_calculators import *
from tsfresh.feature_extraction.extraction import extract_features

################################################################################

def preprocess(samples):
    samples = remove_mag_component(samples)
    columns = []
    for i in range(0, samples.shape[1]):
        rows_to_select = range(0, samples.shape[0])
        cols_to_select = [i]
        #columns.append(samples[np.ix_(rows_to_select, cols_to_select)])
        columns.append(samples[:, i])
   # return first_location_of_maximum(samples)
    first_mins = map(first_location_of_minimum, columns) 
    first_maxs = map(first_location_of_maximum, columns) 
    #last_mins = map(last_location_of_minimum, columns) 
    #last_maxs = map(last_location_of_maximum, columns) 


    r = []
    r += map(first_location_of_minimum, columns) 
    r += map(count_above_mean, columns) 
    r += map(count_below_mean, columns) 
#    r += map(longest_strike_above_mean, columns) 
#    r += map(longest_strike_below_mean, columns) 
    r += map(lambda a, b: a - b, first_mins, first_maxs)
    #r += map(lambda a, b: a - b, last_mins, last_maxs)
    r += map(fft_max_filter_single_column, columns) 
    r += map(mean_abs_change, columns) 
    r += map(standard_deviation, columns) 

    #columns = map(lambda x: local_averages(x, 2), columns) # smooth out 
    #r += map(fft_max_filter_single_column, columns) 

    #r += map(lambda x: sum(integral(x)), columns) 
    to_return = np.asarray(r)
    #print 'RSHAPE > ', to_return.shape
    return to_return.reshape((1, -1))

################################################################################

def preprocess_old(samples):
    samples = remove_mag_component(samples)
    return fft_max_filter(samples)

################################################################################

def get_acc_component(samples):
    if type(samples) == list:
        return np.asarray(samples[0:2])#3])
        
    if type(samples) == np.ndarray:
        rows_to_select = range(0, samples.shape[0])
        cols_to_select = [0, 1]#, 2]
        return samples[np.ix_(rows_to_select, cols_to_select)]
    
################################################################################

def get_gyr_component(samples):
    if type(samples) == list:
        return np.asarray(samples[6:9])
        
    if type(samples) == np.ndarray:
        rows_to_select = range(0, samples.shape[0])
        cols_to_select = [6, 7, 8]
        return samples[np.ix_(rows_to_select, cols_to_select)]

################################################################################

def remove_mag_component(samples):
    if type(samples) == list:
        return np.asarray(samples[0:3] + samples[6:9])
        
    if type(samples) == np.ndarray:
        rows_to_select = range(0, samples.shape[0])
        cols_to_select = [0, 1, 2, 6, 7, 8]
        return samples[np.ix_(rows_to_select, cols_to_select)]

################################################################################

def fft_max_filter_single_column(samples_single_column):
    return max(np.real(np.fft.fft(samples_single_column)))

################################################################################

def fft_max_filter(samples):
    r = []

    for i in range(0, len(samples[0])):
        r.append(max(np.real(np.fft.fft(samples[:, i]))))

    return np.asarray(r).reshape(1, len(r))

################################################################################

def integral(column):
    r = []
    sum_ = 0
    for val in column:
        sum_ += val
        r.append(sum_)
    return np.asarray(r)

################################################################################

def local_averages(column, window_size):
    r = []
    for j in range(0, len(column)):
        local_values = []
        for i in range(-window_size, window_size):
            if 0 < i < len(column):
                local_values.append(column[i])
        r.append((sum(local_values)) / float(len(local_values)))
    return r

################################################################################

class IntegrationFilter(object):
    
    WEIGHT = .1

    def __init__(self, initial_mean):
        self.mean = float(initial_mean)

    def feed(self, number):
        self.mean = self.mean * (1 - WEIGHT) + number * WEIGHT

    def get_mean(self):
        return self.mean

################################################################################
