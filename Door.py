from pico2d import *

class Door:
    def __init__(self):
        self.image = load_image('resource/stagedoor.png')

    def get_bb(self):
        return 580, 65, 620, 145

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 105)