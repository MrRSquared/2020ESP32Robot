try:
  import usocket as socket
except:
  import socket
from machine import Pin
led = Pin(2, Pin.OUT)

address_info = socket.getaddrinfo('192.168.4.1', 80)
print("Hostinfo: {}".format(address_info))
address = address_info[0][-1]
s = socket.socket()
s.bind(address)
s.listen(5)