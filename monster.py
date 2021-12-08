from pico2d import *
import game_framework
import random
import server
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Mon:
    def __init__(self):
        self.x = random.randint(200, 5000)
        self.maxx = self.x + 100
        self.minx = self.x - 100
        self.y = 80
        self.image = load_image('resource/monster.png')
        self.dieimage = load_image('resource/monsterdie.png')
        self.frame = 0
        self.dframe = 0
        self.rand = random.random()
        self.dir = self.rand  # dir -1:왼쪽 dir 1: 오른쪽
        self.cx=0


    def get_bb(self):
        return self.x-16, self.y-26, self.x+16, self.y+26

    def do(self):

        pass


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.dframe =(self.dframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        if server.mario.velocity > 0 and server.mario.x>350:
            self.cx -= 2
        elif server.mario.velocity < 0 and server.mario.x>350:
            self.cx += 2
        if self.x >= self.maxx:
            self.dir = -random.random()
        elif self.x <= self.minx:
            self.dir = random.random()
        self.x += self.dir
        pass

    def draw(self):
        self.image.clip_draw(int(self.frame)*35, 0, 35, 53, self.x+self.cx, self.y)
        # self.dieimage.clip_draw(int(self.dframe)*44, 0, 44, 53, self.x, self.y)