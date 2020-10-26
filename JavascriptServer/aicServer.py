#This code comes courtesy of Rinus. 
#Find it here...
#https://github.com/RinusW/WiPy
try:
  import usocket as socket
except:
  import socket
from time import sleep
from machine import Pin, PWM
frequency = 5000

led=PWM(Pin(2), frequency)

def AiCWebserv():
    # minimal Ajax in Control Webserver
    address_info = socket.getaddrinfo('192.168.4.1', 80)
    print("Hostinfo: {}".format(address_info))
    address = address_info[0][-1]
    s = socket.socket()
    s.bind(address)
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print("Got a connection from %s" % str(addr))
        request = conn.recv(1024)
        conn.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: nanoWiPy\nContent-Type: text/html\n\n')
    ##		print("Content = %s" % str(request))
        request = str(request)
        ib = request.find('Val=')
        if ib > 0 :
            ie = request.find(' ', ib)
            Val = request[ib+4:ie]
            print("Val =", Val)
            duty_cycle = int(Val)
            led.duty(duty_cycle)
            conn.send(Val)
        else:
            with open('aicWebpage.html', 'r') as html:
                conn.send(html.read())
        conn.sendall('\n')
        conn.close()
        print("Connection wth %s closed" % str(addr))