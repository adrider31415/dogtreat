import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)

ControlPin = [7,11,13,15]
N = 1


for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)


seq = [[1, 0, 0, 0],\
       [1, 1, 0, 0],\
       [0, 1, 0, 0],\
       [0, 1, 1, 0],\
       [0, 0, 1, 0],\
       [0, 0, 1, 1],\
       [0, 0, 0, 1],\
       [1, 0, 0, 1]]

def dispense(t):
    for pin in ControlPin:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,0)

        for i in range(N*512):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                    time.sleep(t)
