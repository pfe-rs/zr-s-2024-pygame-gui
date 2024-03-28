import pygame

class Label(pygame.sprite.Sprite):
    def __init__(self, text, font, color=(0, 0, 0)):
        super().__init__()
        self.font = font
        self.text = text
        self.color = color
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()

    def set_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()

    def change_pos(self, pos):
        self.rect.topleft = pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)


Label.draw(4)