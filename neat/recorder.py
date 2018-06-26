from random import shuffle
from os import system
from time import sleep
from time import strftime
from sensor import Sensor
from numpy import savetxt

MOVEMENTS = [
#    '01_FORWARD_SLIDE',
    '04_HEEL_RAISE',
    '12_PRONATION',
#    '21_SWEEP_OUTWARDS',
]
NUMBER_OF_REPETITIONS_PER_MOVEMENT = 25
SECONDS_PER_MOVEMENT = 1.0

to_be_recorded = MOVEMENTS * NUMBER_OF_REPETITIONS_PER_MOVEMENT
shuffle(to_be_recorded)

def init_sensor():
    sensor = Sensor()
    print 'Sensor getting ready...'
    samples = sensor.get_samples(SECONDS_PER_MOVEMENT)
    print 'Sensor ready.'
    sleep(1)

def record_one_movement(movement_name, recording_path):
    system('clear')
    print movement
    sleep(0.4) # Wait for the human to read the movement name.

    file_path = recording_path + '/'
    file_path += strftime('rec_' + movement_name + '_%y%m%d_%H%M%S') + '.txt'

    samples = sensor.get_samples(SECONDS_PER_MOVEMENT)
    savetxt(file_path, samples)

    print 'Recorded.'
    sleep(1)

def main(recording_path):
    init_sensor()
    for movement in to_be_recorded:
        record_one_movement(movement_name, recording_path)
