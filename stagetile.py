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
    def draw(self):
        # self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.background.canvas_width, server.background.canvas_height, 0, 0)
        for i in range(70):
            self.image.draw(self.x * i,0)
            self.image.draw(self.x * i, 23)
            self.underimage.draw(self.x * i, 55)

        for i in range(73, 88):
            self.image.draw(self.x * i,0)
            self.image.draw(self.x * i, 23)
            self.underimage.draw(self.x * i, 55)

        for i in range(90, 160):
            self.image.draw(self.x * i,0)
            self.image.draw(self.x * i, 23)
            self.underimage.draw(self.x * i, 55)

        for i in range(163, 233):
            self.image.draw(self.x * i,0)
            self.image.draw(self.x * i, 23)
            self.underimage.draw(self.x * i, 55)
        pass

    def update(self):
        self.window_left = clamp(0, int(server.mario.x) - server.stagetile.canvas_width // 2,
                                 server.stagetile.x - server.stagetile.canvas_width)
        pass