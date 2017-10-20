# coding=utf-8
import pygame
from pygame.locals import *
"""
    1.创建飞机的对象
    2.添加其中的属性和方法
"""


class HeroPlane(object):

    # 初始化飞机位置
    def __init__(self, screen):
        # 设置飞机默认的位置
        self.x = 150
        self.y = 600

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

    # 左移动
    def moveLeft(self):
        self.x -= 10

    # 右移动
    def moveRight(self):
        self.x += 10

    # 发射子弹的方法
    def shutBullet(self):
        pass


if __name__ == "__main__":
    # 1.创建一个窗口
    screen = pygame.display.set_mode((400, 800), 0, 32)

    # 2.选择图片充当背景
    background = pygame.image.load("./feiji/background.png").convert()

    # 3. 创建一个飞机对象
    heroPlane = HeroPlane(screen)

    # 3.将图片渲染到窗口内
    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        # 显示飞机
        heroPlane.display()

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

        # 刷新界面
        pygame.display.update()



