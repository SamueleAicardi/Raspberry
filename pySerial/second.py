'''
Created on Nov 3, 2015

@author: samuele
'''

import serial
ser = serial.Serial('dev/ttyUSB0', 9600)
ser.write('5')
