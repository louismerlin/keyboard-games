from logipy import logi_led
import time
import ctypes

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
        if c=='0':
            self.counter_shoot()
        elif c=='p':
            self.counter_shoot()
        elif c=='m':
            self.counter_shoot()
        elif c=='!':
            self.counter_shoot()


        elif self.someone_won !=0:
            self.ended = True

            shutdown()

input('Press enter to shutdown SDK...')
SurfIt s;

s.getKey('1')


logi_led.logi_led_shutdown()
