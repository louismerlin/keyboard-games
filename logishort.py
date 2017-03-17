from logipy import logi_led

def init()
    logi_led.logi_led_init()

def all(r, g, b)
    logi_led.logi_led_lighting(r, g, b)

def one(k, r, g, b)
    logi_led.logi_led_lighting_for_key_with_scan_code(k, r, g, b)
