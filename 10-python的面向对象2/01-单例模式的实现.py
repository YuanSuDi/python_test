# coding=utf-8
class Dog:
    __instance = None

    # 单例模式需要重写__new__方法，并返回生成的实例对象
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:

            # cls.__instance = object.__new__(cls)
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def t1(self):
        print("t1调用")


dog1 = Dog()
dog2 = Dog()
dog1.t1()
print("dog1地址：%s" % id(dog1))
print("dog2地址：%s" % id(dog2))
