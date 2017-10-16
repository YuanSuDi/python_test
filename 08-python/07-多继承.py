# coding=utf-8

class base(object):
    def test(self):
        print('----base test----')


class A(base):
    def test(self):
        print('----A test----')


# 定义一个父类
class B(base):
    def test(self):
        print('----B test----')


# 定义一个子类，继承自A、B
class C(B, A):
    pass


obj_C = C()
obj_C.test()

# 可以查看C类的对象搜索方法时的先后顺序
print(C.__mro__)
