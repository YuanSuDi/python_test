import os
import sys


# 遍历文件夹复制py文件
def testPyc(path):
    file_dirs = os.listdir(path)
    for file in file_dirs:
        global_path = "%s/%s" % (path, file)
        if os.path.isdir(global_path):
            # 如果是文件夹，再次调用该方法
            testPyc(global_path)
        else:
            # 判断文件夹是否存在
            if os.path.exists("test1"):
                file_count = file.rfind(".")
                file_dw = file[file_count+1:]
                if file_dw == "py":
                    in_file = open(global_path, "rb")
                    out_file = open("test1/%s" % file, "wb")
                    out_file.write(in_file.read())
                    out_file.close()
                    in_file.close()
            else:
                os.mkdir("test1")
                file_count = file.rfind(".")
                file_dw = file[file_count + 1:]
                if file_dw == "py":
                    in_file = open("%s/%s" % (path, file), "rb")
                    out_file = open("test1/%s" % file, "wb")
                    out_file.write(in_file.read())
                    out_file.close()
                    in_file.close()


# 获取输入的参数
args = sys.argv
i = 1
while i < len(args):
    testPyc(args[i])
    i += 1

