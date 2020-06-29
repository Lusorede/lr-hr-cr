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
import threading
import logging
import logging.handlers
import bluetooth
import RPi.GPIO as GPIO
import time
import pexpect
from rpi_ws281x import *
import argparse
import dbus
from advertisement import Advertisement
from service import Application, Service, Characteristic, Descriptor
from gpiozero  import CPUTemperature
hostname = socket.gethostname()
GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
NOTIFY_TIMEOUT = 1000

class LCAdvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.add_local_name(hostname)
        self.add_local_sn(hostname)
        self.include_tx_power = True

#class LCService(Service):
#    LC_SVC_UUID = "00000001-6c75-736f-7264-6c726875676f"
#
#    def __init__(self, index):
#        self.cartype = True
#
#        Service.__init__(self, index, self.LC_SVC_UUID, True)
#        self.add_characteristic(LCCharacteristic(self))
#        self.add_characteristic(UnitCharacteristic(self))
#
#    def is_cartype(self):
#        return self.cartype
#
#    def set_cartype(self, cartype):
#        self.cartype = cartype
#
##class LCCharacteristic(Characteristic):
#    LC_CHARACTERISTIC_UUID = "00000002-6c75-736f-7264-6c726875676f"
#
#    def __init__(self, service):
#        self.notifying = False
#
#        Characteristic.__init__(
#                self, self.LC_CHARACTERISTIC_UUID,
#                ["notify", "read"], service)
#        self.add_descriptor(LCDescriptor(self))
#
#    def get_temperature(self):
#        value = []
#        unit = "C"
#
#        cpu = CPUTemperature()
#        temp = cpu.temperature
#        if self.service.is_cartype():
#            temp = (temp * 1.8) + 32
#            unit = "F"
#
#        strtemp = str(round(temp, 1)) + " " + unit
#        for c in strtemp:
#            value.append(dbus.Byte(c.encode()))
#
#        return value
#
#    def set_temperature_callback(self):
#        if self.notifying:
#            value = self.get_temperature()
#            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
#
#        return self.notifying
#
#    def StartNotify(self):
#        if self.notifying:
#            return
#
#        self.notifying = True
#
#        value = self.get_temperature()
#        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
#        self.add_timeout(NOTIFY_TIMEOUT, self.set_temperature_callback)
#
#    def StopNotify(self):
#        self.notifying = False
#
#    def ReadValue(self, options):
#        value = self.get_temperature()
#
#        return value
#
#class LCDescriptor(Descriptor):
#    LC_DESCRIPTOR_UUID = "2901"
#    LC_DESCRIPTOR_VALUE = "CPU Temperature"
#
#    def __init__(self, characteristic):
#        Descriptor.__init__(
#                self, self.LC_DESCRIPTOR_UUID,
#                ["read"],
#                characteristic)
#
#    def ReadValue(self, options):
#        value = []
#        desc = self.LC_DESCRIPTOR_VALUE
#
#        for c in desc:
#            value.append(dbus.Byte(c.encode()))
#
#        return value
#
#class UnitCharacteristic(Characteristic):
#    UNIT_CHARACTERISTIC_UUID = "00000003-6c75-736f-7264-6c726875676f"
#
#    def __init__(self, service):
#        Characteristic.__init__(
#                self, self.UNIT_CHARACTERISTIC_UUID,
#                ["read", "write"], service)
#        self.add_descriptor(UnitDescriptor(self))
#
#    def WriteValue(self, value, options):
#        val = str(value[0]).upper()
#        if val == "C":
#            self.service.set_cartype(False)
#        elif val == "F":
#            self.service.set_farenheit(True)
#
#    def ReadValue(self, options):
#        value = []
#
#        if self.service.is_farenheit(): val = "F"
#        else: val = "C"
#        value.append(dbus.Byte(val.encode()))
#
#        return value
#
#class UnitDescriptor(Descriptor):
#    UNIT_DESCRIPTOR_UUID = "2901"
#    UNIT_DESCRIPTOR_VALUE = "Temperature Units (F or C)"
#
#    def __init__(self, characteristic):
#        Descriptor.__init__(
#                self, self.UNIT_DESCRIPTOR_UUID,
#                ["read"],
#                characteristic)
#
#    def ReadValue(self, options):
#        value = []
#        desc = self.UNIT_DESCRIPTOR_VALUE
#
#        for c in desc:
#            value.append(dbus.Byte(c.encode()))
#
#        return value
#
######################

