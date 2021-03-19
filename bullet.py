import position
import random

class bullet(position.position):
    def __init__(self,x,y):
        super().set_position(x,y)

game_bullet = []
# bullet(random.randint(0,50),34)

def clear_bullets():
    global game_bullet
    game_bullet = []