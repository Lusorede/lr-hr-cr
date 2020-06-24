import struct
from bluepy.btle import *


class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print(data)

per = Peripheral("4C:4E:03:08:5B:A9","random")
per.setDelegate(MyDelegate())

print("Connected")

try:
    per.writeCharacteristic(14,bytes('aa','utf-8'))
    print("writing done")
    while True:
        if per.waitForNotifications(1.0):
            print("Notification")
            continue
    print("Waiting")
finally:
    per.disconnect()
    print ("Disconnected")
