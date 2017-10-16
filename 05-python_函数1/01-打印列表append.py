# coding=utf-8
a = [11,22,33]
b = [55,666]
# 虽然 a.append(b)修改了元素a，但是其本身的表达式并没有结果，如果这样直接赋值a的值为None
a = a.append(b)
print(a)
