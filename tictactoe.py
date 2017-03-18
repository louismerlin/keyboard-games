from logishort import *
from getch import *
from logipy import logi_led
from logimap import logimap
import time

class TicTacToe:

    accepted_keys = {
        b't':[0x14, 0, 0],
        b'y':[0x15, 0, 1],
        b'u':[0x16, 0, 2],
        b'g':[0x22, 1, 0],
        b'h':[0x23, 1, 1],
        b'j':[0x24, 1, 2],
        b'b':[0x30, 2, 0],
        b'n':[0x31, 2, 1],
        b',':[0x32, 2, 2]
    }

    def __init__:
        init()
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        time.sleep(1)
        all(20, 20, 100)
        draw()
        turn_count = 0
        someone_won = 0

    def status():
        someone_won = play(key)
        return someone_won




    def getKey(c):
        while turn_count != 9 and someone_won == 0:
                  #print(someone_won)
                  key = getch()
                  while accepted_keys.get(key) == None and key != b'\x1b':
                      key = getch()
                  if key == b'\x1b':
                      break
                  someone_won = play(key)
                  turn_count += 1

              if someone_won==0:
                  all(100,100,100)
              elif someone_won==1:
                  all(100,0,0)
              elif someone_won==2:
                  all(0,100,0)
                    print("Player " + str(someone_won) + " won !!")
                shutdown()




    def draw():
        for key in accepted_keys:
            k = accepted_keys[key]
            if(board[k[1]][k[2]] == 0):
                one(k[0], 0, 0, 0)
            if(board[k[1]][k[2]] == 1):
                one(k[0], 100, 0, 0)
            if(board[k[1]][k[2]] == 2):
                one(k[0], 0, 100, 0)



    def checkWin():
        b = board
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


    def play(c):
        k = accepted_keys.get(c)
        player = turn_count % 2 + 1
        board[k[1]][k[2]] = player
        draw()
        return checkWin()
