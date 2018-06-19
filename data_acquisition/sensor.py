# -*- coding: UTF-8 -*-

from fnmatch import fnmatch
from os import listdir
from serial import Serial
from struct import unpack

DATA_POINT_SIZE = 40 # in bytes

SEND_ONE_DATA_POINT = '.'
BEGIN_SENDING = 'b'
STOP_SENDING = 's'

# Twelve bytes: Three float values for xyz coordinates, 4 bytes each.
def unpack_xyz(twelve_bytes):
    x = unpack('f', twelve_bytes[0:4])[0]
    y = unpack('f', twelve_bytes[4:8])[0]
    z = unpack('f', twelve_bytes[8:12])[0]
    return x, y, z

# Forty bytes: One timestamp (µs). xyz coordinates for accelerometer,
# magnetometer, and gyroscope. Each 4 bytes long. (1 + 3 x 3) x 4B = 40B
def unpack_data_point(forty_bytes):
    time = unpack('I', forty_bytes[0:4])[0]
    acc = unpack_xyz(forty_bytes[4:16])
    mag = unpack_xyz(forty_bytes[16:28])
    gyr = unpack_xyz(forty_bytes[28:40])

    # acc[0] is x-coordinate of acc. gyr[2] is z-coordinate of gyro. And so on.
    return time, acc, mag, gyr

class Sensor(object):

    def __init__(self):
        found_device = ''
        for device in listdir('/dev/'):
            if fnmatch(device, 'ttyUSB*'):
                found_device = device
        self.ser = Serial('/dev/' + found_device, 115200, timeout=0.1)

    def get_a_raw_sample(self):
        # Command Arduino to send one data point.
        self.ser.write(SEND_ONE_DATA_POINT)

        # Arduino's answer should be a byte array of size DATA_POINT_SIZE.
        raw_data = self.ser.read(DATA_POINT_SIZE)
    
        return raw_data


    def get_a_sample(self):
        # Command Arduino to send one data point.
        self.ser.write(SEND_ONE_DATA_POINT)

        # Arduino's answer should be a byte array of size DATA_POINT_SIZE.
        raw_data = self.ser.read(DATA_POINT_SIZE)

        if len(raw_data) != DATA_POINT_SIZE:
            raise Exception('ERROR: Unexpected data point size.')
        else:
            return unpack_data_point(raw_data)

    # Duration given in seconds.
    def get_data_points(self, duration):
        self.ser.read(DATA_POINT_SIZE) # Discard first data point.

        data_points = []
        self.ser.write(BEGIN_SENDING)
        for _ in range(0, int(duration * 100)): # 100 samples per second.
            data_point = self.ser.read(DATA_POINT_SIZE)
            if len(data_point) == DATA_POINT_SIZE:
                data_points.append(unpack_data_point(data_point))
        self.ser.write(STOP_SENDING)

        return data_points
    
    def __del__(self):
        self.ser.close()
