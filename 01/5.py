#!/usr/bin/python
# coding=utf-8
# python列表
'''  List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）。
列表用[ ]标识。是python最通用的复合数据类型。看这段代码就明白。
列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
'''

list = ['asa','jhon',345,2.33,80.9 ]
tinylist = [2121,"ssss",'tom']
tinylist[0] = 'hahaha';
print list  # 输出完整列表
print list[0]  # 输出列表第一个元素
print list[2:4]  # 输出第三到第五个元素
print list[2:]  # 输出第二以后的元素
print tinylist * 5  # 输出列表两次
print list + tinylist  # 输出组合的列表
