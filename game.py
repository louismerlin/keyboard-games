from logishort import *
from getch import *
from logipy import logi_led
from logimap import logimap
import time


init()
time.sleep(1) # Give the SDK a second to initialize

all(17, 28, 47)

matrice = [[(0,0,0)] for i in range(3)]


def blue_plays(c):
    key = logimap.get(var)
    one(key, 100, 0, 0)

def red_plays(c):
    key = logimap.get(var)
    one(key, 0, 100, 0)


var = getch()
compteur = 0
#while var!=b'\x1b':


one(logi_led.T, 0, 0, 0)
one(logi_led.Y, 0, 0, 0)
one(logi_led.U, 0, 0, 0)
one(logi_led.H, 0, 0, 0)
one(logi_led.J, 0, 0, 0)
one(logi_led.B, 0, 0, 0)
one(logi_led.N, 0, 0, 0)
one(logi_led.M, 0, 0, 0)
one(logi_led.G, 0, 0, 0)

for i in range(9):
    #if var!=b'\x1b':
    key = logimap.get(var)

    if i%2==0:
        if compteur==0:
            blue_plays(var)
            ++compteur

    else:
         if compteur==0:
            red_plays(var)
            ++compteur

    compteur=0

    #if key:
        #one(key, 0, 0, 0)

    var = getch()

#input('Press enter to shutdown SDK...')

shutdown()
