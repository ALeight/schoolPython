from pyglet import *

window = window.Window()
batch = graphics.Batch()

height = 500
width = 500


def time(t, dr):
    if t > 1:
        return dr*(-1)
    elif t < 0:
        return dr*(-1)
    return dr


def timef(d, t):
    if d > 0:
        return t**3
    return 1 - (1-t)**3


def sp(x):
    return x * x * (3 - 2 * x)


items = []
magcirc = []

class Circle(shapes.Circle):
    time, ts = 0, 2  # ts = time speed
    dr = 1
    s = False  # indicate smoothstep

    def __init__(self, x, y, r, c):
        super().__init__(x, y, r, c)
        self.batch = batch
        self.radius = r
        self.color = c
        self.x = x
        self.y = y

    @classmethod
    def updateTime(cls, dt):
        for obj in items + magcirc:
            obj.time += dt * obj.dt / obj.ts


# circle 1 - red ball
circle1 = shapes.Circle(30, window.height - 30, 20, color=(255, 0, 0, 255), batch=batch)
# circle 2 - yellow ball
circle2 = shapes.Circle(230, window.height - 80, 20, color=(255, 255, 0, 255), batch=batch)
# green ball
circle3 = shapes.Circle(230, window.height - 80, 20, color=(0, 255, 0, 255), batch=batch)
# blue ball
circle4 = shapes.Circle(20, window.height - 80, 20, color=(0, 0, 255, 255), batch=batch)
# red static circle
circle5 = shapes.Circle(100, window.height - 310, 50, color=(255, 0, 0, 255), batch=batch)
# interpolate red - green
circle6 = shapes.Circle(200, window.height - 310, 50, color=(0, 0, 255, 255), batch=batch)
# interpolate radius 25-50
circle7 = shapes.Circle(300, window.height - 310, 50, color=(0, 255, 0, 255), batch=batch)


def quadbez(obj, t, s, c, e):
    obj.x = s[0]*(1-t)**2 + c[0]*(1-t)*2*t + e[0]*t**2
    obj.y = s[1]*(1-t)**2 + c[1]*(1-t)*2*t + e[1]*t**2


# red ball
posx = 0
posy = window.height - 30
startx = 30
endx = 410
tpos = 0

# yellow ball
dir1 = 1.0
pos2x = 0
pos2y = window.height - 80
start2x = 20
end2x = 400
tpos2 = 0

# green ball
dir3 = 1.0
pos3x = 0
pos3y = window.height - 130
start3x = 40
end3x = 400
tpos3 = 0

# blue ball
dir4 = 1.0
pos4x = 0
s4x = 20
pos4y = window.height - 180
end4x = 400
tpos4 = 0

# interpolate size red circle
size1 = 0
r1 = 0
r2 = 50
tsize = 0
dir5 = 1.0

# interpolate color from red to green
color1 = 0
ecolor = [255, 0, 0]
scolor = [0, 255, 0]
ccol = [255, 0, 0]
dir6 = 1

# interpolate size and color
colorS = [0, 255, 0]
colorE = [255, 255, 0]
colort = 0
ccol2 = [0, 255, 0]
r = [50, 25]
r3 = 50
dir7 = 1

# bezier curve
timer = 0
startpos = [500, 400]
controlpos = [500, 0]
endpos = [20, 150]


@window.event
def on_draw():
    window.clear()
    batch.draw()
    circle1.x = posx
    circle1.y = posy

    circle2.x = pos2x
    circle2.y = pos2y

    circle3.x = pos3x
    circle3.y = pos3y

    circle4.x = pos4x
    circle4.y = pos4y

    circle5.radius = size1

    circle6.color = ccol

    circle7.radius = r3
    circle7.color = ccol2


def update(dt):
    global posx, tpos, dir1
    global pos2x, tpos2
    global pos3x, tpos3, dir3, pos4x, tpos4, dir4, s4x
    global size1, r1, r2, tsize, dir5
    global scolor, ecolor, color1, dir6, circle6, ccol
    global r, ccol2, colorS, colorE, dir7, colort, r3
    global magcirc, timer, startpos, endpos, controlpos
    # red circle
    tpos += dt / 5
    if tpos > 1:
        tpos = 0

    posx = (1-tpos)*startx + tpos*endx

    # yellow circle
    tpos2 += dt * dir1 / 2
    dir1 = time(tpos2, dir1)

    pos2x = (1-tpos2)*start2x + tpos2*end2x

    # green circle
    tpos3 += dt * dir3 / 2
    dir3 = time(tpos3, dir3)

    pos3x = (1-sp(tpos3))*start3x + sp(tpos3)*end3x

    # blue circle
    tpos4 += dt * dir4 / 5
    pp = timef(dir4, tpos4)
    dir4 = time(pp, dir4)

    pos4x = (1-pp)*s4x + pp*end4x

    # red r change
    tsize += dt * dir5 / 2
    dir5 = time(tsize, dir5)
    size1 = (1-sp(tsize))*r1 + sp(tsize)*r2

    # red to green interpolation
    color1 += dt * dir6 / 2
    dir6 = time(color1, dir6)

    circle6.color = ccol
    ccol[0] = max(0, min(255, int((1 - color1) * scolor[0] + color1 * ecolor[0])))
    ccol[1] = max(0, min(255, int((1 - color1) * scolor[1] + color1 * ecolor[1])))

    # interpolate radius and color
    colort += dt * dir7 / 2
    dir7 = time(colort, dir7)

    circle7.color = ccol2
    r3 = (1-sp(colort))*r[0] + sp(colort)*r[1]
    ccol2[0] = max(0, min(255, int((1 - sp(colort)) * colorS[0] + sp(colort) * colorE[0])))
    ccol2[1] = max(0, min(255, int((1 - sp(colort)) * colorS[1] + sp(colort) * colorE[1])))

    # bezier curve
    timer += 1
    if timer*dt >= 1/5:
        magcirc.append([shapes.Circle(500, 400, 15, color=(204, 0, 204), batch=batch), 1, 0])
        timer = 0

    for obj in magcirc:
        obj[2] += dt * obj[1] / 2
        obj[1] = time(obj[2], obj[1])
        quadbez(obj[0], obj[2], startpos, controlpos, endpos)
        if obj[1] == -1:
            magcirc.pop(0)


clock.schedule_interval(update, 1/60)
app.run()
