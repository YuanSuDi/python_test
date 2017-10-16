# -*- coding:utf-8 -*-

# 普通函数
def test1(a,b):
    return a+b
result1 = test1(20,34)

# 匿名函数
test2 = lambda a,b:a+b

result2 = test2(19,32)
print("result1=%d,result2=%d"%(result1,result2))

