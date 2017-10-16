# coding=utf-8
i = 0
while i<=10:
    i += 1
    if i == 5:
        continue # 跳出本次循环
    if i>7:
        break # 跳出当前循环
    print("i=%d"%i)
    
