import random

import pyglet as pg
from pyglet import shapes
import random

window = pg.window.Window()
batch = pg.graphics.Batch()


def updatepos(dt):
    global circle, velx, vely
    circle.x += dt * velx
    circle.y += dt * vely

    if circle.x > window.width - circle.radius:
        circle.x = window.width - circle
        velx *= -1.0    # turns circle around
    elif circle.x < circle.radius:
        circle.x = circle.radius

    if circle.y > window.height - circle.radius:
        circle.y = window.height - circle
        vely *= -1.0
    elif circle.y < circle.radius:
        circle.y = circle.radius

def diffposition(x, y):
    pos_x = random.randint(window.width - 200, window.height - 100)
    pos_y = random.randint(window.width - 200, window.height - 100)
    return x, y


rectangle = shapes.Rectangle(100, 250, 100, 100, color=(255, 255, 255), batch=batch)
ellipse = shapes.Ellipse(180, 360, 100, 85, color=(255, 255, 255), batch=batch)
star = shapes.Star(450, 200, 200, 25, 8, color=(255, 255, 255), batch=batch)
line = shapes.Line(700, 200, 200, 100, 100, color=(255, 255, 255), batch=batch)


@window.event()
def on_draw():
    window.clear()
    batch.draw()

pg.app.run()
