from pico2d import *
import game_framework
import stage_1
import gameworld
from start_ground import StartGround
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
		# elif event.type == SDL_KEYDOWN:
		# 	if event.key ==SDLK_RIGHT:
		# 		direct += 1
		# 	elif event.key ==SDLK_LEFT:
		# 		direct -= 1
		# 	elif event.key ==SDLK_SPACE:
		# 		y+=20
		# 	elif event.key == SDLK_DOWN:
		# 		if x>=500 and x<650:
		# 			game_framework.change_state(Mariostage)
		# 		elif x>=600 and x<=650:
		# 			game_framework.change_state(Mariostage)
		# elif event.type == SDL_KEYUP:
		# 	if event.key ==SDLK_RIGHT:
		# 		direct -= 1
		# 	elif event.key ==SDLK_LEFT:
		# 		direct += 1
		# 	elif event.key == SDLK_SPACE:
		# 		y -=20

            
def enter():
    global startground, background, door
    startground = StartGround()
    server.mario= Mario()
    door = Door()
    background = load_image('resource/mapbackground.png')
    gameworld.add_object(door, 1)
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
	background.draw(300, 300)
	for game_object in gameworld.all_objects():
		game_object.draw()
	update_canvas()



def pause():
    pass


def resume():
    pass