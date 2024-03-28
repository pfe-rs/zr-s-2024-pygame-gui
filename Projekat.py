import pygame
from Klase import *
from Labela import Label
import random
import string

background_colour = (0, 0, 0)
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Pygame GUI')
screen.fill(background_colour)
pygame.display.flip()
running = True
laj = []
laj.append(Lajsna(450, 200, 600, 30))

# Initialize font
pygame.font.init()
font = pygame.font.SysFont('Arial', 36)  # Using Arial font, change if needed

# Create label with random text
label = Label(font)
label.change_pos((50, 50))  # Set position of the label

while running:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_u) or event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for lajsna in laj:
                if (x >= lajsna.x and x <= lajsna.x + lajsna.width) and (y > lajsna.y and y < lajsna.y + lajsna.height):
                    lajsna.click(x, y)
                    if lajsna.press == 0:
                        laj.remove(lajsna)
        if event.type == pygame.MOUSEBUTTONUP:
            for lajsna in laj:
                lajsna.press = 2
        if event.type == pygame.MOUSEMOTION:
            for lajsna in laj:
                if lajsna.press == 1:
                    lajsna.drag(x - lajsna.prevpress[0], y - lajsna.prevpress[1], x, y)
    x, y = pygame.mouse.get_pos()
    screen.fill(background_colour)
    for lajsna in laj:
        lajsna.draw(screen)
    pygame.draw.circle(screen, (254, 254, 254), [x, y], 7)

    # Draw the label
    label.draw(screen)

    pygame.display.update()

    # Update the display
    pygame.display.flip()

pygame.quit()
