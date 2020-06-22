#Neopixel Lusorede
#Author: Hugo Rodrigues
#Version: 0.04
#Lusorede
#email: hugo.rodrigues@lusorede.pt
import os
import os.path
import sys
import glob
import socket
import logging
import logging.handlers
import bluetooth
import RPi.GPIO as GPIO
import time
from rpi_ws281x import *
import argparse

#####################
#LOG_FILENAME = '/var/log/bt-work-py.log'
## Set up a specific logger with our desired output level
#bt_logger = logging.getLogger('BTLogger')
#bt_logger.setLevel(logging.DEBUG)
#
## Add the log message handler to the logger
#handler = logging.handlers.RotatingFileHandler(
#              LOG_FILENAME, maxBytes=20, backupCount=5)
#
#bt_logger.addHandler(handler)
#
## Log some messages
#for i in range(20):
#    bt_logger.debug('i = %d' % i)
#
## See what files are created
#logfiles = glob.glob('%s*' % LOG_FILENAME)
#
#for filename in logfiles:
#    print filename

def clear_screen(): 
 _ = os.system('clear') 

time.sleep(5)
clear_screen()
print "       "
print "       "
print "       "
print "                                ##############################################"
print "                                #            Neopixel Lusorede               #"
print "                                #            Version: 0.04                   #"
print "                                #                Beta Test                   #"
print "                                #               development                  #"
print "                                #                                            #"
print "                                #           ",socket.gethostname(),"            #"
print "                                #                                            #"
print "                                #           suporte@lusorede.pt              #"
print "                                #                                            #"
print "                                ##############################################"
print "       "
print "       "
print "       "
print "       "
print "       "
print "                                 #           #       #    ########    ########    ########    ########    #####       ########    "
print "                                 #           #       #    #           #      #    #      #    #           #     #     #           "
print "                                 #           #       #    #           #      #    #      #    #           #      #    #           "
print "                                 #           #       #    #           #      #    #      #    #           #      #    #           "
print "                                 #           #       #    ########    #      #    ########    ########    #      #    ########    "
print "                                 #           #       #           #    #      #    #   #       #           #      #    #           "
print "                                 #           #       #           #    #      #    #    #      #           #      #    #           "
print "                                 #           #       #           #    #      #    #     #     #           #     #     #           "
print "                                 ########    #########    ########    ########    #      #    ########    ######      ########    "
print "       "
print "       "
print "       "
print "       "
print "       "
print "                                 LR-CR staring..."
print "                                 Please waiting.."
print "       "
print "       "
print "       "
print "       "
print "       "
if os.path.isfile('/home/ubuntu/lr-hr-cr/btvars.py'):
  import btvars
  scri = btvars.scri 
  scre = btvars.scre
  scgi = btvars.scgi 
  scge = btvars.scge
  scbi = btvars.scbi
  scbe = btvars.scbe
  scyi = btvars.scyi
  scye = btvars.scye


if os.path.isfile('/home/ubuntu/lr-hr-cr/btstrip.py'):
  import btstrip
  LED_COUNT = btstrip.LED_COUNT     
  LED_PIN1   = btstrip.LED_PIN1 
  LED_PIN2   = btstrip.LED_PIN2 
  LED_INVERT = btstrip.LED_INVERT 
  LED_FREQ_HZ = btstrip.LED_FREQ_HZ   
  LED_DMA = btstrip.LED_DMA  
  LED_BRIGHTNESS = btstrip.LED_BRIGHTNESS
  LED_CHANNEL    = btstrip.LED_CHANNEL
  LED_IN_SLOT = btstrip.LED_IN_SLOT
  N_SLOTS = btstrip.N_SLOTS

