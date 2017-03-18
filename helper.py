


def put_red(c):

    if c=='T':
        if matrice[0][0] == 0:
            matrice[0][0] = 1
    elif c=='Z':
        if matrice[0][1] == 0:
            matrice[0][1] = 1
    elif c=='U':
        if matrice[0][2] == 0:
            matrice[0][2] = 1
    elif c=='G':
        if matrice[1][0] == 0:
            matrice[1][0] = 1
    elif c=='H':
        if matrice[1][1] == 0:
            matrice[1][1] = 1
    elif c=='J':
        if matrice[1][2] == 0:
            matrice[1][2] = 1
    elif c=='B':
        if matrice[2][0] == 0:
            matrice[2][0] = 1
    elif c=='N':
        if matrice[2][1] == 0:
            matrice[2][1] = 1
    elif c=='M':
        if matrice[2][2] == 0:
            matrice[2][2] = 1

def put_blue(c):

    if c=='T':
        if matrice[0][0] == 0:
            matrice[0][0] = 2
    elif c=='Z':
        if matrice[0][1] == 0:
            matrice[0][1] = 2
    elif c=='U':
        if matrice[0][2] == 0:
            matrice[0][2] = 2
    elif c=='G':
        if matrice[1][0] == 0:
            matrice[1][0] = 2
    elif c=='H':
        if matrice[1][1] == 0:
            matrice[1][1] = 2
    elif c=='J':
        if matrice[1][2] == 0:
            matrice[1][2] = 2
    elif c=='B':
        if matrice[2][0] == 0:
            matrice[2][0] = 2
    elif c=='N':
        if matrice[2][1] == 0:
            matrice[2][1] = 2
    elif c=='M':
        if matrice[2][2] == 0:
            matrice[2][2] = 2


matrice = [[0,0,0],[0,0,0],[0,0,0]]


def check_matrice():
    c=0
    for i in range(0,3):
        for j in range(0,3):
            if matrice[i][j] == 1:
                c = c+1

        if c == 2:
            print("Red wins")
            all(100, 0, 0)


    for i in range(0,3):
        for j in range(0,3):
            if matrice[i][j] == 1:
                c = c+1

        if c == 2:
            print("Blue wins")
            all(0, 0, 100)


    var = getch()





check_matrice()
