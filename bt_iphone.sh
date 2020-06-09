#!/bin/sh
sudo hciconfig hci0 sspmode 1 # Activate SSP which is the current standard
# for bluetooth pairing, this will make the RPi discoverable again but
# with a passkey instead of a PIN code
echo -e "'power off\n quit ' | bluetoothctl" # Make the RPi undiscoverable
sleep 5
echo -e "'power on\n quit ' | bluetoothctl" # Make the RPi discoverable again
sleep 1
sudo hciconfig hci0 sspmode 0 # Deactivate SSP and activate PIN code authentication
exit 0