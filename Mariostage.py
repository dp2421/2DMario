from pico2d import *
import random
import json
import os

import game_framework
import mario_main

name = "MainStage"

background = None
font = None

class Ground:
    def __init__ (self):
        self.grass = load_image('resource/stagegrass.png')
        self.tile = load_image('resource/stagetile.png')
        self.x = 34
    def draw(self):
        for i in range(50):
            self.tile.draw(self.x * i,18)
            self.tile.draw(self.x * i, 36)
            self.grass.draw(self.x * i, 54)
    pass
class Door:
    def __init__(self):
        self.image = load_image('resource/stagedoor.png')
        self.x=500
    def draw(self):
        self.image.draw(self.x, 100)
        self.image.draw(self.x+100, 100)
    pass
class QuestionTile:
    def __init__(self):
        self.image = load_image('resource/questiontile.png')
        self.x = random.randrange(300, 800)
        self.frame = 0
    def draw(self):
        self.image.clip_draw(frame*34, 0, 34, 36, self.x, 140)
        self.frame = (self.frame+1)%4
        delay (0.05)
def enter():
    global mario, ground, idlemario, background, flipmario, qutile, running, x, y, frame, direct
    ground = Ground()
    mario = load_image('resource/mariowalk.png')
    idlemario =load_image('resource/idlemario.png')
    background = load_image('resource/mapbackground.png')
    flipmario = load_image('resource/flipmario.png')
    qutile = QuestionTile()
    running =True
    x = 100
    y=92
    frame = 0
    direct =0
    pass


def exit():
    global mario, ground
    del(mario)
    del(ground)
    pass


def pause():
    pass


def resume():
    pass


# def handle_events():
#     events = get_events()
#     for event in events:
#         if event.type ==SDL_QUIT:
#             game_framework.quit()
#         # elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
#         #     game_framework.change_state(title_state)
#     pass


def update():
    # mario.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    mario.draw()
    update_canvas()
    pass

def handle_events():
    global running
    global x
    global direct
    global y
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key ==SDLK_RIGHT:
                direct += 1
            elif event.key ==SDLK_LEFT:
                direct -= 1
            elif event.key ==SDLK_SPACE:
                y+=20
            # elif event.key == SDLK_DOWN:
        elif event.type == SDL_KEYUP:
            if event.key ==SDLK_RIGHT:
                direct -= 1
            elif event.key ==SDLK_LEFT:
                direct += 1
            elif event.key == SDLK_SPACE:
                y -=20

def draw():
    global frame, x, y, direct
    clear_canvas()
    handle_events()
    background.draw(400, 300)
   
    ground.draw()
    if direct > 0:
        mario.clip_draw(frame*50, 0, 50, 70, x, y)
    elif direct < 0:
        flipmario.clip_draw(frame*50, 0, 50, 70, x, y)
    elif direct == 0:
        idlemario.clip_draw(frame*48, 0, 48, 70, x, y)

    qutile.draw()

    update_canvas()
    frame = (frame+1)%6
    x += direct * 5
    delay(0.05)


