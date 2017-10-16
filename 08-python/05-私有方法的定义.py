# coding=utf-8
class CMCC:

    # 私有方法的定义与定义私有属性类似，就是在方法名前加__，即可申明成私有方法
    def __send_message(self, message):
        print("----正在发送短信（%s）----" % message)
        print("短信发送成功")

    def send_message(self, money, message):
        if money > 999:
            self.__send_message(message)
        else:
            print("余额不足，请充值后再进行操作")

cmcc = CMCC()
cmcc.send_message(100, "你好，世界！")
