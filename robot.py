'''This came from https://www.reddit.com/r/vex/comments/6ucuz3/is_there_any_way_make_a_raspberry_pi_interface/
from __future__ import division
import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50) # sets PWM frequency to 50Hz
while True:
    pwm.set_pwm(0, 0, 205) # reverse ~= 4096 * (5%)
    time.sleep(1)
    pwm.set_pwm(0, 0, 400) # forward ~= 4096 * (10%)
    time.sleep(1)
ESP32 motor code from http://mpy-tut.zoic.org/tut/motors.html
    '''



print(open('./robot.py','rU').read())

'''This came from https://www.reddit.com/r/vex/comments/6ucuz3/is_there_any_way_make_a_raspberry_pi_interface/
from __future__ import division
import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50) # sets PWM frequency to 50Hz
while True:
    pwm.set_pwm(0, 0, 205) # reverse ~= 4096 * (5%)
    time.sleep(1)
    pwm.set_pwm(0, 0, 400) # forward ~= 4096 * (10%)
    time.sleep(1)
ESP32 motor code from http://mpy-tut.zoic.org/tut/motors.html
    '''
import time
import machine

pin_motor1 = machine.Pin(26)
pwm_motor1 = machine.PWM(pin_motor1,freq=50)
pin_motor2 = machine.Pin(27)
pwm_motor2 = machine.PWM(pin_motor2,freq=50)

while True:
  print("reverse")
  pwm_motor1.duty(51) # 51 (51/1023 * 20ms = 1ms) Full Reverse
  pwm_motor2.duty(51)
  time.sleep(5)
  print("forward")
  pwm_motor1.duty(103) # 102 (102/1023 * 20ms = 2ms) Full forward
  pwm_motor2.duty(103)
  time.sleep(5)
  print("stop")
  pwm_motor1.duty(76)# Stop (Maybe?)
  pwm_motor2.duty(76)
  time.sleep(5)
  print("End of Cycle")








