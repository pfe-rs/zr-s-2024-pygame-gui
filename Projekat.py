from Klase import *
import pygame 
background_colour = (0, 0, 0) 
screen = pygame.display.set_mode((1750, 850)) 
pygame.display.set_caption('GUI') 
screen.fill(background_colour) 
pygame.display.flip() 
running = True
while running: 
    for event in pygame.event.get():     
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_u) or event.type==pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            lajsna.click(x,y)
    x, y = pygame.mouse.get_pos()
    #print(x,y)
    screen.fill(background_colour) 
    lajsna= Lajsna(450,200,600,30)
    lajsna.draw(screen)
    pygame.draw.circle(screen,(254,254,254), [x,y], 7)
    pygame.display.update()

        

