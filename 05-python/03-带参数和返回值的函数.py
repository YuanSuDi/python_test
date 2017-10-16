# coding=utf-8
def judge_sanjiao(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


a = int(input("请输入1："))
b = int(input("请输入2："))
c = int(input("请输入3："))
if judge_sanjiao(a, b, c):
    print("能成为三角形")
else:
    print("不能成为三角形")
