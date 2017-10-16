# coding=utf-8
i = 1;
while i<=9:
    if i<=5:
        print("*"*i,end="")
    else:
        print("*"*(10-i),end="")
    i+=1
    print()
