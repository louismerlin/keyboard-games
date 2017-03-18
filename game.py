from logishort import *
from getch import *
from logipy import logi_led
from logimap import logimap
import time

init()
time.sleep(1) # Give the SDK a second to initialize

all(17, 28, 47)




var = getch()

while var!=b'\x1b':
    key = logimap.get(var)
    print(var)
    if key:
        one(key, 0, 0, 0)

    var = getch()

#input('Press enter to shutdown SDK...')

shutdown()
