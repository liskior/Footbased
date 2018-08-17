""" Control the mouse with foot.

This is a simple controller that uses the sensor data to move the cursor. It
does not have anything to do with the machine learning system. Since we already
had the hardware, we took the extra time to implement this as well.

The values are adjusted to provide a more natural feel.

"""

from sensor import Sensor
from pymouse import PyMouse
from os.path import isfile


s = Sensor()
m = PyMouse()

# init sensor
while not s.get_single_sample(): pass

m.move(10000, 10000)
x, y = m.position()
m.move(x / 2, y / 2)

X_THRESHOLD = 2.
Y_THRESHOLD = 3.

def convert(raw_value, threshold):
    PARAM = 1.5
    PARAM2 = 1.5
    if threshold < val < 2 * threshold:
        return val - threshold
    return val

while not isfile('/tmp/stop'):
    sample = s.get_single_sample()[1]

    #y = y * 0.96 + 0.04 * (sample[0] - 1.0) * (1079 / 4.0)

    x = m.position()[0]
    val = sample[8]
    if abs(val) > X_THRESHOLD:
        x -= convert(val, X_THRESHOLD)

    if str(x) == 'nan': continue

    y = m.position()[1]
    val = sample[7]
    if abs(val) > Y_THRESHOLD:
        y -= convert(val, Y_THRESHOLD)

    if abs(val) > 150:
        x,y  = m.position()
        m.click(x, y)
    
    if str(y) == 'nan': continue

    m.move(x, y)
