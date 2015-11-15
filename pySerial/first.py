'''
Created on Nov 3, 2015

@author: samuele
'''

import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

while(True):
    print ser.readline()