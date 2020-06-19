#!/bin/bash   
#Author: Hugo Rodrigues
#Version: 0.000002
#Lusorede
#email: hugo.rodrigues@lusorede.pt

# Run with sudo su


#Initial Setup
apt-get update 
apt-get upgrade -y

apt-get install git net-tools python python-dbus bluetooth bluez bluez-tools rfkill -y
apt-get install dpkg-dev libglib2.0-dev libdbus-1-dev libudev-dev libical-dev libreadline-dev -y
apt-get install pi-bluetooth -y

reboot

git clone https://github.com/Lusorede/lr-hr-cr.git



#Config Bluetooth 

sed -i 's/# deb-src/deb-src/g' /etc/apt/sources.list
apt-get update 
apt-get source bluez
cp /home/ubuntu/lr-hr-cr/simple-agent /home/bluez*/test/simple-agent
#sudo sed -i 's/return ask("Enter PIN Code: ")/return "1996"/g' /usr/src/bluez*/test/simple-agent

wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.49.tar.xz
tar xvf bluez-5.49.tar.xz
cd bluez-5.49
./configure
make
sudo make install
sudo reboot

sudo systemctl start bluetooth
sudo systemctl enable bluetooth
cp /home/ubuntu/lr-hr-cr/btscript.service  /etc/systemd/system/btscript.service
cp /home/ubuntu/lr-hr-cr/btscript.sh /usr/local/bin/btscript.sh
sudo chmod 744 /usr/local/bin/btscript.sh
sudo chmod 664 /etc/systemd/system/btscript.service
sudo systemctl daemon-reload
sudo systemctl enable btscript.service





#sudo /usr/bin/btscript.sh
#sudo cp bt_iphone.sh /usr/bin/bt_iphone.sh
#sudo chmod +x /usr/bin/bt_iphone.sh