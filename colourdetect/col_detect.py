import cv2
import numpy as np
 
 
 
 
 
img = cv2.imread('../../redtest.jpg')
 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
 
#Red color rangle  169, 100, 100 , 189, 255, 255
 
red_lower = np.array([110,50,50])
red_upper = np.array([130,255,255])

#if max BGR is in each position then return that colour

mask = cv2.inRange(hsv, red_lower, red_upper)
print(hsv) 

#imshow requires a GUI and will error if you run the code headless 
#cv2.imshow('image', img)
#cv2.imshow('mask', mask)
 
 
#cv2.waitKey(0)
#cv2.destroyAllWindows()
