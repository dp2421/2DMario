from pico2d import *
import random
import json
import os

import game_framework
name = "MainStage"

background = None
font = None

class Ground:
    def __init__ (self):
        self.grass = load_image('stagegrass.png')
        self.tile = load_image('stagetile.png')
        self.x = 34
    def draw(self):
        for i in range(50):
            self.tile.draw(self.x * i,18)
            self.tile.draw(self.x * i, 36)
            self.grass.draw(self.x * i, 54)
    pass
class Door:
    def __init__(self):
        self.image = load_image('stagedoor.png')
        self.x=500
    def draw(self):
        self.image.draw(self.x, 100)
        self.image.draw(self.x+100, 100)
    pass
def enter():
    global boy, grass
    boy = Boy()
    background = Background()
    pass


def exit():
    global boy, grass
    del(boy)
    del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        # elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
        #     game_framework.change_state(title_state)
    pass


def update():
    boy.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    boy.draw()
    update_canvas()
    pass

def handle_events():
    global running
    global x
    global dir
    global y
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key ==SDLK_RIGHT:
                dir += 1
            elif event.key ==SDLK_LEFT:
                dir -= 1
            elif event.key ==SDLK_SPACE:
                y+=20
            # elif event.key == SDLK_DOWN:
        elif event.type == SDL_KEYUP:
            if event.key ==SDLK_RIGHT:
                dir -= 1
            elif event.key ==SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_SPACE:
                y -=20

            


open_canvas()

ground = Ground()
mario = load_image('mariowalk.png')
idlemario =load_image('idlemario.png')
background = load_image('background.png')
flipmario = load_image('flipmario.png')
running =True
x = 100
y=100
frame = 0
dir =0
while running:
    

    clear_canvas()
    handle_events()
    background.draw(400, 300)
    ground.draw()
    if dir > 0:
        mario.clip_draw(frame*50, 0, 50, 70, x, y)
    elif dir < 0:
        flipmario.clip_draw(frame*50, 0, 50, 70, x, y)
    elif dir == 0:
        idlemario.clip_draw(frame*48, 0, 48, 70, x, y)

    update_canvas()
    frame = (frame+1)%6
    x += dir * 5
    delay(0.05)


