# coding=utf-8


s = ["~abb", "~bccc~", "abc", "123"]
list1 = [x.__sizeof__ for x in s]
print(list1)
