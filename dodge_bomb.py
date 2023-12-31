import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1400, 800


delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_RIGHT: (+5, 0),
    pg.K_LEFT: (-5, 0),
}


bomb_imgs = []


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
    kk = {
    (0, +5):pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 90, 1.0),
    (0, -5):pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), -90, 1.0),
    (+5, -5):pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 45, 1.0),
    (+5, +5):pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), -45, 1.0),
    (+5, 0):pg.transform.flip(kk_img, True, False),
    (-5, +5):pg.transform.rotozoom(kk_img, 45, 1.0),
    (-5, -5):pg.transform.rotozoom(kk_img, -45, 1.0)
    }
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk2_img = pg.image.load("ex02/fig/8.png")
    kk2_img = pg.transform.rotozoom(kk_img, 0, 4.0)
    kk_rect = kk_img.get_rect()
    kk_rect.center= 900,400
    clock = pg.time.Clock()
    go = 0
    tmr = 0
    accs = [a for a in range(0,10)]
    for r in range(1,11):
        bomb_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bomb_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bomb_img.set_colorkey((0, 0, 0))
        bomb_imgs.append(bomb_img)

    bomb_img = pg.Surface((20,20))
    vx = +5 
    vy = +5
    pg.draw.circle(bomb_img,(255,0,0),(10,10),10)
    bomb_rect = bomb_img.get_rect()
    bomb_rect.centerx = random.randint(0, WIDTH)
    bomb_rect.centery = random.randint(0, HEIGHT)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rect.colliderect(bomb_rect):
            print("Game Over")
            print(str(tmr//50)+"秒生き残った")
            return
        
        go = tmr+250    
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]

        for k, tpl in delta.items():
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]

        for k, itm in kk.items():
            if sum_mv == list(k):
                kk_img = itm

        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)] # 追加要素2
        screen.blit(bg_img, [0, 0])
        kk_rect.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rect) != (True,True):
            kk_rect.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rect)
        bomb_rect.move_ip(avx, avy)# 追加要素1
        yoko, tate = check_bound(bomb_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        bomb_rect.move_ip(vx, vy)
        bomb_img = bomb_imgs[min(tmr//500, 9)]
        screen.blit(bomb_img, bomb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()