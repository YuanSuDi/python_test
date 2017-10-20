# coding=utf-8


def extendList(a, list = []):
    # 解决方法如下，当元素不为空时，重新对list进行声明
    # if len(list) > 0:
    #     list = []

    list.append(a)
    return list


# 使用缺省函数调用时，会延续上一个函数调用进去的值
list1 = extendList(10)
list2 = extendList(123, ['aa', 'bb', 'cc'])
list3 = extendList('dd')
print("list1=%s" % list1)
print("list2=%s" % list2)
print("list3=%s" % list3)
print(id(list1))
print(id(list2))
print(id(list3))
# 以上方法执行的结果，list1和list3指向的是同一块内存地址

