#import GPIO library
import RPi.GPIO as GPIO

#set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.IN)

try:
    while True:
        if GPIO.input(35)==1:
            print "Open"
        else:
            print "Close"

finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
