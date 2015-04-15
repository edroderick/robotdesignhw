from ctypes import Structure,c_uint16,c_double,c_ubyte,c_uint32,c_int16,c_uint8

class ROBOT_JOINT_REF(Structure):
      _pack_ = 1
      _fields_ = [("position", c_uint8),
		  ("speed", c_uint8),
		  ("velocity", c_uint8),
		  ("accel", c_uint8),
		  ("id", c_uint8),
		  ("gain", c_uint8),
		  ("posdir", c_uint8),	
		  ("maxspeed", c_uint8),
		  ("maxposition", c_uint8),
		  ("maxaccel", c_uint8),
		  ("torque", c_uint8),
		  ("maxtorque", c_uint8),
		  ("command", c_ubyte)]

