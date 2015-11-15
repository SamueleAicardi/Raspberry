'''
Created on Nov 8, 2015

@author: samuele
'''


import serial

ser = serial.Serial("/dev/ttyUSB0", 9600)

#COMPILE THIS PART EVERY TIME YOU WANT TO CHANGE THE SCALE

invert = False

minValue = 0.0 # value in Volt

maxValue = 4.0 # value in Volt

minInterestedValue = 2.15 # value in Volt

maxInterestedValue = 3.85 #value in Volt

minScale = -50.0 # value in XXX

maxScale = 50.0# value in XXX

#______________________________________________________________


# Computing operations according to the values

maxInterestedValue = maxInterestedValue / maxValue * 1023

minInterestedValue = minInterestedValue / maxValue * 1023

inputRange = maxInterestedValue - minInterestedValue

outputRange = maxScale - minScale

#_____________________________________________

def readAndConvert():
    if invert == False:
        x_in = float(ser.readline())
           
        #x_out = (x_in - minInterestedValue) / inputRange * outputRange + minScale
        x_out = (maxInterestedValue - x_in) / inputRange * 500 + 100 
            
        return x_out
        
    
    if invert == True:
        x_in = float(ser.readline())
        print x_in    
        #x_out = (maxInterestedValue - x_in) / inputRange * outputRange + minScale
        x_out = (x_in - minInterestedValue) / inputRange * 500 + 100
        
        return x_out
        
        
        
from Tkinter import *

import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

def drawPlot():

    # The window is an object of type tk
    root = Tk()
    root.title('Raw_Plot')

    # A canvas object is something you can draw on
    # we put it into the root window
    canvas = Canvas(root, width=800, height=700, bg = 'white')
    # figures out how the canvas sits in the window
    canvas.pack(fill="both", expand=1)

    # draw x and y axes
    canvas.create_line(50,600,770,600, width=2)
    canvas.create_line(50,600,50,100,  width=2)
    
    # BINDED PARAMETERS
    span = (maxScale - minScale) / 10.0    
    
    # markings on x axis
    for i in range(25):
        x = 50 + (i * 30)
        canvas.create_line(x,600,x,595, width=2)
        canvas.create_text(x,600, text='%d'% (30*i), anchor=N)

    # markings on y axis
    if minScale >= 0:
        for i in range(11):
            y = 600 - (i * 50)
            canvas.create_line(50,y,55,y, width=2)
            canvas.create_text(45,y, text='%5.1f'% (span*i), anchor=E)
    if minScale < 0: 
        for i in range(11):
            y = 600 - (i * 50)
            canvas.create_line(50,y,55,y, width=2)
            canvas.create_text(45,y, text='%5.1f'% (span*i), anchor=E)

    
    
    xx = 50;
    while(True):
        #yy = float(ser.readline())
        #yy2 = ((1024 -yy)/1024.0*500+100)
        yy2 = readAndConvert()
        canvas.create_line((xx, yy2, xx+1, yy2), fill="black")
        print xx, yy2
        canvas.update()
        xx=(xx+1) % 720
        if (xx == 0):
            canvas.delete("all")
            xx=50
            canvas.create_line(50,600,770,600, width=2)
            canvas.create_line(50,600,50,100,  width=2)
    
            # markings on x axis
            for i in range(25):
                x = 50 + (i * 30)
                canvas.create_line(x,600,x,595, width=2)
                canvas.create_text(x,600, text='%d'% (30*i), anchor=N)
    
            # markings on y axis
            for i in range(11):
                y = 600 - (i * 50)
                canvas.create_line(50,y,55,y, width=2)
                canvas.create_text(45,y, text='%5.1f'% (span*i), anchor=E)
        
    # display window and wait for it to close
    root.mainloop()
    

def main():

    # detect if this is being run by itself or because it was imported
    if __name__ != "__main__":
        return
    
    drawPlot()

main()