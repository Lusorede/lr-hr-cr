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
from time import sleep, time
from rpi_ws281x import *
#from test import *
import argparse
print ""
print ""
print ""
print ""
print ""
print "LR-CR staring..."
print "Please waiting.."
if os.path.isfile('btvars.py'):
  import btvars
  scri = btvars.scri 
  scre = btvars.scre
  scgi = btvars.scgi 
  scge = btvars.scge
  scbi = btvars.scbi
  scbe = btvars.scbe
  scyi = btvars.scyi
  scye = btvars.scye


if os.path.isfile('btstrip.py'):
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

if os.path.isfile('inputs.py'):
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
GPIO.setwarnings(True)
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
IR01_ST = 0
IR02_ST = 0
IR03_ST = 0
IR04_ST = 0
IR05_ST = 0
IR06_ST = 0
IR07_ST = 0
IR08_ST = 0

IR01_ST = IR01_ST + IR01_ST
IR02_ST = IR02_ST + IR02_ST
IR03_ST = IR03_ST + IR03_ST
IR04_ST = IR04_ST + IR04_ST
IR05_ST = IR05_ST + IR05_ST
IR06_ST = IR06_ST + IR06_ST
IR07_ST = IR07_ST + IR07_ST
IR08_ST = IR08_ST + IR08_ST








sleep(0.5)

# Bluetooh Connection

print "Waiting for Bluetooth connection..."

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address = server_socket.accept()
print "Accepted connection from ",address

sleep(0.5)
print "Please configure car slots."


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
   print ("Car Slot are configured as " )
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
   sred_st = 1
   sgreen_st = 0
   sblue_st = 0
   syellow_st = 0
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
   sred_st = 0
   sgreen_st = 1
   sblue_st = 0
   syellow_st = 0
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
   sred_st = 0
   sgreen_st = 0
   sblue_st = 1
   syellow_st = 0
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
   sred_st = 0
   sgreen_st = 0
   sblue_st = 0
   syellow_st = 1
   client_socket.send(data)
   
def check_basket():
 print ("check_basket")  
 res_red = sum(i for i in IR_RED)
 res_green = sum(i for i in IR_GREEN)
 res_blue = sum(i for i in IR_BLUE)
 res_yellow = sum(i for i in IR_YELLOW)
 print IR_BLUE
 
 
 if (sred_st == 0):
  if res_red > 1:
   print "Wrong Basket"
 if (sred_st == 1):
  if res_red > 1:
   print "Correct Basket"
 if (sgreen_st == 0):
  if res_green > 1:
   print "Wrong Basket"
 if (sgreen_st == 1):
  if res_green > 1:
   print "Correct Basket"  
 if (sblue_st == 0):
  if res_blue > 1:
   print "Wrong Basket"
 if (sblue_st == 1):
  if res_blue > 1:
   print "Correct Basket" 
 if (syellow_st == 0):
  if res_yellow > 1:
   print "Wrong Basket"
 if (syellow_st == 1):
  if res_yellow > 1:
   print "Correct Basket"
 print res_red
 print res_green
 print res_blue
 print res_yellow

