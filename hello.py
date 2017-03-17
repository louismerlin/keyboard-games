from logishort import *
from logipy import *
import time

init()
time.sleep(1) # Give the SDK a second to initialize

all(17, 28, 47)

one(T, 0, 0, 0)
one(Y, 0, 0, 0)
one(U, 0, 0, 0)
one(H, 0, 0, 0)
one(J, 0, 0, 0)
one(B, 0, 0, 0)
one(N, 0, 0, 0)
one(M, 0, 0, 0)

input('Press enter to shutdown SDK...')

shutdown()
