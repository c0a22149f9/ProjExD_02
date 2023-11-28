import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1400, 800


delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_RIGHT: (+5, 0),
    pg.K_LEFT: (-5, 0)
}


def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
    """
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    kk_rect.center= 900,400
    clock = pg.time.Clock()
    tmr = 0
    bomb_img=pg.Surface((20,20))

    pg.draw.circle(bomb_img,(255,0,0),(10,10),10)
    bomb_rect=bomb_img.get_rect()
    bomb_rect.centerx = random.randint(0, WIDTH)
    bomb_rect.centery = random.randint(0, HEIGHT)
    vx = +5 
    vy = +5
    #bomb.set_colorkey((0,0,0))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rect.colliderect(bomb_rect):
            print("Game Over")
            return
            
        key_lst = pg.key.get_pressed()
        sum_mv =[0, 0]
        for k, tpl in delta.items():
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]

        screen.blit(bg_img, [0, 0])
        kk_rect.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rect) != (True,True):
            kk_rect.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rect)
        bomb_rect.move_ip(vx, vy)
        yoko, tate =check_bound(bomb_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        bomb_rect.move_ip(vx,vy)
        screen.blit(bomb_img, bomb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()