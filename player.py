import game_framework
from pico2d import *

import gameworld

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.timer = 1000

    def exit(mario, event):
        if event == SPACE:
            mario.fire_ball()
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mario.timer -= 1
        if mario.timer == 0:
            mario.add_event(SLEEP_TIMER)

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(int(mario.frame) * 19, 0, 19, 33, mario.x, mario.y)
        else:
            mario.image.clip_draw(int(mario.frame) * 19, 0, 19, 33, mario.x, mario.y)


class RunState:

    def enter(mario, event):
        # fill here
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.dir = clamp(-1, mario.velocity, 1)
        pass

    def exit(mario, event):
        if event == SPACE:
            mario.fire_ball()

    def do(mario):
        # fill here
        mario.frame = (mario.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 4
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1600 - 25)
    @staticmethod
    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(int(mario.frame) * 19, 0, 19, 66, mario.x, mario.y)
        else:
            mario.image.clip_draw(int(mario.frame) * 19, 0, 19, 66, mario.x, mario.y)


class SleepState:

    def enter(mario, event):
        mario.frame = 0

    def exit(mario, event):
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_composite_draw(int(mario.frame) * 100, 300, 100, 100, 3.141592 / 2, '', mario.x - 25, mario.y - 25, 100, 100)
        else:
            mario.image.clip_composite_draw(int(mario.frame) * 100, 200, 100, 100, -3.141592 / 2, '', mario.x + 25, mario.y - 25, 100, 100)






next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}

class Mario:

    def __init__(self):
        self.x, self.y = 700 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('resource/Mario_run.png')
        # fill here
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

        # fill here

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

