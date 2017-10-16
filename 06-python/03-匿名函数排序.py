# coding=utf-8
stus = [{"name":"zhangsan", "age":18}, {"name":"lisi", "age":19}, {"name":"wangwu", "age":18}]
# key表示排序规则，reverse表示是否降序排列,默认升序排列
stus.sort(key = lambda x:(x["age"],x['name']),reverse=False)
print(stus)