class LCIRService(Service):
    LCIR_SVC_UUID = "00001800-6c75-736f-7264-6c726875676f"

    def __init__(self, index):
        self.cartype = "teste"

        Service.__init__(self, index, self.LCIR_SVC_UUID, True)
        self.add_characteristic(LCIR01Characteristic(self))
        self.add_characteristic(LCIR02Characteristic(self))
        self.add_characteristic(LCIR03Characteristic(self))
        self.add_characteristic(LCIR04Characteristic(self))
        self.add_characteristic(LCIR05Characteristic(self))
        self.add_characteristic(LCIR06Characteristic(self))
        self.add_characteristic(LCIR07Characteristic(self))
        self.add_characteristic(LCIR08Characteristic(self))
        self.add_characteristic(LCIRWBCharacteristic(self))
        self.add_characteristic(LCIRCBCharacteristic(self))
        self.add_characteristic(CarTypeCharacteristic(self))

    def is_cartype(self):
        return self.cartype

    def set_cartype(self, cartype):
        self.cartype = cartype
class LCIR01Characteristic(Characteristic):
    LCIR01_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349523031"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.LCIR01_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(LCIR01Descriptor(self))

    def get_ir01(self):
        value = []
        #value = [1]
        unit = "C"

        #cpu = CPUTemperature()
        #cpu = ir_slot06_t(slot_type,slot_active)
        #cpu = ir_slot06_t()
        #cpu = 1
        #temp = cpu.temperature
        #value = 1
        #irst = 1
        irst = n.ir_slot06_t(slot_type,slot_active)
        print irst
        #if self.service.is_cartype():
        #    temp = (temp * 1.8) + 32
        #    unit = "F"
        #
        #strtemp = str(round(temp, 1)) + " " + unit
        strtemp = str(irst)
        for c in strtemp:
            value.append(dbus.Byte(c.encode()))

        return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_ir01()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_ir01()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_ir01()

        return value
class LCIR02Characteristic(Characteristic):
    LCIR02_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349523032"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.LCIR02_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(LCIR02Descriptor(self))

    def get_ir02(self):
        value = []
        #value = [1]
        unit = "C"

        #cpu = CPUTemperature()
        #cpu = ir_slot06_t(slot_type,slot_active)
        #cpu = ir_slot06_t()
        #cpu = 1
        #temp = cpu.temperature
        #value = 1
        #irst = 1
        irst = n.ir_slot06_t(slot_type,slot_active)
        print irst
        #if self.service.is_cartype():
        #    temp = (temp * 1.8) + 32
        #    unit = "F"
        #
        #strtemp = str(round(temp, 1)) + " " + unit
        strtemp = str(irst)
        for c in strtemp:
            value.append(dbus.Byte(c.encode()))

        return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_ir02()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_ir02()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_ir02()

        return value
class LCIR03Characteristic(Characteristic):
    LCIR03_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349523033"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.LCIR03_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(LCIR03Descriptor(self))

    def get_ir03(self):
        value = []
        #value = [1]
        unit = "C"

        #cpu = CPUTemperature()
        #cpu = ir_slot06_t(slot_type,slot_active)
        #cpu = ir_slot06_t()
        #cpu = 1
        #temp = cpu.temperature
        #value = 1
        #irst = 1
        irst = n.ir_slot06_t(slot_type,slot_active)
        print irst
        #if self.service.is_cartype():
        #    temp = (temp * 1.8) + 32
        #    unit = "F"
        #
        #strtemp = str(round(temp, 1)) + " " + unit
        strtemp = str(irst)
        for c in strtemp:
            value.append(dbus.Byte(c.encode()))

        return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_ir03()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_ir03()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_ir03()

        return value
