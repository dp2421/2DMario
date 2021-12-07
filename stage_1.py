from pico2d import *
import game_framework
import gameworld
import server

from background import StageBackground
from mushroom import Mushrooms
from player import Mario
from stagetile import StageGround
from monster import Mon
name = "stage_1"

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
            server.mario.handle_event(event)


def enter():
    server.mushroom = Mushrooms()
    server.mario = Mario()
    server.monster = Mon()
    count = [Mon() for i in range(20)]
    server.stagetile = StageGround()
    for server.monster in count:
        gameworld.add_object(server.monster, 1)
    server.background = StageBackground()
    gameworld.add_object(server.stagetile, 1)
    gameworld.add_object(server.background, 0)
    gameworld.add_object(server.mario, 1)
    gameworld.add_object(server.mushroom, 0)
    pass


def exit():
    gameworld.clear()
    pass


def update():
    for game_object in gameworld.all_objects():
        game_object.update()

    if collide(server.mario, server.monster):
        gameworld.remove_object(server.monster)

    # if collide(server.mario, server.block):
    #     server.mushroom.y =180
    #     # mushrooms.x =100
    pass


def draw():
    clear_canvas()
    for game_object in gameworld.all_objects():
        game_object.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass