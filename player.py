import game_framework
# import stage_1
from pico2d import *
import server
from stagetile import StageGround
import gameworld

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_UP, SPACE_DOWN = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN
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

    def exit(mario, event):
        if event == SPACE_UP:
            mario.y = 90
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def draw(mario):
        if mario.dir == 1:
            mario.idleimage.clip_draw(int(mario.frame) * 47, 0, 47, 70, mario.x, mario.y)
        else:
            mario.idleimage.clip_draw(int(mario.frame) * 47, 0, 47, 70, mario.x, mario.y)

class JumpState:
    def enter(mario, event):
        if event == SPACE_DOWN:
            mario.y = 120
        elif event == SPACE_UP:
            mario.y = 90

    def exit(mario, event):
        if event == SPACE_UP:
            mario.y = 90
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
    def draw(mario):
        if mario.dir == 1:
            mario.idleimage.clip_draw(int(mario.frame) * 47, 0, 47, 70, mario.x, mario.y)
        else:
            mario.idleimage.clip_draw(int(mario.frame) * 47, 0, 47, 70, mario.x, mario.y)
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
        if event == SPACE_UP:
            mario.y = 90
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 4
        if game_framework.stack == ['stage_1'] and mario.x >= 725//2:
            mario.x = 725//2
        else:
            mario.x += mario.velocity * game_framework.frame_time

        mario.x = clamp(25, mario.x, 1600 - 25)
    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(int(mario.frame) * 50, 0, 50, 70, mario.x, mario.y)
        else:
            mario.flipimage.clip_draw(int(mario.frame) * 50, 0, 50, 70, mario.x, mario.y)





next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE_DOWN: JumpState, SPACE_UP: JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE_DOWN: JumpState, SPACE_UP: IdleState},
    JumpState: {RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE_DOWN: JumpState, SPACE_UP: RunState}
}

class Mario:

    def __init__(self):
        self.x, self.y = 100 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('resource/mariowalk.png')
        self.idleimage = load_image('resource/idlemario.png')
        self.flipimage = load_image('resource/flipmario.png')
        # fill here
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
    def get_bb(self):
        return self.x - 25, self.y - 35, self.x + 25, self.y + 25

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
            self.x = clamp(50, self.x, server.background.w-50)
            self.y = clamp(50, self.y,server.background.h-50)

    def draw(self):
        self.cur_state.draw(self)

        # fill here

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
#
# import game_framework
# from pico2d import *
#
# import gameworld
# import server
#
# # Boy Run Speed
# PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
# RUN_SPEED_KMPH = 40.0  # Km / Hour
# RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
# RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
# RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
#
# # Boy Action Speed
# TIME_PER_ACTION = 0.5
# ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# FRAMES_PER_ACTION = 4
#
#
#
# # Boy Event
# RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE = range(9)
#
# key_event_table = {
#     (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
#     (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
#     (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
#     (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
#     (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
#     (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
#     (SDL_KEYUP, SDLK_UP): UPKEY_UP,
#     (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
#     (SDL_KEYDOWN, SDLK_SPACE): SPACE
# }
#
#
# # Boy States
#
# class WalkingState:
#
#     def enter(mario, event):
#         if event == RIGHTKEY_DOWN:
#             mario.x_velocity += RUN_SPEED_PPS
#         elif event == RIGHTKEY_UP:
#             mario.x_velocity -= RUN_SPEED_PPS
#         if event == LEFTKEY_DOWN:
#             mario.x_velocity -= RUN_SPEED_PPS
#         elif event == LEFTKEY_UP:
#             mario.x_velocity += RUN_SPEED_PPS
#
#         if event == UPKEY_DOWN:
#             mario.y_velocity += RUN_SPEED_PPS
#         elif event == UPKEY_UP:
#             mario.y_velocity -= RUN_SPEED_PPS
#         if event == DOWNKEY_DOWN:
#             mario.y_velocity -= RUN_SPEED_PPS
#         elif event == DOWNKEY_UP:
#             mario.y_velocity += RUN_SPEED_PPS
#
#
#
#     def exit(mario, event):
#         if event == SPACE:
#             mario.fire_ball()
#
#     def do(mario):
#         mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
#         mario.x += mario.x_velocity * game_framework.frame_time
#         mario.y += mario.y_velocity * game_framework.frame_time
#
#
#     def draw(mario):
#         # cx, cy = server.background.canvas_width//2, server.background.canvas_height//2
#         cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom
#
#         if mario.x_velocity > 0:
#             mario.image.clip_draw(int(mario.frame) * 50, 0, 50, 70, cx, cy)
#             mario.dir = 1
#         elif mario.x_velocity < 0:
#             mario.image.clip_draw(int(mario.frame) * 50, 0, 50, 70, cx, cy)
#             mario.dir = -1
#         else:
#             # if boy x_velocity == 0
#             if mario.y_velocity > 0 or mario.y_velocity < 0:
#                 if mario.dir == 1:
#                     mario.image.clip_draw(int(mario.frame) * 50, 0, 50, 70, cx, cy)
#                 else:
#                     mario.image.clip_draw(int(mario.frame) * 50, 0, 50, 70, cx, cy)
#             else:
#                 # boy is idle
#                 if mario.dir == 1:
#                     mario.image.clip_draw(int(mario.frame) * 100, 300, 100, 100, cx, cy)
#                 else:
#                     mario.image.clip_draw(int(mario.frame) * 100, 200, 100, 100, cx, cy)
#
#
# next_state_table = {
#     WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
#                 UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
#                 SPACE: WalkingState}
# }
#
#
# class Mario:
#
#     def __init__(self):
#         # Boy is only once created, so instance image loading is fine
#         self.image = load_image('resource/mariowalk.png')
#         self.idleimage = load_image('resource/idlemario.png')
#         self.flipimage = load_image('resource/flipmario.png')
#         # self.font = load_font('ENCR10B.TTF', 16)
#         self.dir = 1
#         self.x_velocity, self.y_velocity = 0, 0
#         self.frame = 0
#         self.event_que = []
#         self.cur_state = WalkingState
#         self.cur_state.enter(self, None)
#         self.x, self.y = 200, 100
#
#
#     def get_bb(self):
#         return self.x - 50, self.y - 50, self.x + 50, self.y + 50
#
#
#     def set_background(self, bg):
#         self.bg = bg
#         self.x = self.bg.w / 2
#         self.y = self.bg.h / 2
#
#     def add_event(self, event):
#         self.event_que.insert(0, event)
#
#     def update(self):
#         self.cur_state.do(self)
#         if len(self.event_que) > 0:
#             event = self.event_que.pop()
#             self.cur_state.exit(self, event)
#             self.cur_state = next_state_table[self.cur_state][event]
#             self.cur_state.enter(self, event)
#
#         # self.x = clamp(50, self.x, server.background.w-50)
#         # self.y = clamp(50, self.y,server.background.h-50)
#
#     def draw(self):
#         self.cur_state.draw(self)
#
#
#     def handle_event(self, event):
#         if (event.type, event.key) in key_event_table:
#             key_event = key_event_table[(event.type, event.key)]
#             self.add_event(key_event)
