import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
a = 0
balls = []
vel = []
i = -1

def keydown(key):
    global a
    if key == simplegui.KEY_MAP["W"]:
        a += 1
    elif key == simplegui.KEY_MAP["S"]:
        a -= 1

def draw(canvas):
    global i
    if len(balls) > 0:
        j = -1
        while j < i:
            j += 1
            ball_pos = balls[j]
            ball_vel = vel[j]
            ball_pos[0] += a * ball_vel[0]
            ball_pos[1] += a * ball_vel[1]

            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]

            if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS - 1:
                ball_vel[0] *= -1
            if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS - 1:
                ball_vel[1] *= -1

            canvas.draw_circle(balls[j], BALL_RADIUS, 5, "Blue", "White")


def click(pos):
    global balls, i
    i = i + 1
    balls.append(list(pos))
    vel.append([random.randrange(-5, 5), random.randrange(-5, 5)])


frame = simplegui.create_frame("Движение мячика", WIDTH, HEIGHT)

frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

frame.start()
