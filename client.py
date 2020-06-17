from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("DF:57:3E:D5:08:E7", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()
