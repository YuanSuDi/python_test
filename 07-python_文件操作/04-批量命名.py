# coding=utf-8
import os

folder_name = input("请输入文件夹名：")

# 获取文件夹ong suoyou de wenjianming 中所有的文件名
file_names = os.listdir(folder_name)
i=0
# 对文件进行重命名
for name in file_names:
    print(name)
    i += 1
    old_file_name = folder_name+"/"+name
    new_file_name = "%s/(%d)%s" % (folder_name, i, name)
    os.rename(old_file_name, new_file_name)

