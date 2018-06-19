from random import shuffle
from os import system
from time import sleep

MOVEMENTS = ['TOE RAISE', 'HEEL RAISE']
TIMES_PER_MOVEMENT = 5

to_be_recorded = MOVEMENTS * TIMES_PER_MOVEMENT
shuffle(to_be_recorded)

for movement in to_be_recorded:
    system('echo "("' + movement + ' >> /tmp/current_recording.txt')
    system('clear')
    print movement
    for i in range(5, 0, -1):
        print i 
        sleep(1)
    system('echo ' + movement + ' ")" >> /tmp/current_recording.txt')
    print 'Recorded. Next move...'
    sleep(2)
