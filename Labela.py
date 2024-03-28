import pygame
import random
import string

class Label(pygame.sprite.Sprite):
    def __init__(self, font, color=(0, 0, 0)):
        super().__init__()
        self.font = font
        self.color = color
        self.generate_random_text()
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()

    def generate_random_text(self):
        self.text = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))

    def set_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()

    def change_pos(self, pos):
        self.rect.topleft = pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)
