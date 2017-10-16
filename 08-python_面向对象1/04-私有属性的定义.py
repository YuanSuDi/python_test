# coding=utf-8
class Dao:

    def set_age(self, age):
        # 私有属性的定义，字段名前需要加__自动回成为私有变量
        self.__age = age

    def get_age(self):
        return self.__age

dao = Dao()
dao.set_age(5)
print("小狗的年龄是:%d" % dao.get_age())

# print("小狗的年龄是:%d" % dao.__age)
