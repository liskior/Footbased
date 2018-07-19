import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
objects = (
'Gaussian\nProcess',
'MLP',
'AdaBoost',
'LinearSVC',
'KNeighbors\n(K=3)',
'Quadratic',
'SVC',
'SVC\n(gamma=2)',
'Random\nForest (d=5)',
'SVC\n(linear)',
'Decision\nTree',
'Random\nForest',
'GaussianNB',
)
performance = [
4,
37,
56,
57,
63,
65,
65,
65,
70,
73,
76,
83,
87,
]

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# GLOBAL CONSTANTS
testNames = objects
#testMeta = dict(zip(testNames, ['laps', 'sec', 'min:sec', 'sec', '']))


def plot_student_results(student, scores):
    #  create the figure
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('')

    pos = np.arange(len(testNames))

    rects = ax1.barh(pos, [scores[k] for k in testNames],
                     align='center',
                     height=0.5, color='m',
                     tick_label=testNames)

    ax1.set_title('Classifier accuracy comparison')

    ax1.set_xlim([0, 100])
    ax1.xaxis.set_major_locator(MaxNLocator(11))
    ax1.xaxis.grid(True, linestyle='--', which='major',
                   color='grey', alpha=.25)

    # set X-axis tick marks at the deciles
    cohort_label = ax1.text(.5, -.07, ''.format(cohort_size),
                            horizontalalignment='center', size='small',
                            transform=ax1.transAxes)

    rect_labels = []
    # Lastly, write in the ranking inside each bar to aid in interpretation
    for rect in rects:
        # Rectangle widths are already integer-valued but are floating
        # type, so it helps to remove the trailing decimal point and 0 by
        # converting width to int type
        width = int(rect.get_width())

        rankStr = width
        # The bars aren't wide enough to print the ranking inside
        if (width < 5):
            # Shift the text to the right side of the right edge
            xloc = width + 1
            # Black against white background
            clr = 'black'
            align = 'left'
        else:
            # Shift the text to the left side of the right edge
            xloc = 0.98*width
            # White on magenta
            clr = 'white'
            align = 'right'

        # Center the text vertically in the bar
        yloc = rect.get_y() + rect.get_height()/2.0
        label = ax1.text(xloc, yloc, rankStr, horizontalalignment=align,
                         verticalalignment='center', color=clr, weight='bold',
                         clip_on=True)
        rect_labels.append(label)

    # make the interactive mouse over give the bar title
    return {'fig': fig,
            'ax': ax1,
            'bars': rects,
            'perc_labels': rect_labels,
            }

student = ('Classifier accuracy', 2, 'boy')
scores = dict(zip(testNames, performance))
print scores
cohort_size = 62  # The number of other 2nd grade boys

arts = plot_student_results(student, scores)
plt.show()
