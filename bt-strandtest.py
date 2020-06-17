import os
import bluetooth
import RPi.GPIO as GPIO        #calling for header file which helps in using GPIOs of PI
import time
from rpi_ws281x import *
from strandtest import *
import argparse

# LED strip configuration:
LED_COUNT      = 59      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PW$
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses S$
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800kh$
LED_DMA        = 10      # DMA channel to use for generating signal (tr$
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN tr$

SLOT = 54/9

LED=21
 
scri = 0  
scre = 0
scgi = 0  
scge = 0
scbi = 0 
scbe = 0
scyi = 0 
scye = 0
   
GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)  #initialize GPIO21 (LED) as an output Pin
GPIO.output(LED,0)

def car(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def clear():
   for i in range(strip.numPixels()):
      strip.setPixelColor(i, Color(0, 0, 0))
   strip.show()
def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
		
def fourslotred():
    """Draw rainbow that uniformly distributes itself across all pixels."""
    clear()
    for i in range (15):
        strip.setPixelColor(i, 0xFF0000)
    strip.show()
def fourslotgreen():
    """Draw rainbow that uniformly distributes itself across all pixels."""
    clear()
    for i in range (15,30):
        strip.setPixelColor(i, 0x00FF00)
    strip.show()
def car1():
   strip.setPixelColor(0,0xFF0000)
   strip.setPixelColor(1,0x00FF00)
   strip.setPixelColor(2,0x0000FF)
   strip.show()

def red9():
    """Draw rainbow that uniformly distributes itself across all pixels."""
    clear()
    for i in range (0,(SLOT * 9)):
        strip.setPixelColor(i, 0xFF0000)
    strip.show()
def red8():
    """Draw rainbow that uniformly distributes itself across all pixels."""
    clear()
    for i in range (0,(SLOT * 8)):
        strip.setPixelColor(i, 0xFF0000)
    strip.show()
def carconfig():
   """Draw rainbow that uniformly distributes itself across all pixels."""
   clear()
   for i in range (scri,scre):
       strip.setPixelColor(i, 0xFF0000)
   for i in range (scgi,scge):
       strip.setPixelColor(i, 0x00FF00)
   for i in range (scbi,scbe):
       strip.setPixelColor(i, 0x0000FF)
   for i in range (scyi,scye):
       strip.setPixelColor(i, 0xFFFF00)
   strip.show()  


server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1

server_socket.bind(("",port))
server_socket.listen(1)
 
client_socket,address = server_socket.accept()
print "Accepted connection from ",address
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()
while 1:
 
 data = client_socket.recv(1024)
 print "Received: %s" % data
 
#System Commnds
 if (data == "restart"):    #restart equipment
  print ("Restart LC-HR-CR")
  os.system('systemctl reboot -i')
#Global Commands  
 if (data == "quit"):
   print ("Quit")
   break
 if (data == "clear"):
   print ("Clear")
   clear()
 if (data == "reset"):    
   scri = 0  
   scre = 0
   scgi = 0  
   scge = 0
   scbi = 0 
   scbe = 0
   scyi = 0 
   scye = 0
   print ("Reset Car Configuration")
#Car configuration
 if (data == "cars12"):    
  print ("R4-G3-B1-Y1")
  scrdi = 0  
  scre = 30
  scgi = 31  
  scge = 40
  scbi = 41 
  scbe = 50
  scyi = 51 
  scye = 54
  print scye
  carconfig()

######
 if (data == "0"):    #if '0' is sent from the Android App, turn OFF the LED
  print ("GPIO 21 LOW, LED OFF")
  GPIO.output(LED,0)
 if (data == "1"):    #if '1' is sent from the Android App, turn OFF the LED
  print ("4slotred")
  fourslotred()
 if (data == "2"):    #if '1' is sent from the Android App, turn OFF the LED
  print ("4slotgreen")
  fourslotgreen()
 if (data == "3"):    #if '1' is sent from the Android App, turn OFF the LED
  print ("Car1")
  car1()
 if (data == "9"):    #if '1' is sent from the Android App, turn OFF the LED
  clear();
 if (data == "a"):    #if '1' is sent from the Android App, turn OFF the LED
  print ("Red 9")
  red9()
 if (data == "b"):    #if '1' is sent from the Android App, turn OFF the LED
  print ("Red 8")
  red8()
  
  
#Commands always from the mobile device
 if (data == data.startswith('rgb')):    #if '1' is sent from the Android App, turn OFF the LED
  print ("rgb config")
 
 
client_socket.close()
server_socket.close()
