from logishort import *
from getch import *
from logipy import logi_led
from logimap import logimap
import time

class SurfIt:

    def __init__(self):
        init()
        time.sleep(1)
        all(100, 100, 100)
        self.fn_keys = [0x3b,0x3c,0x3d,0x3e,0x42,0x41,0x40,0x3f]
        self.lives = [3, 2]

    def draw(self):
        all(100, 100, 100)
        for i, life in enumerate(self.lives):
            for key in self.fn_keys[i*4:i*4+life]:
                print(key)
                one(key, 0, 100, 0)

    def shoot(self):
        for i in row_1:
            key = row_1[i]
            time.sleep(1)
            one(key,100,0,0)

s = SurfIt()
s.draw()
one(0x137, 100, 0, 0)
a = input("Appuyez sur entrée: ")
print(a)
shutdown()
