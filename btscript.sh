#!/bin/sh
btmac="$(hcitool dev | grep -o "[[:xdigit:]:]\{11,17\}")"
result=`ps aux | grep -i "simple-agent" | grep -v "grep" | wc -l`
if [ $result -ge 0 ]; then
    sudo hciconfig hci0 piscan
    sudo hciconfig hci0 sspmode 0
	sudo hciconfig hci0 name "LR-CAR-$btmac"
    sudo /usr/bin/python /home/bluez-*/test/simple-agent &
else
    echo "BT Agent already started" 
fi