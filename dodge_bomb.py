import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1400, 800


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    bomb_img=pg.Surface((20,20))

    pg.draw.circle(bomb_img,(255,0,0),(10,10),10)
    bomb_rect=bomb_img.get_rect()
    bomb_rect.centerx = random.randint(0, WIDTH)
    bomb_rect.centery = random.randint(0, HEIGHT)

    #bomb.set_colorkey((0,0,0))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bomb_img, bomb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()