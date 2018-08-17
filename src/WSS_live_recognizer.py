""" Maps predicted movements to workspace switching.

Works only on Linux, if `wmctrl` is present.

This script is essentially a copy DEP_live_recognizer.py, but it switches
workspaces instead of executing actions on a dashboard.

"""

MOVEMENTS = {
    '1': 'FORWARD_SLIDE',
    '2': 'BACKWARD_SLIDE',
    '4': 'HEEL_RAISE',
    '5': 'TOE_RAISE', '11': 'SUPINATION',
    '12': 'PRONATION',
    '19': 'PIVOT_ON_HEEL_INWARDS',
    '20': 'PIVOT_ON_HEEL_OUTWARDS',
}

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

# The user has to wait for one second so we have at least 100 samples.
print 'Wait for one second...'
for _ in range(100):
    sleep(0.01)
    single_sample = s.get_single_sample(with_timestamp=False)
    live_samples = np.vstack((live_samples, single_sample))

THRESHOLD = 15
predict = 0 # samples
last_predictions = []

from collections import Counter

from sys import stdout

ws_horiz = 0
ws_vert = 0

def switch_ws(hor, ver):
    from os import system
    system('wmctrl -o ' + str(hor * 2000) + ',' + str(ver * 2000))

while True:
    from time import sleep
    sleep(0.01)
    single_sample = s.get_single_sample(with_timestamp=False)
    live_samples = np.vstack((live_samples, single_sample))
    last100 = live_samples[-100:]
    if sum(single_sample[6:9]) > THRESHOLD:
        predict = 60
        last_predictions = []
    if predict > 0:
        predict -= 1
    if 20 > predict > 0:
        predict -= 1
        question = np.asarray(preprocess(last100))
        p = str(clf.predict(question)).rstrip('\']').lstrip('[\'')
        last_predictions.append(MOVEMENTS[p])

        if predict == 0:
            final_answer = Counter(last_predictions).most_common(1)[0][0]
            print final_answer
            from os import system
            if final_answer in ('HEEL_RAISE', 'TOE_RAISE', 'FORWARD_SLIDE', 'BACKWARD_SLIDE'):
                print 'VERTICAL'
                ws_vert ^= 1
                switch_ws(ws_horiz, ws_vert)
            if final_answer in ('PIVOT_ON_HEEL_OUTWARDS', 'PIVOT_ON_HEEL_INWARDS', 'SUPINATION', 'PRONATION'):
                print 'HORIZONTAL'
                ws_horiz ^= 1
                switch_ws(ws_horiz, ws_vert)
