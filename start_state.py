import game_framework
from pico2d import *


name = "TitleState"
image = None
spaceimage = None
mainsign=None

Frame=0
def enter():
    global image
    global spaceimage
    global mainsign
    mainsign = load_image('resource/main_2.png')
    spaceimage=load_image('resource/start_enter.png')
    image =load_image('resource/startbackground.png')
    pass


def exit():
    global image
    global spaceimage
    global mainsign
    del(image)
    del(spaceimage)
    del(mainsign)
    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_KP_ENTER):
                game_framework.change_state(mainstate)
    pass


def draw():
    clear_canvas()
    image.draw(350, 262)
    spaceimage.draw(350, 200)
    mainsign.draw(350, 350)
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






