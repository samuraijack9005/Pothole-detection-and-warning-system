#Libraries
import RPi.GPIO as GPIO
import time
from gps1 import coordinates
from gps1 import write_csv1

 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
Buzzer=19

maxtime=0.04

GPIO.setup(Buzzer, GPIO.OUT)
GPIO.output(Buzzer,0)
 
#set GPIO Pins
GPIO_TRIGGER = 3
GPIO_ECHO = 2
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    
    timeout = StartTime + maxtime
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0 and StartTime<timeout:
        StartTime = time.time()
    StopTime = time.time()
    timeout = StopTime + maxtime
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1 and StopTime<timeout:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            if (dist>20):
                 print ("pot hole detected")
##                 print('location'+coordinates())
##                 write_csv1()
                 
                 GPIO.output(Buzzer,1)
                 time.sleep(0.5)
                 GPIO.output(Buzzer,0)
                 print ("Measured Distance = %.1f cm" % dist)
                 
                 time.sleep(2)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
