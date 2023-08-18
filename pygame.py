import pygame,sys
from pygame.locals import *
import random
import time
pygame.init()

DISPLAYSURF =pygame.display.set_mode((800,600))
IMAGE=pygame.image.load("pygame/me2.png")
Rect = IMAGE.get_rect()
Rect.center=(400,100)

bullet=pygame.image.load("pygame/bullet2.png")

pot=pygame.image.load("pygame/pot.png")

scorefont=pygame.font.Font(None,60)






Prect=pot.get_rect()
Prect.centerx=Rect.centerx
Prect.centery=Rect.centery+450
# 初始化子弹，即生成子弹，需要在miku的顶部中间位置初始化出一枚子弹
rect = bullet.get_rect()
rect.centerx = Rect.centerx-70
rect.centery = Rect.centery-50
# 在屏幕上绘制子弹"
score=0
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    pressed =pygame.key.get_pressed()
    """  if pressed[K_LEFT]:
        Rect.move_ip(-1,0)
    if pressed[K_RIGHT]:
        Rect.move_ip(1,0)"""
    """if pressed[K_UP]:
        Rect.move_ip(0,-1)
    if pressed[K_DOWN]:
        Rect.move_ip(0,1)
    if   pressed[K_SPACE]:
        rect.move_ip(0,-1)"""
    if not  pressed[K_RSHIFT]:
        rect.move_ip(0,5) 
        
    if   pressed[K_a]:
        Prect.move_ip(-1,0)
    if   pressed[K_d]:
        Prect.move_ip(1,0)
    Rect.centerx += random.randint(-8, 8)     
        #动起来
    if  0>= Rect.centerx :
        Rect.centerx+=50
    if  Rect.centerx>=800 :
        Rect.centerx-=50
    if Prect.centerx-80<=rect.centerx<=Prect.centerx+80 and Prect.top-2.5<= rect.centery <=Prect.top+2.5:
        score+=1
    scoreText=scorefont.render('Score:'+str(score),True,(255,255,255))   
    DISPLAYSURF.fill((0,0,0))
    DISPLAYSURF.blit(IMAGE,Rect)
    DISPLAYSURF.blit(bullet,rect)
    DISPLAYSURF.blit(pot,Prect)
    DISPLAYSURF.blit(scoreText,(0,0))
    #画锅，miku，还有葱
    pygame.display.update()
    if rect.centery> 500:
        rect = bullet.get_rect()
        rect.centerx = Rect.centerx-70
        rect.centery = Rect.centery-50
    
    #特色检测碰撞

