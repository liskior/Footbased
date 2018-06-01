#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (10)

Adafruit_BNO055 bno = Adafruit_BNO055();

void setup(void)
{
  Serial.begin(115200);
  Serial.println("BEGIN");

  /* Initialise the sensor */
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }

  delay(1000);

  /* Display the current temperature */
  int8_t temp = bno.getTemp();
  Serial.print("Current Temperature: ");
  Serial.print(temp);
  Serial.println(" C");
  Serial.println("");

  bno.setExtCrystalUse(true);
}




// IT WAS COPY PASTE UP UNTIL HERE


void wait_until_whitespace() {
  BEGINNING:

  if (Serial.available()) {
    if (Serial.read() != ' ') goto BEGINNING;
  }
  else goto BEGINNING;

  Serial.println("RESUME");
}

void print_data(Adafruit_BNO055::adafruit_vector_type_t vector_type) {
  const int PRECISION = 4;
  imu::Vector<3> vec = bno.getVector(vector_type);
  Serial.print("\t"); Serial.print(vec.x(), PRECISION);
  Serial.print(","); Serial.print(vec.y(), PRECISION);
  Serial.print(","); Serial.print(vec.z(), PRECISION);
}

void loop(void)
{
  if (Serial.available()) {
    if (Serial.read() == 's') {
      Serial.println("PAUSE");
      wait_until_whitespace();
    }
  }

  Serial.print(micros());
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

  Serial.println("");
}
