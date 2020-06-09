#!/bin/bash   
#Author: Hugo Rodrigues
#Version: 0.000001
#Lusorede
#email: hugo.rodrigues@lusorede.pt

#Initial Setup
apt-get update 
apt-get upgrade -y

apt-get install python cockpit -y

sudo cp ~/lr-hr-cr/www/* /var/www/html

#Config Bluetooth 
apt-get install bluetooth bluez bluez-tools rfkill -y
sudo sed -i 's/#deb-src/deb-src/g' /etc/apt/sources.list
apt-get update 
sudo apt-get source bluez
cd /usr/src/bluez*
sudo sed -i 's/return ask("Enter PIN Code: ")/return "1996"/g' //usr/src/bluez*/test/simple-agent
sudo cp btscript.sh /usr/bin/btscript.sh
sudo chmod +x /usr/bin/btscript.sh
sudo sed -i '/exit 0/i /usr/bin/btscript.sh' /etc/rc.local
cd /usr/bin
sudo ./btscript.sh
sudo cp bt_iphone.sh /usr/bin/bt_iphone.sh
sudo chmod +x /usr/bin/bt_iphone.sh