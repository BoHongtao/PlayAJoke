import pygame
from pygame.sprite import Sprite

class Monter(Sprite):
    def __init__(self, screen):
        print("产生一个外星怪物")
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(r'D:\codeingSpace\pythoncode\game\Alien\images\monter.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image, self.rect)