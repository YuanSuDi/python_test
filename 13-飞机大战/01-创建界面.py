# coding=utf-8
import pygame
from pygame.locals import *

# 1.完成界面和背景图的显示

if __name__ == "__main__":
    # 1.创建一个窗口
    screen = pygame.display.set_mode((400, 800), 0, 32)

    # 2.选择图片充当背景
    background = pygame.image.load("./feiji/background.png").convert()

    # 3.将图片渲染到窗口内
    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))

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

                if event.key == K_w or event.key == K_UP:
                    print("up")

                if event.key == K_d or event.key == K_RIGHT:
                    print("right")

                if event.key == K_s or event.key == K_DOWN:
                    print("down")

                if event.key == K_SPACE:
                    print("space")



        # 刷新界面
        pygame.display.update()



