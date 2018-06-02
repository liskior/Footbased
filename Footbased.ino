#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <SoftwareSerial.h>// import the serial library

SoftwareSerial BlueTuth(10, 11); // RX, TX
int ledpin = 13; // led on D13 will show blink on / off
int BluetoothData; // the data given from Computer

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (10)

Adafruit_BNO055 bno = Adafruit_BNO055();

void setup(void)
{
  BlueTuth.begin(9600);
  BlueTuth.println("Bluetooth On");
  BlueTuth.println("BEGIN");

  /* Initialise the sensor */
  if (!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    BlueTuth.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

  delay(1000);

  /* Display the current temperature */
  int8_t temp = bno.getTemp();
  BlueTuth.print("Current Temperature: ");
  BlueTuth.print(temp);
  BlueTuth.println(" C");
  BlueTuth.println("");

  bno.setExtCrystalUse(true);
}




// IT WAS COPY PASTE UP UNTIL HERE


void wait_until_whitespace() {
BEGINNING:

  if (BlueTuth.available()) {
    if (BlueTuth.read() != 'b') goto BEGINNING;
  }
  else goto BEGINNING;

  BlueTuth.println("RESUME");
}

void print_data(Adafruit_BNO055::adafruit_vector_type_t vector_type) {
  const int PRECISION = 4;
  imu::Vector<3> vec = bno.getVector(vector_type);
  BlueTuth.print("\t"); BlueTuth.print(vec.x(), PRECISION);
  BlueTuth.print(","); BlueTuth.print(vec.y(), PRECISION);
  BlueTuth.print(","); BlueTuth.print(vec.z(), PRECISION);
}

void loop(void)
{
  if (BlueTuth.available()) {
    if (BlueTuth.read() == 's') {
      BlueTuth.println("PAUSE");
      wait_until_whitespace();
    }
  }

  BlueTuth.print(micros());
  print_data(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  print_data(Adafruit_BNO055::VECTOR_MAGNETOMETER );
  print_data(Adafruit_BNO055::VECTOR_GYROSCOPE    );

  // Each print_data takes about 3ms. So printing 9DOF takes about 10ms.
  // Which gives 1000ms/10ms=100Hz sampling rate.
  // Which is greater than Erik Pescara's "at least 80Hz".
  // So keep the following lines commented out to remain above 80Hz.
  // The problem is, samples are not very evenly spaced (in time).
  // Hopefully this will not be a problem.

  // print_data(Adafruit_BNO055::VECTOR_EULER        );
  // print_data(Adafruit_BNO055::VECTOR_LINEARACCEL  );
  // print_data(Adafruit_BNO055::VECTOR_GRAVITY      );

  BlueTuth.println("");
}
