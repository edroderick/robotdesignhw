import serial

ser = serial.Serial('/dev/ttyACM3', 9600)
#ser2 = serial.Serial('/dev/ttyAMA0', 9600)
ser.write(chr(68))
#a = [1, 2, 3]
#ser2.write(a)
#print ser.readline()
#chr
