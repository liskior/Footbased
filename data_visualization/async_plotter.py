import matplotlib
import matplotlib.pyplot as plt
from sys import argv

input_file = open(argv[1], 'r')
data_points = eval(input_file.readline())

data_arrays = [] # First one is for time. See output of parse_input.
for _ in range(0, 10):
    data_arrays.append([])

for time, acc, mag, gyr in data_points:
    data_arrays[0].append((time - data_points[0][0]) / 1000000.)
    data_arrays[1].append(acc[0])
    data_arrays[2].append(acc[1])
    data_arrays[3].append(acc[2])
    data_arrays[4].append(mag[0])
    data_arrays[5].append(mag[1])
    data_arrays[6].append(mag[2])
    data_arrays[7].append(gyr[0])
    data_arrays[8].append(gyr[1])
    data_arrays[9].append(gyr[2])

# window size
plt.figure(figsize=(15, 5))

# blue is x, green is y, red is z

plt.subplot(1, 3, 1)
plt.plot(data_arrays[0], data_arrays[1])
plt.plot(data_arrays[0], data_arrays[2])
plt.plot(data_arrays[0], data_arrays[3])
plt.title('Accelerometer')
plt.xlabel('Time (s)')

plt.subplot(1, 3, 2)
plt.plot(data_arrays[0], data_arrays[4])
plt.plot(data_arrays[0], data_arrays[5])
plt.plot(data_arrays[0], data_arrays[6])
plt.title('Magnetometer')
plt.xlabel('Time (s)')

plt.subplot(1, 3, 3)
plt.plot(data_arrays[0], data_arrays[7])
plt.plot(data_arrays[0], data_arrays[8])
plt.plot(data_arrays[0], data_arrays[9])
plt.title('Gyrometer')
plt.xlabel('Time (s)')

plt.show()

input_file.close()
