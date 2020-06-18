#Neopixel Lusorede
#Author: Hugo Rodrigues
#Version: 0.000002
#Lusorede
#email: hugo.rodrigues@lusorede.pt
import os
import os.path
import sys
import bluetooth
import RPi.GPIO as GPIO
import time
from rpi_ws281x import *
from strandtest import *
import argparse

if os.path.isfile('/home/pi/btvars.py'):
  import btvars
  scri = btvars.scri 
  scre = btvars.scre
  scgi = btvars.scgi 
  scge = btvars.scge
  scbi = btvars.scbi
  scbe = btvars.scbe
  scyi = btvars.scyi
  scye = btvars.scye
  print (scri)
  print (scre)
  print (scgi)
  print (scge)
  print (scbi)
  print (scbe)
  print (scyi)
  print (scye)

if os.path.isfile('/home/pi/btstrip.conf'):
  import btstrip.conf
  LED_COUNT = btstrip.LED_COUNT     
  LED_PIN   = btstrip.LED_PIN  

  LED_FREQ_HZ = btstrip.LED_FREQ_HZ   
  LED_DMA = btstrip.LED_DMA  
  LED_BRIGHTNESS = btstrip.LED_BRIGHTNESS

  print ("LED_COUNT=" + LED_COUNT )
  print ("LED_PIN=" + LED_PIN   )
  print ("LED_FREQ_HZ=" + LED_FREQ_HZ    )
  print ("LED_DMA=" + LED_DMA )
  print ("LED_BRIGHTNESS=" + LED_BRIGHTNESS )
  print ("LED_INVERT=" + LED_INVERT )


#LED_COUNT      = 59      # Number of LED pixels.
#LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PW$
##LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses S$
#LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800kh$
#LED_DMA        = 10      # DMA channel to use for generating signal (tr$
#LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
#LED_INVERT     = False   # True to invert the signal (when using NPN tr$

SLOT = LED_COUNT/8

LED=21



configlabel = 'undefined'
  
GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)  #initialize GPIO21 (LED) as an output Pin
GPIO.output(LED,0)

def reg_var():
  f = open( '/home/pi/btvars.py', 'w' )
  f.write( 'scri = ' + repr(scri) + '\n' )
  f.write( 'scre = ' + repr(scre) + '\n' )
  f.write( 'scgi = ' + repr(scgi) + '\n' )
  f.write( 'scge = ' + repr(scge) + '\n' )
  f.write( 'scbi = ' + repr(scbi) + '\n' )
  f.write( 'scbe = ' + repr(scbe) + '\n' )
  f.write( 'scyi = ' + repr(scyi) + '\n' )
  f.write( 'scye = ' + repr(scye) + '\n' )
  f.close()

def clear():
   for i in range(strip.numPixels()):
      strip.setPixelColor(i, Color(0, 0, 0))
   strip.show()
