# coding=utf-8

input_year = int(input("请输入年份："))
input_month = int(input("请输入月份："))
input_day = int(input("请输入日期："))


# 判断是否是闰年
def test_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        return True
    else:
        return False


# 判断是几月份，计算前面月份是多少天
def test_month(month):
    if test_year(input_year):
        if month == 1:
            return 0
        elif month == 2:
            return 31
        elif month == 3:
            return 31 + 29
        elif month == 4:
            return 31 + 29 + 31
        elif month == 5:
            return 31 + 29 + 31 + 30
        elif month == 6:
            return 31 + 29 + 31 + 30 + 31
        elif month == 7:
            return 31 + 29 + 31 + 30 + 31 + 30
        elif month == 8:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31
        elif month == 9:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
        elif month == 10:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30
        elif month == 11:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        elif month == 12:
            return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        else:
            return None
    else:
        if month == 1:
            return 0
        elif month == 2:
            return 31
        elif month == 3:
            return 31 + 28
        elif month == 4:
            return 31 + 28 + 31
        elif month == 5:
            return 31 + 28 + 31 + 30
        elif month == 6:
            return 31 + 28 + 31 + 30 + 31
        elif month == 7:
            return 31 + 28 + 31 + 30 + 31 + 30
        elif month == 8:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31
        elif month == 9:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
        elif month == 10:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
        elif month == 11:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        elif month == 12:
            return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        else:
            return None


# 统计有多少天
def sum_day(day):
    result = test_month(input_month)
    if result:
        result += day
        return result
    else:
        return None


result_day = sum_day(input_day)
if result_day:
    print("你输入的日期是%d的第%d天" % (input_year, result_day))
else:
    print("输入有误，请重新输入！")
