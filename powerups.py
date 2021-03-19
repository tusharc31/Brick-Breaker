import position
import time
import slider
import display_file
import player
import ball
import bullet

class powerup(position.position):

    def __init__(self, x, y):
        self.y_vel = 1
        self.time_of_activation = 0
        self.used = 0
        super().set_position(x, y)

    def activate(self):
        print('Activating power up')

    def deactivate(self):
        print('Deactivating power up')


class powerup_expand(powerup):

    def __init__(self, x, y):
        self.hash = 5
        self.image = '⇈'
        super().__init__(x, y)

    def activate(self):
        print('Activating power up')
        if int(1.5*slider.game_slider.length) <= 90:
            slider.game_slider.length = int(1.5*slider.game_slider.length)
            if slider.game_slider.x_pos + slider.game_slider.length > 120:
                slider.game_slider.x_pos = 120 - slider.game_slider.length
        else:
            self.used = 0

    def deactivate(self):
        print('Deactivating power up')
        if int(slider.game_slider.length/1.5) >= 40:
            slider.game_slider.length = int(slider.game_slider.length/1.5)


class powerup_shrink(powerup):

    def __init__(self, x, y):
        self.hash = 6
        self.image = '⇊'
        super().__init__(x, y)

    def activate(self):
        print('Activating power up')
        if int(slider.game_slider.length/1.5) >= 15:
            slider.game_slider.length = int(slider.game_slider.length/1.5)
        else:
            self.used = 0

    def deactivate(self):
        print('Deactivating power up')
        slider.game_slider.length = int(1.5*slider.game_slider.length)
        if slider.game_slider.x_pos + slider.game_slider.length > 120:
            slider.game_slider.x_pos = 120 - slider.game_slider.length

class powerup_fastball(powerup):

    def __init__(self, x, y):
        self.hash = 7
        self.image = '⚡'
        super().__init__(x, y)

    def activate(self):
        print('Activating power up')
        ball.game_ball.x_vel = 4*ball.game_ball.x_vel

    def deactivate(self):
        print('Deactivating power up')
        if int(ball.game_ball.x_vel/4) != 0:
            ball.game_ball.x_vel = int(ball.game_ball.x_vel/2)


class powerup_grabball(powerup):

    def __init__(self, x, y):
        self.hash = 8
        self.image = '🤚'
        super().__init__(x, y)

    def activate(self):
        print('Activating power up')
        ball.game_ball.grab_status = 1

    def deactivate(self):
        print('Deactivating power up')
        ball.game_ball.grab_status = 0
        player.stats.status = 'A'



class powerup_fireball(powerup):

    def __init__(self, x, y):
        self.hash = 9
        self.image = '🔥'
        super().__init__(x, y)

    def activate(self):
        print('Activating power up')
        ball.game_ball.state = ball.game_ball.state+1

    def deactivate(self):
        print('Deactivating power up')
        ball.game_ball.state = ball.game_ball.state-1




class powerup_thruball(powerup):

    def __init__(self, x, y):
        self.hash = 8
        self.image = '🤚'
        super().__init__(x, y)

    def activate(self):
        print('Activating power up')
        ball.game_ball.thru_status = 1

    def deactivate(self):
        print('Deactivating power up')
        ball.game_ball.thru_status = 0

class powerup_multiplier(powerup):

    def __init__(self, x, y):
        self.hash = 8
        self.image = '🤚'
        super().__init__(x, y)

    def activate(self):
        print('Activating power up')
        ball.cnt = ball.cnt + 1

    def deactivate(self):
        print('Deactivating power up')
        ball.cnt = ball.cnt - 1 # Automatically remove last

class powerup_laser(powerup):

    def __init__(self, x, y):
        self.hash = 9
        self.image = '▲'
        self.last = time.time()
        super().__init__(x, y)

    def activate(self):
        print('Activating power up')
        self.last = time.time()
        slider.game_slider.start = time.time()
        slider.game_slider.state=slider.game_slider.state+1

    def deactivate(self):
        print('Deactivating power up')
        slider.game_slider.state=slider.game_slider.state-1

super_power = []

def delete_super_power():
    global super_power
    super_power = []

def disable_powerup():

    k = len(super_power)
    k = k - 1

    while k >= 0:

        if super_power[k].used == 0 and super_power[k].y_pos <= 0:
            super_power.pop(k)

        elif super_power[k].used == 1 and time.time()-super_power[k].time_of_activation >= 10:
            super_power[k].deactivate()
            super_power.pop(k)

        k = k-1

