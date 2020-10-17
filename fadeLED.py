from time import sleep
from machine import Pin, PWM
frequency = 5000

led=PWM(Pin(2), frequency)
 
while True:
  for duty_cycle in range(0, 1024):
    led.duty(duty_cycle)
    sleep(0.005)
    #duty_cycle+=1