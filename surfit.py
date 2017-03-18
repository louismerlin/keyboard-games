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
        self.someone_won = 0
        self.ended = False
        #self.loop()

    def loop(self):
        self.draw()
        time.sleep(0.5)
        self.loop()



    def draw(self):
        all(100, 100, 100)
        for i, life in enumerate(self.lives):
            for key in self.fn_keys[i*4:i*4+life]:
                one(key, 0, 100, 0)

    def shoot(self, r):
            for i in rectangle[r]:
                key = i
                time.sleep(0.1)
                one(i-1,100,100,100)
                one(i,100,0,0)

    def counter_shoot(self, r):
            for i in reversed(rectangle[r]):
                key = i
                time.sleep(0.1)
                one(i+1,100,1000,100)
                one(i,0,100,0)

    def getKey(self, c):
        print(c)
        if not self.ended:
            #if rectangle[i][O].get(c) != None and c != b'\x1b':
            #   self.someone_won = self.play(c)
            #if self.someone_won == 0:
            #    self.someone_won=-1
            if c=='1':
                self.shoot()
            elif c=='a':
                self.shoot()
            elif c=='q':
                self.shoot()
            elif c=='y':
                self.shoot()


            elif self.someone_won !=0:
                self.ended = True

                shutdown()


    def block(self,r,i):
        if i==1 or i==8:
        self.g_board[r][i] = 1

    def boucle(self):
        for i in range(0,10):
            for j in range(0,10):
                if g_board[i][j] != 1:
                    key = rectangle[i][j]
                    one(key,100,100)






#var = getch()
#s.run_game(var)
#one(0x137, 100, 0, 0)
