import rgb
import time
import random
import buttons, defines

rgb.clear()

pixels = []
pixel_speed = 0.05


def createpixels(x, y):
    pixels.append([x, y, random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)])


def removepixels():
    index = 0
    while index < 200:
        pixels.pop(0)
        index += 1


def init():
    if len(pixels) > 700:
        removepixels()

    index = 0

    while index < 200:
        createpixels(random.randint(0, 31), random.randint(0, 7))
        index += 1

    rgb.clear()

    for x in pixels:
        rgb.pixel((x[2], x[3], x[4]), (x[0], x[1]))


def callback_button_up(button_is_down):
    if button_is_down:
        global pixel_speed
        pixel_speed = pixel_speed * 1.2
        pass


buttons.register(defines.BTN_UP, callback_button_up)


def callback_button_down(button_is_down):
    if button_is_down:
        global pixel_speed
        pixel_speed = pixel_speed / 1.2
        pass


buttons.register(defines.BTN_DOWN, callback_button_down)


while True:
    time.sleep(pixel_speed)
    init()