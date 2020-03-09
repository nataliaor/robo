import cv2
import numpy as np
 
 
 
 
 
imgr_blue = cv2.imread('../../newbluetest.jpg')
imgr_red = cv2.imread('../../redtest.jpg')
imgr_green = cv2.imread('../../greentest.jpg')

#Red color rangle  169, 100, 100 , 189, 255, 255
def col_detect(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    red_lower = np.array([0,50,0])
    red_upper = np.array([20,255,255])
    red_mask = cv2.inRange(hsv,red_lower,red_upper)

    blue_lower = np.array([190,50,0])
    blue_upper = np.array([220,255,255])
    blue_mask = cv2.inRange(hsv,blue_lower,blue_upper)

    green_lower = np.array([80,50,0])
    green_upper = np.array([145,255,255])
    green_mask = cv2.inRange(hsv,green_lower,green_upper)

    #mask = red_mask + blue_mask + green_mask

    #if np.array_equal(mask, green_mask):
    if np.any(cv2.inRange(hsv,red_lower,red_upper)):
        print('red detected')
    elif np.any(cv2.inRange(hsv,blue_lower,blue_upper)):
    #elif np.array_equal(mask,blue_mask):
        print('Blue detected')
    #elif np.array_equal(mask, red_mask):
    elif np.any(cv2.inRange(hsv,green_lower,green_upper)):
        print('green detected')
    else:
        print('no colour found')

print('blue check')
col_detect(imgr_blue)

print('red check')
col_detect(imgr_red)

print('green check')
col_detect(imgr_green)

#if max BGR is in each position then return that colour

#mask = cv2.inRange(hsv, red_lower, red_upper)

    
#np.any(cv2.inRange(hsv,red_lower, red_upper))
#print(hsv) 

#imshow requires a GUI and will error if you run the code headless 
#cv2.imshow('image', img)
#cv2.imshow('mask', mask)
 
 
#cv2.waitKey(0)
#cv2.destroyAllWindows()
