# coding=utf-8
filename = input("请输入要复制的文件名：")
new_file_count = filename.rfind(".")

# 截取文件名生产新的文件名
new_filename = filename[:new_file_count]+"[复件]"+filename[new_file_count:]

# 打开文件输入流
read_file = open(filename, "rb")
write_file = open(new_filename, "wb")
while True:
    content = read_file.read(1024)
    if len(content) == 0:
        break
    write_file.write(content)

# 关闭流
write_file.close()
read_file.close()
