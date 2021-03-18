import position
import existence
import slider
import random

class ball(position.position, existence.existence):

    def __init__(self, x, y):
        self.x_vel = 2
        self.y_vel = -1
        self.grab_status = 0
        self.thru_status = 0
        super().set_position(x, y)

    def reverse_y_vel(self):
        self.y_vel = -self.y_vel

    def reverse_x_vel(self):
        self.x_vel = -self.x_vel

    def reverse_x_y_vel(self):
        self.y_vel = -self.y_vel
        self.x_vel = -self.x_vel

    def increase_speed(self):
        # self.y_vel = 2*self.y_vel
        self.x_vel = 2*self.x_vel

    def decrease_speed(self):
        # self.y_vel = self.y_vel/2
        self.x_vel = self.x_vel/2

    def update_pos(self):
        self.x_pos = self.x_pos = self.x_vel
        self.y_pos = self.y_pos = self.y_vel

    def next_x_pos(self):
        return self.x_pos+self.x_vel

    def next_y_pos(self):
        return self.y_pos+self.y_vel

game_ball = ball(random.randint(slider.game_slider.x_pos, slider.game_slider.x_pos+slider.game_slider.length),33)
