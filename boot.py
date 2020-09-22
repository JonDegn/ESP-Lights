# https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/

print('booting...')

try:
  import usocket as socket
except:
  import socket

from machine import Pin

import network, sys, os, esp, gc

esp.osdebug(None)

gc.collect()
ssid = '<SSID>'
password = '<PASSWORD>'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


