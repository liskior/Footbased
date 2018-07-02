import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numpy import loadtxt
from sensor import Sensor

HISTORY = 80

sensor = Sensor()

fig = plt.figure(figsize=(15, 5))
acc_plot = plt.subplot(1, 2, 1)
plt.title('Accelerometer')
gyr_plot = plt.subplot(1, 2, 2)
plt.title('Gyroscope')

timestamps = []
acc_x = []
acc_y = []
acc_z = []
gyr_x = []
gyr_y = []
gyr_z = []

def animate(interval):
    sample = sensor.get_single_sample()

    if not sample:
        return

    timestamp, values = sample

    global timestamps, gyr_x, gyr_y, gyr_z
    timestamps.append(float(timestamp) / 10 ** 6)

    acc_x.append(values[0])
    acc_y.append(values[1])
    acc_z.append(values[2])

    gyr_x.append(values[6])
    gyr_y.append(values[7])
    gyr_z.append(values[8])

    acc_plot.clear()
    acc_plot.plot(timestamps[-HISTORY:], acc_x[-HISTORY:])
    acc_plot.plot(timestamps[-HISTORY:], acc_y[-HISTORY:])
    acc_plot.plot(timestamps[-HISTORY:], acc_z[-HISTORY:])

    gyr_plot.clear()
    gyr_plot.plot(timestamps[-HISTORY:], gyr_x[-HISTORY:])
    gyr_plot.plot(timestamps[-HISTORY:], gyr_y[-HISTORY:])
    gyr_plot.plot(timestamps[-HISTORY:], gyr_z[-HISTORY:])

ani = animation.FuncAnimation(fig, animate, interval=40) # interval in ms
plt.show()
