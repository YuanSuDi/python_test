# coding=utf-8

i = 1
while i<=9:
    j = 1
    while j<=i:
        z = j*i
        print("%dx%d=%d"%(j,i,z),end="  ")
        j+=1
    print()
    i+=1
