import pygame as pg


class Paddle(pg.sprite.Sprite):
    def __init__(self, screen, topleft):
        super().__init__()
        self.screen = screen
        self.topleft = topleft
        self.movey = 0
        self.image = pg.image.load("pic/paddle.png").convert()
        self.rect = self.image.get_rect(topleft=tuple(self.topleft))

    def control(self, new_movey):
        self.movey = new_movey

    def update(self):
        self.rect.y += self.movey
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 615:
            self.rect.y = 615
