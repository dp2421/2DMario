from pico2d import *
import game_framework

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Mushrooms:
    def __init__(self):
        self.image = load_image('resource/rooms.png')
        self.x = 200
        self.y = 150
        self.frame=0

    def get_bb(self):
        return self.x-17, self.y-17, self.x+17, self.y+17

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass

    def draw(self):
        self.image.draw(self.x, self.y)