import pyglet as pg
from pyglet import shapes
from pyglet.window import key


window = pg.window.Window()


mylist = [1, 3, 5, 2, 2, 6, 7, 8, 5, 5, 5, 8]


# Computing a function which returns number of elements larger than both its predecessor and its successor
# Finish the implementation of the function
def counter(someList):
    count = 0
    if len(someList) < 3:
        return 0
    # for x in SomeList[2:] --> [2:], the colon implies it copies the list
    for x in range(len(someList[2:])):  # numbers before and after colon implies where list is sliced
        if (someList[x - 1] < someList[x]) and (someList[x] > someList[x + 1]):
            count += 1
        if someList[x] == -1:
            break
    return count


line = shapes.Line(100, 150, 200, 300, color=(150, 150, 0))


def line_position():
    if line.x > window.width - line.get_width():
        line.x -= 1


@window.event
def on_draw():
    window.clear()
    line.draw()


# working with dictionary
directions = {'left': False, 'right': False, 'up': False, 'down': False}
speed = 5


# keep in mind, if 'left' is pressed, it is true for rest, unless on_key_release
@window.event
def on_key_press(symbol: int, modifiers: int):
    if symbol == key.LEFT:
        directions['left'] = True
    if symbol == key.RIGHT:
        directions['right'] = True
    if symbol == key.UP:
        directions['up'] = True
    if symbol == key.DOWN:
        directions['down'] = True


@window.event
def on_key_release(symbol: int, modifiers: int):
    if symbol == key.LEFT:
        directions['left'] = False
    if symbol == key.RIGHT:
        directions['right'] = False
    if symbol == key.UP:
        directions['up'] = False
    if symbol == key.DOWN:
        directions['down'] = False


def update(dt: float):
    if directions['left']:
        line.x -= speed
    if directions['right']:
        line.x += speed
    if directions['up']:
        line.y += speed
    if directions['down']:
        line.y -= speed


pg.clock.schedule_interval(update, 1.0/60.0)
pg.app.run()
