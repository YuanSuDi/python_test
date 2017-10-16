class TestNew(object):
    def __init__(self):
        print("-----init-----")

    def __del__(self):
        print("-----del-----")

    # 重写__new__方法时，一定要有返回值，将object对象的__new__方法返回回去，实例化时才会调用__init__方法和__del__方法
    def __new__(cls):
        print("-----new-----")
        # return object.__new__(cls)
# 不会调用__init__和__del__方法
testNew = TestNew()
testNew = None


class Dog(object):
    def __init__(self):
        print("----init方法-----")

    def __del__(self):
        print("----del方法-----")

    def __str__(self):
        print("----str方法-----")
        return "对象的描述信息"

    def __new__(cls):  # cls此时是Dog指向的那个类对象

        # print(id(cls))

        print("----new方法-----")
        return object.__new__(cls)
# 会调用__init__和__del__方法
# print(id(Dog))
xtq = Dog()

