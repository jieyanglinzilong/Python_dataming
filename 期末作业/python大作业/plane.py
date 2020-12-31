#-*- coding: utf-8 -*-
import pygame
from sys import exit
from pygame.locals import *
import random

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed

# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
        self.rect = player_rect[0]
        self.rect.topleft = init_pos
        self.speed = 8
        self.bullets = pygame.sprite.Group()
        self.is_hit = False

    # 发射子弹
    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

    # 向上移动，需要判断边界
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    # 向下移动，需要判断边界
    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    # 向左移动，需要判断边界
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    # 向右移动，需要判断边界        
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

# 敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = enemy_img
       self.rect = self.image.get_rect()
       self.rect.topleft = init_pos
       self.down_imgs = enemy_down_imgs
       self.speed = 2

    def move(self):
        self.rect.top += self.speed

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My Pocket Plane')
background = pygame.image.load('resources/image/moon.png').convert()
game_over = pygame.image.load('resources/image/gameover.png')
plane_img = pygame.image.load('resources/image/shoot.png')

# 设置玩家飞机不同状态的图片列表，多张图片展示为动画效果
player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))

player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos)

bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

enemy1_rect = pygame.Rect(534, 612, 57, 43)
enemy1_img = plane_img.subsurface(enemy1_rect)
enemy1_down_imgs = plane_img.subsurface(pygame.Rect(267, 347, 57, 43))


enemies1 = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()
shoot_frequency = 0
enemy_frequency = 0
score = 0
clock = pygame.time.Clock()
running = True


pygame.init()
ck = pygame.display.set_mode((480,800))
pygame.display.set_caption("My Pocket Plane")
clock = pygame.time.Clock()
start_ck = pygame.Surface(ck.get_size())
start_ck2 = pygame.Surface(ck.get_size())
start_ck = start_ck.convert()
start_ck2 = start_ck2.convert()
start_ck.fill((255,255,255))
start_ck2.fill((0,255,0))
# 加载各个素材图片 并且赋予变量名
i1 = pygame.image.load("image/s1.png")
i1.convert()
i11 = pygame.image.load("image/s2.png")
i11.convert()

i2 = pygame.image.load("image/n2.png")
i2.convert()
i21 = pygame.image.load("image/n1.png")
i21.convert()

i31 = pygame.image.load("image/n3.png")




#  以下为选择开始界面鼠标检测结构。
n1 = True
while n1:
    clock.tick(30)
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    if x1 >= 100 and x1 <= 555 and y1 >= 361 and y1 <=427:
        start_ck.blit(i11, (150, 350))
        if buttons[0]:
            n1 = False

    elif x1 >= 100 and x1 <= 555 and y1 >= 481 and y1 <=507:
        start_ck.blit(i21, (150, 450))
        if buttons[0]:
            pygame.quit()
            exit()

    else:
        start_ck.blit(i1, (150, 350))
        start_ck.blit(i2, (150, 450))
        start_ck.blit(i31, (40, 50))


    ck.blit(start_ck,(0,0))
    pygame.display.update()


    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            pygame.quit()
            exit()

ck.blit(start_ck2,(0,0))
pygame.display.update()



while running:
    clock.tick(80)

    if not player.is_hit:
        if shoot_frequency % 100 == 0:
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 20:
            shoot_frequency = 0

    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0

    for bullet in player.bullets:
        # 以固定速度移动子弹
        bullet.move()
        # 移动出屏幕后删除子弹
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)   

    for enemy in enemies1:
        #2. 移动敌机
        enemy.move()
        #3. 敌机与玩家飞机碰撞效果处理
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            break
        #4. 移动出屏幕后删除敌人
        if enemy.rect.top < 0:
            enemies1.remove(enemy)

    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)

    screen.fill(0)
    screen.blit(background, (0, 0))

    # 绘制玩家飞机
    if not player.is_hit:
        screen.blit(player.image[0], player.rect) 
    else:
        # 玩家飞机被击中后的效果处理
        screen.blit(player.image[1], player.rect)
        running = False

    # 敌机被子弹击中效果显示
    for enemy_down in enemies_down:
        enemies_down.remove(enemy_down)
        score += 1
        screen.blit(enemy_down.down_imgs, enemy_down.rect)

    player.bullets.draw(screen)
    enemies1.draw(screen)

    # 绘制得分
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render('score: '+str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 获取键盘事件（上下左右按键）
    key_pressed = pygame.key.get_pressed()

    # 处理键盘事件（移动飞机的位置）
    if key_pressed[K_w] or key_pressed[K_UP]:
        player.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        player.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        player.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        player.moveRight()

font = pygame.font.Font(None, 64)
text = font.render('分数: '+ str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
screen.blit(game_over, (0, 0))
screen.blit(text, text_rect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
