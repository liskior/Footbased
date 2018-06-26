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

data, target = extract_data_and_target_from_dir('../raw_data/dataset3/')

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(data, target)

from sensor import Sensor
s = Sensor()
while not s.get_single_sample(): pass
from time import sleep
print 'Get ready'
sleep(1)
print 'Go!'
sleep(.4)
samples = s.get_samples(100)

from preprocessor import preprocess
print clf.predict(preprocess(samples))

from async_plotter import plot_to_new_window
plot_to_new_window(samples)
