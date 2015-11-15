'''
Created on Nov 15, 2015

@author: samuele
'''

import flask
import serial
import sys


ser = serial.Serial("/dev/ttyUSB0", 9600)

app = flask.Flask(__name__)

@app.route('/on', methods=['GET'])
def turnOn():
    ser.write("a");
    print "on"
    return "on"
    
@app.route('/off', methods=['GET'])
def turnOff():
    ser.write("b");
    print "off"
    return "off"
    
if __name__ == '__main__':
    '''app.run(debug=True)'''
    try:
        app.run(host="192.168.1.101", port=8080)
    except:
        print "Porta 8080 gia' in uso, exit!"
        sys.exit(-1)