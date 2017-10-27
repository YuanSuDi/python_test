# coding=utf-8
import random

import pygame
from pygame.locals import *
import time
"""
    基本每个类都会用到显示的对象，这里将显示的对象抽取出来
"""


# 基类
class Base(object):
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name


# 公共的飞机类
class PublicPlane(Base):
    def __init__(self, screen, name):
        super().__init__(screen, name)
        self.image = pygame.image.load(self.imageName).convert()
        self.bullets = []

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

    def sheBullet(self):
        bullet = PublicBullet(self.x, self.y, self.screen, self.name)
        self.bullets.append(bullet)


# 玩家飞机类
class HeroPlane(PublicPlane):

    # 初始化飞机位置
    def __init__(self, screen, name):
        # 设置飞机默认的位置
        self.x = 150
        self.y = 630

        # 用来保存英雄飞机需要的图片名字
        self.imageName = "./feiji/hero.gif"
        super().__init__(screen, name)

    # 左移动
    def moveLeft(self):
        if not self.x < -10:
            self.x -= 10

    # 右移动
    def moveRight(self):
        if not self.x > 300:
            self.x += 10


# 敌机的实体类
class EnemyPlane(PublicPlane):
    def __init__(self, screen, name):
        self.x = 45
        self.y = 10
        self.imageName = "./feiji/enemy-1.gif"
        super().__init__(screen, name)
        self.run = "right"

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
            super().sheBullet()


# 公共的子弹类
class PublicBullet(Base):
    def __init__(self, x, y, screen, planeName):
        super().__init__(screen, planeName)

        if self.name == "hero":
            self.x = x + 40
            self.y = y - 10
            imageName = "./feiji/bullet-3.gif"
        else:
            self.x = x + 30
            self.y = y + 30
            imageName = "./feiji/bullet-1.gif"

        self.image = pygame.image.load(imageName).convert()

    def move(self):
        if self.name == "hero":
            self.y -= 2
        elif self.name == "enemy":
            self.y += 2

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 判断子弹是否移出了屏幕
    def judge(self):
        if self.y < 0 or self.y > 820:
            return True
        else:
            return False


if __name__ == "__main__":
    # 1.创建一个窗口
    screen = pygame.display.set_mode((400, 800), 0, 32)

    # 2.选择图片充当背景
    background = pygame.image.load("./feiji/background.png").convert()

    # 3. 创建一个飞机对象
    heroPlane = HeroPlane(screen, "hero")
    enemyPlane = EnemyPlane(screen, "enemy")
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
                    heroPlane.sheBullet()

        # 通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        time.sleep(0.01)
        # 刷新界面
        pygame.display.update()
