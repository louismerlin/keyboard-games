from rectangle import *
from logishort import *
from getch import *
from logipy import logi_led
from logimap import logimap
import threading
import time


class SurfIt:



    def __init__(self):
        init()
        time.sleep(1)
        all(100, 100, 100)
        self.fn_keys = [0x3b,0x3c,0x3d,0x3e,0x42,0x41,0x40,0x3f]
        self.lives = [4, 4]
        self.someone_won = 0
        self.bullets = [None, None]
        self.shields = [None, None]
        self.ended = False
        threading.Thread(target=self.loop, args=()).start()

    def loop(self):
        self.draw()
        self.physics()
        time.sleep(0.1)
        self.loop()

    def draw(self):
        #all(100, 100, 100)
        for i, life in enumerate(self.lives):
            for key in self.fn_keys[i*4 + life:i*4 + 4]:
                one(key, 100, 100, 100)
            for key in self.fn_keys[i*4:i*4+life]:
                one(key, 0, 100, 0)
        for i, b in enumerate(self.bullets):
            if b != None:
                key = rectangle[b[0]][abs(i*9-b[1])]
                if b[1] > 0:
                    prev = rectangle[b[0]][abs(i*9+1-b[1])]
                    one(prev, 100, 100, 100)
                one(key, 100, 0, 0)
            else:
                for x in range(0, 4):
                    one(rectangle[x][i*9], 100, 100, 100)
        for i, s in enumerate(self.shields):
            if s!= None:
                key = rectangle[s[0]][abs(i*9-1)]
                one(key, 0, 0, 100)


    def physics(self):
        for i, b in enumerate(self.bullets):
            if b != None:
                b[1] += 1
                if b[1] >= 10:
                    self.bullets[i] = None
                    self.lives[abs(i-1)] -= 1
        for i, s in enumerate(self.shields):
            if s != None:
                s[1] += 1
                if s[1] >= 10:
                    #TODO vacilation of the extreme
                    one(rectangle[s[0]][abs(i*9-1)], 100, 100, 100)
                    self.shields[i] = None
        if self.bullets[0] != None and self.shields[1]!= None:
            if self.bullets[0][0] == self.shields[1][0]:
                if self.bullets[0][1]==8:
                    one(rectangle[self.bullets[0][0]][7], 100, 100, 100)
                    self.bullets[0] = None
        if self.bullets[1] != None and self.shields[0]!= None:
            if self.bullets[1][0] == self.shields[0][0]:
                if self.bullets[1][1]==8:
                    one(rectangle[self.bullets[1][0]][2], 100, 100, 100)
                    self.bullets[1] = None


        if self.bullets[0] != None and self.bullets[1] != None:
            if self.bullets[0][0] == self.bullets[1][0] and (self.bullets[0][1] + self.bullets[1][1]) >= 10:
                #TODO SWAG EXPLOSION
                for y in range(0, 10):
                    one(rectangle[self.bullets[0][0]][y], 100, 100, 100)
                self.bullets[0] = None
                self.bullets[1] = None
        if self.lives[0] <= 0:
            self.ended = True
            self.someone_won = 2
        if self.lives[1] <= 0:
            self.ended = True
            self.someone_won = 1


    def shoot(self, p, r):
        if self.bullets[p] == None:
            self.bullets[p] = [r, 0]

    def protect(self, p, r):
        if self.shields[p] == None:
            self.shields[p] = [r, 0]

    def getKey(self, c):
        if not self.ended:
            #if rectangle[i][O].get(c) != None and c != b'\x1b':
            #   self.someone_won = self.play(c)
            #if self.someone_won == 0:
            #    self.someone_won=-1
            if c=='&':
                self.shoot(0, 0)
            elif c=='a':
                self.shoot(0, 1)
            elif c=='q':
                self.shoot(0, 2)
            elif c=='w':
                self.shoot(0, 3)
            if c=='à':
                self.shoot(1, 0)
            elif c=='p':
                self.shoot(1, 1)
            elif c=='m':
                self.shoot(1, 2)
            elif c=='!':
                self.shoot(1, 3)
            elif c=='é':
                self.protect(0, 0)
            elif c=='z':
                self.protect(0, 1)
            elif c=='s':
                self.protect(0, 2)
            elif c=='x':
                self.protect(0, 3)
            elif c=='ç':
                self.protect(1, 0)
            elif c=='o':
                self.protect(1, 1)
            elif c=='l':
                self.protect(1, 2)
            elif c==':':
                self.protect(1, 3)


            elif self.someone_won !=0:
                self.ended = True

                shutdown()


    def block(self,r,i):
        if i==1 or i==8:
            self.g_board[r][i] = 1





#var = getch()
#s.run_game(var)
#one(0x137, 100, 0, 0)
