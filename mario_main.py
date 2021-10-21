from pico2d import *
import game_framework
import Mariostage

class Ground:
	def __init__ (self):
		self.image = load_image('main_ground.png')
		self.x = 34
	def draw(self):
		for i in range(50):
			self.image.draw(self.x * i,18)
			self.image.draw(self.x * i, 36)
			self.image.draw(self.x * i, 54)
	pass
class Door:
	def __init__(self):
		self.image = load_image('stagedoor.png')
		self.x=500
	def draw(self):
		self.image.draw(self.x, 100)
		self.image.draw(self.x+100, 100)
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
			elif event.key == SDLK_DOWN:
				if x>=500 and x<650:
					game_framework.change_state(Mariostage)
				elif x>=600 and x<=650:
					game_framework.change_state(Mariostage)
				# else:
				# 	웅크리는 모션
		elif event.type == SDL_KEYUP:
			if event.key ==SDLK_RIGHT:
				dir -= 1
			elif event.key ==SDLK_LEFT:
				dir += 1
			elif event.key == SDLK_SPACE:
				y -=20

            
def enter():
    global mario, ground
    ground = Ground()
    mario = load_image('mariowalk.png')
    idlemario =load_image('idlemario.png')
    door = Door()
    background = load_image('background.png')
    flipmario = load_image('flipmario.png')
    pass


def exit():
    global mario, ground
    del(mario)
    del(ground)
    del(door)
    del(background)
    del(flipmario)
    del(idlemario)
    pass
open_canvas(700, 500)

ground = Ground()
mario = load_image('mariowalk.png')
idlemario =load_image('idlemario.png')
door = Door()
background = load_image('background.png')
flipmario = load_image('flipmario.png')
running =True
x = 300
y=100
frame = 0
dir =0
while running:
	

	clear_canvas()
	handle_events()
	background.draw(400, 300)
	door.draw()
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