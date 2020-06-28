void initGPS() {
}

String getGPSTime(){
  return getDateTime2(gps.time);
}

String getGPSLat(){
  return getDataInThisFormat(gps.location.lat(), gps.location.isValid(), 6);
}

String getGPSLong(){
  return getDataInThisFormat(gps.location.lng(), gps.location.isValid(), 6);
}

String getGPSAlt(){
  return getDataInThisFormat(gps.altitude.meters(), gps.altitude.isValid(), 1);
}

String getGPSNumSat(){
  return getInt2(gps.satellites.value(), gps.satellites.isValid());
}

// This custom version of delay() ensures that the gps object
// is being "fed".
void smartDelay(unsigned long ms)
{
  unsigned long start = millis();
  do 
  {
    
    while (gps_uart.available())
      gps.encode(gps_uart.read());
  } while (millis() - start < ms);
}

String getDataInThisFormat(double val, bool valid, int prec)                              //Function to print float values
{
  if (!valid)
  {
    return "-1";
  }
  else
  {
    String toReturn = String(val,prec);
    return toReturn;
  }
  smartDelay(0);
}

String getInt2(unsigned long val, bool valid)                                    //Function to print int values
{ 
  if (valid)
    return String(val);
  else
    return "-1";
  
  smartDelay(0);
}

String getDateTime2(TinyGPSTime &t)
{  
  if (!t.isValid())
  {
    return "-1";
  }
  else
  {
    char sz[32];
    sprintf(sz, "%02d%02d%02d ", t.hour(), t.minute(), t.second());
    String s(sz); 
    return s;
  }
  smartDelay(0);
}