class LCIR04Characteristic(Characteristic):
    LCIR04_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349523034"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.LCIR04_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(LCIR04Descriptor(self))

    def get_ir04(self):
        value = []
        #value = [1]
        unit = "C"

        #cpu = CPUTemperature()
        #cpu = ir_slot06_t(slot_type,slot_active)
        #cpu = ir_slot06_t()
        #cpu = 1
        #temp = cpu.temperature
        #value = 1
        #irst = 1
        irst = n.ir_slot06_t(slot_type,slot_active)
        print irst
        #if self.service.is_cartype():
        #    temp = (temp * 1.8) + 32
        #    unit = "F"
        #
        #strtemp = str(round(temp, 1)) + " " + unit
        strtemp = str(irst)
        for c in strtemp:
            value.append(dbus.Byte(c.encode()))

        return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_ir04()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_ir04()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_ir04()

        return value
class LCIR05Characteristic(Characteristic):
    LCIR05_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349523035"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.LCIR05_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(LCIR05Descriptor(self))

    def get_ir05(self):
        value = []
        #value = [1]
        unit = "C"

        #cpu = CPUTemperature()
        #cpu = ir_slot06_t(slot_type,slot_active)
        #cpu = ir_slot06_t()
        #cpu = 1
        #temp = cpu.temperature
        #value = 1
        #irst = 1
        irst = n.ir_slot06_t(slot_type,slot_active)
        print irst
        #if self.service.is_cartype():
        #    temp = (temp * 1.8) + 32
        #    unit = "F"
        #
        #strtemp = str(round(temp, 1)) + " " + unit
        strtemp = str(irst)
        for c in strtemp:
            value.append(dbus.Byte(c.encode()))

        return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_ir05()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_ir05()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_ir05()

        return value

class LCIR06Characteristic(Characteristic):
    LCIR06_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349523036"

    def __init__(self, service):
        self.notifying = False
        self.indicating = False

        Characteristic.__init__(
                self, self.LCIR06_CHARACTERISTIC_UUID,
                ["notify", "read", "indicate"], service)
        self.add_descriptor(LCIR06Descriptor(self))

    def get_ir06(self):
		value = []
		data_send = "ir06_slot_st"
		con(data_send)
		data = s.recv(1024)
		print "ir06_slot_st"
		print data
		strtemp = str(data)
		
		for c in strtemp:
		 value.append(dbus.Byte(c.encode()))

		return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_ir06()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_ir06()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False
	
    def StartIndicate(self):
        if self.indicating:
         return

        self.indicating = True

        value = self.get_ir06()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopIndicate(self):
        self.indicating = False

    def ReadValue(self, options):
        value = self.get_ir06()

        return value
class LCIR07Characteristic(Characteristic):
    LCIR07_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349523037"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.LCIR07_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(LCIR07Descriptor(self))

    def get_ir07(self):
        value = []
        #value = [1]
        unit = "C"

        #cpu = CPUTemperature()
        #cpu = ir_slot06_t(slot_type,slot_active)
        #cpu = ir_slot06_t()
        #cpu = 1
        #temp = cpu.temperature
        #value = 1
        #irst = 1
        irst = n.ir_slot06_t(slot_type,slot_active)
        print irst
        #if self.service.is_cartype():
        #    temp = (temp * 1.8) + 32
        #    unit = "F"
        #
        #strtemp = str(round(temp, 1)) + " " + unit
        strtemp = str(irst)
        for c in strtemp:
            value.append(dbus.Byte(c.encode()))

        return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_ir06()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_ir07()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_ir07()

        return value
