""" Script to score classifiers.

Put all the training data into a single folder before running this script:
`mkdir /tmp/recall; cp ../recordings/rec*/*.txt /tmp/recall/`

Then record some testing data of your own into /tmp/test_data.

The script then outputs a confusion_matrix and how well different classifiers in
CLASSIFIERS do.

"""
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

data, target = extract_data_and_target_from_dir('/tmp/recall/')
#data, target = extract_data_and_target_from_dir('../raw_data/dataset5')
data2, target2 = extract_data_and_target_from_dir('/tmp/test_data/')

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

CLASSIFIERS = [
    ('SVC()', svm.SVC()),
    ('LinearSVC()', svm.LinearSVC()),
    ('KNeighborsClassifier(3)', KNeighborsClassifier(3)),
    ('SVC(kernel="linear"', SVC(kernel="linear", C=0.025)),
    ('SVC(gamma=2', SVC(gamma=2, C=1)),
    ('GaussianProcessClassifier(1.0 * RBF(1.0))', GaussianProcessClassifier(1.0 * RBF(1.0))),
    ('DecisionTreeClassifier(max_depth=5)', DecisionTreeClassifier(max_depth=5)),
    ('RandomForestClassifier(max_depth=5', RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)),
    ('RandomForestClassifier()', RandomForestClassifier()),
    ('MLPClassifier(alpha=1)', MLPClassifier(alpha=1)),
    ('AdaBoostClassifier()', AdaBoostClassifier()),
    ('GaussianNB()', GaussianNB()),
    ('Quadratic', QuadraticDiscriminantAnalysis()), 
]


scores_dict = { }

for name, classifier in CLASSIFIERS:
    classifier.fit(data, target)
    scores = cross_val_score(classifier, data, target, cv=5)
#    print name, scores
    scores_dict[name] = float(sum(scores)) / len(scores)

print '===================='

for item in scores_dict.items():
    print item[0], item[1]

print '===================='

classifier = GaussianNB()
classifier.fit(data, target)
from sklearn.metrics import confusion_matrix
print confusion_matrix(target2, classifier.predict(data2))

#print clf.score(data[-1].reshape(1, -1), target[-1].reshape(1, -1))

'''
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
'''
