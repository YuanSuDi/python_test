# coding=utf-8
rows = 1
while rows<=5:
    i = 1
    print(" "*(5-rows),end="")
    while i<=rows*2-1:
        print("*",end="")
        i+=1
    rows+=1
    print()

