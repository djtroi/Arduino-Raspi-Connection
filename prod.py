import serial
import RPi.GPIO as GPIO
from time import sleep

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.flushInput()





bandbreite = 1000
benutzer1 = 1
benutzer5 = 5
benutzer10 = 10

#u_bandbreite = bandbreite / benutzer

while True: 
    linein = ser.readline()
    if linein > 0:
        u_bandbreite = bandbreite / benutzer5

        print(u_bandbreite)