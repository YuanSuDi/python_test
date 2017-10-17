# coding=utf-8
class Dog:
    __instance = None

    # 单例模式2使用
    def __new__(cls, *args, **kwargs):
        return None

    # 单例模式的实现方式2，重写__new__方法让其返回None，再写一个类方法返回需要生成的实例对象，不推介
    @classmethod
    def newInstance(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    @staticmethod
    def staticNewInstance():
        if Dog.__instance is None:
            Dog.__instance = object.__new__(Dog)
            return Dog.__instance
        else:
            return Dog.__instance

    def t1(self):
        print("t1调用")

dog1 = Dog.newInstance()
dog2 = Dog.newInstance()
dog3 = Dog.staticNewInstance()
dog1.t1()
print("dog1地址：%s" % id(dog1))
print("dog2地址：%s" % id(dog2))
print("dog3地址：%s" % id(dog3))
dog3.t1()
