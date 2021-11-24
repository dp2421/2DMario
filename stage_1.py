from pico2d import *
import game_framework
import gameworld

from mushroom import Mushrooms
from block import Blocks
from player import Mario
from stagetile import StageGround
from monster import Mon
name = "stage_1"
mario = None
idlemario = None
background = None
flipmario = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            mario.handle_event(event)


def enter():
    global mario, startground, background, monster, qblock, mushrooms
    mushrooms = Mushrooms()
    startground = StageGround()
    mario = Mario()
    monster = Mon()
    qblock= Blocks()
    background = load_image('resource/mapbackground.png')
    gameworld.add_object(startground, 0)
    gameworld.add_object(mario, 1)
    gameworld.add_object(monster, 1)
    gameworld.add_object(qblock, 1)
    gameworld.add_object(mushrooms, 0)
    pass


def exit():
    gameworld.clear()
    pass


def update():
    for game_object in gameworld.all_objects():
        game_object.update()

    if collide(mario, monster):
        gameworld.remove_object(monster)

    if collide(mario, qblock):
        gameworld.remove_object(qblock)


    pass


def draw():
    clear_canvas()
    background.draw(300, 300)
    for game_object in gameworld.all_objects():
        game_object.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass