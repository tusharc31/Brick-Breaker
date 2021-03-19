import time

class details_of_player():
    def __init__(self,status,score,time,lives,level):
        self.status = status
        self.score = score
        self.time = time
        self.lives = lives
        self.level = level
    
    def decrease_life(self):
        self.lives = self.lives - 1

stats = details_of_player('P',0,time.time(),5,1)