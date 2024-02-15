from pyglet import *

window = window.Window()


height = 500
width = 500


# circle 1 - red ball
circle1 = shapes.Circle(30, window.height - 30, 50, color=(255, 0, 0, 255))
circle2 = shapes.Circle(230, window.height - 80, 50, color=(0, 255, 0, 255))


# red ball
posx = 0
posy = 0
startx = 30
starty = window.height - 20
endx = 410
endy = window.height - 20
tpos = 0

# yellow ball
dir = 1.0
pos2x = 0
pos2y = 0
start2x = 20
start2y = window.height - 80
end2x = 230
end2y = window.height - 80
tpos2 = 0


@window.event
def on_draw():
    window.clear()
    circle1.draw()
    circle1.x = posx
    circle1.y = posy

    circle2.draw()
    circle2.x = pos2x
    circle2.y = pos2y


def update(dt):
    global posx, posy, tpos, dir
    global pos2x, pos2y, tpos2

    tpos += dt * 0.6
    if tpos > 1:
        tpos = 0
    if tpos < 0:
        tpos = 0

    posx = (1-tpos)*startx + tpos*endx
    posy = (1-tpos)*starty + tpos*endy

    # yellow ball
    tpos2 += dt * dir
    if tpos2 > 1:
        dir = -1.0
    if tpos2 < 0:
        dir = 1.0

    pos2x = (1-tpos2)*start2x + tpos2*end2x
    pos2y = (1-tpos2)*start2y + tpos2*end2y


clock.schedule_interval(update, 1/60)
app.run()
