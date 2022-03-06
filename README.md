# snake_eater
import pygame
import time
pygame.init()

dis_width = 800
dis_heigth = 600

dis=pygame.display.set_mode((dis_width, dis_heigth))
pygame.display.set_caption(('snake game'))

white=(255, 255, 255)
black=(0, 0, 0)
red=(255,0,0)
blue=(0, 0, 255)

snake_block=10
snake_speed=30

font_style=pygame.pygame.font.SysFont(None, 13)

game_over=False

x1= 300
y1_change= 0

clock=pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x1_change= -10
                y1_change= 0
            elif event.key==pygame.K_RIGHT:
                x1_change= 10
                y1_change= 0
            elif event.key==pygame.K_UP:
                y1_change= -10
                x1_change= 0
            elif event.key==pygame.K_DOWN:
                y1_change= 10
                x1_change= 0

 x1 += x1_change
    y1 += y1_change

    dis.fill(white)
    pygame.draw.rect(dis,black, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(18)

pygame.quit()
quit()
