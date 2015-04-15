/*/* Blink(LED)
 
 Turns on the built-in LED(Status LED) on for 0.1 second, then off for 0.1 second,
 repeatedly. BOARD_LED_PIN is defined previously, so just use it without declaration.
 BOARD_LED_PIN was connected to pin 16 in CM-900, but connected to pin 14 in OpenCM9.04.

                Compatibility
CM900                  O
OpenCM9.04             O

 created 16 Nov 2012
 by ROBOTIS CO,.LTD.
 */

char inChar;
byte index = 0;

void setup() {
  // Set up the pin 10 as an output:
  pinMode(BOARD_LED_PIN, OUTPUT);
  Serial3.begin(57600);
}


void loop() {
 

  if(Serial3.available() > 0){
    char inData[20];
    while(Serial3.available()>0){
      if(index < 19){
        inChar = Serial3.read(); //read a character
        inData[index] = inChar;
        index++;
        inData[index] = '\0';
      }
    }
  
  index = 0;
  SerialUSB.print("ret: ");
  SerialUSB.println(inData);
  
  if(inData[0] == char(68)){
    
    for(int i=0; i<100; i++){
      toggleLED();
      delay(100);
    }
  }
  delay(20);
}
}