if os.path.isfile('/home/ubuntu/lr-hr-cr/inputs.py'):
  import inputs
  IR_Sensor_1 = inputs.IR_Sensor_1
  IR_Sensor_2 = inputs.IR_Sensor_2
  IR_Sensor_3 = inputs.IR_Sensor_3
  IR_Sensor_4 = inputs.IR_Sensor_4
  IR_Sensor_5 = inputs.IR_Sensor_5
  IR_Sensor_6 = inputs.IR_Sensor_6
  IR_Sensor_7 = inputs.IR_Sensor_7
  IR_Sensor_8 = inputs.IR_Sensor_8
  I_Restart = inputs.I_Restart
  I_Pair = inputs.I_Pair
  IR_time = inputs.IR_time
  Restart_time = inputs.Restart_time
  Pair_time = inputs.Pair_time
  
  


#LED_COUNT      = 59      # Number of LED pixels.
#LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PW$
##LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses S$
#LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800kh$
#LED_DMA        = 10      # DMA channel to use for generating signal (tr$
#LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
#LED_INVERT     = False   # True to invert the signal (when using NPN tr$
#LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

SLOT = (LED_COUNT - LED_IN_SLOT) / N_SLOTS

sred_st=0
sgreen_st=0
sblue_st=0
syellow_st=0
slot_type = 9999
slot_active = 9999

#LED=21

#IR_Sensor_1 = 6
#IR_Sensor_2 = 13
#IR_Sensor_3 = 19
#IR_Sensor_4 = 26
#IR_Sensor_5 = 12
#IR_Sensor_6 = 16
#IR_Sensor_7 = 20
#IR_Sensor_8 = 21


configlabel = 'undefined'
  
GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setwarnings(False)
channels = [LED_PIN1,LED_PIN2]
GPIO.cleanup(channels)
GPIO.setup (LED_PIN1,GPIO.OUT)
GPIO.output (LED_PIN1,0)
GPIO.setup (LED_PIN2,GPIO.OUT)
GPIO.output (LED_PIN2,1)
GPIO.setup (IR_Sensor_1,GPIO.IN,GPIO.PUD_UP)
GPIO.setup (IR_Sensor_2,GPIO.IN,GPIO.PUD_UP)
GPIO.setup (IR_Sensor_3,GPIO.IN,GPIO.PUD_UP)
GPIO.setup (IR_Sensor_4,GPIO.IN,GPIO.PUD_UP)
GPIO.setup (IR_Sensor_5,GPIO.IN,GPIO.PUD_UP)
GPIO.setup (IR_Sensor_6,GPIO.IN,GPIO.PUD_UP)
GPIO.setup (IR_Sensor_7,GPIO.IN,GPIO.PUD_UP)
GPIO.setup (IR_Sensor_8,GPIO.IN,GPIO.PUD_UP)
GPIO.setup (I_Restart,GPIO.IN,GPIO.PUD_UP)
GPIO.setup (I_Pair,GPIO.IN,GPIO.PUD_UP)

#GPIO.output(LED,0)











##### Strip Configuration

