# -*- coding: UTF-8 -*-
""" Sensor proxy.

This module is responsible for communicating with the sensor. Usage:

from sensor import Sensor
s = Sensor()
s.get_single_sample() # Get one single sample (Acc & Mag & Gyr XYZ w/ timestamp)
s.get_samples(100) # Get 100 samples with 10ms in between.

This will not work unless the sensor is attached. Do not forget to give the
necessary permissions. You may either `sudo python this_script.py` or
`chmod 777 /dev/sensor` (Usually "/dev/ttyUSB0")

"""

from fnmatch import fnmatch
from os import listdir
from serial import Serial
from struct import unpack
from numpy import asarray
from os.path import lexists

SAMPLE_SIZE = 40 # in bytes

SEND_ONE_SAMPLE = '.'
BEGIN_SENDING = 'b'
STOP_SENDING = 's'

def find_device():
    possible_device_locations = [
        '/dev/tty.wchusbserial1410',
        '/dev/ttyUSB0',
        '/dev/ttyUSB1',
        '/dev/ttyUSB2',
    ]

    for candidate in possible_device_locations:
        if lexists(candidate):
            return candidate

    raise 'DEVICE NOT FOUND!'

class Sensor(object):

    def __init__(self, path_to_device=''):
        if path_to_device == '':
            path_to_device = find_device()

        self.ser = Serial(path_to_device, 115200, timeout=0.025)

        print 'Initializing the sensor...'

        # Wait till sensor starts returning values.
        while not self.get_single_sample(): pass

        # Wait till sensor starts returning values other than zero.
        sensor_data = 0
        while sensor_data == 0: sensor_data = sum(self.get_single_sample()[1])

        print 'Sensor initialized.'

    def __read_a_sample(self):
        return self.ser.read(SAMPLE_SIZE)

    def __unpack_raw_sample(self, raw_sample, with_timestamp=False):
        # Arduino's answer should be a byte array of size SAMPLE_SIZE.
        if len(raw_sample) != SAMPLE_SIZE:
            l = str(len(raw_sample))
            msg = 'ERROR: Unexpected number of bytes in sample: ' + l
            raise Exception(msg)

        # Convert raw bytes into four byte long floating point numbers.
        values = asarray(unpack('f' * 9, raw_sample[4:SAMPLE_SIZE]))

        if with_timestamp:
            timestamp = unpack('I', raw_sample[0:4])[0]
            return (timestamp, values)
        else:
            return values

    def get_single_sample(self, with_timestamp=True):
        # Just in case.
        self.ser.write(STOP_SENDING)

        # Tell Arduino to send a single sample.
        self.ser.write(SEND_ONE_SAMPLE)

        raw_sample = self.__read_a_sample()

        if not raw_sample:
            return None

        return self.__unpack_raw_sample(raw_sample, with_timestamp)

    def get_samples(self, number_of_samples):
        # Just in case.
        self.ser.write(STOP_SENDING)

        # Tell Arduino to begin sending samples.
        self.ser.write(BEGIN_SENDING)

        # Discard the first sample. (Initialization issues, I guess.)
        self.__read_a_sample()

        raw_samples = []
        for _ in range(0, number_of_samples):
            raw_samples.append(self.__read_a_sample())

        self.ser.write(STOP_SENDING)

        samples = []
        for raw_sample in raw_samples:
            samples.append(self.__unpack_raw_sample(raw_sample))
        #samples = map(lambda x: self.__unpack_raw_sample(x), raw_samples)

        return asarray(samples)
    
    def __del__(self):
        self.ser.close()
