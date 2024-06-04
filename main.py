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
paddle1 = paddle.Paddle(screen=scr, topleft=[20, 200], variant=0)
paddle2 = paddle.Paddle(screen=scr, topleft=[1145, 200], variant=1)
sprite_group = pg.sprite.Group()
sprite_group.add(o_ball)
sprite_group.add(paddle1)
sprite_group.add(paddle2)

score_font = pg.font.Font("fonts/jungle-adventurer-cufonfonts/JungleAdventurer.ttf", 50)
click_anywhere_to_start_font = pg.font.Font("fonts/jungle-adventurer-cufonfonts/JungleAdventurer.ttf", 100)
click_anywhere_to_start_text = click_anywhere_to_start_font.render("CLICK ANYWHERE TO START", True, "Black")

started = False
wait = False
finished = False

if __name__ == "__main__":
    while True:
        pg.display.flip()

        scr.fill("White")

        if not started:
            scr.blit(click_anywhere_to_start_text, (70, 350))

            if pg.mouse.get_pressed()[0]:
                started = True
                wait = True

        if started and not finished:
            pg.draw.line(scr, "Black", (600, 0), (600, 800), 10)
            pg.draw.rect(scr, "Black", (0, 0, 1200, 800), 10)

            if o_ball.rect.colliderect(paddle1.rect):
                o_ball.vector[0] = -o_ball.vector[0]
            if o_ball.rect.colliderect(paddle2.rect):
                o_ball.vector[0] = -o_ball.vector[0]

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if started and not finished:
                if ev.type == pg.KEYDOWN:
                    if ev.key == pg.K_w:
                        paddle1.control(-10)
                    elif ev.key == pg.K_s:
                        paddle1.control(10)
                    if ev.key == pg.K_UP:
                        paddle2.control(-10)
                    elif ev.key == pg.K_DOWN:
                        paddle2.control(10)
                if ev.type == pg.KEYUP:
                    if ev.key in (pg.K_w, pg.K_s):
                        paddle1.control(0)
                    if ev.key in (pg.K_UP, pg.K_DOWN):
                        paddle2.control(0)

        if started and not finished:
            paddle1.update()
            paddle2.update()
            o_ball.update()
            sprite_group.draw(scr)

            score1 = score_font.render(str(o_ball.score1), True, "Black")
            score2 = score_font.render(str(o_ball.score2), True, "Black")
            scr.blit(score1, (580 - score1.get_width(), 20))
            scr.blit(score2, (630 + score1.get_width(), 20))

            if o_ball.score1 == 7 or o_ball.score2 == 7:
                finished = True

        if wait:
            pg.time.wait(800)
            wait = False

        if finished:
            if o_ball.score1 > o_ball.score2:
                red_won = click_anywhere_to_start_font.render(f"Red won {o_ball.score1}:{o_ball.score2}", True, "Red")
                scr.blit(red_won, (600 - red_won.get_width()//2, 350))
            else:
                blue_won = click_anywhere_to_start_font.render(f"Blue won {o_ball.score1}:{o_ball.score2}", True, "Blue")
                scr.blit(blue_won, (600 - blue_won.get_width()//2, 350))
        clck.tick(50)
