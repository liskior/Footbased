# -*- coding: UTF-8 -*-

from serial import Serial
from struct import unpack

ser = Serial('/dev/ttyUSB3', 115200, timeout=0.1)

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

SEND_ONE_DATA_POINT = '.'
BEGIN_SENDING = 'b'
STOP_SENDING = 's'

# ONE-SHOT:
ser.write(SEND_ONE_DATA_POINT)
print unpack_data_point(ser.read(40))

from time import sleep
sleep(2)

# CONTINUOUS:
ser.write(BEGIN_SENDING)
for _ in range(1, 300):
    data_point = ser.read(40)
    if len(data_point) == 40:
        print unpack_data_point(data_point)
ser.write(STOP_SENDING)

ser.close()
