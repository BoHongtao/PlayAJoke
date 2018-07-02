import pygame
from pygame.sprite import Sprite

class Monter(Sprite):
    # True=>右   False=>左
    fleet_direction = 1

    def __init__(self, screen):
        print("产生一个外星怪物")
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(r'D:\git\pygame\PlayAJoke\Alien\images\monter.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.alien_speed_factor = 0.5

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # 怪物是否碰到了边框
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # print("更新怪物位置")
        # 可以向右移动
        # if self.fleet_direction==1:
        self.x += (self.alien_speed_factor * self.fleet_direction)
        print(self.x)
        self.rect.x = self.x
        print("向右")
        print(self.alien_speed_factor * self.fleet_direction)
        if self.check_edges()==True:
            print("到达边界")
            self.fleet_direction = -1