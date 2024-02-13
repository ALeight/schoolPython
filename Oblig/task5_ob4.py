import pyglet as pg
from pyglet import *
import math
from math import sin, cos

window = pg.window.Window()
batch1 = pg.graphics.Batch()
batch2 = pg.graphics.Batch()

height = 1000
width = 1000

circles = []
circlez = []

'''
staticcircle = []
numstatic = 1
for i in range(numstatic):
    pos1x = 150
    pos1y = 200
    pos2x = 300
    pos2y = 200
    pos3x = 450
    pos3y = 200

    staticcircle.append(shapes.Circle(pos1x, pos1y, 75, color=(150, 255, 255), batch=batch1)),
    staticcircle.append(shapes.Circle(pos2x, pos2y, 75, color=(100, 150, 255), batch=batch1)),
    staticcircle.append(shapes.Circle(pos3x, pos3y, 75, color=(250, 200, 255), batch=batch1))
'''


def makeCircle():
    global circles
    circles = [shapes.Circle(150, 200, 50, color=(150, 255, 255), batch=batch2),
               shapes.Circle(300, 200, 75, color=(100, 150, 255), batch=batch2),
               shapes.Circle(450, 200, 50, color=(250, 200, 255), batch=batch2)]
    return circles


@window.event
def on_draw():
    window.clear()
    batch1.draw()
    batch2.draw()


value = 0
makeCircle()


def update(dt):
    global value, circles
    value += 0.05
    if circles:
        for indx, circle in enumerate(circles):
            if indx == 0:
                circle.radius += sin(value) * 1.3
                next_r = circles[indx + 1].radius
                print(f"value: {value}")
                if circle.radius > next_r:
                    circle.radius -= (circle.radius - next_r) * 0.5

                print(f"next_r{next_r}")
                print(f"circle.r {circle.radius}")

                if circle.radius < 0:
                    circle.radius = 1
                    circle.radius += sin(value) * 1.3

            if indx == 1:
                circle.color = (100, 150, 255)

            if indx == 2:
                circle.radius -= sin(value)
                circle.color = (250, 200, 255)

                if circle.radius < -1:
                    circle.radius = 1
                    circle.radius += sin(value)


pg.clock.schedule_interval(update, 1 / 60)
pg.app.run()
