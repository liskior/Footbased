import matplotlib.pyplot as plt

def __plot(samples):
    # window size
    plt.figure(figsize=(15, 5))

    # blue is x, green is y, red is z

    x_axis = range(0, samples.shape[0])

    plt.subplot(1, 3, 1)
    plt.title('Accelerometer')
    plt.xlabel('Time (s)')
    plt.plot(x_axis, samples[:, 0])
    plt.plot(x_axis, samples[:, 1])
    plt.plot(x_axis, samples[:, 2])

    plt.subplot(1, 3, 2)
    plt.title('Magnetometer')
    plt.xlabel('Time (s)')
    plt.plot(x_axis, samples[:, 3])
    plt.plot(x_axis, samples[:, 4])
    plt.plot(x_axis, samples[:, 5])

    plt.subplot(1, 3, 3)
    plt.title('Gyrometer')
    plt.xlabel('Time (s)')
    plt.plot(x_axis, samples[:, 6])
    plt.plot(x_axis, samples[:, 7])
    plt.plot(x_axis, samples[:, 8])

def plot_to_new_window(samples):
    __plot(samples)
    plt.show()

def plot_to_png(samples, filename):
    assert(filename.endswith('.png'))
    __plot(samples)
    plt.savefig(filename)
