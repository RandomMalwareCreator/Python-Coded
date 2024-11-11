import sys
import time
import random
import ctypes
import win32gui
import win32con
import win32api
import colorsys
from time import sleep

def draw_rects(dc, count, width, height, dx, dy):
    screen_width = 1920
    screen_height = 1080
    for i in range(count):
        x = random.randint(0, screen_width - width)
        y = random.randint(0, screen_height - height)
        win32gui.PatBlt(dc, x, y, width, height, win32con.PATINVERT)
        width -= dx
        height -= dy

def screen_stretch(hdc, sw, sh, size, delay):
    win32gui.StretchBlt(
        hdc,
        int(size / 2),
        int(size / 2),
        sw - size,
        sh - size,
        hdc,
        0,
        0,
        sw,
        sh,
        win32con.SRCCOPY,
    )
    sleep(delay)

def hsv_color_shift(hdc, sw, sh, color):
    rgb_color = colorsys.hsv_to_rgb(color, 1.0, 1.0)
    brush = win32gui.CreateSolidBrush(
        win32api.RGB(
            int(rgb_color[0]) * 255, int(rgb_color[1]) * 255, int(rgb_color[2]) * 255
        )
    )
    win32gui.SelectObject(hdc, brush)
    win32gui.BitBlt(
        hdc,
        random.randint(-10, 10),
        random.randint(-10, 10),
        sw,
        sh,
        hdc,
        0,
        0,
        win32con.SRCCOPY,
    )
    win32gui.BitBlt(
        hdc,
        random.randint(-10, 10),
        random.randint(-10, 10),
        sw,
        sh,
        hdc,
        0,
        0,
        win32con.PATINVERT,
    )

def main(*argv):
    hdc = win32gui.GetDC(0)
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    sw, sh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    delay = 0.1
    size = 100
    count = 100
    width, height = 250, 250
    dx, dy = 10, 10
    color = 0

    while True:
        draw_rects(hdc, count, width, height, dx, dy)
        screen_stretch(hdc, sw, sh, size, delay)
        hsv_color_shift(hdc, sw, sh, color)

        color += 0.05
        if color >= 1.0:
            color = 0

if __name__ == "__main__":
    print("Python {:s} {:03d}bit on {:s}\n".format(" ".join(elem.strip() for elem in sys.version.split("\n")),
                                                   64 if sys.maxsize > 0x100000000 else 32, sys.platform))

    main(*sys.argv[1:])
