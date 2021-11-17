from pico2d import *
import game_framework


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 4
class Mon:
    def __init__(self):
        self.x = 200
        self.y = 80
        self.image = load_image('resource/monster.png')
        self.frame = 0
        self.dir = 0.1 # dir -1:왼쪽 dir 1: 오른쪽

    def get_bb(self):
        return self.x-16, self.y-26, self.x+16, self.y+26

    def do(self):

        pass


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        if self.x >= 250:
            self.dir = -0.1
        elif self.x <= 150:
            self.dir = 0.1
        self.x += self.dir
        pass

    def draw(self):
        self.image.clip_draw(int(self.frame)*35, 0, 35, 53, self.x, self.y)