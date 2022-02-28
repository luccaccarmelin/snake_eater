import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))

pygame.display.set_caption(('snake game'))

white=(255, 255, 255)
red=(255,0,0)

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        print(event)

    pygame.draw.rect(dis,white,[200, 150, 10, 10])
    pygame.display.update()
    
    pygame.draw.rect(dis,white,[215, 150, 10, 10])
    pygame.display.update()
    
    pygame.draw.rect(dis,white,[225, 150, 10, 10])
    pygame.display.update()

pygame.quit()
quit()
