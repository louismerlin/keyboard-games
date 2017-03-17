from logipy import logi_led
import time
import ctypes

logi_led.logi_led_init()
time.sleep(1) # Give the SDK a second to initialize
logi_led.logi_led_set_lighting(100, 0, 0)
input('Press enter to shutdown SDK...')

logi_led.logi_led_shutdown()
