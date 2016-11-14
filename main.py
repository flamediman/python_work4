import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
speed = 1
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = [HEIGHT/2-PAD_HEIGHT/2, HEIGHT/2+PAD_HEIGHT/2]
paddle2_pos = [HEIGHT/2-PAD_HEIGHT/2, HEIGHT/2+PAD_HEIGHT/2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

def spawn_ball(direction):
    global ball_pos, ball_vel, speed
    speed = 1
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(3, 6), -random.randrange(2, 5)]
    else:
        ball_vel = [- random.randrange(3, 6), -random.randrange(2, 5)]


def move_ball():
    global ball_pos
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

def move_paddle(paddle_pos, paddle_vel):
    if paddle_pos[0] + paddle_vel >= 0 and paddle_pos[1] + paddle_vel <= HEIGHT:
        paddle_pos[0] += paddle_vel
        paddle_pos[1] += paddle_vel
    return paddle_pos


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH / 2, 0], [PAD_WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH / 2, 0], [WIDTH - PAD_WIDTH / 2, HEIGHT], 1, "White")
    move_ball()

    if ball_pos[0] <= PAD_WIDTH / 2 + BALL_RADIUS - 1:
        score1 += 1
        spawn_ball(RIGHT)
    if ball_pos[0] >= WIDTH - BALL_RADIUS - 1 - PAD_WIDTH / 2:
        score2 += 1
        spawn_ball(LEFT)
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS - 1:
        ball_vel[1] *= -1;

    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "white", "White")
    canvas.draw_text(str(score1), [WIDTH//2-50, 30], 30, "White")
    canvas.draw_text(str(score2), [WIDTH//2+50, 30], 30, "White")


    paddle1_pos = move_paddle(paddle1_pos, paddle1_vel)
    paddle2_pos = move_paddle(paddle2_pos, paddle2_vel)

    canvas.draw_line([PAD_WIDTH, paddle1_pos[0]], [PAD_WIDTH, paddle1_pos[1]], PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH-PAD_WIDTH-1, paddle2_pos[0]], [WIDTH-PAD_WIDTH-1, paddle2_pos[1]], PAD_WIDTH, 'White')

    if ball_pos[0] <= 2*PAD_WIDTH+BALL_RADIUS and (ball_pos[1]+BALL_RADIUS >= paddle1_pos[0] and ball_pos[1]+BALL_RADIUS <= paddle1_pos[1] or ball_pos[1]-BALL_RADIUS >= paddle1_pos[0] and ball_pos[1]-BALL_RADIUS <= paddle1_pos[1]):
        ball_vel[0] *= -1.1
    if ball_pos[0] >= WIDTH - BALL_RADIUS -1-2*PAD_WIDTH and (ball_pos[1]+BALL_RADIUS >= paddle2_pos[0] and ball_pos[1]+BALL_RADIUS <= paddle2_pos[1] or ball_pos[1]-BALL_RADIUS >= paddle2_pos[0] and ball_pos[1]-BALL_RADIUS <= paddle2_pos[1]):
        ball_vel[0] *= -1.1

def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 4
    if key == simplegui.KEY_MAP["W"]:
        paddle1_vel = -vel
    elif key == simplegui.KEY_MAP["S"]:
        paddle1_vel = vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["W"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["S"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

spawn_ball(RIGHT)
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()
