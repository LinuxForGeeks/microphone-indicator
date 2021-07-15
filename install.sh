#!/bin/bash

if [ "$(id -u)" != "0" ]; then
echo “This script must be run as root” 2>&1
exit 1
fi

sh uninstall.sh

mkdir /usr/share/micindicator
cp -R resources /usr/share/micindicator/

cp *.py /usr/share/micindicator/
chmod 755 -R /usr/share/micindicator/

cp micindicator.desktop /etc/xdg/autostart/
chmod 755 /etc/xdg/autostart/micindicator.desktop

cp micindicator.desktop /usr/share/applications/
chmod 755 /usr/share/applications/micindicator.desktop

ln -s /usr/share/micindicator/micindicator.py /usr/local/bin/micindicator
chmod 755 /usr/local/bin/micindicator
