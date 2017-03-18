from rectangle import *
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
        self.lives = [4, 4]
        self.g_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        someone_won = 0

    def draw(self):
        all(100, 100, 100)
        for i, life in enumerate(self.lives):
            for key in self.fn_keys[i*4:i*4+life]:
                one(key, 0, 100, 0)

    def shoot(self, r):
            for i in rectangle[r]:
                print(i)
                print(r)
                key = i
                time.sleep(0.1)
                one(i-1,100,100,100)
                one(i,100,0,0)

    def counter_shoot(self, r):
            for i in reversed(rectangle[r]):
                print(i)
                print(r)
                key = i
                time.sleep(0.1)
                one(i+1,100,1000,100)
                one(i,0,100,0)

    def getKey(self, c):
        if not self.ended:
            if self.rectangle[i][O].get(c) != None and c != b'\x1b':
                self.someone_won = self.play(c)
            if self.someone_won == 0:
                self.someone_won=-1
            if self.someone_won !=0:
                self.ended = True
                shutdown()

    def run_game(self,c):
        if c=='1':
            self.shoot()
        elif c=='a':
            self.shoot()



s = SurfIt()
s.draw()
#var = getch()
#s.run_game(var)
#one(0x137, 100, 0, 0)


s.shoot(0)
s.shoot(1)
s.shoot(2)
s.shoot(3)
s.counter_shoot(0)
s.counter_shoot(1)
s.counter_shoot(2)
s.counter_shoot(3)
input("Appuyez sur entrée")


shutdown()
