def extract_features_and_label_from_file(path_to_file):
    from numpy import loadtxt
    from preprocessor import preprocess

    filename = path_to_file.split('/')[-1]

    label = filename.split('_')[1].lstrip('0')

    samples = loadtxt(path_to_file)
    features = preprocess(samples)

    return features, label

def extract_data_and_target_from_dir(path_to_dataset_dir):
    from fnmatch import fnmatch
    from os import listdir
    from numpy import asarray
    
    data = []
    target = []

    file_count = 0
    for filename in listdir(path_to_dataset_dir):
        if fnmatch(filename, 'rec_*.txt'):
            file_count += 1
            path_to_file = path_to_dataset_dir + '/' + filename
            features, label = extract_features_and_label_from_file(path_to_file)
            data.append(features)
            target.append(label)

    return asarray(data).reshape(file_count, -1), asarray(target)

data, target = extract_data_and_target_from_dir('dataset4')

#from sklearn import svm
#clf = svm.SVC()
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(data, target)

from sensor import Sensor
s = Sensor()
while not s.get_single_sample(): pass

from preprocessor import preprocess

import numpy as np
live_samples = []

while True:
    from time import sleep
    sleep(0.01)
    live_samples.append(s.get_single_sample(with_timestamp=False))
    if len(live_samples) > 100:
        question = preprocess(live_samples[-100:]).reshape(1, -1)
        print 'QUESTION', question
        print clf.predict(question)
