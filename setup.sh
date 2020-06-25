#!/bin/bash   
#Author: Hugo Rodrigues
#Version: 0.1
#Lusorede
#email: hugo.rodrigues@lusorede.pt

###############################
##       INITIAL SETUP       ##
###############################
sudo su
apt-get update 
apt-get upgrade -y
apt-get install git net-tools python python-dbus python-pip bluetooth bluez bluez-tools rfkill -y
apt-get install dpkg-dev libglib2.0-dev libdbus-1-dev libudev-dev libical-dev libreadline-dev -y
timedatectl set-timezone Europe/Lisbon
reboot
###############################
##         LR-CR APP         ##
###############################
sudo su
apt-get update 
apt-get upgrade -y

git clone https://github.com/Lusorede/lr-hr-cr.git
cd lr-hr-cr
sudo touch /var/log/bt-work-py.log
sudo chmod 777 /var/log/bt-work-py.log 

###############################
##      BLUETOOTH-BLUEZ      ##
###############################
sed -i 's/# deb-src/deb-src/g' /etc/apt/sources.list
apt-get update -y
exit
sudo chown -Rv _apt:root /var/cache/apt/archives/partial/
sudo chmod -Rv 700 /var/cache/apt/archives/partial/
sudo apt-get source bluez -y
sudo cp /home/ubuntu/lr-hr-cr/simple-agent /home/bluez*/test/simple-agent
#sudo sed -i 's/return ask("Enter PIN Code: ")/return "1996"/g' /usr/src/bluez*/test/simple-agent

#wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.49.tar.xz
#tar xvf bluez-5.49.tar.xz
#cd bluez-5.49
#./configure
#make
#sudo make install
sudo reboot
###############################
##    BLUETOOTH-ANDROID      ##
###############################
sudo su
apt-get update 
apt-get upgrade -y
apt-get auto-clean
apt-get auto-remove
sudo systemctl start bluetooth
sudo systemctl enable bluetooth
cp /home/ubuntu/lr-hr-cr/btscript.service  /etc/systemd/system/btscript.service
cp /home/ubuntu/lr-hr-cr/btscript.sh /usr/local/bin/btscript.sh
sudo chmod 744 /usr/local/bin/btscript.sh
sudo chmod 664 /etc/systemd/system/btscript.service
bluetoothctl power on
quit
sudo systemctl daemon-reload
sudo systemctl enable btscript.service
sudo systemctl start btscript
 
sudo cp /home/ubuntu/lr-hr-cr/bt-work.service  /etc/systemd/system/bt-work.service 
sudo chmod 664 /etc/systemd/system/bt-work.service
sudo systemctl daemon-reload
sudo systemctl enable bt-work.service
sudo systemctl start bt-work
###############################
##       BLUETOOTH-iOS       ##
###############################

#sudo /usr/bin/btscript.sh
#sudo cp bt_iphone.sh /usr/bin/bt_iphone.sh
#sudo chmod +x /usr/bin/bt_iphone.sh

###############################
##           BLE-PYTHON      ##
###############################
sudo pip install bluepy pexpect
sudo reboot
###############################
##    LR-CR BLE-WORKER       ##
###############################
sudo cp /home/ubuntu/lr-hr-cr/ble-work.service  /etc/systemd/system/ble-work.service
sudo chmod 664 /etc/systemd/system/ble-work.service
sudo systemctl daemon-reload
sudo systemctl enable ble-work.service
###############################
sudo su
apt-get update 
apt-get upgrade -y
reboot




