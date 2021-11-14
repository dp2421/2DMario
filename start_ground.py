from pico2d import *

class StartGround:
    def __init__ (self):
        self.image = load_image('resource/main_ground.png')
        self.x = 34
    def draw(self):
        for i in range(50):
            self.image.draw(self.x * i,18)
            self.image.draw(self.x * i, 36)
            self.image.draw(self.x * i, 54)
    pass