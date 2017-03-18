from logishort import *
from getch import *
from logipy import logi_led
from logimap import logimap
import time

class TicTacToe:

    def __init__(self):
        init()
        time.sleep(1)
        self.accepted_keys = {
            't':[0x14, 0, 0],
            'y':[0x15, 0, 1],
            'u':[0x16, 0, 2],
            'g':[0x22, 1, 0],
            'h':[0x23, 1, 1],
            'j':[0x24, 1, 2],
            'b':[0x30, 2, 0],
            'n':[0x31, 2, 1],
            ',':[0x32, 2, 2]
        }
        
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        all(20, 20, 100)
        self.turn_count = 0
        self.someone_won = 0
        self.draw()
        self.ended = False

    def getKey(self, c):
        if not self.ended:
            if self.accepted_keys.get(c) != None and c != b'\x1b':
                self.someone_won = self.play(c)
                self.turn_count += 1
            if self.someone_won == 0 and (c == b'\x1b' or self.turn_count >= 9):
                self.someone_won = -1
            if self.someone_won != 0:
                self.ended = True
                shutdown()

    def draw(self):
        for key in self.accepted_keys:
            k = self.accepted_keys[key]
            if(self.board[k[1]][k[2]] == 0):
                one(k[0], 0, 0, 0)
            if(self.board[k[1]][k[2]] == 1):
                one(k[0], 100, 0, 0)
            if(self.board[k[1]][k[2]] == 2):
                one(k[0], 0, 100, 0)

    def checkWin(self):
        b = self.board
        won = 0
        #print(str(b[0][0]) + " " + str(b[0][1]) + " " + str(b[0][2]))
        #print(str(b[0][0] == b[0][1] and b[0][0] == b[0][2]))
        if (b[0][0] == b[0][1] and b[0][0] == b[0][2]) or (b[0][0] == b[1][0] and b[0][0] == b[2][0]) or (b[0][0] == b[1][1] and b[0][0] == b[2][2]):
            won = int(b[0][0])
        elif (b[1][1] == b[2][1] and b[1][1] == b[1][2]) or (b[1][1] == b[1][0] and b[1][1] == b[1][2]) or (b[1][1] == b[0][1] and b[1][1] == b[2][1]):
            won = int(b[1][1])
        elif (b[2][2] == b[2][0] and b[2][2] == b[2][1]) or (b[2][2] == b[0][2] and b[2][2] == b[1][2]):
            won = int(b[2][2])
        return won

    def play(self, c):
        k = self.accepted_keys.get(c)
        player = self.turn_count % 2 + 1
        self.board[k[1]][k[2]] = player
        self.draw()
        return self.checkWin()
