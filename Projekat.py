from ClassWindowMenager import *
from ClassProzor import *
from ClassLajsna import *
from Labela import *
from Observer import *
import pygame
background_colour = (0, 0, 0) 
screen = pygame.display.set_mode((1750, 850)) 
pygame.display.set_caption('GUI') 
screen.fill(background_colour) 
pygame.display.flip() 
event_handler=EventHandler()
event_handler.add_event("close_window",WindowMenager.remove_prozor)
running = True
prozori=[]
window_menager=WindowMenager()
while running: 
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():     
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_u) or (event.type==pygame.QUIT):
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            window_menager.add_prozor()
        if event.type==pygame.MOUSEBUTTONDOWN:
            window_menager.check_click(x,y)
            # for prozor in prozori:
            #     if(x>=prozor.x and x<=prozor.x+prozor.width) and (y>prozor.y and y<prozor.y+prozor.height):
            #         prozor.click(x,y)
            #         if prozor.lajsna.press==0:
            #             prozori.remove(prozor)
                #print(lajsna.press)
        if event.type==pygame.MOUSEBUTTONUP:
            window_menager.mouseup()
        if event.type==pygame.MOUSEMOTION:
            window_menager.drag(x,y)
    
    #print(x,y)
    screen.fill(background_colour) 
    window_menager.draw(screen)
    pygame.draw.circle(screen,(254,254,254), [x,y], 7)
    pygame.display.update()

    # Update the display
    pygame.display.flip()

pygame.quit()
