import pygame
pygame.init()
width=800
height=600

window=pygame.display.set_mode((width,height))
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    
pygame.quit()        