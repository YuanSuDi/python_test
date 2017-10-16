# coding=utf-8
name = input("请输入你的姓名：")
age = int(input("请输入你的年龄："))

if not age>=18:
    print("%s你才%d，回家写作业"%(name,age))
else:
    print("%s你可以去网吧"%name)
