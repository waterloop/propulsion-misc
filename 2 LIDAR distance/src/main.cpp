#include <Arduino.h>
#include <Wire.h>
#include <VL53L1X.h>

/*CONNECT PINS for every LIDAR AS BELOW:
Vin to 3.3V
GND to GND
SCL to G22
SDA to G21
XSHUT seperatly for each LIDAR to each pin as outlined below
*/

// The Arduino pins connected to the XSHUT pins of each sensor.
const uint8_t xshutPins[sensorCount] = { 18, 19 };


// The number of sensors in your system.
const uint8_t sensorCount = 2;

VL53L1X sensors[sensorCount];

void setup() {
  Serial.begin(9600);
  Wire.begin();
  Wire.setClock(400000); // use 400 kHz I2C

  // Disable/reset all sensors by driving their XSHUT pins low.
  for (uint8_t i = 0; i < sensorCount; i++) {
    pinMode(xshutPins[i], OUTPUT);
    digitalWrite(xshutPins[i], LOW);
  }

  // Enable, initialize, and start each sensor, one by one.
  for (uint8_t i = 0; i < sensorCount; i++) {
    // Stop driving this sensor's XSHUT low. This should allow the carrier
    // board to pull it high. (We do NOT want to drive XSHUT high since it is
    // not level shifted.) Then wait a bit for the sensor to start up.
    pinMode(xshutPins[i], INPUT);
    delay(10);

    sensors[i].setTimeout(500);
    if (!sensors[i].init()) {
      Serial.print("Failed to detect and initialize sensor ");
      Serial.println(i);
      while (1);
    }

    // Each sensor must have its address changed to a unique value other than
    // the default of 0x29 (except for the last one, which could be left at
    // the default). To make it simple, we'll just count up from 0x2A.
    sensors[i].setAddress(0x2A + i);

    sensors[i].startContinuous(50);
  }
}

void loop() {
  // Read from each sensor and print the distance.
  for (uint8_t i = 0; i < sensorCount; i++) {
    uint16_t distance = sensors[i].read();
    Serial.print("Sensor ");
    Serial.print(i+1);
    Serial.print(": ");
    Serial.print(distance);
    Serial.print(" mm \t");
  }
  Serial.println();
  delay(100);
}

