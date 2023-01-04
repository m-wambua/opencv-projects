import numpy as np

import cv2

shape_image=cv2.imread('shape.png')


grey_image=cv2.cvtColor(shape_image,cv2.COLOR_BGR2GRAY)
ret, thresh=cv2.threshold(grey_image,127,125,1)

contours,h=cv2.findContours(thresh,1,2)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print (len(approx))
    if len(approx)==3:
        print ("triangle")
        cv2.drawContours(shape_image,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print ("square")
        cv2.drawContours(shape_image,[cnt],0,(0,0,255),-1)
    elif len(approx) > 15:
        print ("circle")
        cv2.drawContours(shape_image,[cnt],0,(0,255,255),-1)

cv2.imshow('shape_image',shape_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 