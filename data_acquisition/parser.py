import numpy as np
import re
from pyparsing import nestedExpr


def parse(filepath):

    # f = open('/Users/asinitsyna/workspace/footbased/Footbased/raw_data/dataset1/rec_HEEL_RAISE_180620_011331', 'r')
    f = open(filepath, 'r')
    lines = f.read()

    text = re.sub('[^0-9\ \.\-]+', " ", lines)
    numbers = list(text.split())
    output = np.array(numbers)
    output = np.delete(output, np.arange(0, output.size, 10))
    print(output)


def parseNested(filepath):

    f = open(filepath, 'r')
    lines = f.read()

    text = '(' + re.sub('[^0-9\ \.\-\(\)]+', " ", lines) + ')'
    output = nestedExpr('(', ')').parseString(text).asList()
    for i in output:
        for j in i:
            j.remove(j[0])
    print(output)


parseNested("/Users/asinitsyna/workspace/footbased/Footbased/raw_data/dataset1/rec_HEEL_RAISE_180620_011331")