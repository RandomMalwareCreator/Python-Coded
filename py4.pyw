#!/usr/bin/env python

import sys
import time
from win32con import PATINVERT
from win32gui import GetDC, PatBlt
import random

def draw_rects(dc, count, width, height, dx, dy):
    screen_width = 1920
    screen_height = 1080
    
    for i in range(count):
        x = random.randint(0, screen_width - width)
        y = random.randint(0, screen_height - height)
        PatBlt(dc, x, y, width, height, PATINVERT)
        width -= dx
        height -= dy

def main(*argv):
    dc = GetDC(0)
    
    while True:
        draw_rects(dc, 100, 250, 250, 10, 10)
        time.sleep(0.1)

if __name__ == "__main__":
    print("Python {:s} {:03d}bit on {:s}\n".format(" ".join(elem.strip() for elem in sys.version.split("\n")),
                                                   64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    
    main(*sys.argv[1:])
