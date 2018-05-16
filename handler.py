### BEGIN INIT INFO
# Provides:          scriptname
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

#! /usr/bin/python

import time
import os
import socket

UDP_IP = ("10.134.1.55")
UDP_PORT = 6060

NANO_IP = "10.134.1.103/api/v1/33US1tcNrE7rbhHYFdGCD1OSKxEriI1k/state"

nano_on = '{"on" : {"value":true}}'
nano_off = '{"on" : {"value":false}}'
	
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

try:
	while True:
		data, addr = sock.recvfrom(256)
		
		if data == b"Einschalten":
			print ("command received:", data)
			sock.sendto(nano_on, (NANO_IP, UDP_PORT))
            
		elif data == b"Ausschalten":
			print ("command received:", data)
			sock.sendto(nano_off, (NANO_IP, UDP_PORT))
            
		else:
			print ("retipe command")
            
	
except ValueError:
	print ('error!')
