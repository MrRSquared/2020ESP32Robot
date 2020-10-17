import time
from machine import Pin
import uasyncio as asyncio


async def killer(duration):
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
        print('type asyncBlink() to run again.')

test()