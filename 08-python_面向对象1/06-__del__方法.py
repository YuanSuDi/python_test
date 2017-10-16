# coding=utf-8
class DelTest:
    # 当没有任何变量指向该对象时，此方法就会被调用
    def __del__(self):
        print("--对象已没有引用--")

delTest = DelTest()
delTest1 = delTest
# delTest = None
del delTest
del delTest1

print("==================")