strip1 = Adafruit_NeoPixel(LED_COUNT, LED_PIN1, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip2 = Adafruit_NeoPixel(LED_COUNT, LED_PIN2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, 1)
strip1.begin()
strip2.begin()
def begin_car():
  for i in range (0,LED_COUNT):
       strip1.setPixelColor(i, Color(255,255,255))
       strip2.setPixelColor(i, Color(255,255,255))
  strip1.show()
  strip2.show()
def fin_car():
  for i in range (0,LED_COUNT):
       strip1.setPixelColor(i, Color(1,1,1))
       strip2.setPixelColor(i, Color(1,1,1))
  strip1.show()
  strip2.show()
begin_car()
time.sleep(500/1000)


def wait_bt_Connection():
  for i in range (0,LED_COUNT):
   strip1.setPixelColor(i, Color(204,255,0))
   strip2.setPixelColor(i, Color(204,255,0))
   
  strip1.show()
  strip2.show()
  time.sleep(1000/1000)
  



# Bluetooh Connection




print "      Waiting for Bluetooth connection..."

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address = server_socket.accept()
wait_bt_Connection()

print "      Accepted connection from ",address
add_con = str(address) + "_connect"
time.sleep(10/1000)
client_socket.send(add_con)
 
time.sleep(0.5)
print "      Please configure car slots."


def reg_var():
  f = open( 'btvars.py', 'w' )
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
   for i in range(strip1.numPixels()):
      strip1.setPixelColor(i, Color(0, 0, 0))
   for i in range(strip2.numPixels()):
      strip2.setPixelColor(i, Color(0, 0, 0))
   strip1.show()
   strip2.show()
def carconfig():
   clear()
   reg_var()
   for i in range (scri,scre):
       strip1.setPixelColor(i, 0xFF0000)
       strip2.setPixelColor(i, 0xFF0000)
   for i in range (scgi,scge):
       strip1.setPixelColor(i, 0x00FF00)
       strip2.setPixelColor(i, 0x00FF00)
   for i in range (scbi,scbe):
       strip1.setPixelColor(i, 0x0000FF)
       strip2.setPixelColor(i, 0x0000FF)
   for i in range (scyi,scye):
       strip1.setPixelColor(i, 0xFFFF00)
       strip2.setPixelColor(i, 0xFFFF00)
   strip1.show()
   strip2.show()
   client_socket.send(data)
   print ("      Car Slot Configuration" )
   print ("      " )
   print ("      " )
   print ("      " )
   print ("      " )
def sred():
   for i in range (scri,scre):
       strip1.setPixelColor(i, 0xFF0000)
       strip2.setPixelColor(i, 0xFF0000)
   for i in range (scgi,scge):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   for i in range (scbi,scbe):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   for i in range (scyi,scye):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   strip1.show()  
   strip2.show()  
   client_socket.send(data)
def sgreen():
   for i in range (scri,scre):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   for i in range (scgi,scge):
       strip1.setPixelColor(i, 0x00FF00)
       strip2.setPixelColor(i, 0x00FF00)
   for i in range (scbi,scbe):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   for i in range (scyi,scye):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   strip1.show()  
   strip2.show()  
   client_socket.send(data)   
def sblue():
   for i in range (scri,scre):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   for i in range (scgi,scge):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   for i in range (scbi,scbe):
       strip1.setPixelColor(i, 0x0000FF)
       strip2.setPixelColor(i, 0x0000FF)
   for i in range (scyi,scye):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   strip1.show()
   strip2.show()
   client_socket.send(data)  
def syellow():
   for i in range (scri,scre):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   for i in range (scgi,scge):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   for i in range (scbi,scbe):
       strip1.setPixelColor(i, 0x000000)
       strip2.setPixelColor(i, 0x000000)
   for i in range (scyi,scye):
       strip1.setPixelColor(i, 0xFFFF00)
       strip2.setPixelColor(i, 0xFFFF00)
   strip1.show() 
   strip2.show() 
   client_socket.send(data)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

#rainbow(strip1)
#rainbow(strip2)

				
################################
# IR SENSORS
################################

def ir_slot01(channel):
 client_socket.send('ir_slot01')
 ir_slot01_t(slot_type,slot_active)
def ir_slot02(channel):
 client_socket.send('ir_slot02')
 ir_slot02_t(slot_type,slot_active)
def ir_slot03(channel):
 client_socket.send('ir_slot03')
 ir_slot03_t(slot_type,slot_active)
def ir_slot04(channel):
 client_socket.send('ir_slot04')
 ir_slot04_t(slot_type,slot_active)
def ir_slot05(channel):
 client_socket.send('ir_slot05')
 ir_slot05_t(slot_type,slot_active)
def ir_slot06(channel):
 client_socket.send('ir_slot06')
 ir_slot06_t(slot_type,slot_active)
def ir_slot07(channel):
 client_socket.send('ir_slot07')
 ir_slot07_t(slot_type,slot_active)
def ir_slot08(channel):
 client_socket.send('ir_slot08')
 ir_slot08_t(slot_type,slot_active)
def ir_slot01_t(slot_type,slot_active):
 n=0
 if slot_type == 9999:
  print "      Please define Car Slot Type"
  client_socket.send('define_car')
 time.sleep(10/1000) 
 if slot_active == 0000:
  print "      Please Start Shopping"
  client_socket.send('define_slot_active')
  time.sleep(10/1000)
 if slot_active == 1000:
  if slot_type == 8000 or slot_type == 7100 or slot_type == 6200 or slot_type == 6110 or slot_type == 5300 or slot_type == 5210 or slot_type == 5111 or slot_type == 4400 or slot_type == 4310 or slot_type == 4220 or slot_type == 4211 or slot_type == 3320 or slot_type == 3311 or slot_type == 3221 or slot_type == 2222:
	n = 1
 if slot_active == 0100:
  if slot_type == 0001:
	n = 1	
 if slot_active == 0010:
  if slot_type == 0001:    
	n = 1 
 if slot_active == 0001:
  if slot_type == 0001:    
	n = 1 
 if n == 1:
  print "      Correct Basket"
  client_socket.send('correct_basket')
  time.sleep(10/1000)
 else:
	 print "      Wrong Basket"
	 client_socket.send('wrong_basket')
	 time.sleep(10/1000) 
def ir_slot02_t(slot_type,slot_active):
 n=0
 if slot_type == 9999:
  print "      Please define Car Slot Type"
  client_socket.send('define_car')
 time.sleep(10/1000) 
 if slot_active == 0000:
  print "      Please Start Shopping"
  client_socket.send('define_slot_active')
  time.sleep(10/1000)
 if slot_active == 1000:
  if slot_type == 8000 or slot_type == 7100 or slot_type == 6200 or slot_type == 6110 or slot_type == 5300 or slot_type == 5210 or slot_type == 5111 or slot_type == 4400 or slot_type == 4310 or slot_type == 4220 or slot_type == 4211 or slot_type == 3320 or slot_type == 3311 or slot_type == 3221 or slot_type == 2222:
	n = 1
 if slot_active == 0100:
  if slot_type == 0001:
	n = 1	
 if slot_active == 0010:
  if slot_type == 0001:    
	n = 1 
 if slot_active == 0001:
  if slot_type == 0001:    
	n = 1 
 if n == 1:
  print "      Correct Basket"
  client_socket.send('correct_basket')
  time.sleep(10/1000)
 else:
	 print "      Wrong Basket"
	 client_socket.send('wrong_basket')
	 time.sleep(10/1000) 
def ir_slot03_t(slot_type,slot_active):
 n=0
 if slot_type == 9999:
  print "      Please define Car Slot Type"
  client_socket.send('define_car')
 time.sleep(10/1000) 
 if slot_active == 0000:
  print "      Please Start Shopping"
  client_socket.send('define_slot_active')
  time.sleep(10/1000)
 if slot_active == 1000:
  if slot_type == 8000 or slot_type == 7100 or slot_type == 6200 or slot_type == 6110 or slot_type == 5300 or slot_type == 5210 or slot_type == 5111 or slot_type == 4400 or slot_type == 4310 or slot_type == 4220 or slot_type == 4211 or slot_type == 3320 or slot_type == 3311 or slot_type == 3221:
	n = 1
 if slot_active == 0100:
  if slot_type == 2222:
	n = 1	
 if slot_active == 0010:
  if slot_type == 0001:    
	n = 1 
 if slot_active == 0001:
  if slot_type == 0001:    
	n = 1 
 if n == 1:
  print "      Correct Basket"
  client_socket.send('correct_basket')
  time.sleep(10/1000)
 else:
	 print "      Wrong Basket"
	 client_socket.send('wrong_basket')
	 time.sleep(10/1000) 
def ir_slot04_t(slot_type,slot_active):
 n=0
 if slot_type == 9999:
  print "      Please define Car Slot Type"
  client_socket.send('define_car')
 time.sleep(10/1000) 
 if slot_active == 0000:
  print "      Please Start Shopping"
  client_socket.send('define_slot_active')
  time.sleep(10/1000)
 if slot_active == 1000:
  if slot_type == 8000 or slot_type == 7100 or slot_type == 6200 or slot_type == 6110 or slot_type == 5300 or slot_type == 5210 or slot_type == 5111 or slot_type == 4400 or slot_type == 4310 or slot_type == 4220 or slot_type == 4211:
	n = 1
 if slot_active == 0100:
  if slot_type == 3320 or slot_type == 3311 or slot_type == 3221 or slot_type == 2222:
	n = 1	
 if slot_active == 0010:
  if slot_type == 0001:    
	n = 1 
 if slot_active == 0001:
  if slot_type == 0001:    
	n = 1 
 if n == 1:
  print "      Correct Basket"
  client_socket.send('correct_basket')
  time.sleep(10/1000)
 else:
	 print "      Wrong Basket"
	 client_socket.send('wrong_basket')
	 time.sleep(10/1000) 
def ir_slot05_t(slot_type,slot_active):
 n=0
 if slot_type == 9999:
  print "      Please define Car Slot Type"
  client_socket.send('define_car')
 time.sleep(10/1000) 
 if slot_active == 0000:
  print "      Please Start Shopping"
  client_socket.send('define_slot_active')
  time.sleep(10/1000)
 if slot_active == 1000:
  if slot_type == 8000 or slot_type == 7100 or slot_type == 6200 or slot_type == 6110 or slot_type == 5300 or slot_type == 5210 or slot_type == 5111:
	n = 1
 if slot_active == 0100:
  if slot_type == 4400 or slot_type == 4310 or slot_type == 4220 or slot_type == 4211 or slot_type == 3320 or slot_type == 3311 or slot_type == 3221:
	n = 1	
 if slot_active == 0010:
  if slot_type == 2222:    
	n = 1 
 if slot_active == 0001:
  if slot_type == 0001:    
	n = 1 
 if n == 1:
  print "      Correct Basket"
  client_socket.send('correct_basket')
  time.sleep(10/1000)
 else:
	 print "      Wrong Basket"
	 client_socket.send('wrong_basket')
	 time.sleep(10/1000)
def ir_slot06_t(slot_type,slot_active):
 n=0
 if slot_type == 9999:
  print "      Please define Car Slot Type"
  client_socket.send('define_car')
 time.sleep(10/1000) 
 if slot_active == 0000:
  print "      Please Start Shopping"
  client_socket.send('define_slot_active')
  time.sleep(10/1000)
 if slot_active == 1000:
  if slot_type == 8000 or slot_type == 7100 or slot_type == 6200 or slot_type == 6110:
	n = 1
 if slot_active == 0100:
  if slot_type == 5300 or slot_type == 5210 or slot_type == 5111 or slot_type == 4400 or slot_type == 4310 or slot_type == 4220 or slot_type == 4211 or slot_type == 3320 or slot_type == 3311:
	n = 1	
 if slot_active == 0010:
  if slot_type == 3221 or slot_type == 2222:    
	n = 1 
 if slot_active == 0001:
  if slot_type == 0001:    
	n = 1 
 if n == 1:
  print "      Correct Basket"
  client_socket.send('correct_basket')
  time.sleep(10/1000)
 else:
	 print "      Wrong Basket"
	 client_socket.send('wrong_basket')
	 time.sleep(10/1000)
def ir_slot07_t(slot_type,slot_active):
 n=0
 if slot_type == 9999:
  print "      Please define Car Slot Type"
  client_socket.send('define_car')
 time.sleep(10/1000) 
 if slot_active == 0000:
  print "      Please Start Shopping"
  client_socket.send('define_slot_active')
  time.sleep(10/1000)
 if slot_active == 1000:
  if slot_type == 8000 or slot_type == 7100:
	n = 1
 if slot_active == 0100:
  if slot_type == 6200 or slot_type == 6110 or slot_type == 5300 or slot_type == 5210 or slot_type == 4400 or slot_type == 4310:
	n = 1	
 if slot_active == 0010:
  if slot_type == 5111 or slot_type == 4220 or slot_type == 4221 or slot_type == 3320 or slot_type == 3311 or slot_type == 3221:    
	n = 1 
 if slot_active == 0001:
  if slot_type == 2222:    
	n = 1 
 if n == 1:
  print "      Correct Basket"
  client_socket.send('correct_basket')
  time.sleep(10/1000)
 else:
	 print "      Wrong Basket"
	 client_socket.send('wrong_basket')
	 time.sleep(10/1000)  
def ir_slot08_t(slot_type,slot_active):
 n=0
 if slot_type == 9999:
  print "      Please define Car Slot Type"
  client_socket.send('define_car')
 time.sleep(10/1000) 
 if slot_active == 0000:
  print "      Please Start Shopping"
  client_socket.send('define_slot_active')
  time.sleep(10/1000)
 if slot_active == 1000:
  if slot_type == 8000:
	n = 1
 if slot_active == 0100:
  if slot_type == 7100 or slot_type == 6200 or slot_type == 5300 or slot_type == 4400:
	n = 1	
 if slot_active == 0010:
  if slot_type == 6110 or slot_type == 5210 or slot_type == 4310 or slot_type == 4220 or slot_type == 3320:    
	n = 1 
 if slot_active == 0001:
  if slot_type == 5111 or slot_type == 4211 or slot_type == 3311 or slot_type == 3221  or slot_type == 2222:    
	n = 1 
 if n == 1:
  print "      Correct Basket"
  client_socket.send('correct_basket')
  time.sleep(10/1000)
 else:
	 print "      Wrong Basket"
	 client_socket.send('wrong_basket')
	 time.sleep(10/1000)  


# if GPIO.input(16)==1:
#  print "      Open"
#if GPIO.input(36)==1:
# print "      Open"
GPIO.add_event_detect (IR_Sensor_1, GPIO.RISING, callback=ir_slot01, bouncetime=IR_time) #IR1 IR2 Slot 1 PIN31
GPIO.add_event_detect (IR_Sensor_2, GPIO.RISING, callback=ir_slot02, bouncetime=IR_time) #IR3 IR4 Slot 2 PIN33
GPIO.add_event_detect (IR_Sensor_3, GPIO.RISING, callback=ir_slot03, bouncetime=IR_time) #IR5 IR6 Slot 2 PIN35
GPIO.add_event_detect (IR_Sensor_4, GPIO.RISING, callback=ir_slot04, bouncetime=IR_time) #IR7 IR8 Slot 2 PIN37
GPIO.add_event_detect (IR_Sensor_5, GPIO.RISING, callback=ir_slot05, bouncetime=IR_time) #IR9 IR10 Slot 2 PIN32
GPIO.add_event_detect (IR_Sensor_6, GPIO.RISING, callback=ir_slot06, bouncetime=IR_time) #IR11 IR12 Slot 2 PIN36
GPIO.add_event_detect (IR_Sensor_7, GPIO.RISING, callback=ir_slot07, bouncetime=IR_time) #IR13 IR14 Slot 2 PIN30
GPIO.add_event_detect (IR_Sensor_8, GPIO.RISING, callback=ir_slot08, bouncetime=IR_time) #IR15 IR16 Slot 2 PIN40


                    












def in_restart(channel):
 client_socket.send('in_restart')
 os.system('systemctl reboot -i')
def bt_pair(channel):
 client_socket.send('bt_pair')	
	
GPIO.add_event_detect (I_Restart, GPIO.RISING, callback=in_restart, bouncetime=Restart_time) #Restart Button PIN29
GPIO.add_event_detect (I_Pair, GPIO.RISING, callback=bt_pair, bouncetime=Pair_time) #Pair BT Button PIN23



while 1:
    
  
  
  
  
  
 

 data = client_socket.recv(1024)
 print "      Received: %s" % data
#System Commnds
 if (data == "restart"):    #restart equipment
  print ("       ")
  print ("       ")
  print ("       ")
  print ("      Restart LC-CR")
  print ("      Please wait about 45s")
  print ("      ")
  print ("      ")
  print ("      ")
  print ("      ")
  print ("      ")
  os.system('systemctl reboot -i')

#Global Commands  
 if (data == "quit"):
   print ("      Quit")
   break
 if (data == "clear"):
   print ("      Clear")
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
   print ("      Reset Car Configuration")
 if (data == "reload"):
   print ("      Reload LR-CR")
   print ("      Please wait...")
   print ("      ")
   clear()
   os.system("systemctl restart bt-work")
#Car configuration
 if (data == "cars01"):  
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R8 | G0 | B0 | Y0 |")
  print ("      .----.----.----.----.")
  print ("      ")     
  scri = 0
  scre = scri + 7 + 8 * SLOT
  scgi = scre + 1
  scge = scgi + 0 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  slot_type = 8000
  configlabel = data
  carconfig()
 if (data == "cars02"): 
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R7 | G1 | B0 | Y0 |")
  print ("      .----.----.----.----.")
  print ("      ")     
  scri = 0 * SLOT
  scre = scri + 6 + 7 * SLOT
  scgi = scre + 1
  scge = scgi + 1 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  slot_type = 7100
  configlabel = data
  carconfig()
 if (data == "cars03"):  
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R6 | G2 | B0 | Y0 |")
  print ("      .----.----.----.----.")
  print ("      ")     
  scri = 0 * SLOT
  scre = scri + 5 + 6 * SLOT
  scgi = scre + 1
  scge = scgi + 1 + 2 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  slot_type = 6200
  configlabel = data
  carconfig()
 if (data == "cars04"):  
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R6 | G1 | B1 | Y0 |")
  print ("      .----.----.----.----.")
  print ("      ")   
  scri = 0 * SLOT
  scre = scri + 5 + 6 * SLOT
  scgi = scre + 1
  scge = scgi + 1 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  slot_type = 6110
  configlabel = data
  carconfig()
 if (data == "cars05"):  
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R5 | G3 | B0 | Y0 |")
  print ("      .----.----.----.----.")
  print ("      ") 
  scri = 0 * SLOT
  scre = scri + 4 + 5 * SLOT
  scgi = scre + 1
  scge = scgi + 2 + 3 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  slot_type = 5300
  configlabel = data
  carconfig()
 if (data == "cars06"): 
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R5 | G2 | B1 | Y0 |")
  print ("      .----.----.----.----.")
  print ("      ")   
  scri = 0 * SLOT
  scre = scri + 4 + 5 * SLOT
  scgi = scre + 1
  scge = scgi + 1 + 2 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  slot_type = 5210
  configlabel = data
  carconfig()
 if (data == "cars07"): 
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R5 | G1 | B1 | Y1 |")
  print ("      .----.----.----.----.")
  print ("      ")  
  scri = 0 * SLOT
  scre = scri + 4 + 5 * SLOT
  scgi = scre + 1
  scge = scgi + 1 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 1 * SLOT
  slot_type = 5111
  configlabel = data
  carconfig()
 if (data == "cars08"):  
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R4 | G4 | B0 | Y0 |")
  print ("      .----.----.----.----.")
  print ("      ")  
  scri = 0 * SLOT
  scre = scri + 3 + 4 * SLOT
  scgi = scre + 1
  scge = scgi + 3 + 4 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  slot_type = 4400
  configlabel = data
  carconfig()
 if (data == "cars09"):   
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R4 | G3 | B1 | Y0 |")
  print ("      .----.----.----.----.")
  print ("      ")  
  scri = 0 * SLOT
  scre = scri + 3 + 4 * SLOT
  scgi = scre + 1
  scge = scgi + 2 + 3 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  slot_type = 4310
  configlabel = data
  carconfig()
 if (data == "cars10"):
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R4 | G2 | B2 | Y0 |")
  print ("      .----.----.----.----.")
  print ("      ") 
  scri = 0 * SLOT
  scre = scri + 3 + 4 * SLOT
  scgi = scre + 1
  scge = scgi + 1 + 2 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 + 2 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  slot_type = 4220
  configlabel = data
  carconfig()
 if (data == "cars11"): 
  print ("      ")
  print ("      .----.----.----.----.")
  print ("      | R4 | G2 | B1 | Y1 |")
  print ("      .----.----.----.----.")
  print ("      ")   
  scri = 0 * SLOT
  scre = scri + 3 + 4 * SLOT
  scgi = scre + 1
  scge = scgi + 1 + 2 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 1 * SLOT
  slot_type = 4211
  configlabel = data
  carconfig()
 if (data == "cars12"):    
   print ("      ")
   print ("      .----.----.----.----.")
   print ("      | R3 | G3 | B2 | Y0 |")
   print ("      .----.----.----.----.")
   print ("      ")    
   scri = 0 * SLOT
   scre = scri + 2 + 3 * SLOT
   scgi = scre + 1
   scge = scgi + 2 + 3 * SLOT
   scbi = scge + 1
   scbe = scbi + 1 + 2 * SLOT
   scyi = scbe + 1
   scye = scyi + 0 * SLOT
   slot_type = 3320
   configlabel = data
   carconfig() 
 if (data == "cars13"):    
   print ("      ")
   print ("      .----.----.----.----.")
   print ("      | R3 | G3 | B1 | Y1 |")
   print ("      .----.----.----.----.")
   print ("      ")    
   scri = 0 * SLOT
   scre = scri + 2 + 3 * SLOT
   scgi = scre + 1
   scge = scgi + 2 + 3 * SLOT
   scbi = scge + 1
   scbe = scbi + 1 * SLOT
   scyi = scbe + 1
   scye = scyi + 1 * SLOT
   slot_type = 3311
   configlabel = data
   carconfig()
 if (data == "cars14"):    
   print ("      ")
   print ("      .----.----.----.----.")
   print ("      | R3 | G2 | B2 | Y1 |")
   print ("      .----.----.----.----.")
   print ("      ")   
   scri = 0 * SLOT
   scre = scri + 2 + 3 * SLOT
   scgi = scre + 1
   scge = scgi + 1 + 2 * SLOT
   scbi = scge + 1
   scbe = scbi + 1 + 2 * SLOT
   scyi = scbe + 1
   scye = scyi + 1 * SLOT
   slot_type = 3221
   configlabel = data
   carconfig() 
 if (data == "cars15"):    
   print ("      ")
   print ("      .----.----.----.----.")
   print ("      | R2 | G2 | B2 | Y2 |")
   print ("      .----.----.----.----.")
   print ("      ")
   scri = 0 * SLOT
   scre = scri + 1 + 2 * SLOT
   scgi = scre + 1
   scge = scgi + 1 + 2 * SLOT
   scbi = scge + 1
   scbe = scbi + 1 + 2 * SLOT
   scyi = scbe + 1
   scye = scyi + 1 + 2 * SLOT
   slot_type = 2222
   configlabel = data
   carconfig()

######
 if (data == "start"):    
   clear()
   slot_active = 0000
   print configlabel + " shop start"
 if (data == "sred"):    
   sred()
   slot_active = 1000
   print configlabel + " Red"
 if (data == "sblue"):    
   sblue()
   slot_active = 0010
   print configlabel + " Blue"
 if (data == "sgreen"):    
   sgreen()
   slot_active = 0100
   print configlabel + " Green"
 if (data == "syellow"):    
   syellow()
   slot_active = 0001
   print configlabel + " Yellow"
 if (data == "finalized"):    
   carconfig()
   slot_active = 0000
   print configlabel + " shop finalized"   
   fin_car()

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
       strip1.setPixelColor(i,  Color(colorr,colorg,colorb))
       strip2.setPixelColor(i,  Color(colorr,colorg,colorb))
  strip1.show()
  strip2.show()
  
client_socket.close()
server_socket.close()
