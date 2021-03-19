import position
import random

class slider(position.position):
    def __init__(self,x,y):
        self.length = 40
        self.state = 0
        self.shoot = -1
        self.remain = 0
        self.start = -1
        super().set_position(x,y)

    def move_left(self):
        if self.x_pos >= 5:
            self.x_pos = self.x_pos - 5

    def move_right(self):
        if self.x_pos+self.length+5 <= 120:
            self.x_pos = self.x_pos + 5


game_slider = slider(random.randint(0,50),34)
