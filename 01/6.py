#!/usr/bin/python
# coding=utf-8
"""
元组是另一个数据类型，类似于List（列表）。
元组用"()"标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表。
"""
tuple2 = ('adda', 2121, 3.33, 222.2, 'yoy')
print tuple2  # 输出完整元组
print tuple2[0]  # 输出元组的第一个元素
print tuple2[1:3]  # 输出第二个至第三个的元素
print tuple2[2:]  # 输出从第三个开始至列表末尾的所有元素
