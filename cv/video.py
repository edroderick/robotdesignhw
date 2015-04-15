import numpy as np
import cv2
cap = cv2.VideoCapture(0)
#capture frame by frame
ret, frame = cap.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('frame',gray)
cv2.waitKey(0)
