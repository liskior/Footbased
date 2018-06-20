from random import shuffle
from os import system
from time import sleep
from time import strftime
from sensor import Sensor

MOVEMENTS = [
    '01_FORWARD_SLIDE',
    '04_HEEL_RAISE',
    '12_PRONATION',
    '21_SWEEP_OUTWARDS',
]
NUMBER_OF_REPETITIONS_PER_MOVEMENT = 5
SECONDS_PER_MOVEMENT = 1.0
RECORDING_PATH = '../raw_data/'

to_be_recorded = MOVEMENTS * NUMBER_OF_REPETITIONS_PER_MOVEMENT
shuffle(to_be_recorded)

sensor = Sensor()

for movement in to_be_recorded:
    file_name = strftime('rec_' + movement + '_%y%m%d_%H%M%S')
    output_file = open(RECORDING_PATH + file_name,
 'wb')

    system('clear')
    print movement
    sleep(0.4) # Wait for the human to read the movement name.

    output_file.write(str(sensor.get_data_points(SECONDS_PER_MOVEMENT)) + '\n')
    
    output_file.close()

    print 'Recorded. Next move...'
    sleep(1)
