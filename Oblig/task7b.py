import pyglet as pg
from pyglet import shapes, image
import random
from math import pi


window = pg.window.Window(1920, 1080)
batch = pg.graphics.Batch()


rectangle = shapes.Rectangle(650, 40, 100, 100, color=(120, 210, 150), batch=batch)
ellipse = shapes.Ellipse(180, 300, 100, 85, color=(180, 255, 255), batch=batch)
star = shapes.Star(700, 300, 100, 20, 6, color=(10, 255, 255), batch=batch)
line = shapes.Line(350, 50, 300, 200, 5, color=(76, 160, 25), batch=batch)
square = shapes.Rectangle(50, 75, 100, 100, color=(210, 210, 55), batch=batch)
triangle = shapes.Triangle(500, 25, 600, 100, 50, 25, color=(150, 210, 150), batch=batch)
arc = shapes.Arc(890, 75, 75, angle=3*pi/2, color=(150, 210, 150), batch=batch)


def create_circles(n):
    circles = []
    for x in range(n):
        pos_x = random.randint(10, window.width - 10)
        pos_y = random.randint(10, window.height - 10)
        radius = random.randint(10, 25)
        circles.append(shapes.Circle(pos_x, pos_y, radius=radius,
                                     color=(random.randrange(155, 255, 25),
                                            random.randrange(155, 255, 25),
                                            random.randrange(155, 255, 25))
                                     , batch=batch))
    return circles


sirkel = create_circles(1000)


@window.event()
def on_draw():
    window.clear()
    batch.draw()


pg.app.run()
