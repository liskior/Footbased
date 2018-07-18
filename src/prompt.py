MOVEMENTS = [
    'SUPINATION',
    'HEEL_RAISE',
    'TOE_RAISE',
    'PIVOT_ON_HEEL_OUTWARDS',
    'PIVOT_ON_HEEL_INWARDS',
    'FORWARD_SLIDE',
    'BACKWARD_SLIDE',
]

def prompt(text, path):
    from os import system
    system('date "+%H%M%S%Nprompted" >> ' + path)
    system('echo "' + text + '" >> ' + path)
    system('xcowsay --time 1 --cow-size=small --at=0,0 ' + text)

def start_new_file(path):
    from time import sleep
    from random import shuffle
    l = MOVEMENTS * 5
    shuffle(l)
    for movement in l:
        sleep(5)
        prompt(movement, path)


if __name__ == '__main__':
    from sys import argv
    from time import sleep
    start_new_file(argv[1])
