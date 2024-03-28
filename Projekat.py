from Klase import *
import pygame 
background_colour = (0, 0, 0) 
screen = pygame.display.set_mode((1750, 850)) 
pygame.display.set_caption('GUI') 
screen.fill(background_colour) 
pygame.display.flip() 
running = True
laj=[]
laj.append(Lajsna(450,200,600,30))
while running: 
    for event in pygame.event.get():     
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_u) or event.type==pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            for lajsna in laj:
                if(x>=lajsna.x and x<=lajsna.x+lajsna.w) and (y>lajsna.y and y<lajsna.y+lajsna.h):
                    lajsna.click(x,y)
                    if lajsna.press==0:
                        laj.remove(lajsna)
                #print(lajsna.press)
        if event.type==pygame.MOUSEBUTTONUP:
            for lajsna in laj:
                lajsna.press=2
        if event.type==pygame.MOUSEMOTION:
            for lajsna in laj:
                if lajsna.press==1:
                    lajsna.drag(x-lajsna.prevpress[0],y-lajsna.prevpress[1],x,y)
    x, y = pygame.mouse.get_pos()
    #print(x,y)
    screen.fill(background_colour) 
    for lajsna in laj:
        lajsna.draw(screen)
    pygame.draw.circle(screen,(254,254,254), [x,y], 7)
    pygame.display.update()

        

