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
from mapping import Mapping
m = Mapping()


from sys import stdout

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
            if final_answer == 'SUPINATION': m.open_list(0)
            elif final_answer == 'HEEL_RAISE': m.click(2)
            elif final_answer == 'TOE_RAISE': m.click(1)
            elif final_answer == 'PIVOT_ON_HEEL_OUTWARDS': m.next()
            elif final_answer == 'PIVOT_ON_HEEL_INWARDS':
                m.next()
                m.next()
            elif final_answer == 'FORWARD_SLIDE': m.choose(2)
            elif final_answer == 'BACKWARD_SLIDE': m.choose(1)
