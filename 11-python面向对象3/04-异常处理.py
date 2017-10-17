# coding=utf-8
try:
    # 如果在try的某一行代码发生异常，则在try内发生异常的那行代码后面的语句都不会执行
    print("--进入有可能发生异常的代码块--")
    # i = 1/0
    numstr = input("num：")
    num = int(numstr)
    print("num = %d" % num)
    # print("num = %d" % num1)
    # open("sss.txt","r")
    print("--有异常该语句会不执行--")
except(NameError, FileNotFoundError):
    print("变量未定义，或者文件未找到")
except Exception as e:
    # i = 1/0
    print("--如果用了Exception,那么意味着只要上面的except没有捕获到异常,这个except一定会捕获到--")
    print(e)
else:
    print("--没有异常会执行的语句else--")
finally:
    print("--无论是否发生异常都会执行的语句finally--")

print("--end--")