strip1 = Adafruit_NeoPixel(LED_COUNT, LED_PIN1, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip2 = Adafruit_NeoPixel(LED_COUNT, LED_PIN2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, 1)
strip1.begin()
strip2.begin()

################################
# IR SENSORS
################################
IR01_ST_I = 0
IR02_ST_I = 0
IR03_ST_I = 0
IR04_ST_I = 0
IR05_ST_I = 0
IR06_ST_I = 0
IR07_ST_I = 0
IR08_ST_I = 0


def reg_matrix():
 res_red = sum(i for i in IR_RED)
 res_green = sum(i for i in IR_GREEN)
 res_blue = sum(i for i in IR_BLUE)
 res_yellow = sum(i for i in IR_YELLOW)
 print res_Blue
 
def ir_slot01(channel):
 if IR_Sensor_1:
  client_socket.send('ir_slot01')
  IR01_ST = 1
 else:
  client_socket.send('ir_slot01_DOWN')
  IR01_ST = 0
def ir_slot02(channel):
 client_socket.send('ir_slot02')
def ir_slot03(channel):
 client_socket.send('ir_slot03')
def ir_slot04(channel):
 client_socket.send('ir_slot04')
def ir_slot05(channel):
 client_socket.send('ir_slot05')
def ir_slot06(channel):
 if GPIO.event_detected(IR_Sensor_6):
  #	IR06_ST = IR06_ST + 1
  IR06_ST = IR06_ST_I + 1
  IR06_ST = IR06_ST + IR06_ST
  reg_matrix()
  
  print IR06_ST
  print('Button 06 pressed')
  
  print IR_BLUE
 if IR_Sensor_6:
  client_socket.send('ir_slot06')

  #print IR06_ST
  check_basket()
  print "IR06_up"
 sleep(0.5)

def ir_slot07(channel):
 if IR_Sensor_7:
  client_socket.send('ir_slot07')
  IR07_ST = 1
  print IR07_ST
 IR07_ST = 0
 print IR07_ST 
def ir_slot08(channel):
 client_socket.send('ir_slot08')


# if GPIO.input(16)==1:
#  print "Open"
#if GPIO.input(36)==1:
# print "Open"
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
 if GPIO.event_detected(IR_Sensor_1):
  print('Button pressed')
  ir_slot01()
 if GPIO.event_detected(IR_Sensor_2):
  print('Button pressed')
  ir_slot02()
 if GPIO.event_detected(IR_Sensor_3):
  print('Button pressed')
  ir_slot03()
 if GPIO.event_detected(IR_Sensor_4):
  print('Button pressed')
  ir_slot04()
 if GPIO.event_detected(IR_Sensor_5):
  print('Button pressed')
  ir_slot05()
 
 if GPIO.event_detected(IR_Sensor_7):
  print('Button pressed')
  ir_slot07()
 if GPIO.event_detected(IR_Sensor_8):
  print('Button pressed')
  ir_slot08()      
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
  scre = scri + 7 + 8 * SLOT
  scgi = scre + 1
  scge = scgi + 0 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars02"):    
  print ("R7-G1-B0-Y0")
  scri = 0 * SLOT
  scre = scri + 6 + 7 * SLOT
  scgi = scre + 1
  scge = scgi + 1 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars03"):    
  print ("R6-G2-B0-Y0")
  scri = 0 * SLOT
  scre = scri + 5 + 6 * SLOT
  scgi = scre + 1
  scge = scgi + 1 + 2 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars04"):    
  print ("R6-G1-B1-Y0")
  scri = 0 * SLOT
  scre = scri + 5 + 6 * SLOT
  scgi = scre + 1
  scge = scgi + 1 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars05"):    
  print ("R5-G3-B0-Y0")
  scri = 0 * SLOT
  scre = scri + 4 + 5 * SLOT
  scgi = scre + 1
  scge = scgi + 2 + 3 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars06"):    
  print ("R5-G2-B1-Y0")
  scri = 0 * SLOT
  scre = scri + 4 + 5 * SLOT
  scgi = scre + 1
  scge = scgi + 1 + 2 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars07"):    
  print ("R5-G1-B1-Y1")
  scri = 0 * SLOT
  scre = scri + 4 + 5 * SLOT
  scgi = scre + 1
  scge = scgi + 1 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 1 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars08"):    
  print ("R4-G4-B0-Y0")
  scri = 0 * SLOT
  scre = scri + 3 + 4 * SLOT
  scgi = scre + 1
  scge = scgi + 3 + 4 * SLOT
  scbi = scge + 1
  scbe = scbi + 0 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars09"):    
  print ("R4-G3-B1-Y0")
  scri = 0 * SLOT
  scre = scri + 3 + 4 * SLOT
  scgi = scre + 1
  scge = scgi + 2 + 3 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars10"):    
  print ("R4-G2-B2-Y0")
  scri = 0 * SLOT
  scre = scri + 3 + 4 * SLOT
  scgi = scre + 1
  scge = scgi + 1 + 2 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 + 2 * SLOT
  scyi = scbe + 1
  scye = scyi + 0 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars11"):    
  print ("R4-G2-B1-Y1")
  scri = 0 * SLOT
  scre = scri + 3 + 4 * SLOT
  scgi = scre + 1
  scge = scgi + 1 + 2 * SLOT
  scbi = scge + 1
  scbe = scbi + 1 * SLOT
  scyi = scbe + 1
  scye = scyi + 1 * SLOT
  configlabel = data
  carconfig()
 if (data == "cars12"):    
   print ("R3-G3-B2-Y0")
   scri = 0 * SLOT
   scre = scri + 2 + 3 * SLOT
   scgi = scre + 1
   scge = scgi + 2 + 3 * SLOT
   scbi = scge + 1
   scbe = scbi + 1 + 2 * SLOT
   scyi = scbe + 1
   scye = scyi + 0 * SLOT
   configlabel = data
   carconfig() 
 if (data == "cars13"):    
   print ("R3-G3-B1-Y1")
   scri = 0 * SLOT
   scre = scri + 2 + 3 * SLOT
   scgi = scre + 1
   scge = scgi + 2 + 3 * SLOT
   scbi = scge + 1
   scbe = scbi + 1 * SLOT
   scyi = scbe + 1
   scye = scyi + 1 * SLOT
   configlabel = data
   carconfig()
 if (data == "cars14"):    
   print ("R3-G2-B2-Y1")
   scri = 0 * SLOT
   scre = scri + 2 + 3 * SLOT
   scgi = scre + 1
   scge = scgi + 1 + 2 * SLOT
   scbi = scge + 1
   scbe = scbi + 1 + 2 * SLOT
   scyi = scbe + 1
   scye = scyi + 1 * SLOT
   configlabel = data
   carconfig() 
 if (data == "cars15"):    
   print ("R2-G2-B2-Y2")
   scri = 0 * SLOT
   scre = scri + 1 + 2 * SLOT
   scgi = scre + 1
   scge = scgi + 1 + 2 * SLOT
   scbi = scge + 1
   scbe = scbi + 1 + 2 * SLOT
   scyi = scbe + 1
   scye = scyi + 1 + 2 * SLOT
   IR_RED = [IR01_ST,IR02_ST]
   IR_GREEN = [IR03_ST,IR04_ST]
   IR_BLUE = [IR05_ST,IR06_ST]
   IR_YELLOW = [IR07_ST,IR08_ST]
   configlabel = data
   carconfig()  
   print IR_BLUE

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
       strip1.setPixelColor(i,  Color(colorr,colorg,colorb))
       strip2.setPixelColor(i,  Color(colorr,colorg,colorb))
  strip1.show()
  strip2.show()
  
client_socket.close()
server_socket.close()