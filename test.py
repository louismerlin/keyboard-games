from logipy import logi_led
import time
import ctypes

logi_led.logi_led_init()

logi_led.logi_led_set_lighting(100, 100, 100)

var = input("Please enter something: ")
print "you entered", var




input('Press enter to shutdown SDK...')



logi_led.logi_led_shutdown()
