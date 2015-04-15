import robostruct as rst
import time
import socket
import pickle
import struct

IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP Receive
sock.bind((IP, PORT))    
sock.listen(10)
print 'listening'
conn, addr = sock.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

position = 0
speed = 0
velocity = 0
accel = 0
gain = 0
posdir = 0	
maxspeed = 0
maxposition = 0
maxaccel = 0
torque = 0
maxtorque = 0
command = 2


ref = rst.ROBOT_JOINT_REF()


data = conn.recv(1000000)
ref = struct.unpack(data)
	'''
	if (ref.command == 1):
		position = ref.position
		speed = ref.speed
		velocity = ref.velocity
		accel = ref.accel
		gain = ref.gain
		posdir = ref.posdir
		maxspeed = ref.maxspeed
		maxposition = ref.maxposition
		maxaccel = ref.maxaccel
		torque = ref.torque
		maxtorque = ref.maxtorque

		print ref
	elif (ref.command == 0):
		sock.send(pickle.dumps(ref))
	else:
		print 'invalid command'
	'''
print ref.command


