from pico2d import *
import server
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 4
first_blocks = [2, 0, 0, 0, 1, 2, 1, 2, 1]
for i in range(60):
    first_blocks.append(0)

first_blocks.extend([1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 1,
    2, 0, 0, 0, 0, 2, 0, 0, 2, 0,
    0, 2, 0, 0, 0, 0, 0, 1,
    0, 0, 1, 1, 1, 0, 0, 0, 1, 1])

for i in range(60):
    first_blocks.append(0)

first_blocks.extend([1, 1, 2, 1])

class StageGround:
    def __init__ (self):
        self.blockimage = load_image('resource/main_ground.png')
        self.qimage = load_image('resource/questiontile.png')
        self.image = load_image('resource/stagetile.png')
        self.underimage = load_image('resource/stagegrass.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.x = 34
        self.by=200
        self.cx =0
        self.frame = 0

    def draw(self):
        for i in range(70):
            self.image.draw(self.x * i + self.cx,0)
            self.image.draw(self.x * i + self.cx, 23)
            self.underimage.draw(self.x * i + self.cx, 55)

        for i in range(73, 88):
            self.image.draw(self.x * i + self.cx,0)
            self.image.draw(self.x * i + self.cx, 23)
            self.underimage.draw(self.x * i + self.cx, 55)

        for i in range(90, 160):
            self.image.draw(self.x * i + self.cx,0)
            self.image.draw(self.x * i + self.cx, 23)
            self.underimage.draw(self.x * i + self.cx, 55)

        for i in range(163, 233):
            self.image.draw(self.x * i + self.cx,0)
            self.image.draw(self.x * i + self.cx, 23)
            self.underimage.draw(self.x * i + self.cx, 55)

        for index, value in enumerate(first_blocks):
            if value == 0:
                pass
            elif value == 1:
                self.blockimage.draw(680+index*30 + self.cx, self.by)
                pass
            elif value == 2:
                self.qimage.clip_draw(int(self.frame) * 34, 0, 35, 36, 680+index*30 + self.cx, self.by)
                pass
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if server.mario.velocity > 0 and server.mario.x>=350:
            self.cx -= 2
        elif server.mario.velocity < 0 and server.mario.x>=350:
            self.cx += 2
        pass