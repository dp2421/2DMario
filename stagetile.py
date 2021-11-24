from pico2d import *


class StageGround:
    def __init__ (self):
        self.image = load_image('resource/stagetile.png')
        self.underimage = load_image('resource/stagegrass.png')
        self.x = 34
    def draw(self):
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
        pass