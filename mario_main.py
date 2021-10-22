from pico2d import *
import game_framework
# import Mariostage
import start_state


name = "MainState"
ground = None
mario = None
idlemario =None
door = None
background = None
flipmario = None

class Ground:
	def __init__ (self):
		self.image = load_image('resource/main_ground.png')
		self.x = 34
	def draw(self):
		for i in range(50):
			self.image.draw(self.x * i,18)
			self.image.draw(self.x * i, 36)
			self.image.draw(self.x * i, 54)
	pass
class Door:
	def __init__(self):
		self.image = load_image('resource/stagedoor.png')
		self.x=500
	def draw(self):
		self.image.draw(self.x, 100)
		self.image.draw(self.x+100, 100)
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
			elif event.key == SDLK_DOWN:
				if x>=500 and x<650:
					game_framework.change_state(Mariostage)
				elif x>=600 and x<=650:
					game_framework.change_state(Mariostage)
				# else:
				# 	웅크리는 모션
		elif event.type == SDL_KEYUP:
			if event.key ==SDLK_RIGHT:
				direct -= 1
			elif event.key ==SDLK_LEFT:
				direct += 1
			elif event.key == SDLK_SPACE:
				y -=20

            
def enter():
    global mario, ground, idlemario, door, background, flipmario, y, direct, x, frame
    ground = Ground()
    mario = load_image('resource/mariowalk.png')
    idlemario =load_image('resource/idlemario.png')
    door = Door()
    background = load_image('resource/startbackground.png')
    flipmario = load_image('resource/flipmario.png')
    y=120
    x= 300
    direct =0
    frame = 0
    pass


def exit():
    global mario, ground, door, background, flipmario, idlemario
    del(mario)
    del(ground)
    del(door)
    del(background)
    del(flipmario)
    del(idlemario)
    pass

# ground = Ground()
# mario = load_image('mariowalk.png')
# idlemario =load_image('idlemario.png')
# door = Door()
# background = load_image('background.png')
# flipmario = load_image('flipmario.png')
# running =True

def draw():
	global x, y, direct, frame
	clear_canvas()
	handle_events()
	background.draw(350, 262)
	door.draw()
	ground.draw()
	if direct > 0:
		mario.clip_draw(frame*50, 0, 50, 70, x, y)
	elif direct < 0:
		flipmario.clip_draw(frame*50, 0, 50, 70, x, y)
	elif direct == 0:
		idlemario.clip_draw(frame*48, 0, 48, 70, x, y)

	update_canvas()
	frame = (frame+1)%6
	x += direct * 5
	delay(0.05)

def update():

	pass

def pause():
    pass


def resume():
    pass