# coding=utf-8
class Dog(object):
    __instance = None  # 存放对象的变量
    __init_flag = False  # 是否初始化过的标志

    # 重写new方法
    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    # 重写init方法
    def __init__(self, name):
        if not Dog.__init_flag:
            self.name = name
            Dog.__init_flag = True

dog1 = Dog("小哈")
print(dog1.name)
print(id(dog1))
# 第二个对象并没有初始化
dog2 = Dog("大哈")
print(dog2.name)
print(id(dog2))
