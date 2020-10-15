
# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

import enableAP
import webrepl
import server

import esp
esp.osdebug(None)

import gc
gc.collect()

webrepl.start()




