import pygame as pg
import random as rand


class Ball(pg.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.topleft = [rand.randint(300, 900), rand.randint(200, 600)]
        self.vector = [0, 0]
        while self.vector[0] == 0 or self.vector[1] == 0:
            self.vector = [rand.randint(-10, 10), rand.randint(-10, 10)]
        self.image = pg.image.load("pic/ball.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=tuple(self.topleft))

    def update(self):
        self.rect.x += self.vector[0]
        self.rect.y += self.vector[1]