class LCIR08Characteristic(Characteristic):
    LCIR08_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349523038"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.LCIR08_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(LCIR08Descriptor(self))

    def get_ir08(self):
        value = []
        #value = [1]
        unit = "C"

        #cpu = CPUTemperature()
        #cpu = ir_slot06_t(slot_type,slot_active)
        #cpu = ir_slot06_t()
        #cpu = 1
        #temp = cpu.temperature
        #value = 1
        #irst = 1
        irst = n.ir_slot06_t(slot_type,slot_active)
        print irst
        #if self.service.is_cartype():
        #    temp = (temp * 1.8) + 32
        #    unit = "F"
        #
        #strtemp = str(round(temp, 1)) + " " + unit
        strtemp = str(irst)
        for c in strtemp:
            value.append(dbus.Byte(c.encode()))

        return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_ir08()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_ir08()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_ir08()

        return value
class LCIRWBCharacteristic(Characteristic):
    LCIRWB_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349525742"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.LCIRWB_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(LCIRWBDescriptor(self))

    def get_IRWB(self):
        value = []
        #value = [1]
        unit = "C"

        #cpu = CPUTemperature()
        #cpu = ir_slot06_t(slot_type,slot_active)
        #cpu = ir_slot06_t()
        #cpu = 1
        #temp = cpu.temperature
        #value = 1
        #irst = 1
        irst = n.ir_slot06_t(slot_type,slot_active)
        print irst
        #if self.service.is_cartype():
        #    temp = (temp * 1.8) + 32
        #    unit = "F"
        #
        #strtemp = str(round(temp, 1)) + " " + unit
        strtemp = str(irst)
        for c in strtemp:
            value.append(dbus.Byte(c.encode()))

        return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_IRWB()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_IRWB()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_IRWB()

        return value
class LCIRCBCharacteristic(Characteristic):
    LCIRCB_CHARACTERISTIC_UUID = "00002A56-6c75-736f-7264-4c4349524342"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.LCIRCB_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(LCIRCBDescriptor(self))

    def get_IRWB(self):
        value = []
        #value = [1]
        unit = "C"

        #cpu = CPUTemperature()
        #cpu = ir_slot06_t(slot_type,slot_active)
        #cpu = ir_slot06_t()
        #cpu = 1
        #temp = cpu.temperature
        #value = 1
        #irst = 1
        irst = n.ir_slot06_t(slot_type,slot_active)
        print irst
        #if self.service.is_cartype():
        #    temp = (temp * 1.8) + 32
        #    unit = "F"
        #
        #strtemp = str(round(temp, 1)) + " " + unit
        strtemp = str(irst)
        for c in strtemp:
            value.append(dbus.Byte(c.encode()))

        return value

    def set_irst_callback(self):
        if self.notifying:
            value = self.get_IRWB()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True

        value = self.get_IRWB()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_irst_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_IRWB()

        return value




		
class LCIR01Descriptor(Descriptor):
    LCIR01_DESCRIPTOR_UUID = "2901"
    LCIR01_DESCRIPTOR_VALUE = "IR01"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIR01_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIR01_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
class LCIR02Descriptor(Descriptor):
    LCIR02_DESCRIPTOR_UUID = "2901"
    LCIR02_DESCRIPTOR_VALUE = "IR02"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIR02_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIR02_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
class LCIR03Descriptor(Descriptor):
    LCIR03_DESCRIPTOR_UUID = "2901"
    LCIR03_DESCRIPTOR_VALUE = "IR03"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIR03_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIR03_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
class LCIR04Descriptor(Descriptor):
    LCIR04_DESCRIPTOR_UUID = "2901"
    LCIR04_DESCRIPTOR_VALUE = "IR04"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIR04_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIR04_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
class LCIR05Descriptor(Descriptor):
    LCIR05_DESCRIPTOR_UUID = "2901"
    LCIR05_DESCRIPTOR_VALUE = "IR05"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIR05_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIR05_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
