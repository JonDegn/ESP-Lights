# https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/

print('booting...')

try:
  import usocket as socket
except:
  import socket

from machine import Pin

import network, sys, os, esp, gc, machine

esp.osdebug(None)

gc.collect()
ssid = '<SSID>'
password = '<PASSWORD>'
address = '<ADDRESS>'
subnet = '<SUBNET>'
gateway = '<GATEWAY>'
dns = '<DNS>'

station = network.WLAN(network.STA_IF)

station.active(True)
station.ifconfig((address, subnet, gateway, dns))
station.connect(ssid, password)

while not station.isconnected():
  machine.idle()

print('Connection successful')
print(station.ifconfig())
