import pygame as pg
import sys
import ball
import paddle

pg.init()

scr = pg.display.set_mode((1200, 800))
pg.display.set_caption("PongBongGame")
clck = pg.time.Clock()

icon = pg.image.load("pic/ball.png")

pg.display.set_icon(icon)

o_ball = ball.Ball(screen=scr)
paddle1 = paddle.Paddle(screen=scr, topleft=[10, 0])
paddle2 = paddle.Paddle(screen=scr, topleft=[1155, 0])
sprite_group = pg.sprite.Group()
sprite_group.add(o_ball)
sprite_group.add(paddle1)
sprite_group.add(paddle2)

if __name__ == "__main__":
    while True:
        pg.display.flip()

        scr.fill("White")
        pg.draw.line(scr, "Black", (600, 0), (600, 800), 10)

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_w:
                    paddle1.control(-10)
                elif ev.key == pg.K_s:
                    paddle1.control(10)
                elif ev.key == pg.K_UP:
                    paddle2.control(-10)
                elif ev.key == pg.K_DOWN:
                    paddle2.control(10)
            if ev.type == pg.KEYUP:
                if ev.key in (pg.K_w, pg.K_s):
                    paddle1.control(0)
                if ev.key in (pg.K_UP, pg.K_DOWN):
                    paddle2.control(0)

        o_ball.update()
        paddle1.update()
        paddle2.update()
        sprite_group.draw(scr)

        clck.tick(50)
