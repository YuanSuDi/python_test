# coding=utf-8
class Cat:
    def eat(self):
        print("猫吃鱼加%s，再加%s" % (self.food, self.play))

    # __str__方法
    def __str__(self):
        return self.food

    def __init__(self, play):
        self.play = play

cat = Cat("玩个球")
cat.food = "猪肉"
cat.eat()
print(cat)
