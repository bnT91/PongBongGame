import pygame as pg


class Paddle(pg.sprite.Sprite):
    def __init__(self, screen, topleft, variant):
        super().__init__()
        self.screen = screen
        self.topleft = topleft
        self.movey = 0
        if not variant:
            self.image = pg.image.load("pic/paddle.png").convert()
        else:
            self.image = pg.image.load("pic/paddle (1).png").convert()
        self.rect = self.image.get_rect(topleft=tuple(self.topleft))

    def control(self, new_movey):
        self.movey = new_movey

    def update(self):
        self.rect.y += self.movey
        if self.rect.y < 20:
            self.rect.y = 20
        elif self.rect.y > 563:
            self.rect.y = 563
