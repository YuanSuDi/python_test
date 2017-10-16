# coding=utf-8
f = open("ww.txt", "r")
content = f.read(1000)
print(""+f.__str__())
print(content)
f.close()

