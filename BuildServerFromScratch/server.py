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
def web_page():
    file = open("index.html", "r")
    page = file.read()
    file.close()
    return page
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print(request) # for debugging
  response = web_page()
  conn.send("HTTP/1.1 200 OK\n")
  conn.send("Content-typpe: text/html\n")
  conn.send("Connection: close\n\n")
  conn.sendall(response)
  conn.close()