# -*- coding: UTF-8 -*-

from fnmatch import fnmatch
from os import listdir
from serial import Serial
from struct import unpack
from numpy import asarray

SAMPLE_SIZE = 40 # in bytes

SEND_ONE_SAMPLE = '.'
BEGIN_SENDING = 'b'
STOP_SENDING = 's'

def find_device():
    device_name = ''
    for device in listdir('/dev/'):
        if fnmatch(device, 'ttyUSB*'):
            device_name = device
    if not device_name:
        raise 'DEVICE NOT FOUND!'
    return '/dev/' + device_name

class Sensor(object):

    def __init__(self, path_to_device=''):
        if path_to_device == '':
            path_to_device = find_device()

        self.ser = Serial(path_to_device, 115200, timeout=0.025)

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

    def get_single_sample(self):
        # Just in case.
        self.ser.write(STOP_SENDING)

        # Tell Arduino to send a single sample.
        self.ser.write(SEND_ONE_SAMPLE)

        raw_sample = self.__read_a_sample()

        if not raw_sample:
            return None

        return self.__unpack_raw_sample(raw_sample, with_timestamp=True)

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
