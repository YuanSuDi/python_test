# coding=utf-8
def test1(b, c, a=20):
    print(a)
    print(b)
    print(c)


test1(b=22, c=33)


def test2(a, b, *args, **kwargs):
    print("a=%s" % a)
    print("b=%s" % b)
    print(args)
    print(kwargs)
list1 = [1, 2, 3, 4, 5, 6]
args1 = {'name':'tom', 'age':23}
# 在实参中*,**表示对元祖/字典进行拆包
test2("bili", "2233", *list1, **args1)
# 两种传参方式
test2("元组", "we", 1, 2, 3, 4, 5, name="laownag", age=23)


