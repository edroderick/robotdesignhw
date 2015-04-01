#!/usr/bin/env python

#import controller_include as ci
import csv


#import diff_drive
#import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np
import serial
import math

#import actuator_sim as ser

'''
CONTROLLER_REF_NAME  = 'controller-ref-chan'
error = ach.Channel(ci.CONTROLLER_REF_NAME)
error.flush()
controller = ci.CONTROLLER_REF()
'''
ser = serial.Serial('/dev/ttyACM0', 9600)

cap = cv2.VideoCapture(0)
cap.set(3,1280)

cap.set(4,1024)

time.sleep(2)

cap.set(15,-8.0)

ret, frame = cap.read()
height, width, depth = frame.shape
#print 'H = ', height, ' W = ', width
cv2.waitKey(5)

while True:

    ret, frame = cap.read()
    img = frame

    # Convert RGB to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define upper and lower range of blue color in HSV
    lower_blue = np.array([90, 50, 50], dtype=np.uint8)
    upper_blue = np.array([130,255,255], dtype=np.uint8)

    # Threshold the HSV image to get only blue
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 5)
    dilation = cv2.dilate(erosion, kernel, iterations = 5)

    # Use findContours to get the boundry of the green blob
    contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if (len(contours) > 0):
	cnt = contours[0]
	#Finding centroids of best_cnt and draw a circle there
	M = cv2.moments(cnt)
	cx = (M['m10']/M['m00'])
	cy = (M['m01']/M['m00'])
	cv2.circle(img,(int(cx),int(cy)),5,(0,0,255),-1)

    else: #if no color seen, set error to 0
	cx = width/2.0
	cy = height/2.0

    cv2.imshow('wctrl',img)
    cv2.waitKey(5)

    print 'cx = ', cx
    print 'width = ', width

    ex = (cx/width)*2-1

    fov = 60

    theta = (fov/2.0)*ex

    thetad = 0
    etheta = thetad - theta

    print etheta

    kp = .1
    kd = 1
    ki = 1

    PID = kp*etheta

    a = int(0)
    a = a|(int(np.abs(PID))&0x7F)
    if (PID < 0):
        a = a|0x80

    ser.write(chr(a))
    #print "chr = ", int(ser.read())

    # send the error to controller
    #controller.x = x
    #controller.y = y
    #error.put(controller)
    #time.sleep(.1)
