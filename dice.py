# 9-14
from random import randint
class Die():
    def __init__(self,slides = 6):
        self.slides = slides

    def roll_die(self):
        print(randint(1,self.slides))

die6 = Die()
for i in range(0,6):
    die6.roll_die()

die20 = Die(20)
for i in range(0,10):
    die20.roll_die()
