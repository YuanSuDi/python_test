# coding=utf-8
import random

import pygame
from pygame.locals import *
import time
"""
    优化射出边界的子弹
"""


# 玩家飞机类
class HeroPlane(object):

    # 初始化飞机位置
    def __init__(self, screen):
        # 设置飞机默认的位置
        self.x = 150
        self.y = 630

        # 设置要显示内容的窗口
        self.screen = screen

        # 用来保存英雄飞机需要的图片名字
        self.imageName = "./feiji/hero.gif"

        # 根据名字生成飞机图片
        self.image = pygame.image.load(self.imageName).convert()

        # 用来保存英雄飞机发射出的所有子弹
        self.bullets = []

    # 显示飞机的方法
    def display(self):
        # 设置飞机
        self.screen.blit(self.image, (self.x, self.y))

        # 设置子弹之前，判断有哪些子弹移出了屏幕
        delBullets = []

        for x in self.bullets:
            if x.judge():
                delBullets.append(x)

        # 将移出屏幕的子弹从子弹列表中删除
        for x in delBullets:
            self.bullets.remove(x)

        # 设置子弹
        for bullet in self.bullets:
            bullet.move()
            bullet.display()

    # 左移动
    def moveLeft(self):
        if not self.x < -10:
            self.x -= 10

    # 右移动
    def moveRight(self):
        if not self.x > 300:
            self.x += 10

    # 发射子弹的方法
    def shutBullet(self):
        bullet = Bullet(self.x, self.y, self.screen)
        self.bullets.append(bullet)


"""
    子弹类
    1.子弹的显示
    2.子弹的移动
"""


class Bullet(object):
    # 初始化子弹位置
    def __init__(self, x, y, screen):
        self.x = x+40
        self.y = y-10
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet-3.gif").convert()

    # 子弹的移动
    def move(self):
        self.y -= 3

    # 子弹的显示
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 判断子弹是否移出了屏幕
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


# 敌机的实体类
class EnemyPlane:
    def __init__(self, screen):
        self.x = 45
        self.y = 10
        self.screen = screen
        self.image = pygame.image.load("./feiji/enemy-1.gif").convert()
        self.bullets = []  # 存储子弹
        self.run = "right"

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # 设置子弹之前，判断有哪些子弹移出了屏幕
        delBullets = []

        for x in self.bullets:
            if x.judge():
                delBullets.append(x)

        # 将移出屏幕的子弹从子弹列表中删除
        for x in delBullets:
            self.bullets.remove(x)

        # 设置子弹
        for bullet in self.bullets:
            bullet.move()
            bullet.display()

    def move(self):
        # 根据是否碰到边界而改变移动的方向
        if self.run == "right":
            self.x += 2
        else:
            self.x -= 2

        if self.x < 0:
            self.run = "right"
        elif self.x > 350:
            self.run = "left"

    # 敌机发射子弹
    def sheBullet(self):
        num = random.randint(1, 100)
        if num == 88:
            newBullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullets.append(newBullet)


# 敌机子弹的实体类
class EnemyBullet(object):
    def __init__(self, x, y, screen):
        self.x = x+30
        self.y = y+30
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet1.png").convert()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 2

    def judge(self):
        if self.y > 820:
            return True
        else:
            return False


if __name__ == "__main__":
    # 1.创建一个窗口
    screen = pygame.display.set_mode((400, 800), 0, 32)

    # 2.选择图片充当背景
    background = pygame.image.load("./feiji/background.png").convert()

    # 3. 创建一个飞机对象
    heroPlane = HeroPlane(screen)
    enemyPlane = EnemyPlane(screen)
    # 5.将图片渲染到窗口内
    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        # 显示飞机
        heroPlane.display()
        # 显示敌机
        enemyPlane.display()
        enemyPlane.sheBullet()
        # 移动敌机
        enemyPlane.move()
        # 获取键盘鼠标事件
        for event in pygame.event.get():

            # 判断是否点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()

            # 判断是否按下了键盘
            if event.type == KEYDOWN:
                # 检测案件是否为a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    heroPlane.moveLeft()

                if event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    heroPlane.moveRight()

                if event.key == K_SPACE:
                    print("space")
                    heroPlane.shutBullet()

        # 通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        time.sleep(0.01)

        # 刷新界面
        pygame.display.update()

