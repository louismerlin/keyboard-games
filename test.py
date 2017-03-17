from logipy import logi_led
import time
import ctypes

logi_led.logi_led_init()

logi_led.logi_led_set_lighting(100, 100, 100)

var = input("Please enter something: ")
print ("you entered", var)

if var=="hugo":
    logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.H, 0, 0, 0)
    logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.U, 0, 0, 0)
    logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.G, 0, 0, 0)
    logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.O, 0, 0, 0)



def eteindre_string(str):

    newList = list(str)
    for i in range(len(newList)):
        logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.i, 0, 0, 0)




input('Press enter to shutdown SDK...')



logi_led.logi_led_shutdown()
