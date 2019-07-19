import serial
import RPi.GPIO as GPIO
from time import sleep


led_pin = 21
button_pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)



ser = serial.Serial('/dev/ttyACM1', 9600)


while True:
    try: incoming_data == ser.read()
if incoming_data = '1':
    GPIO.output(led_pin, 1)
elif incoming_data == '0':
    GPIO.output(led_pin, 0)

if button_state == 1:
    ser.write('1')

elif button_state == 0:
    ser.write('0')
    except KeyboardInterrupt:
        GPIO.cleanup()