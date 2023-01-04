import numpy as np
import cv2 

image =cv2.imread('image-2.png')

hsv_convert=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_range=np.array([110,50,50])
upper_range=np.array([130,255,255])

mask_toput=cv2.inRange(hsv_convert,lower_range,upper_range)
cv2.imshow('image', image)
cv2.imshow('mask',mask_toput)
while(True):
    k=cv2.waitKey(5) & 0xFF 
    if k==27:
     break
