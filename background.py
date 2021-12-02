import random
import server

from pico2d import *

class StageBackground:

    def __init__(self):
        self.image = load_image('resource/mapbackground.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h


    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, 0, server.background.canvas_width, server.background.canvas_height, 0, 0)
        pass

    def update(self):
        # fill here
        self.window_left = clamp(0, int(server.mario.x) - server.background.canvas_width // 2, server.background.w -server.background.canvas_width)
        pass

    def handle_event(self, event):
        pass