from pico2d import *
import game_framework
import random

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 4
class Mon:
    def __init__(self):
        self.x = random.randint(0, 5000)
        self.y = 80
        self.image = load_image('resource/monster.png')
        self.dieimage = load_image('resource/monsterdie.png')
        self.frame = 0
        self.dframe = 0
        self.dir = 0.1 # dir -1:왼쪽 dir 1: 오른쪽


    def get_bb(self):
        return self.x-16, self.y-26, self.x+16, self.y+26

    def do(self):

        pass


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.dframe =(self.dframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        if self.x >= 250:
            self.dir = -0.1
        elif self.x <= 150:
            self.dir = 0.1
        self.x += self.dir
        pass

    def draw(self):
        self.image.clip_draw(int(self.frame)*35, 0, 35, 53, self.x, self.y)
        # self.dieimage.clip_draw(int(self.dframe)*44, 0, 44, 53, self.x, self.y)