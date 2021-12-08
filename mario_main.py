from pico2d import *
import game_framework
import stage_1
import gameworld
from start_ground import StartGround
from background import StageBackground
from player import Mario
import server

name = "MainState"
mario = None
idlemario =None
door = None
background = None
flipmario = None

class Door:
	def __init__(self):
		self.image = load_image('resource/stagedoor.png')
		self.x=600
	def draw(self):
		self.image.draw(self.x, 100)
	pass
	def update(self):
		pass

def handle_events():
	events = get_events()
	for event in events:
		if event.type ==SDL_QUIT:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			game_framework.quit()
		elif server.mario.x> 550 and server.mario.x <650 and event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
			game_framework.change_state(stage_1)
		else:
			server.mario.handle_event(event)

            
def enter():
	global startground
	startground = StartGround()
	server.mario= Mario()
	server.door = Door()
	server.background = StageBackground()
	gameworld.add_object(server.door, 1)
	gameworld.add_object(server.background,0)
	gameworld.add_object(startground, 0)
	gameworld.add_object(server.mario, 1)
	pass

def exit():
	gameworld.clear()
	pass

def update():
	for game_object in gameworld.all_objects():
		game_object.update()

def draw():
	clear_canvas()
	for game_object in gameworld.all_objects():
		game_object.draw()
	update_canvas()

def pause():
    pass


def resume():
    pass