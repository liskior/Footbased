import numpy as np

################################################################################

def preprocess(samples):
    samples = remove_mag_component(samples)
    return fft_max_filter(samples)

################################################################################

def remove_mag_component(samples):
    from numpy import ix_
    rows_to_select = range(0, samples.shape[0])
    cols_to_select = [0, 1, 2, 6, 7, 8]
    return samples[ix_(rows_to_select, cols_to_select)]

################################################################################

def fft_max_filter(samples):
    r = []

    for i in range(0, len(samples[0])):
        r.append(max(np.real(np.fft.fft(samples[:, i]))))

    return np.asarray(r).reshape(1, len(r))

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
