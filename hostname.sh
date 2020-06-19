#!/bin/sh
btmac="$(hcitool dev | grep -o "[[:xdigit:]:]\{11,17\}")"
sudo hostnamectl set-hostname "LR-CAR-$btmac"
sudo reboot