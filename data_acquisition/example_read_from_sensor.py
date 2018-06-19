# -*- coding: UTF-8 -*-

# Don't forget to sudo.

# In case of error, simply retrying sometimes solves the problem.

from sensor import Sensor

sensor = Sensor()

print sensor.get_a_data_point() # ONE-SHOT
print sensor.get_data_points(2) # CONTINUOUS (Read for two seconds)
