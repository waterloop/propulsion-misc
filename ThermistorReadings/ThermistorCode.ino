// Waterloop Thermistor Code

//These values are in the datasheet
#define RT0 100000   // 100KΩ
#define B 4334   // K for 85-100C range
//--------------------------------------
#define VCC 5    //Supply voltage
#define R 6800  //R=6.8KΩ --> Necessary known initial resistance value
#define T0 298.15
// Globals

// 5 voltage reads, for 4 thermistors
float V[5] = {0.0, 0.0, 0.0, 0.0, 0.0};

void setup() {
  // Setting the baud rate
  Serial.begin(9600); 

  // printing out the log header
  for(int i = 0; i< 4; ++i)
  {
    Serial.print("Therm"); Serial.print(i+1); Serial.print(",");  
  }
  
  Serial.print("\n");
}

void loop() {  
  // Collecting voltage readings
  for(int i = 0; i < 5; ++i)
  {
    V[i] = (VCC/1023.000) * analogRead(i);
  }
  // Determining total resistance
  float RT = (VCC*R)/(VCC-V[0]);

  // Determining total current
  float IT = VCC/(RT+R);

  // Calculating and printing thermistor temperatures
  for(int i = 0; i < 4; ++i)
  {
    // Calculating voltage drop due to resistance
    float RTherm = (V[i+1]-V[i])/IT;
    
    // converting resistor value to temperature in Kelvin (formula in datasheet)
    float TempT = (B*T0)/(T0*(log(RTherm) - log(RT0))+B);
    
    // logging temperature in Degrees centigrade - .csv format
    Serial.print(TempT - 273.15);
    Serial.print(',');
  }
  Serial.print("\n");
}
