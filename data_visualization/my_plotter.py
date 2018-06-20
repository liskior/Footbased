import matplotlib.pyplot as plt

def plot_array(x_array, y_array):
    plt.plot(x_array, y_array)
    plt.xlabel('Time (s)')

def plot_array_group(x_array, y_array_group, title=''):
    for array in y_array_group:
        assert(len(array) == len(x_array))

    if title != '':
        plt.title(title)

    for y_array in y_array_group:
        plt.plot(x_array, y_array)

def plot_array_groups(x_array, y_array_groups, titles=[]):
    if titles != []:
        assert(len(titles) == len(y_array_groups))

    for y_array_group in y_array_groups:
        for y_array in y_array_group:
            assert(len(y_array) == len(x_array))

    number_of_groups = len(y_array_groups)

    i = 1
    for y_array_group in y_array_groups:
        plt.subplot(1, number_of_groups, i)
        if titles != []:
            plt.title(titles[i - 1])
        plot_array_group(x_array, y_array_group)
        i += 1

def show():
    plt.show()

def set_xlabel(label):
    plt.xlabel(label)

def save_plot(png_file_name):
    plt.savefig(png_file_name)

def example_usage():
    DATA = [
        [
            [1,2], [2,4]
        ], 
        [
            [-10,2], [2,4]
        ], 
        [
            [-1,2], [2,4]
        ], 
    ]
    plot_array_groups([1,2], DATA, ['one', 'two', 'three'])
    set_xlabel('your label')
    show()
    plt.draw()

example_usage()

