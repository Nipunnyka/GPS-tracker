#include <SoftwareSerial.h>
#include <TinyGPS++.h>

#define GPSBaud 9600
#define SERIALBaud 9600

SoftwareSerial gps_uart(2, 3); // RX, TX

TinyGPSPlus gps;        //4. The TinyGPS++ object

String gps_lattitude = "";
String gps_longitude = "";
int count = 0;

void setup() {
  Serial.begin(SERIALBaud);
  
  gps_uart.begin(GPSBaud);
  setGPSValues();
  smartDelay(1000);
}

void loop() {
  setGPSValues();
  smartDelay(800);
  Serial.println(gps_lattitude + " " + gps_longitude + " " + String(count));
}

void setGPSValues(){
  count = (count+1)%10000;
  gps_lattitude = getGPSLat();
  gps_longitude = getGPSLong();
}
