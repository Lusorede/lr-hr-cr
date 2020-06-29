#Neopixel Lusorede
#Author: Hugo Rodrigues
#Version: 0.04
#Lusorede
#email: hugo.rodrigues@lusorede.pt
import os
import os.path
import sys
import socket
import logging
import time







print "      Waiting for Bluetooth connection..."





server_inputs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_inputs.connect(('localhost', 50001))

print "      Please configure car slots."
while 1:
 
 input_send = 'ir06_slot_st'
 server_inputs.sendall(input_send)
 inputdata = server_inputs.recv(1024)
 print inputdata
 time.sleep(1)

 
time.sleep(0.5)






