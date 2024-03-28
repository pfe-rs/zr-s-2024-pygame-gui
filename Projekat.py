from ClassProzor import *
from ClassLajsna import *
import pygame
background_colour = (0, 0, 0) 
screen = pygame.display.set_mode((1750, 850)) 
pygame.display.set_caption('GUI') 
screen.fill(background_colour) 
pygame.display.flip() 
running = True
prozori=[]
while running: 
    for event in pygame.event.get():     
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_u) or event.type==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            prozori.append(Prozor(100,50,1500,750,'a'))
        if event.type==pygame.MOUSEBUTTONDOWN:
            for prozor in prozori:
                if(x>=prozor.x and x<=prozor.x+prozor.width) and (y>prozor.y and y<prozor.y+prozor.height):
                    prozor.click(x,y)
                    if prozor.lajsna.press==0:
                        prozori.remove(prozor)
                #print(lajsna.press)
        if event.type==pygame.MOUSEBUTTONUP:
            for prozor in prozori:
                prozor.lajsna.press=2
        if event.type==pygame.MOUSEMOTION:
            for prozor in prozori:
                if prozor.lajsna.press==1:
                    prozor.drag(x-prozor.lajsna.prevpress[0],y-prozor.lajsna.prevpress[1],x,y)
    x, y = pygame.mouse.get_pos()
    #print(x,y)
    screen.fill(background_colour) 
    for prozor in prozori:
        prozor.draw(screen)
    pygame.draw.circle(screen,(254,254,254), [x,y], 7)
    pygame.display.update()

        

