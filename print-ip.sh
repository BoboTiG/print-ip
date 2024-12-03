#!/bin/sh
# JMSinfo SAS: print IP on iface up.

show_ip() {
        local iface=$1
	local lan=$(/bin/ip addr show $iface | grep 'inet ' | cut -d'/' -f1 | cut -d' ' -f6)

	[ ! -z "$lan" ] && echo "$iface|$lan"
}

wan() {
	local wan=$(/usr/bin/dig -4 +short myip.opendns.com @resolver1.opendns.com)
	[ ! -z "$wan" ] && echo "WAN|$wan"
}

cd /opt/print-ip
/usr/bin/python3 print.py $(show_ip wlan0) $(show_ip eth0) $(wan)

exit 0
