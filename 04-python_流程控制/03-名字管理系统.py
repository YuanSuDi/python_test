# coding=utf-8
#1. 打印功能提示
print("="*50)
print("    名字关系系统 V8.6")
print(" 1:添加一个新的名字")
print(" 2:删除一个名字")
print(" 3:修改一个名字")
print(" 4:查询一个名字")
print(" 5:退出系统")
print("="*50)

names = [] # 定义一个空的列表来存储添加的名字

while True:

    # 2.获取用户的选择
    num = int(input("请输入功能序号："))

    # 3.根据用户选择执行功能
    if num==1:
        new_name = input("请输入要添加的名字：")
        if new_name in names:
            # 输入的名字已存在
            print("您输入的名字已存在")
        else:
            names.append(new_name)
            print("名字【%s】添加成功"%new_name)
    elif num==2:
        pass
    elif num==3:
        pass
    elif num==4:
        find_name = input("请输入要查找的名字：")
        if find_name in names:
            print("查找名字【%s】成功"%find_name)
        else:
            print("查无此人")
    elif num==5:
        print("退出系统成功！")
        break
    else:
        print("输入错误，请重新输入！")





