""" With this script we generated the confusion matrix we used in the
presentation and the final document.

This is basically find_confusion_matrix_for_participants.py. The difference is;
English movement names are encoded (hence the name of this file) into integers,
so that the code we found on stackoverflow.com can plot.

"""

participant3 = [
    ('111', '111'),
    ('66', '111'),
    ('44', '111'),
    ('55', '111'),
    ('33', '77'),
    ('22', '66'),
    ('77', '111'),
    ('77', '66'),
    ('22', '66'),
    ('55', '111'),
    ('22', '111'),
    ('66', '88'),
    ('66', '111'),
    ('55', '111'),
    ('55', '111'),
    ('33', '88'),
    ('77', '111'),
    ('111', '111'),
    ('33', '111'),
    ('66', '77'),
    ('22', '66'),
    ('55', '33'),
    ('111', '111'),
    ('44', '44'),
    ('44', '111'),
    ('77', '111'),
    ('44', '111'),
    ('33', '111'),
    ('22', '66'),
    ('44', '44'),
    ('111', '111'),
]

participant4 = [
    ('66', '77'),
    ('66', '77'),
    ('111', '77'),
    ('111', '111'),
    ('33', '77'),
    ('77', '66'),
    ('66', '77'),
    ('44', '66'),
    ('44', '66'),
    ('22', '22'),
    ('22', '77'),
    ('33', '77'),
    ('111', '111'),
    ('33', '77'),
    ('77', '77'),
    ('22', '66'),
    ('77', '77'),
    ('66', '66'),
    ('111', '111'),
    ('111', '111'),
    ('22', '66'),
    ('55', '77'),
    ('33', '77'),
    ('55', '77'),
    ('33', '77'),
    ('55', '77'),
    ('77', '66'),
    ('55', '44'),
    ('44', '44'),
    ('22', '66'),
    ('77', '77'),
]

participant5 = [
    ('66', '22'),
    ('55', '33'),
    ('66', '55'),
    ('22', '22'),
    ('77', '66'),
    ('111', '111'),
    ('77', '66'),
    ('77', '66'),
    ('77', '66'),
    ('111', '111'),
    ('66', '22'),
    ('66', '66'),
    ('77', '66'),
    ('44', '44'),
    ('33', '77'),
    ('22', '22'),
    ('33', '66'),
    ('33', '22'),
    ('111', '111'),
    ('55', '55'),
    ('22', '66'),
    ('33', '66'),
    ('55', '88'),
    ('44', '44'),
    ('66', '22'),
    ('44', '44'),
    ('111', '111'),
    ('33', '33'),
    ('22', '22'),
    ('44', '44'),
    ('22', '22'),
]

PARTICIPANTS = participant3, participant4, participant5

from sklearn.metrics import confusion_matrix

#### ALL DATA ##################################################################

prompts = []
predicts = []

for participant in PARTICIPANTS:
    for prompt, predict in participant:
        predicts.append(predict)
        prompts.append(prompt)

cm_all = confusion_matrix(prompts, predicts)
print cm_all

#### FIRST HALF ################################################################

prompts = []
predicts = []

for participant in PARTICIPANTS:
    middle = len(participant) / 2
    firsthalf = participant[:middle]
    for prompt, predict in firsthalf:
        predicts.append(predict)
        prompts.append(prompt)

cm1 = confusion_matrix(prompts, predicts)
print cm1

### SECOND HALF ################################################################

prompts = []
predicts = []

for participant in PARTICIPANTS:
    middle = len(participant) / 2
    secondhalf = participant[middle:]
    for prompt, predict in secondhalf:
        predicts.append(predict)
        prompts.append(prompt)

cm2 = confusion_matrix(prompts, predicts)
print cm2



def colormap(input_matrix):
    import numpy as np
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    intersection_matrix = input_matrix

    ax.matshow(intersection_matrix, cmap=plt.cm.Blues)

    for i in xrange(8):
        for j in xrange(8):
            c = intersection_matrix[j,i]
            ax.text(i, j, str(c), va='center', ha='center')
    intersection_matrix = input_matrix

    ax.matshow(intersection_matrix, cmap=plt.cm.Blues)

    for i in xrange(8):
        for j in xrange(8):
            c = intersection_matrix[j,i]
            ax.text(i, j, str(c), va='center', ha='center')

    plt.show()

colormap(cm_all)
#colormap(cm1)
#colormap(cm2)

