import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
	input = raw_input("Enter Data to Send: ")
	print input

	ser.write(data)
	time.sleep(.05)
	returned = ser.readline()
	print returned

	



