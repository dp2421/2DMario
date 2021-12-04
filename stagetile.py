from pico2d import *
import server
class StageGround:
    def __init__ (self):
        self.image = load_image('resource/stagetile.png')
        self.underimage = load_image('resource/stagegrass.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.x = 34
        self.cx =0
    def draw(self):
        # self.x = server.background.window_left - server.mario.x
        # self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.background.canvas_width, server.background.canvas_height, 0, 0)
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
        pass

    def update(self):
        if server.mario.velocity > 0 and server.mario.x>=350:
            print('right')
            self.cx -= 2
        elif server.mario.velocity < 0 and server.mario.x>=350:
            print('left')
            self.cx += 2
        pass