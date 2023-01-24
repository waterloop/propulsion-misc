int val;
int encoder0PinA = 3;
int encoder0PinB = 2;
int encoder0Pos = 0;
int encoder0PinALast = LOW;
const int clicksPerRev = 400;
unsigned long startMillis = 0;  
unsigned long currentMillis = 0;
unsigned long rotationTime = 0;
int period = 0;
double revCount = 0;
double rpm = 0;
double Lvelocity = 0;
int n = LOW;

void setup() {
  pinMode (encoder0PinA, INPUT);
  pinMode (encoder0PinB, INPUT);
  Serial.begin (9600);
  Serial.println("Rotations/Minute,Time");
}

void loop() {
  n = digitalRead(encoder0PinA);
  if ((encoder0PinALast == LOW) && (n == HIGH)) {
    if (digitalRead(encoder0PinB) == LOW) {
      encoder0Pos--; //CCW
    } else {
      encoder0Pos++; //CW
    }
    
  }  
  currentMillis = millis(); 
  if (abs(encoder0Pos) == clicksPerRev) {  
    
    rotationTime = millis() - startMillis;
    rpm = 60000/rotationTime;
    //Lvelocity = (0.01595929068 * rpm);//this not so random number (0.0158) is (pi*diameter(meter))/60 ... the flywheel has a diameter of 12 inches so 0.3048 meters
    Lvelocity = (0.01529432024 * rpm);//diamter is 11.5 inches
    
    Serial.print(rpm);
    Serial.print(",");
//    Serial.println (rpm);
   // Serial.print("Meters/Second: ");
  //  Serial.println(Lvelocity);
    Serial.print(millis());
    Serial.println("");
    
    encoder0Pos = 0;
    startMillis = currentMillis; 
  }
  encoder0PinALast = n;
}
