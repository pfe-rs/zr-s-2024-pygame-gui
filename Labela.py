import pygame
import random
import string

class Label(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial',15)
        self.x = x
        self.y = y
        self.color = (0,0,0)
        self.generate_random_text()
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def generate_random_text(self):
        self.text = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))

    def set_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def change_pos(self, x, y):
        print(self.x, self.y)
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        # print(self.x, self.y)
        surface.blit(self.image, self.rect)
