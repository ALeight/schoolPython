# First part: There are two tasks, by pressing "space" user should
# be able to switch between the two tasks


import pyglet as pg
from pyglet import shapes
from pyglet.window import key
import random as rd


window = pg.window.Window(caption="Bendik S. Kristoffersen")
batch1 = pg.graphics.Batch()
batch2 = pg.graphics.Batch()


colors = [(255, 0, 0), (0, 255, 0), (150, 150, 0)]
# for task a, I need four distinct colours. Second part is creating line-segments and several disks moving
# around the screen with random velocities chosen at the start.
def task_circle(n):
    makecircles = []
    for i in range(n):
        pos_x = rd.randint(1, window.width - 10)
        pos_y = rd.randint(1, window.height - 10)
        radicircles = rd.randint(10, 21)
        makecircles.append(shapes.Circle(pos_x, pos_y, radicircles,
                                         color=(210, 170, 0), batch=batch1))
    return makecircles


def task_line(n):
    linelist = []
    for i in range(n):
        ycoordlines = rd.randint(1, 3)
        pos_x = rd.randrange(25, window.width - 50, 5)
        pos_y = rd.randrange(1, window.height - 25, 5)
        pos_x2 = rd.randrange(25, window.width - 50, 5)
        pos_y2 = rd.randrange(1, window.height - 25, 5)
        linelist.append(shapes.Line(pos_x, pos_y, pos_x2, pos_y2, ycoordlines, color=
                                    (rd.randrange(105, 170, 15),
                                        rd.randrange(105, 170, 15),
                                        rd.randrange(171, 209, 15)), batch=batch2))
    return linelist


def task_b():
    pass


makeacircle = task_circle(10)
makealine = task_line(5)


@window.event
def on_key_press(symbol, modifiers):
    pass


@window.event
def on_draw():
    window.clear()
    batch1.draw()
    batch2.draw()


def update(dt):
    global makeacircle, makealine
    vel_x = rd.randint(15, 50)
    vel_y = rd.randint(15, 50)

    for circle in makeacircle:
        circle.x += dt * vel_x
        circle.y += dt * vel_y
        if circle.x > window.width - circle.radius:
            circle.x = window.width - circle.radius
            # if circle at the end of the screen, it should appear at the other side
            vel_x *= -1  # reversing x-velocity
        elif circle.x < circle.radius:
            circle.x = circle.radius
            vel_x *= -1

        if circle.y > window.height - circle.radius:
            circle.y = window.height - circle.radius
            vel_y *= -1  # reversing y-velocity
        elif circle.y < circle.radius:
            circle.y = circle.radius
            vel_y *= -1

    for line in makealine:
        line.x += dt * vel_x
        line.y += dt * vel_y

        if line.x > window.width:
            line.x = window.width
            vel_x *= -1
        elif line.x < window.width:
            pass

        if line.y > window.height:
            pass


pg.clock.schedule_interval(update, 1/60)
pg.app.run()
