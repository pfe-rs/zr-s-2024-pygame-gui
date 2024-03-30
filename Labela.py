import pygame
import random
import string

labele=['Prozor 1','Prozorcic','Prozor 2','Prozor celavi','Prozor 3','Prozor VSK','Prozorko','Window.py','WindowMaster.py',"Observer.py",'Necu da se igram vise.py','Anja Vujanac <3','Pomocnik Bosanac']

class Label(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global labele
        super().__init__()
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial',15)
        self.x = x
        self.y = y
        self.color = (0,0,0)
        self.text=random.choice(labele)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def set_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def change_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        # print(self.x, self.y)
        surface.blit(self.image, self.rect)
