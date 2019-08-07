#importing modules

import cv2   
import numpy as np
import os
import time
import RPi.GPIO as GPIO

##from atttachem import sendMail
from gps1 import coordinates
from gps1 import write_csv1
#capturing video through webcam
cap=cv2.VideoCapture(0)
##cap=cv2.imread('Pothole.jpg')

buzzer = 19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT)


import geocoder 
g = geocoder.ip('me')
##g.debug()

#print(str(g.latlng))
lat= g.latlng[0]-0.001136

lng= g.latlng[1]+0.01039

while(1):

        
##        print('https://www.google.com/maps/?q="{}{}'.format(lat,lng))
        
        _, img = cap.read()
        cv2.imwrite('frame.jpg',img)
        COUNTER = 0    
        #converting frame(img i.e BGR) to HSV (hue-saturation-value)

        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        blue_lower=np.array([110,50,50],np.uint8)
        blue_upper=np.array([130,255,255],np.uint8)

        blue=cv2.inRange(hsv,blue_lower,blue_upper)

        #Morphological transformation, Dilation  	
        kernal = np.ones((5 ,5), "uint8")

        blue=cv2.dilate(blue,kernal)
        res1=cv2.bitwise_and(img, img, mask =blue)


        (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>900):
                        COUNTER += 1
			print(COUNTER)
			if COUNTER >=3:     
                                print('Location'+cordinates())
                                write_csv1()
                                x,y,w,h = cv2.boundingRect(contour)	
                                img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                                cv2.putText(img,"Pothole Detector",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
                                time.sleep(1)
                                print('Pot Hole detected')
                                GPIO.output(buzzer,1)
                                time.sleep(1)
                                GPIO.output(buzzer,0)
##                        sendMail( ["pawar9005@gmail.com"],
##        "Pot Hole Detected",
##        'http://www.google.com/maps/?q="{},{}'.format(lat,lng),
##        ["frame.jpg"] )


        cv2.imshow("Image",img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break  
          

    
