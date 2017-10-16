#!/usr/bin/python
# coding=utf-8

a = 0
b = 30
c = a or b
if a or b:
    print ("a or b为真,值为", c)
else:
    print ("a or b为假,值为", c)
