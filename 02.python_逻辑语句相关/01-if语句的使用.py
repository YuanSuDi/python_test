age = input("请输入一个年龄")
#将输入的字符转化成数字
age_num = int(age)
if age_num>20:
    print("您的年龄是%d,已成年"%age_num)
else:
    print("您的年龄是%s，未成年"%age)
