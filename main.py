import pygame as pg
import sys

pg.init()

scr = pg.display.set_mode((1200, 600))
clck = pg.time.Clock()

while True:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            sys.exit()