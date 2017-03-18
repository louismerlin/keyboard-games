from logishort import *
from getch import *
from logipy import logi_led
from logimap import logimap
import time


accepted_keys = {
    b't':0x14,
    b'y':0x15,
    b'u':0x16,
    b'g':0x22,
    b'h':0x23,
    b'j':0x24,
    b'b':0x30,
    b'n':0x31,
    b',':0x32
}

init()
time.sleep(1) # Give the SDK a second to initialize

all(17, 28, 47)

one(logi_led.T, 0, 0, 0)
one(logi_led.Y, 0, 0, 0)
one(logi_led.U, 0, 0, 0)
one(logi_led.H, 0, 0, 0)
one(logi_led.J, 0, 0, 0)
one(logi_led.B, 0, 0, 0)
one(logi_led.N, 0, 0, 0)
one(logi_led.M, 0, 0, 0)
one(logi_led.G, 0, 0, 0)


#gmatrice = [[(0,0,0)] for i in range(3)]


def blue_plays(c):
    key = logimap.get(var)
    one(key, 100, 0, 0)
    put_blue(c)

def red_plays(c):
    key = logimap.get(var)
    one(key, 0, 100, 0)
    put_red(c)

def put_red(c):
    c=c.upper()
    if c==b'T':
        if matrice[0][0] == 0:
            matrice[0][0] = 1
    elif c==b'W':
        if matrice[0][1] == 0:
            matrice[0][1] = 1
    elif c==b'U':
        if matrice[0][2] == 0:
            matrice[0][2] = 1
    elif c==b'G':
        if matrice[1][0] == 0:
            matrice[1][0] = 1
    elif c==b'H':
        if matrice[1][1] == 0:
            matrice[1][1] = 1
    elif c==b'J':
        if matrice[1][2] == 0:
            matrice[1][2] = 1
    elif c==b'B':
        if matrice[2][0] == 0:
            matrice[2][0] = 1
    elif c==b'N':
        if matrice[2][1] == 0:
            matrice[2][1] = 1
    elif c==b'M':
        if matrice[2][2] == 0:
            matrice[2][2] = 1

def put_blue(c):
    c=c.upper()
    if c==b'T':
        if matrice[0][0] == 0:
            matrice[0][0] = 2
    elif c==b'W':
        if matrice[0][1] == 0:
            matrice[0][1] = 2
    elif c==b'U':
        if matrice[0][2] == 0:
            matrice[0][2] = 2
    elif c==b'G':
        if matrice[1][0] == 0:
            matrice[1][0] = 2
    elif c==b'H':
        if matrice[1][1] == 0:
            matrice[1][1] = 2
    elif c==b'J':
        if matrice[1][2] == 0:
            matrice[1][2] = 2
    elif c==b'B':
        if matrice[2][0] == 0:
            matrice[2][0] = 2
    elif c==b'N':
        if matrice[2][1] == 0:
            matrice[2][1] = 2
    elif c==b'M':
        if matrice[2][2] == 0:
            matrice[2][2] = 2


matrice = [[0,0,0],[0,0,0],[0,0,0]]


def check_matrice_red():
    c=0
    for i in range(0,3):
        for j in range(0,3):
            if matrice[i][j] == 1:
                c = c+1

        if c == 2:
            return True
            print("Red wins")
        else:
            return False

def check_matrice_blue():
    c=0
    for i in range(0,3):
        for j in range(0,3):
            if matrice[i][j] == 2:
                c = c+1

        if c == 2:
            return True
            print("Blue wins")
        else:
            return False

def blue_wins():
    all(0, 0, 100)


def red_wins():
    all(100, 0, 0)



compteur = 0
#while var!=b'\x1b':





for i in range(9):
    var = getch()
    key = accepted_keys.get(var)
    print(key == None)
    print(key)

    while key == None:
        var = getch()
        key = accepted_keys.get(var)

    if var==b'\x1b':
        break


    if i%2==0:
        if compteur==0:
            blue_plays(var)
        if check_matrice_blue():
            blue_wins
        compteur=compteur+1

    else:
        if compteur==0:
            red_plays(var)
        if check_matrice_red():
            red_wins
        compteur=compteur+1

    compteur=0

    #if key:
        #one(key, 0, 0, 0)

    print(matrice)

#input('Press enter to shutdown SDK...')

shutdown()
