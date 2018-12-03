import RPi.GPIO as GPIO
import time

LEDPIN = 14 #GPIO14, Pin 8  

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEDPIN,GPIO.OUT)

def blink():
    GPIO.output(LEDPIN,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LEDPIN,GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(LEDPIN,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LEDPIN,GPIO.LOW)
    time.sleep(1)

def turnLedOn(enabled):
    if(enabled):
        GPIO.output(LEDPIN,GPIO.HIGH)
    else:
        GPIO.output(LEDPIN,GPIO.LOW)

if __name__ == "__main__":
    turnLedOn(False)    
    blink()
    blink()
    blink()
    turnLedOn(True)


