import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#練習1
    bg2_img = pg.transform.flip(bg_img, True, False)#8
    kk_img = pg.image.load("fig/3.png")#練習3
    kk_img = pg.transform.flip(kk_img, True, False)#練習3
    kk_rct = kk_img.get_rect()#10-1
    kk_rct.center = 300, 200 #10-2
    screen.blit(kk_img, kk_rct)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return


            
        key_lst = pg.key.get_pressed() #10-3
        kk_rct.move_ip((-1,0))#e-1-1
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0, -1))
        
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, 1))

        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((2, 0)) #e-1-2

        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))

        x = tmr%3200 #5 #9
        screen.blit(bg_img, [-x, 0])#練習2 #5
        screen.blit(bg2_img, [-x+1600, 0])#7 #8
        screen.blit(bg_img, [-x+3200, 0])#9
        screen.blit(kk_img, kk_rct)#練習4 #10-5
        pg.display.update()
        tmr += 1        
        clock.tick(200)#6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()