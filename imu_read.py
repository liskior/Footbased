import sys
device = sys.argv[1]

import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = device
ser.open()
while True:
    print ser.readline() 
