# Complete project details at https://RandomNerdTutorials.com
# The specific tutorial can be found here... https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/
try:
  import usocket as socket
except:
  import socket
from machine import Pin
led = Pin(2, Pin.OUT)

def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<!DOCTYPE html>
<html>
<body>

<canvas id="myCanvas" width="200" height="100" style="border:1px solid #000000;">
Your browser does not support the HTML canvas tag.
</canvas>

</body>
</html>"""
  return html

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('', 80))
address_info = socket.getaddrinfo('192.168.4.1', 80)
print("Hostinfo: {}".format(address_info))
address = address_info[0][-1]
s = socket.socket()
s.bind(address)
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()