#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055();

struct xyz {
    float x, y, z;
};

// This struct should be 40 bytes long. (long and float are 4 bytes)
struct data_point {
    unsigned long time;
    struct xyz acc, mag, gyr;
};

// Serial.write() can either send a single byte or a byte array. This union
// enables me to send my data_point struct.
union data_point_with_accessible_bytes {
    struct data_point data;
    byte bytes[sizeof(struct data_point)];
};

void setup() {
    Serial.begin(115200);

    // Initialize the sensor - Comes from Adafruit's example.
    if(!bno.begin()) {
        Serial.print("Error: No BNO055 detected.");
        while(1);
    }
    bno.setExtCrystalUse(true); 
}

void copy(struct xyz target, imu::Vector<3> source) {
    target.x = source[0];
    target.y = source[1];
    target.z = source[2];
}

#define SEND_ONE_DATA_POINT '.'
#define BEGIN_SENDING 'b'
#define STOP_SENDING 's'

// Sampling period in microseconds.
#define PERIOD 10000

void send_one_data_point() {
    // Enforce the sampling period:
    static unsigned long previous_time = 0;
    unsigned long current_time = micros();
    while (current_time - previous_time < PERIOD) {
        // Active waiting is no good. What is the professional solution?
        current_time = micros();
    }
    previous_time = current_time;

    // Write sensor data to serial port:
    union data_point_with_accessible_bytes sample;
    sample.data.time = current_time;
    copy(sample.data.acc, bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER));
    copy(sample.data.mag, bno.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER));
    copy(sample.data.gyr, bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE));
    Serial.write(sample.bytes, 40);
}

char Sending = false;

void loop() {
    if (Serial.available()) {
        switch (Serial.read()) {
            case SEND_ONE_DATA_POINT: 
                send_one_data_point();
                break;
            case BEGIN_SENDING:
                Sending = true;
                break;
            case STOP_SENDING:
                Sending = false;
                break;
        }
    }
    else {
        if (Sending) {
            send_one_data_point();
        }
    }
}
