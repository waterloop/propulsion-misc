#include "HX711.h"

HX711 scale;
x
void setup() {
Serial.begin(9600);
scale.begin(3, 2); // Set the DT and SCK pins
//scale.set_scale(1); // Set the calibration factor
scale.tare(); // Reset the scale to 0
}

void loop() {
if (scale.is_ready()) {
    long reading = scale.read();
    Serial.print("HX711 reading: ");
    Serial.println(reading);
  } else {
    Serial.println("HX711 not found.");
  }

  delay(100);
}
