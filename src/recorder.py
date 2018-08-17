""" Records training data.

We used this to record training data. This needs two command line arguments.
First argument is the directory to save the data. Second argument is the file
name. Note that since a new file will be created for each movement, the date and
the name of the movement is going to be appended to the provided file name,
along with a txt extension.

"""


from random import shuffle
from os import system
from time import sleep
from time import strftime
from sensor import Sensor
from numpy import savetxt
from sys import argv

MOVEMENTS = [
    '01_FORWARD_SLIDE',
    '02_BACKWARD_SLIDE',
    '04_HEEL_RAISE',
    '05_TOE_RAISE',
    '11_SUPINATION',
    '12_PRONATION',
    '19_PIVOT_ON_HEEL_INWARDS',
    '20_PIVOT_ON_HEEL_OUTWARDS',
]

SAMPLES_PER_MOVEMENT = 100

def init_sensor():
    global sensor
    sensor = Sensor()
    print 'Sensor getting ready...'
    while not sensor.get_single_sample(): pass
    print 'Sensor ready.'
    sleep(1)

def record_one_movement(movement_name, recording_path, recording_name=''):
    global sensor

    system('clear')
    print movement_name

    #sleep(0.4) # Wait for the human to read the movement name.
    print 'Press enter to start recording.'
    raw_input()

    file_path = recording_path + '/'
    file_path += strftime('rec_' +  '_' + movement_name +
            '_%y%m%d_%H%M%S') + recording_name + '.txt'

    samples = sensor.get_samples(SAMPLES_PER_MOVEMENT)
    import async_plotter 
    async_plotter.plot_to_new_window(samples)
    print 'Press enter to save the recording. Press space then enter to discard.'
    if raw_input():
        print 'Discarded.'
        print 'Try again.'
        sleep(1)
        record_one_movement(movement_name, recording_path, recording_name)
    else:
        savetxt(file_path, samples)
        print 'Recorded.'
    sleep(1)

def start_recording(recording_path, recording_name=''):
    NUMBER_OF_REPETITIONS_PER_MOVEMENT = 10

    to_be_recorded = MOVEMENTS * NUMBER_OF_REPETITIONS_PER_MOVEMENT
    shuffle(to_be_recorded)

    init_sensor()
    for movement in to_be_recorded:
        print movement
        record_one_movement(movement, recording_path, recording_name)

if __name__ == '__main__':
    if len(argv) >= 3: name = argv[2]
    start_recording(argv[1], name)
