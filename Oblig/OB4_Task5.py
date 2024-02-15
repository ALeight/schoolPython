from pyglet import *

window = window.Window()


height = 500
width = 500


def clamp(n, low, hi):
    return max(low, min(hi, n))


def smoothstep(e1, e2, x):
    x = max(0, min((x-e1) / (e2 - e1)), 1)
    return x * x * (3 - 2 * x)


# circle 1 - red ball
circle1 = shapes.Circle(30, window.height - 30, 35, color=(255, 0, 0, 255))
# circle 2 - yellow ball
circle2 = shapes.Circle(230, window.height - 80, 35, color=(255, 255, 0, 255))
# green ball
circle3 = shapes.Circle(230, window.height - 80, 35, color=(0, 255, 0, 255))


# red ball
posx = 0
posy = 0
startx = 30
starty = window.height - 50
endx = 410
endy = window.height - 50
tpos = 0

# yellow ball
dir1 = 1.0
pos2x = 0
pos2y = 0
start2x = 20
start2y = window.height - 150
end2x = 400
end2y = window.height - 150
tpos2 = 0

# green ball
dir3 = 1.0
pos3x = 0
pos3y = 0
start3x = 40
start3y = window.height - 230
end3x = 400
end3y = start3y  # This should work right
tpos3 = 0


@window.event
def on_draw():
    window.clear()
    circle1.draw()
    circle1.x = posx
    circle1.y = posy

    circle2.draw()
    circle2.x = pos2x
    circle2.y = pos2y

    circle3.draw()
    circle3.x = pos3x
    circle3.y = pos3y


def update(dt):
    global posx, posy, tpos, dir1
    global pos2x, pos2y, tpos2
    global pos3x, pos3y, tpos3, dir3

    # red ball
    tpos += dt * 0.6
    if tpos > 1:
        tpos = 0

    posx = (1-tpos)*startx + tpos*endx
    posy = (1-tpos)*starty + tpos*endy

    # yellow ball
    tpos2 += dt * dir1 * 0.6
    if tpos2 > 1:
        dir1 = -1.0
    if tpos2 < 0:
        dir1 = 1.0

    pos2x = (1-tpos2)*start2x + tpos2*end2x
    pos2y = (1-tpos2)*start2y + tpos2*end2y

    # green ball
    tpos3 += dt * dir3
    if tpos3 > 1:
        dir3 = -1.0
    if tpos3 < 0:
        dir3 = 1.0

    pos3x = smoothstep(start3x, end3x, tpos3)
    pos3y = smoothstep(start3y, end3y, tpos3)


clock.schedule_interval(update, 1/60)
app.run()
