# coding=utf-8

def test1():
    print("---test1---")


def test2():
    print("---test2---")


class Test1(object):
    def test11(self):
        print("---test11---")


class Test2(object):
    def test21(self):
        print("---test21---")


# __name__变量：谁执行就会赋值为谁,如果执行本文件时，赋值为"__main__"
if __name__ == "__main__":
    test1()
    test2()