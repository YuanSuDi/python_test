# coding=utf-8

# 1.打印提示功能
print("="*50)
print("1.添加名片")
print("2.删除名片")
print("3.查找名片")
print("4.查找所有名片")
print("5.退出系统")
print("="*50)

# 存放名片的列表
card_infos=[]
while True:
    num = int(input("请输入功能序号："))
    if num==1:
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        QQ = input("请输入QQ号：")
        gender = input("请输入性别：")
        
        # 存放单个个人信息的字典
        info = {}
        info["name"] = name
        info["age"] = age
        info["QQ"] = QQ
        info["gender"] = gender

        #将字典放入列表中
        card_infos.append(info)
        print("名片添加成功")
    elif num==2:
        pass
    elif num==3:
        name = input("请输入要查找的姓名：")
        flag = 0
        for tmp in card_infos:
            if name==tmp["name"]:
                print("姓名\t年龄\t性别\tQQ号")
                print("%s\t%s\t%s\t%s"%(tmp["name"],tmp["age"],tmp["gender"],tmp["QQ"]))
                flag = 1
        if flag ==0:
            print("查无此人")


        pass
    elif num==4:
        print("姓名\t年龄\t性别\tQQ号")
        for tmp in card_infos:
            print("%s\t%s\t%s\t%s"%(tmp["name"],tmp["age"],tmp["gender"],tmp["QQ"]))
    elif num==5:
        print("退出系统成功！")
        break



