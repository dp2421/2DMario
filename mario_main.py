from pico2d import *
import game_framework
import Mariostage
import start_state
import gameworld
from start_ground import StartGround
from player import Mario


name = "MainState"
ground = None
mario = None
idlemario =None
door = None
background = None
flipmario = None

class Door:
	def __init__(self):
		self.image = load_image('resource/stagedoor.png')
		self.x=500
	def draw(self):
		self.image.draw(self.x, 100)
		self.image.draw(self.x+100, 100)
	pass

def handle_events():
	events = get_events()
	for event in events:
		if event.type ==SDL_QUIT:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			game_framework.quit()
		else:
			mario.handle_event(event)
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
    global mario, startground, background
    startground = StartGround()
    mario= Mario()
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

	update_canvas()



def pause():
    pass


def resume():
    pass