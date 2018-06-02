import serial
ser = serial.Serial()
ser.baudrate = 38400
ser.port = '/dev/cu.HC-05-DevB-1'
ser.open()
while True:
    print ser.readline()
