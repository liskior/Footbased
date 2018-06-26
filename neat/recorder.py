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

SAMPLES_PER_MOVEMENT = 100

def init_sensor():
    global sensor
    sensor = Sensor()
    print 'Sensor getting ready...'
    samples = sensor.get_single_sample()
    samples = sensor.get_single_sample()
    print 'Sensor ready.'
    sleep(1)

def record_one_movement(movement_name, recording_path):
    global sensor

    system('clear')
    print movement_name
    sleep(0.4) # Wait for the human to read the movement name.

    file_path = recording_path + '/'
    file_path += strftime('rec_' + movement_name + '_%y%m%d_%H%M%S') + '.txt'

    samples = sensor.get_samples(SAMPLES_PER_MOVEMENT)
    savetxt(file_path, samples)

    print 'Recorded.'
    sleep(1)

def start_recording(recording_path):
    NUMBER_OF_REPETITIONS_PER_MOVEMENT = 25

    to_be_recorded = MOVEMENTS * NUMBER_OF_REPETITIONS_PER_MOVEMENT
    shuffle(to_be_recorded)

    init_sensor()
    for movement in to_be_recorded:
        print movement
        record_one_movement(movement, recording_path)
