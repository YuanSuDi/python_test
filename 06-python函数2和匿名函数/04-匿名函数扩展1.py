# coding=utf-8
def test(a,b,func):
    return func(a,b)

result = test(11,22,lambda a,b:a+b)
print("a+b=%d"%result)
