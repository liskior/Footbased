# Don't forget to run this script with sudo.

# Exit if device is not connected.
ls /dev/ttyUSB* || exit

DEVICE=`ls /dev/ttyUSB*`

# The recording will be written here.
OUTPUT_FILE="/tmp/imu_recording `date`" 

# Start recording the raw data from the IMU sensor.
python imu_read.py $DEVICE >> $OUTPUT_FILE &
READ_PID=$!

# Wait for two seconds for the sensor to initialize itself.
sleep 2

for movement_id in `cat movements.txt`; do
    # Show human the movement to be recorded.
    mupdf "movements/$movement_id.pdf"
    echo "NOT RECORDING. Take your time to understand the movement."
    echo "Close the PDF reader to start recording. (Shortcut: q)"


    # Mark the beginning of the movement.
    echo "<$movement_id>" >> $OUTPUT_FILE

    # Show human the movement to be recorded again.
    # But this time, we are recording the data.
    # Note that "record" means "mark the beginning and the end".
    # We are actually recording the whole time.
    mupdf "movements/$movement_id.pdf"
    echo "RECORDING!"
    echo "Close the PDF reader to stop recording. (Shortcut: q)"

    # Mark the end of the movement.
    echo "</$movement_id>" >> $OUTPUT_FILE

# Stop reading raw data from the IMU.
kill $READ_PID
