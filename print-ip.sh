#!/bin/sh
# JMSinfo SAS: print IP on iface up.

ip() {
        local iface=$1
	local lan=$(/sbin/ifconfig $iface | grep inet | cut -d':' -f2 | cut -d' ' -f1)

	[ ! -z "$lan" ] && echo "$iface|$lan"
}

wan() {
	local wan=$(/usr/bin/dig +short myip.opendns.com @resolver1.opendns.com)
	[ ! -z "$wan" ] && echo "WAN|$wan"
}

cd /opt/print-ip
/usr/bin/python3 print.py $(ip wlan0) $(ip eth0) $(wan)

exit 0
