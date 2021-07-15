#!/bin/bash

if [ "$(id -u)" != "0" ]; then
echo “This script must be run as root” 2>&1
exit 1
fi

rm -rf /usr/share/micindicator
rm -f /usr/share/applications/micindicator.desktop
rm -f /etc/xdg/autostart/micindicator.desktop
rm -f /usr/local/bin/micindicator
