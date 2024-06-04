import pygame as pg
import random as rand


class Ball(pg.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.topleft = [600, rand.randint(200, 600)]
        self.vector = [0, 0]
        if rand.randint(0, 1) == 0:
            self.vector[0] = rand.randint(5, 10)
        else:
            self.vector[0] = -rand.randint(5, 10)
        if rand.randint(0, 1) == 0:
            self.vector[1] = rand.randint(5, 10)
        else:
            self.vector[1] = -rand.randint(5, 10)
        self.image = pg.image.load("pic/ball.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=tuple(self.topleft))

        self.score1 = 0
        self.score2 = 0

    def reroll(self):
        self.topleft = [584, rand.randint(200, 600)]
        self.rect.x = 584
        self.rect.y = self.topleft[1]
        self.vector = [0, 0]
        if rand.randint(0, 1) == 1:
            self.vector[0] = rand.randint(self.score1 + self.score2 + 5, self.score1 + self.score2 + 10)
        else:
            self.vector[0] = -rand.randint(self.score1 + self.score2 + 5, self.score1 + self.score2 + 10)
        if rand.randint(0, 1) == 1:
            self.vector[1] = rand.randint(self.score1 + self.score2 + 5, self.score1 + self.score2 + 10)
        else:
            self.vector[1] = -rand.randint(self.score1 + self.score2 + 5, self.score1 + self.score2 + 10)

    def update(self):
        self.rect.x += self.vector[0]
        self.rect.y += self.vector[1]

        if self.rect.y >= 758:
            self.rect.y = 758
            self.vector[1] = -self.vector[1]
        if self.rect.y <= 10:
            self.rect.y = 10
            self.vector[1] = -self.vector[1]
        if self.rect.x <= 35:
            self.score2 += 1
            self.reroll()
        if self.rect.x >= 1133:
            self.score1 += 1
            self.reroll()
