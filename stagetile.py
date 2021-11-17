from pico2d import *
from player import Mario

# mario = Mario()

class StageGround:
    def __init__ (self):
        self.image = load_image('resource/stagetile.png')
        self.underimage = load_image('resource/stagegrass.png')
        self.x = 34
    def draw(self):
        for i in range(50):
            self.image.draw(self.x * i,0)
            self.image.draw(self.x * i, 23)
            self.underimage.draw(self.x * i, 55)
        pass

    def update(self):
        # if mario.dir == 1:
        #     self.x -= 1
        # else:
        #     self.x += 1

        pass