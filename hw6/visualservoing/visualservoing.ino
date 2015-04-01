/*
 Serial1 : Dynamixel_Poart
 Serial2 : Serial_Poart(4pin_Molex)
 Serial3 : Serial_Poart(pin26:Tx3, pin27:Rx3)
 
 TxD3(Cm9_Pin26) <--(Connect)--> RxD(PC)
 RxD3(Cm9_Pin27) <--(Connect)--> TxD(PC)
 */

#define DXL_BUS_SERIAL1 1 //Dynamixel on Serial1(USART1) <-OpenCM9.04 
#define DXL_BUS_SERIAL2 3 //Dynamixel on Serial2(USART2) <-LN101,BT210 
#define DXL_BUS_SERIAL3 3 //Dynamixel on Serial3(USART3) <-OpenCM 485EXP

Dynamixel Dxl(DXL_BUS_SERIAL1);

char inChar;
byte index = 0;
int maxspeed = 400;


void setup() {
  // Set up the pin 10 as an output:
  Dxl.begin(3);
  Dxl.wheelMode(1);

}


void loop() {
 
  if(SerialUSB.available() > 0){
    char inData[20];
    while(SerialUSB.available()>0){
      if(index < 19){
        inChar = SerialUSB.read(); //read a character
        inData[index] = inChar;
        index++;
        inData[index] = '\0';
      }
    }
  
  index = 0;
  SerialUSB.print(inData[0]);
  double v = (double)(inData[0]&0x7F)/127.0;
  if((inData[0]&0x80) > 0){
   v = v*-1.0; 
  }
  int vfinal = ((v-1)/2.0)*1023;
  Dxl.goalSpeed(1, vfinal);
 
  delay(100);
}
}

