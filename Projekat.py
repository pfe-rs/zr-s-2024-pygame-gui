
import pygame 
background_colour = (0, 0, 0) 
screen = pygame.display.set_mode((1000, 600)) 
pygame.display.set_caption('Pygame GUI') 
screen.fill(background_colour) 
pygame.display.flip() 
running = True
while running: 
    for event in pygame.event.get():     
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                running = False


