import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio
import csv

 
gpio.setmode(gpio.BCM)

 
port = "/dev/ttyAMA0" # the serial port to which the pi is connected.
 
#create a serial object
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

##data = ser.readline()
##while 1:
##    try:
##        data = ser.readline()
##    except:
##print("loading") 
##wait for the serial port to churn out data

##print(data)


lati=0
long=0
while True:
    
    data = ser.readline()
##    except:
##        print("loading")
 
    if data[0:6] =='$GPGGA': # the long and lat data are always contained in the GPGGA string of the NMEA data
 
        msg = pynmea2.parse(data)
        latval = msg.latitude
        longval = msg.longitude
        lati=latval
        long =longval
        break
print((lati,long))
def coordinates():
    return lati,long;

def write_csv1():
        la,ln=coordinates()
        row1 = [la,ln]
        with open('Data.csv', mode='a') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(row1)
            file.close()
    
        
    
 
#parse the latitude and print



    
 
#parse the longitude and print

##concatlong =str(longval)
##print((concatlat,concatlong))
    

##def cordinates(concatlat,concatlong):
##    return (concatlat, concatlong)
##def write_csv(lati,long):
##   import csv
##
##    row = [lati,long]
##
##    with open('data.csv', 'a') as csvFile:
##        writer = csv.writer(csvFile)
##        writer.writerow(row)
##
##    csvFile.close() 
    


           
time.sleep(0.5)#wait a little before picking the next data.
