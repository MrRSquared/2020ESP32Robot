'''This module is for using an esp32 to control a robot. Currently it supports motors and basic io (dio/aio) functionality.'''
import time
from machine import Pin
import uasyncio as asyncio


'''async def killer(duration):
    await asyncio.sleep(duration)

async def toggle(mLed, time_ms):
    while True:
        await asyncio.sleep_ms(time_ms)
        mLed.value(1)
        await asyncio.sleep_ms(time_ms)
        Led.value(0)

async def main(duration):
    print("Flash LED's for {} seconds".format(duration))
    led=Pin(2,Pin.OUT)  # Initialise three on board LED's
    t=1
    asyncio.create_task(toggle(led, t))
    asyncio.run(killer(duration)
 
def test(duration=20):
    try:
        asyncio.run(main(duration))
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        asyncio.new_event_loop()
        print('type asyncBlink() to run again.')'''

class motor(pin)
    this.pin = pin
    pin_motor = machine.Pin(pin)
    pwm_motor = machine.PWM(pin_motor,freq=50)
    while True:
        pwm_motor.duty(1000) #Full Reverse
        time.sleep(5)
        pwm_motor.duty(2000) # Full forward
        time.sleep(5)
        pwm_motor.duty(1500)# Stop (Maybe?)
        
test()