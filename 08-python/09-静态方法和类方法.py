# coding=utf-8
class Father:
    # 类属性
    name = "laoba"

    def __init__(self):
        print("this is father")

    def eat(self):
        print("%s吃饭" % Father.name)

    @classmethod
    def clsMethod(cls):
        print("class method")

    @staticmethod
    def staticmethod():
        print("static method")



class Son(Father):
    def __init__(self, name):
        self.sonname = name
        print("this is son")
        Father.__init__(self)

    def eat(self):
        print("%s吃饭" % self.sonname)

# 创建对象实例
son = Son("小明")
son.eat()
# 调用普通方法时，必须含有一个实例化的对象
Father.eat(son)
# 调用类属性,也可以继承
print("Father调用类属性%s" % Father.name)
print("Father调用类属性%s" % Father().name)
print("Son调用父类类属性%s" % Son.name)
# 当子类也有name全局变量，取得的是子类的属性值
print("Son调用父类类属性%s" % son.name)

# 调用静态方法和类方法，可以直接调用，并且可以被继承
Father.staticmethod()
Father.clsMethod()
Son.staticmethod()
Son.clsMethod()


# 这两种调用方法不可用
# Father.clsMethod(Father)
# Son.clsMethod(Father)



