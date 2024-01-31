# First part: There are two tasks, by pressing "space" user should
# be able to switch between the two tasks


import pyglet as pg
import sympy as sp
from pyglet import shapes
from pyglet.window import key
import random as rd

window = pg.window.Window(caption="Bendik S. Kristoffersen")
batch1 = pg.graphics.Batch()  # task A
batch2 = pg.graphics.Batch()  # task A
batch3 = pg.graphics.Batch()  # task B

colors = [(255, 153, 51), (153, 255, 153), (153, 255, 255), (204, 153, 255)]

is_task = 0  # to switch using SPACE


class Circle:
    def __init__(self, x, y, radius, vel_x, vel_y, color, batch):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color
        self.batch = batch


def task_circle(n):
    global colors
    makecircles = []
    for i in range(n):
        pos_x = rd.randint(50, window.width - 10)
        pos_y = rd.randint(50, window.height - 10)
        vel_x = rd.randint(-100, 100)
        vel_y = rd.randint(-100, 100)
        radicircles = rd.randint(25, 35)
        circle = shapes.Circle(pos_x, pos_y, radicircles, color=colors[0], batch=batch1)
        #makecircles.append(shapes.Circle(pos_x, pos_y, radicircles, vel_x, vel_y, color=colors[0], batch=batch1))
        circle.vel_x = vel_x
        circle.vel_y = vel_y
        makecircles.append(circle)

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
        vel_x = rd.randint(-50, 100)
        vel_y = rd.randint(-50, 100)
        line = shapes.Line(pos_x, pos_y, pos_x2, pos_y2, width, color=colors[1], batch=batch2)
        line.vel_x = vel_x
        line.vel_y = vel_y
        linelist.append(line)
    return linelist


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def absv(u):
    return sp.sqrt(u[0]**2 + u[1]**2)


def vec_subtraction(u, v):
    return [u[0].x - v[1].x, u[0].y - v[1].y]


def vec_projection(u, v):
    scalar = dot(u, v) / dot(v, v)
    return [scalar * v.x, scalar * v.y]


def task_b():
    global colors
    shapelist = [shapes.Line(400, 160, 370, 160, 80, color=colors[2], batch=batch3),
                 shapes.Line(390, 150, 360, 150, 100, color=colors[1], batch=batch3),
                 shapes.Line(550, 160, 520, 160, 80, color=colors[2], batch=batch3),
                 shapes.Line(560, 150, 530, 150, 80, color=colors[3], batch=batch3),
                 shapes.Rectangle(360, 190, 200, 150, color=colors[0], batch=batch3),
                 shapes.Ellipse(460, 350, 50, 50, color=colors[1], batch=batch3),
                 shapes.Triangle(360, 310, 410, 340, 360, 460, color=colors[2], batch=batch3),
                 shapes.Triangle(260, 310, 360, 370, 360, 460, color=colors[0], batch=batch3),
                 shapes.Triangle(560, 310, 510, 340, 560, 460, color=colors[3], batch=batch3),
                 shapes.Triangle(660, 310, 560, 370, 560, 460, color=colors[2], batch=batch3),
                 shapes.Circle(433, 360, 12, 12, color=colors[0], batch=batch3),
                 shapes.Circle(471, 360, 12, 12, color=colors[0], batch=batch3)]
    #
    return [shapelist]


def update_circle(dt, makeacircle):
    for circle in makeacircle:
        circle.x += dt * circle.vel_x
        circle.y += dt * circle.vel_y

        if circle.x > window.width - circle.radius:
            circle.x = -circle.radius
        elif circle.x < -circle.radius:
            circle.x = window.width - circle.radius

        if circle.y > window.height - circle.radius:
            circle.y = -circle.radius
        elif circle.y < -circle.radius:
            circle.y = window.height - circle.radius


def update_line(dt, makealine):
    for line in makealine:

        line.x += dt * line.vel_x
        line.x2 += dt * line.vel_x
        line.y += dt * line.vel_y
        line.y2 += dt * line.vel_y

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
        circle.color = colors[0]
        for i in range(len(makeacircle)):
            if circle is not makeacircle[i]:
                distance = sp.sqrt((makeacircle[i].x - circle.x) ** 2 + (makeacircle[i].y - circle.y)**2)
                if distance < makeacircle[i].radius + circle.radius:
                    circle.color = colors[2]


def line_circle_intersection(makealine, makeacircle):
    global colors
    for line in makealine:
        for circle in makeacircle:
            v = [circle.x - line.x, circle.y - line.y]  # From P1 -> Circle
            u = [circle.x - line.x2, circle.y - line.y2]
            distance1 = sp.sqrt(v[0] ** 2 + v[1] ** 2)


makeacircle = task_circle(3)
makealine = task_line(10)
makeanimal = task_b()


@window.event
def on_key_press(symbol, modifiers):
    global is_task

    if symbol == key.SPACE:
        is_task = 1 - is_task


@window.event
def on_draw():
    window.clear()
    if is_task == 0:  # Not pressed space yet
        batch1.draw()
        batch2.draw()
    elif is_task == 1:  # Space pressed
        batch3.draw()


def update(dt):
    update_line(dt, makealine)
    update_circle(dt, makeacircle)
    circlecollision(dt, makeacircle)


pg.clock.schedule_interval(update, 1 / 60)
pg.app.run()
