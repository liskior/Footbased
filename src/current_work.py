""" Not important.

Some experiments we did. This script is not used.

"""

import numpy as np
from os.path import isdir
from os import listdir
from preprocessor import *
from first import firj

class Experiment(object):

    def __init__(self, dataset, preprocessor_function, classifier, evaluator):
        self.__features = preprocessor_function(dataset.get_data())
        self.__labels = dataset.get_labels()

        self.__dataset = dataset
        self.__preprocess = preprocessor_function
        self.__classifier = classifier
        self.__evaluator = evaluator

    def run(self): # TODO this is actually an evaluator
        for i in range(0, self.__dataset.number_of_sample_sets()):
            train, test = self.__leave_one_out(i)

            train_samples, train_labels = train
            self.__classifier.fit(train_samples, train_labels)

        features = self.__preprocess(self.__dataset)
        labels = self.__dataset.get_labels()

    def __leave_one_out(self, i):
        sample_sets_to_take = range(0, len(self.__dataset))
        sample_sets_to_take.remove(i)

        train_samples = self.__[np.ix_(sample_sets_to_take)]
        train_labels = self.__labels[np.ix_(sample_sets_to_take)]

        test_samples = self.__dataset.get_data()[i]
        test_labels = self.__dataset.get_labels()[i]

        return (train_samples, train_labels), (test_samples, test_labels)


class Dataset(object):
    __data = []

    __labels = []

    def __init__(self, path):
        if not isdir(path):
            raise Exception('Directory not found: ' + path)
        
        for samples_file in filter(lambda x: x.endswith('.txt'), listdir(path)):
            data.append(np.loadtxt(samples_file))
            labels.append(self.__label_from_file_name(samples_file))

            self.__data = np.asarray(data)
            self.__labels = np.asarray(labels)

    def __label_from_file_name(self, file_name):
        return int(filename.split('_')[1].lstrip('0'))

    def get_data(self):
        return self.__data

    def get_labels(self):
        return self.__labels
        
    def __len__(self):
        return len(self.get_labels())

class Features(object):
    def __init__(self, 
