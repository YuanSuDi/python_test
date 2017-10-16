# coding=utf-8
class Dog:
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


dog = Dog()
dog.set_age(5)
print("狗的年龄为%d岁" % dog.get_age())
print(dog.age)
