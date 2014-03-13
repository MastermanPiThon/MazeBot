# Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with a Lego Motor 

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_ULTRASONIC_CONT   #Set the type of sensor at PORT_1

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

result = BrickPiUpdateValues()

while True:
    
    while not result and BrickPi.Sensor[PORT_1]>20:
    	print "Running Forward"
    	print BrickPi.Sensor[PORT_1]
        BrickPi.MotorSpeed[PORT_A] = -255  #Set the speed of MotorA (-255 to 255)
    	BrickPi.MotorSpeed[PORT_B] = -255  #Set the speed of MotorB (-255 to 255)
        BrickPiUpdateValues()       
    print BrickPi.Sensor[PORT_1]
    BrickPiUpdateValues()
    
    while not result and BrickPi.Sensor[PORT_1]<20:
    	print "Turning..."
    	print BrickPi.Sensor[PORT_1]
        BrickPi.MotorSpeed[PORT_A] = 255
    	BrickPi.MotorSpeed[PORT_B] = -255  #Set the speed of MotorB (-255 to 255)
   	ot = time.time()
    	while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
            time.sleep(3)
            BrickPiUpdateValues()

   # print "Running Reverse"
   # BrickPi.MotorSpeed[PORT_A] = -255  #Set the speed of MotorA (-255 to 255)
   # BrickPi.MotorSpeed[PORT_B] = 255  #Set the speed of MotorB (-255 to 255)
   # ot = time.time()
   # while(time.time() - ot < 1.0):    #running while loop for 3 seconds
   #     BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
   #    time.sleep(.1)              # sleep for 100 ms
