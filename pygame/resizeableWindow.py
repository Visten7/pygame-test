import pygame
pygame.init()
width=800
height=600

window=pygame.display.set_mode((width,height),pygame.RESIZABLE)
is_resizeable=True
bg_color=(0,255,255)#cyan color
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.VIDEORESIZE:
            if is_resizeable:
                width=event.w
                height=event.h
                window=pygame.display.set_mode((width,height),pygame.RESIZABLE)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                is_resizeable=not is_resizeable
                if is_resizeable:
                    window=pygame.display.set_mode((width,height),pygame.RESIZABLE)
                else:
                    window=pygame.display.set_mode((width,height),pygame.NORESIZE)
    window.fill(bg_color)
    pygame.display.update() 
pygame.quit()                   