class LCIR06Descriptor(Descriptor):
    LCIR06_DESCRIPTOR_UUID = "2901"
    LCIR06_DESCRIPTOR_VALUE = "IR06"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIR06_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIR06_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
class LCIR07Descriptor(Descriptor):
    LCIR07_DESCRIPTOR_UUID = "2901"
    LCIR07_DESCRIPTOR_VALUE = "IR07"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIR07_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIR07_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
class LCIR08Descriptor(Descriptor):
    LCIR08_DESCRIPTOR_UUID = "2901"
    LCIR08_DESCRIPTOR_VALUE = "IR08"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIR08_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIR08_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
class LCIRWBDescriptor(Descriptor):
    LCIRWB_DESCRIPTOR_UUID = "2901"
    LCIRWB_DESCRIPTOR_VALUE = "IRWB"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIRWB_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIRWB_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
class LCIRCBDescriptor(Descriptor):
    LCIRCB_DESCRIPTOR_UUID = "2901"
    LCIRCB_DESCRIPTOR_VALUE = "IRCB"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.LCIRCB_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.LCIRCB_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value

class CarTypeCharacteristic(Characteristic):
    CarType_CHARACTERISTIC_UUID = "4c75736f-7265-6465-736f-6c726875676f"
    #con = con(val)
    def __init__(self, service):
        Characteristic.__init__(
                self, self.CarType_CHARACTERISTIC_UUID,
                ["read", "write"], service)
        self.add_descriptor(CarTypeDescriptor(self))

    #def WriteValue(self, value, options):
    #    val = str(value[0]).upper()
    #    if val == "C":
    #        self.service.set_cartype(False)
    #    elif val == "F":
    #        self.service.set_cartype(True)
    def WriteValue(self, value, options):
	   n = 1
	   n = n + 1
	   val = str(value).upper()
	   val =("%s" % ''.join([str(v) for v in value]))
	   data_send = val
	   if n > 0:  
	    n = 0
	    con(data_send)
		
	   self.service.set_cartype(data_send)
	   #print data
    def ReadValue(self, options):
        value = []
        value = self.service.is_cartype

        #if self.service.is_cartype(): val = "F"
        #else: val = "C"
        #value.append(dbus.Byte(val.encode()))

        return value
	
		
class CarTypeDescriptor(Descriptor):
    CarType_DESCRIPTOR_UUID = "2901"
    CarType_DESCRIPTOR_VALUE = "Car Commands"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.CarType_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.CarType_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value

class CollectInputs():
 def collect(self):
   while 1:
    input_send = 'ir06_slot_st'
    con_input(input_send)
    inputdata = s.recv(1024)
    print inputdata
    time.sleep(1)
		
		
#def printit(ir06_slot_st):
#  st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  st.connect(('localhost', 50000))
#  time.sleep(1)
#  ir_st = "ir06_slot_st"
#  #con_ir_st(ir_st)
#  print ir_st
#  time.sleep(50/1000)
#  st.sendall("ir06_slot_st")
#  data = st.recv(1024)
#  return data



def con(data_send):
 s.sendall(data_send)
 data = s.recv(1024)
 return data
def con_input(input_send):
 server_inputs.sendall(input_send)
 inputdata = s.recv(1024)
 return inputdata
 #s.close()
 #print 'Received', repr(data)
#def con_ir_st(ir_st):
# st.sendall(ir_st)
# data = st.recv(1024)
# return ir_st
 #s.close()
 #print 'Received', repr(data)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
time.sleep(50/1000)
server_inputs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_inputs.connect(('localhost', 50000))




##class CollectIR():
## while True:
##  time.sleep(1)
##  ir_st = "ir06_slot_st"
##  con_ir_st(ir_st)
##  print ir_st
##  time.sleep(50/1000)


#########################		

app = Application()
#app.add_service(LCService(0))
app.add_service(LCIRService(0))

app.register()

adv = LCAdvertisement(0)
adv.register()


try:
    app.run()
    
except KeyboardInterrupt:
    app.quit()
    server_inputs.close()

 