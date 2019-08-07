import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    TRIG = 3
    ECHO = 2
    maxTime = 0.04
    def distance():
        
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)

        GPIO.output(TRIG,False)

        time.sleep(0.01)

        GPIO.output(TRIG,True)

        time.sleep(0.00001)

        GPIO.output(TRIG,False)

        pulse_start = time.time()
        timeout = pulse_start + maxTime
        while GPIO.input(ECHO) == 0 and pulse_start < timeout:
            pulse_start = time.time()

        pulse_end = time.time()
        timeout = pulse_end + maxTime
        while GPIO.input(ECHO) == 1 and pulse_end < timeout:
            pulse_end = time.time()

        TimeElapsed = pulse_end - pulse_start
        distance = (TimeElapsed * 34300) / 2


            return distance
        
except:
    GPIO.cleanup()
