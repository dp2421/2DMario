import game_framework
import pico2d
import start_state
import gameworld

pico2d.open_canvas(700, 525)
game_framework.run(start_state)
pico2d.close_canvas()