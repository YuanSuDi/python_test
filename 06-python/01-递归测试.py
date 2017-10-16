# coding=utf-8

def recusion(a):
    if a>1:
        return a*recusion(a-1)
    else:
        return 1

result = recusion(5)
print("阶乘结果为：%d"%result)

