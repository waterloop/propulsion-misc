#include <Arduino.h>
#include <Wire.h>
#include <VL53L1X.h>

const uint8_t NUM_LIDAR = 2; // The number of LIDAR sensors in your system.

// The Arduino pins connected to the XSHUT pins of each sensor.
// Set to -1 if XSHUT pins are not used.
const int8_t X_SHUT_PINS[NUM_LIDAR] = { 21, 20 };

const uint8_t I2C_SDA = 8;
const uint8_t I2C_SCL = 9;

// The array to hold VL53L1X sensor objects.
VL53L1X sensors[NUM_LIDAR];

void setup() {
  Serial.begin(9600);
  //Serial.println("test2");
  Wire.begin(I2C_SDA, I2C_SCL);
  Wire.setClock(400000); // use 400 kHz I2C

pinMode(4, OUTPUT);
  

  // Disable/reset all sensors by driving their XSHUT pins low, if used.
  for (uint8_t i = 0; i < NUM_LIDAR; i++) {
    if (X_SHUT_PINS[i] >= 0) { // Check if XSHUT pin is used for this sensor.
      pinMode(X_SHUT_PINS[i], OUTPUT);
      digitalWrite(X_SHUT_PINS[i], LOW);
    }
  }

  // Enable, initialize, and start each sensor, one by one.
  for (uint8_t i = 0; i < NUM_LIDAR; i++) {
    if (X_SHUT_PINS[i] >= 0) { // Check if XSHUT pin is used for this sensor.
      // Stop driving this sensor's XSHUT low. This should allow the carrier
      // board to pull it high. (We do NOT want to drive XSHUT high since it is
      // not level shifted.) Then wait a bit for the sensor to start up.
      pinMode(X_SHUT_PINS[i], INPUT);
      delay(10);
    }

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
  //Serial.println("test2");
  for (uint8_t i = 0; i < 1; i++) {
    uint16_t distance = sensors[i].read();
    Serial.print("Sensor ");
    Serial.print(i+1);
    Serial.print(": ");
    Serial.print(distance);
    Serial.print(" mm \t");
    analogWriteResolution(8);
    analogWrite(4, distance/2);
  }
  Serial.println();
  delay(100);
}