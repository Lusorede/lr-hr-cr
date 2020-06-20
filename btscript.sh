#!/bin/sh
eth0mac="$(cat /sys/class/net/eth0/address)"
result=`ps aux | grep -i "simple-agent" | grep -v "grep" | wc -l`
hostn="LR-CAR-$eth0mac"
sudo hostnamectl set-hostname $hostn
if [ $result -ge 0 ]; then
    sudo hciconfig hci0 piscan
    sudo hciconfig hci0 sspmode 0
    sudo hciconfig hci0 name "LR-CAR-$eth0mac"
    sudo /usr/bin/python /home/ubuntu/bluez*/test/simple-agent &
else
    echo "BT Agent already started" 
fi
