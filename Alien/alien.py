import sys,pygame,random
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from monter import Monter
import game_functions as gf

def run_game():
    pygame.init()
    # 设置size
    screen = pygame.display.set_mode((1200,800))
    # 设置title
    pygame.display.set_caption('Alien')
    # init ship
    ship = Ship(screen)
    # init monster
    monster = Group()
    bullets = Group()
    # 随机怪物的数量
    monsters_num = random.uniform(0, 10)
    gf.create_alien(screen, monster, monsters_num)
    while True:
        # 检测键盘事件
        gf.check_events(ship,screen,bullets)
        # 改变自己位置
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                print("删除消失的子弹")
                bullets.remove(bullet)
        # 如果自己移动，重绘屏幕
        gf.update_screen(screen, ship,bullets,monster)

run_game()