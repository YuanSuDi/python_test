# coding=utf-8
# 导入相关包
import random

# 提示用户输入
player = int(input("请输入 0石头 1剪刀 2布"))

# 自动生成一个数字
computer = random.randint(0,2)

# 对数据进行判断 有三种结果 胜，平，负
if(player==0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0):
    print("你胜利了")
elif player==computer:
    print("平局，请重新来过")
else:
    print("你输了")

