import pyglet as pg
from pyglet import shapes, image
import random


window = pg.window.Window()
batch = pg.graphics.Batch()

# for the giggles
pic = image.load('C:/Users/BendikKristoffersen/PycharmProjects/pythonProject/bunaSTRETCH.png')
sprite = pg.sprite.Sprite(img=pic)


def create_circles(n):
    circles = []
    for x in range(n):
        pos_x = random.randint(10, window.width - 10)
        pos_y = random.randint(10, window.height - 10)
        radius = random.randint(10, 25)
        circles.append(shapes.Circle(pos_x, pos_y, radius=radius,
                                     color=(random.randrange(155, 255, 25),
                                            random.randrange(100, 255, 25),
                                            random.randrange(100, 255, 25))
                                     , batch=batch))
    return circles


circlez = create_circles(100)


velx = random.uniform(-50, 100)
vely = random.uniform(25, 100)


def updatepos(dt):
    global circlez, velx, vely

    for circle in circlez:
        circle.x += dt * velx
        circle.y += dt * vely

        if circle.x > window.width - circle.radius:
            circle.x = window.width - circle.radius
            velx *= -1.0  # turns circle around
        elif circle.x < circle.radius:
            circle.x = circle.radius

        if circle.y > window.height - circle.radius:
            circle.y = window.height - circle.radius
            vely *= -1.0
        elif circle.y < circle.radius:
            circle.y = circle.radius
    print(velx, vely)


@window.event()
def on_draw():
    window.clear()
    sprite.draw()
    batch.draw()


pg.clock.schedule_interval(updatepos, 1.0/60.0)  # update 60 times per second

pg.app.run()
