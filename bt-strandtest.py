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
def sred():
   for i in range (scri,scre):
       strip.setPixelColor(i, 0xFF0000)
   for i in range (scgi,scge):
       strip.setPixelColor(i, 0x000000)
   for i in range (scbi,scbe):
       strip.setPixelColor(i, 0x000000)
   for i in range (scyi,scye):
       strip.setPixelColor(i, 0x000000)
   strip.show()   
def sgreen():
   for i in range (scri,scre):
       strip.setPixelColor(i, 0x000000)
   for i in range (scgi,scge):
       strip.setPixelColor(i, 0x00FF00)
   for i in range (scbi,scbe):
       strip.setPixelColor(i, 0x000000)
   for i in range (scyi,scye):
       strip.setPixelColor(i, 0x000000)
   strip.show()  
def sblue():
   for i in range (scri,scre):
       strip.setPixelColor(i, 0x000000)
   for i in range (scgi,scge):
       strip.setPixelColor(i, 0x000000)
   for i in range (scbi,scbe):
       strip.setPixelColor(i, 0x0000FF)
   for i in range (scyi,scye):
       strip.setPixelColor(i, 0x000000)
   strip.show()  
def syellow():
   for i in range (scri,scre):
       strip.setPixelColor(i, 0x000000)
   for i in range (scgi,scge):
       strip.setPixelColor(i, 0x000000)
   for i in range (scbi,scbe):
       strip.setPixelColor(i, 0x000000)
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
 if (data == "cars01"):    
  print ("R9-G0-B0-Y0")
  scrdi = 0  
  scre = 54
  scgi = 0  
  scge = 0
  scbi = 0 
  scbe = 0
  scyi = 0 
  scye = 0
  configlabel = data
  carconfig()
 if (data == "cars02"):    
  print ("R8-G1-B0-Y0")
  scrdi = 0  
  scre = 48
  scgi = 48 
  scge = 54
  scbi = 0 
  scbe = 0
  scyi = 0 
  scye = 0
  configlabel = data
  carconfig()
 if (data == "cars03"):    
  print ("R7-G2-B0-Y0")
  scrdi = 0  
  scre = 39
  scgi = 39 
  scge = 54
  scbi = 0
  scbe = 0
  scyi = 0 
  scye = 0
  configlabel = data
  carconfig()
 if (data == "cars04"):    
  print ("R7-G1-B1-Y0")
  scrdi = 0  
  scre = 42
  scgi = 42 
  scge = 48
  scbi = 48
  scbe = 54
  scyi = 0 
  scye = 0
  configlabel = data
  carconfig()
 if (data == "cars05"):    
  print ("R6-G3-B0-Y0")
  scrdi = 0  
  scre = 33
  scgi = 33
  scge = 54
  scbi = 0
  scbe = 0
  scyi = 0 
  scye = 0
  configlabel = data
  carconfig()
 if (data == "cars06"):    
  print ("R6-G2-B1-Y0")
  scrdi = 0  
  scre = 33
  scgi = 33
  scge = 45
  scbi = 45
  scbe = 54
  scyi = 0 
  scye = 0
  configlabel = data
  carconfig()
 if (data == "cars07"):    
  print ("R6-G1-B1-Y1")
  scrdi = 0  
  scre = 33
  scgi = 33
  scge = 39
  scbi = 39
  scbe = 45
  scyi = 45
  scye = 54
  configlabel = data
  carconfig()
 if (data == "cars08"):    
  print ("R5-G4-B0-Y0")
  scrdi = 0  
  scre = 27
  scgi = 27
  scge = 54
  scbi = 0
  scbe = 0
  scyi = 0 
  scye = 0
  configlabel = data
  carconfig()
 if (data == "cars09"):    
  print ("R5-G3-B1-Y0")
  scrdi = 0  
  scre = 27
  scgi = 27
  scge = 45
  scbi = 45
  scbe = 54
  scyi = 0 
  scye = 0
  configlabel = data
  carconfig()
 if (data == "cars10"):    
  print ("R5-G2-B2-Y0")
  scrdi = 0  
  scre = 27
  scgi = 27
  scge = 39
  scbi = 39
  scbe = 54
  scyi = 0 
  scye = 0
  configlabel = data
  carconfig()
 if (data == "cars11"):    
  print ("R5-G2-B1-Y1")
  scrdi = 0  
  scre = 27
  scgi = 27
  scge = 39
  scbi = 39
  scbe = 45
  scyi = 45
  scye = 54
  configlabel = data
  carconfig()
 if (data == "cars12"):    
   print ("R4-G4-B1-Y0")
   scrdi = 0  
   scre = 21
   scgi = 21  
   scge = 45
   scbi = 45 
   scbe = 54
   scyi = 0 
   scye = 0
   configlabel = data
   carconfig()  
 if (data == "cars13"):    
   print ("R4-G3-B2-Y0")
   scrdi = 0  
   scre = 21
   scgi = 21  
   scge = 39
   scbi = 39 
   scbe = 54
   scyi = 0 
   scye = 0
   configlabel = data
   carconfig()
 if (data == "cars14"):    
   print ("R4-G3-B1-Y1")
   scrdi = 0  
   scre = 21
   scgi = 21  
   scge = 39
   scbi = 39 
   scbe = 45
   scyi = 45
   scye = 54
   configlabel = data
   carconfig()
 if (data == "cars15"):    
   print ("R4-G2-B2-Y1")
   scrdi = 0  
   scre = 21
   scgi = 21  
   scge = 33
   scbi = 33 
   scbe = 45
   scyi = 45
   scye = 54
   configlabel = data
   carconfig()   
 if (data == "cars16"):    
   print ("R3-G3-B3-Y0")
   scrdi = 0  
   scre = 16
   scgi = 16  
   scge = 33
   scbi = 33 
   scbe = 54
   scyi = 0
   scye = 0
   configlabel = data
   carconfig()   
 if (data == "cars17"):    
   print ("R3-G3-B2-Y1")
   scrdi = 0  
   scre = 16
   scgi = 16  
   scge = 33
   scbi = 33 
   scbe = 45
   scyi = 45
   scye = 54
   configlabel = data
   carconfig()   
 if (data == "cars18"):    
   print ("R3-G2-B2-Y2")
   scrdi = 0  
   scre = 16
   scgi = 16  
   scge = 27
   scbi = 27 
   scbe = 39
   scyi = 39
   scye = 54
   configlabel = data
   print configlabel
   carconfig()      
   
######
 if (data == "start"):    
   clear()
   print configlabel + " shop start"
 if (data == "sred"):    
   sred()
   print configlabel + " Red"
 if (data == "sblue"):    
   sblue()
   print configlabel + " Blue"
 if (data == "sgreen"):    
   sgreen()
   print configlabel + " Green"
 if (data == "syellow"):    
   syellow()
   print configlabel + " Yellow"
 if (data == "finalized"):    
   carconfig()
   print configlabel + " shop finalized"   
##############################
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
