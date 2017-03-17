from logishort import *
import time

init()
time.sleep(1) # Give the SDK a second to initialize

all(17, 28, 47)

one(logi_led.T, 0, 0, 0)
one(logi_led.Y, 0, 0, 0)
one(logi_led.U, 0, 0, 0)
one(logi_led.H, 0, 0, 0)
one(logi_led.J, 0, 0, 0)
one(logi_led.B, 0, 0, 0)
one(logi_led.N, 0, 0, 0)
one(logi_led.M, 0, 0, 0)

input('Press enter to shutdown SDK...')

shutdown()