def carconfig():
   clear()
   reg_var()
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
  print ("R8-G0-B0-Y0")
  scri = 0
  scre = scri + 8 * SLOT
  scgi = scre
  scge = scgi + 0 * SLOT
  scbi = scge
  scbe = scbi + 0 * SLOT
  scyi = scbe
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars02"):    
  print ("R7-G1-B0-Y0")
  scri = 0 * SLOT
  scre = scri + 7 * SLOT
  scgi = scre
  scge = scgi + 1 * SLOT
  scbi = scge
  scbe = scbi + 0 * SLOT
  scyi = scbe
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars03"):    
  print ("R6-G2-B0-Y0")
  scri = 0 * SLOT
  scre = scri + 6 * SLOT
  scgi = scre
  scge = scgi + 2 * SLOT
  scbi = scge
  scbe = scbi + 0 * SLOT
  scyi = scbe
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars04"):    
  print ("R6-G1-B1-Y0")
  scri = 0 * SLOT
  scre = scri + 6 * SLOT
  scgi = scre
  scge = scgi + 1 * SLOT
  scbi = scge
  scbe = scbi + 1 * SLOT
  scyi = scbe
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars05"):    
  print ("R5-G3-B0-Y0")
  scri = 0 * SLOT
  scre = scri + 5 * SLOT
  scgi = scre
  scge = scgi + 3 * SLOT
  scbi = scge
  scbe = scbi + 0 * SLOT
  scyi = scbe
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars06"):    
  print ("R5-G2-B1-Y0")
  scri = 0 * SLOT
  scre = scri + 5 * SLOT
  scgi = scre
  scge = scgi + 2 * SLOT
  scbi = scge
  scbe = scbi + 1 * SLOT
  scyi = scbe
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars07"):    
  print ("R5-G1-B1-Y1")
  scri = 0 * SLOT
  scre = scri + 5 * SLOT
  scgi = scre
  scge = scgi + 1 * SLOT
  scbi = scge
  scbe = scbi + 1 * SLOT
  scyi = scbe
  scye = scyi + 1 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars08"):    
  print ("R4-G4-B0-Y0")
  scri = 0 * SLOT
  scre = scri + 4 * SLOT
  scgi = scre
  scge = scgi + 4 * SLOT
  scbi = scge
  scbe = scbi + 0 * SLOT
  scyi = scbe
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars09"):    
  print ("R4-G3-B1-Y0")
  scri = 0 * SLOT
  scre = scri + 4 * SLOT
  scgi = scre
  scge = scgi + 3 * SLOT
  scbi = scge
  scbe = scbi + 1 * SLOT
  scyi = scbe
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars10"):    
  print ("R4-G2-B2-Y0")
  scri = 0 * SLOT
  scre = scri + 4 * SLOT
  scgi = scre
  scge = scgi + 2 * SLOT
  scbi = scge
  scbe = scbi + 2 * SLOT
  scyi = scbe
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars11"):    
  print ("R4-G2-B1-Y1")
  scri = 0 * SLOT
  scre = scri + 4 * SLOT
  scgi = scre
  scge = scgi + 2 * SLOT
  scbi = scge
  scbe = scbi + 1 * SLOT
  scyi = scbe
  scye = scyi + 1 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars12"):    
   print ("R3-G3-B2-Y0")
   scri = 0 * SLOT
   scre = scri + 3 * SLOT
   scgi = scre
   scge = scgi + 3 * SLOT
   scbi = scge
   scbe = scbi + 2 * SLOT
   scyi = scbe
   scye = scyi + 0 * SLOT
   configlabel = data
   carconfig() 
 if (data == "cars13"):    
   print ("R3-G3-B1-Y1")
   scri = 0 * SLOT
   scre = scri + 3 * SLOT
   scgi = scre
   scge = scgi + 3 * SLOT
   scbi = scge
   scbe = scbi + 1 * SLOT
   scyi = scbe
   scye = scyi + 1 * SLOT
   configlabel = data
   carconfig()
 if (data == "cars14"):    
   print ("R3-G2-B2-Y1")
   scri = 0 * SLOT
   scre = scri + 3 * SLOT
   scgi = scre
   scge = scgi + 2 * SLOT
   scbi = scge
   scbe = scbi + 2 * SLOT
   scyi = scbe
   scye = scyi + 1 * SLOT
   configlabel = data
   carconfig() 
 if (data == "cars15"):    
   print ("R2-G2-B2-Y2")
   scri = 0 * SLOT
   scre = scri + 2 * SLOT
   scgi = scre
   scge = scgi + 2 * SLOT
   scbi = scge
   scbe = scbi + 2 * SLOT
   scyi = scbe
   scye = scyi + 2 * SLOT
   configlabel = data
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

#Commands always from the mobile device
 if (data.startswith('caa',0 ,3)): 
  carslotr = int(data[3]) * SLOT
  carslotg = int(data[4]) * SLOT
  carslotb = int(data[5]) * SLOT
  carsloty = int(data[6]) * SLOT
  scri = 0 
  scre = carslotr
  scgi = scre  
  scge = scgi + carslotg
  scbi = scge
  scbe = scbi + carslotb
  scyi = scbe
  scye = scyi + carsloty
  print (scri)
  print (scre)
  print (scgi)
  print (scge)
  print (scbi)
  print (scbe)
  print (scyi)
  print (scye)
  carconfig()
 if (data.startswith('rgb-',0 ,4)):    #rgb-255255255IIEE
  clear()
  carslotri = int(data[13:15])
  carslotre = int(data[15:17])  
  colorr = int(data[4:7])
  colorg = int(data[7:10])
  colorb = int(data[10:13])
  print (carslotri)
  print (carslotre)
  print (colorr)
  print (colorg)
  print (colorb)
  carslotcolor = 0
  if (carslotcolor == "r"):
   hexcolor = 0xFF0000
  if (carslotcolor == "g"):
   hexcolor = 0x00FF00
  if (carslotcolor == "b"):
   hexcolor = 0x0000FF
  if (carslotcolor == "y"):
   hexcolor = 0xFFFF00
  for i in range (carslotri,carslotre):
       strip.setPixelColor(i,  Color(colorr,colorg,colorb))
  strip.show()
  
client_socket.close()
server_socket.close()
