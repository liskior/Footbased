Put foot into neutral position.

Run the following command:

sudo python imu_read.py > "`date`"

Then do the foot movement.

Press CTRL+C.

The recording is written in a file named like a date.

One sample looks like this:
1002228972	0.4200,0.6500,-9.9400	-21.0625,18.7500,37.1875	-0.0625,-0.1250,0.0625

Format:

Microseconds
tab
accelerometer x
,
accelerometer y
,
accelerometer z
tab
magnetometer x
,
magnetometer y
,
magnetometer z
tab
gyroscope x
,
gyroscope y
,
gyroscope z


See also page 14 from:
https://cdn-learn.adafruit.com/downloads/pdf/adafruit-bno055-absolute-orientation-sensor.pdf


<![schema](img/Footbased.png)
