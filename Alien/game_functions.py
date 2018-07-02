import sys,pygame,random
from bullet import Bullet
from monter import Monter
def check_events(ship,screen,bullets):
    #respond to  keyboard and mouse item
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # move right left and openfire
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_SPACE:
                fire_bullet(screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(screen,ship,bullets,monster):
    # background
    bg_color = (230, 230, 230)
    # fill color
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    monster.draw(screen)
    # visualiaze the window
    pygame.display.flip()

# 开火
def fire_bullet(screen, ship, bullets):
    new_bullet = Bullet(screen, ship)
    bullets.add(new_bullet)

# 产生怪物
def create_alien(screen, monters, alien_number):
    for i in range(0,int(alien_number)):
        monter = Monter(screen)
        monter.x = random.uniform(0,1200)
        monter.rect.x = monter.x
        monter.y = random.uniform(100,600)
        monter.rect.y = monter.y
        monters.add(monter)

# 碰撞检测
def check_bullet_alien_collisions(monter, bullets):
    collisions = pygame.sprite.groupcollide(bullets, monter, True, True)
    if collisions:
        print("杀死了怪物")