from pico2d import *
import game_framework
import gameworld

from player import Mario
from stagetile import StageGround
name = "stage_1"
mario = None
idlemario = None
background = None
flipmario = None

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
    global mario, startground, background
    startground = StageGround()
    mario = Mario()
    background = load_image('resource/mapbackground.png')
    gameworld.add_object(startground, 0)
    gameworld.add_object(mario, 1)
    pass


def exit():
    gameworld.clear()
    pass


def update():
    for game_object in gameworld.all_objects():
    	game_object.update()
    pass


def draw():
    clear_canvas()
    background.draw(300, 300)
    for game_object in gameworld.all_objects():
        game_object.draw()
    print(mario.x)
    update_canvas()


def pause():
    pass


def resume():
    pass