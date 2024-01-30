# First part: There are two tasks, by pressing "space" user should
# be able to switch between the two tasks


import pyglet as pg
import sympy as sp
from pyglet import shapes
from pyglet.window import key
import random as rd

window = pg.window.Window(caption="Bendik S. Kristoffersen")
batch1 = pg.graphics.Batch()
batch2 = pg.graphics.Batch()

colors = [(245, 7, 7), (230, 159, 237), (249, 234, 33), (33, 249, 70)]

current_task = 0  # to switch using SPACE


# for task a, I need four distinct colours. Second part is creating line-segments and several disks moving
# around the screen with random velocities chosen at the start.
def task_circle(n):
    global colors
    makecircles = []
    for i in range(n):
        pos_x = rd.randint(50, window.width - 10)
        pos_y = rd.randint(50, window.height - 10)
        radicircles = rd.randint(25, 35)
        makecircles.append(shapes.Circle(pos_x, pos_y, radicircles,
                                         color=colors[0], batch=batch1))
    return makecircles


def task_line(n):
    global colors
    linelist = []
    for i in range(n):
        width = rd.randint(2, 4)
        pos_x = rd.randint(-50, 300)
        pos_y = rd.randint(-50, 300)
        pos_x2 = rd.randint(50, 600)
        pos_y2 = rd.randint(50, 600)
        linelist.append(shapes.Line(pos_x, pos_y, pos_x2, pos_y2, width, color=colors[1], batch=batch2))
    return linelist


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def absv(u):
    return sp.sqrt(u[0]**2 + u[1]**2)


def task_b():
    pass


def update_circle(dt, makeacircle):
    vel_x = rd.randint(-100, 50)
    vel_y = rd.randint(-100, 100)

    for circle in makeacircle:
        circle.x += dt * vel_x
        circle.y += dt * vel_y
        if circle.x > window.width - circle.radius:
            circle.x = -window.width - circle.radius

        elif circle.x < circle.radius:
            circle.x = circle.radius

        if circle.y > window.height - circle.radius:
            circle.y = -window.height - circle.radius
        elif circle.y < circle.radius:
            circle.y = circle.radius


def update_line(dt, makealine):
    for line in makealine:
        vel_x = rd.randint(10, 25)
        vel_y = rd.randint(10, 25)

        line.x += dt * vel_x * 5
        line.x2 += dt * vel_x * 5
        line.y += dt * vel_y * 5
        line.y2 += dt * vel_y * 5

        if min(line.x, line.x2) > window.width:  # last point has exited the screen on right side
            if line.x < line.x2:
                line.x = 0 - abs(line.x - line.x2)
                line.x2 = 0
            else:
                line.x2 = 0 - abs(line.x - line.x2)
                line.x = 0
        elif max(line.x, line.x2) < 0:
            if line.x < line.x2:
                line.x = window.width + abs(line.x - line.x2)
                line.x2 = window.width
            else:
                line.x2 = window.width + abs(line.x - line.x2)
                line.x = window.width
        elif min(line.y, line.y2) > window.height:
            if line.y < line.y2:
                line.y = 0 - abs(line.y - line.y2)
                line.y2 = 0
            else:
                line.y2 = 0 - abs(line.y - line.y2)
                line.y = 0
        elif max(line.y, line.y2) < 0:
            if line.y < line.y2:
                line.y = window.height + abs(line.y - line.y2)
                line.y2 = window.height
            else:
                line.y2 = window.height + abs(line.y - line.y2)
                line.y = window.height


def circlecollision(dt, makeacircle):
    global colors
    for circle in makeacircle:
        for i in range(len(makeacircle)):
            if circle is not makeacircle[i]:
                distance = sp.sqrt((makeacircle[i].x - circle.x) ** 2 + (makeacircle[i].y - circle.y)**2)
                if distance < makeacircle[i].radius + circle.radius:
                    circle.color = colors[3]



def line_circle_intersection(makealine, makeacircle):
    for line in makealine:
        for circle in makeacircle:
            v = [circle.x - line.x, circle.y - line.y]
            u = [circle.x - line.x2, circle.y - line.y2]
            # w = [line.x - circle.x, line.y - circle.y]
            distance = sp.sqrt(v[0]**2 + v[1]**2)


makeacircle = task_circle(5)
makealine = task_line(5)


@window.event
def on_key_press(symbol, modifiers):
    global current_task

    if symbol == key.SPACE:
        current_task = 1 - current_task


@window.event
def on_draw():
    window.clear()
    if current_task == 0:
        batch1.draw()
        batch2.draw()
    #elif current_task == 1:
     #   batch2.draw()


def update(dt):
    update_line(dt, makealine)
    update_circle(dt, makeacircle)
    circlecollision(dt, makeacircle)
    #if current_task == 0:
     #   update_circle(dt, makeacircle)
    #elif current_task == 1:
     #   update_line(dt, makealine)


pg.clock.schedule_interval(update, 1 / 60)
pg.app.run()
