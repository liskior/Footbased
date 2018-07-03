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

data, target = extract_data_and_target_from_dir('rec')

#from sklearn import svm
#clf = svm.SVC()
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(data, target)

from sensor import Sensor
s = Sensor()
while not s.get_single_sample(): pass

from preprocessor import *

import numpy as np
live_samples = np.ndarray((0, 9))

flag = 0

while True:
    from time import sleep
    sleep(0.01)
    live_samples = np.vstack((live_samples, s.get_single_sample(with_timestamp=False)))
    #if len(live_samples) > 100:
    if flag < 100:
        flag += 1
    else:
        last100 = live_samples[-100:]
        mean_acc = np.mean(get_acc_component(last100))
        mean_gyr = np.mean(get_gyr_component(last100))
            #print str(mean_acc) + '\t' + str(mean_gyr)
            #print 'SHAPE>> ', question.shape
            #kprint 'QUESTION', question
        if mean_acc < 1 or mean_acc > 2 or abs(mean_gyr) > 9:
            flag = 0
            question = np.asarray(preprocess(last100))
            live_samples = np.ndarray((0, 9))
            p = clf.predict(question)
            print p
            from os import system
            if p == str(5):
                system('xdotool key j')
            if p == str(12):
                system('xdotool key k')
