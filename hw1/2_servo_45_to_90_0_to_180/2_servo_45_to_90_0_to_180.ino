/* Dynamixel ID Change Example
 
Turns the dynamixel left , then turn right for one 
 second, repeatedly.
 
               Compatibility
 CM900                  O
 OpenCM9.04             O
 
                   Dynamixel Compatibility
               AX    MX      RX    XL-320    Pro
 CM900          O      O      O        O      X
 OpenCM9.04     O      O      O        O      X
 **** OpenCM 485 EXP board is needed to use 4 pin Dynamixel and Pro Series ****
 
 
 created 22 May 2014
 by ROBOTIS CO,.LTD.
 */
 /* Serial device defines for dxl bus */
#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04
#define DXL_BUS_SERIAL2 2  //Dynamixel on Serial2(USART2)  <-LN101,BT210
#define DXL_BUS_SERIAL3 3  //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
/* Dynamixel ID defines */
#define J_ID 1
#define J2_ID 2

Dynamixel Dxl(DXL_BUS_SERIAL1); 
 
void setup() {
  // Initialize the dynamixel bus:
  // Dynamixel 2.0 Baudrate -> 0: 9600, 1: 57600, 2: 115200, 3: 1Mbps  
  Dxl.begin(3);  
  Dxl.jointMode(J_ID); //jointMode() is to use position mode  
  Dxl.jointMode(J2_ID);
}
 
void loop() {
  //Turn dynamixel ID 1 to 45 deg
  Dxl.goalPosition(J_ID, 154); 
  //Turn dynamixel ID 2 to 0 deg
  Dxl.goalPosition(J2_ID, 0);
  delay(500);
  
  //Turn dynamixel ID 2 to 180 deg
  Dxl.goalPosition(J2_ID, 614);
  delay(500);
  
  //Turn dynamixel ID 1 to 90 deg
  Dxl.goalPosition(J_ID, 307); 
  //Turn dynamixel ID 2 to 0 deg
  Dxl.goalPosition(J2_ID, 0);
  delay(500);  
  
  //Turn dynamixel ID 2 to 180 deg
  Dxl.goalPosition(J2_ID, 614);
  delay(500);           
}


