'''
Created on Nov 8, 2015

@author: samuele
'''


import serial

ser = serial.Serial("/dev/ttyUSB0", 9600)

#COMPILE THIS PART EVERY TIME YOU WANT TO CHANGE THE SCALE

invert = True

minValue = 0.0 # value in Volt

maxValue = 4.0 # value in Volt

minInterestedValue = 0.0 # value in Volt

maxInterestedValue = 4.0 #value in Volt

minScale = 0.0 # value in XXX

maxScale = 100.0# value in XXX

#______________________________________________________________


# Computing operations according to the values

maxInterestedValue = maxInterestedValue / maxValue * 1023

minInterestedValue = minInterestedValue / maxValue * 1023

inputRange = maxInterestedValue - minInterestedValue

outputRange = maxScale - minScale

#_____________________________________________

if invert == False:
    while 1:
        x_in = float(ser.readline())
        
        x_out = (x_in - minInterestedValue) / inputRange * outputRange + minScale
        
        print x_out
    

if invert == True:
    while 1:
        x_in = float(ser.readline())
        
        x_out = (maxInterestedValue - x_in) / inputRange * outputRange + minScale
        
        print x_out