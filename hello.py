from logipy import logi_led
import time
import ctypes

logi_led.logi_led_init()
time.sleep(1) # Give the SDK a second to initialize

logi_led.logi_led_set_lighting(17, 28, 47)

logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.T, 0, 0, 0)
logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.Y, 0, 0, 0)
logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.U, 0, 0, 0)
logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.G, 0, 0, 0)
logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.H, 0, 0, 0)
logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.J, 0, 0, 0)
logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.B, 0, 0, 0)
logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.N, 0, 0, 0)
logi_led.logi_led_set_lighting_for_key_with_scan_code(logi_led.M, 0, 0, 0)






input('Press enter to shutdown SDK...')

logi_led.logi_led_shutdown()
