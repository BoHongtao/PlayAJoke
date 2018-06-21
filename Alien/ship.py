import pygame
class Ship():
    moving_right = False
    moving_left = False
    def __init__(self,screen):
        self.screen = screen
        # load image of ship
        self.image = pygame.image.load(r'D:\codeingSpace\pythoncode\game\Alien\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # put ship to screen x ,y s
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right:
            if self.rect.centerx < 1200:
                self.rect.centerx += 1
        if self.moving_left:
            if self.rect.centerx > 0:
                self.rect.centerx -= 1