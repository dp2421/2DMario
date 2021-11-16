from pico2d import *

class Door:
    def __init__(self):
        self.image = load_image('resource/stagedoor.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 105)