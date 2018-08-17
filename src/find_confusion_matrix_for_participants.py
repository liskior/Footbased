""" Go to find_confusion_matrix_for_participants___ENCODED.py

This does not work.

"""

participant3 = [
    ('SUPINATION', 'SUPINATION'),
    ('FORWARD_SLIDE', 'SUPINATION'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'SUPINATION'),
    ('PIVOT_ON_HEEL_INWARDS', 'SUPINATION'),
    ('TOE_RAISE', 'BACKWARD_SLIDE'),
    ('HEEL_RAISE', 'FORWARD_SLIDE'),
    ('BACKWARD_SLIDE', 'SUPINATION'),
    ('BACKWARD_SLIDE', 'FORWARD_SLIDE'),
    ('HEEL_RAISE', 'FORWARD_SLIDE'),
    ('PIVOT_ON_HEEL_INWARDS', 'SUPINATION'),
    ('HEEL_RAISE', 'SUPINATION'),
    ('FORWARD_SLIDE', 'PRONATION'),
    ('FORWARD_SLIDE', 'SUPINATION'),
    ('PIVOT_ON_HEEL_INWARDS', 'SUPINATION'),
    ('PIVOT_ON_HEEL_INWARDS', 'SUPINATION'),
    ('TOE_RAISE', 'PRONATION'),
    ('BACKWARD_SLIDE', 'SUPINATION'),
    ('SUPINATION', 'SUPINATION'),
    ('TOE_RAISE', 'SUPINATION'),
    ('FORWARD_SLIDE', 'BACKWARD_SLIDE'),
    ('HEEL_RAISE', 'FORWARD_SLIDE'),
    ('PIVOT_ON_HEEL_INWARDS', 'TOE_RAISE'),
    ('SUPINATION', 'SUPINATION'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'PIVOT_ON_HEEL_OUTWARDS'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'SUPINATION'),
    ('BACKWARD_SLIDE', 'SUPINATION'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'SUPINATION'),
    ('TOE_RAISE', 'SUPINATION'),
    ('HEEL_RAISE', 'FORWARD_SLIDE'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'PIVOT_ON_HEEL_OUTWARDS'),
    ('SUPINATION', 'SUPINATION'),
]

participant4 = [
    ('FORWARD_SLIDE', 'BACKWARD_SLIDE'),
    ('FORWARD_SLIDE', 'BACKWARD_SLIDE'),
    ('SUPINATION', 'BACKWARD_SLIDE'),
    ('SUPINATION', 'SUPINATION'),
    ('TOE_RAISE', 'BACKWARD_SLIDE'),
    ('BACKWARD_SLIDE', 'FORWARD_SLIDE'),
    ('FORWARD_SLIDE', 'BACKWARD_SLIDE'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'FORWARD_SLIDE'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'FORWARD_SLIDE'),
    ('HEEL_RAISE', 'HEEL_RAISE'),
    ('HEEL_RAISE', 'BACKWARD_SLIDE'),
    ('TOE_RAISE', 'BACKWARD_SLIDE'),
    ('SUPINATION', 'SUPINATION'),
    ('TOE_RAISE', 'BACKWARD_SLIDE'),
    ('BACKWARD_SLIDE', 'BACKWARD_SLIDE'),
    ('HEEL_RAISE', 'FORWARD_SLIDE'),
    ('BACKWARD_SLIDE', 'BACKWARD_SLIDE'),
    ('FORWARD_SLIDE', 'FORWARD_SLIDE'),
    ('SUPINATION', 'SUPINATION'),
    ('SUPINATION', 'SUPINATION'),
    ('HEEL_RAISE', 'FORWARD_SLIDE'),
    ('PIVOT_ON_HEEL_INWARDS', 'BACKWARD_SLIDE'),
    ('TOE_RAISE', 'BACKWARD_SLIDE'),
    ('PIVOT_ON_HEEL_INWARDS', 'BACKWARD_SLIDE'),
    ('TOE_RAISE', 'BACKWARD_SLIDE'),
    ('PIVOT_ON_HEEL_INWARDS', 'BACKWARD_SLIDE'),
    ('BACKWARD_SLIDE', 'FORWARD_SLIDE'),
    ('PIVOT_ON_HEEL_INWARDS', 'PIVOT_ON_HEEL_OUTWARDS'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'PIVOT_ON_HEEL_OUTWARDS'),
    ('HEEL_RAISE', 'FORWARD_SLIDE'),
    ('BACKWARD_SLIDE', 'BACKWARD_SLIDE'),
]

participant5 = [
    ('FORWARD_SLIDE', 'HEEL_RAISE'),
    ('PIVOT_ON_HEEL_INWARDS', 'TOE_RAISE'),
    ('FORWARD_SLIDE', 'PIVOT_ON_HEEL_INWARDS'),
    ('HEEL_RAISE', 'HEEL_RAISE'),
    ('BACKWARD_SLIDE', 'FORWARD_SLIDE'),
    ('SUPINATION', 'SUPINATION'),
    ('BACKWARD_SLIDE', 'FORWARD_SLIDE'),
    ('BACKWARD_SLIDE', 'FORWARD_SLIDE'),
    ('BACKWARD_SLIDE', 'FORWARD_SLIDE'),
    ('SUPINATION', 'SUPINATION'),
    ('FORWARD_SLIDE', 'HEEL_RAISE'),
    ('FORWARD_SLIDE', 'FORWARD_SLIDE'),
    ('BACKWARD_SLIDE', 'FORWARD_SLIDE'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'PIVOT_ON_HEEL_OUTWARDS'),
    ('TOE_RAISE', 'BACKWARD_SLIDE'),
    ('HEEL_RAISE', 'HEEL_RAISE'),
    ('TOE_RAISE', 'FORWARD_SLIDE'),
    ('TOE_RAISE', 'HEEL_RAISE'),
    ('SUPINATION', 'SUPINATION'),
    ('PIVOT_ON_HEEL_INWARDS', 'PIVOT_ON_HEEL_INWARDS'),
    ('HEEL_RAISE', 'FORWARD_SLIDE'),
    ('TOE_RAISE', 'FORWARD_SLIDE'),
    ('PIVOT_ON_HEEL_INWARDS', 'PRONATION'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'PIVOT_ON_HEEL_OUTWARDS'),
    ('FORWARD_SLIDE', 'HEEL_RAISE'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'PIVOT_ON_HEEL_OUTWARDS'),
    ('SUPINATION', 'SUPINATION'),
    ('TOE_RAISE', 'TOE_RAISE'),
    ('HEEL_RAISE', 'HEEL_RAISE'),
    ('PIVOT_ON_HEEL_OUTWARDS', 'PIVOT_ON_HEEL_OUTWARDS'),
    ('HEEL_RAISE', 'HEEL_RAISE'),
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


'''
The matrix axes:
0 BACKWARD_SLIDE
1 FORWARD_SLIDE
2 HEEL_RAISE
3 PIVOT_ON_HEEL_INWARDS
4 PIVOT_ON_HEEL_OUTWARDS
5 PRONATION
6 SUPINATION
7 TOE_RAISE
Row sum = How many times a movement was prompted
Column sum = How many times a movement was predicted
'''

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

