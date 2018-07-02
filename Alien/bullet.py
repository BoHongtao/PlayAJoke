import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    # bullet width and height
    bullet_width = 5
    bullet_height = 15
    bullet_speed_factor = 3
    bullet_color = 255, 0, 0
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, self.bullet_width,self.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = self.bullet_color
        self.speed_factor = self.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)