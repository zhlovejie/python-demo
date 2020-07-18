# -*- coding:utf-8 -*-
# import math
# def quadratic(a,b,c):
#   tmp = math.sqrt(b * b - 4 * a* c)
#   v1 =(-b + tmp) / 2 * a
#   v2 =(-b - tmp) / 2 * a
#   return v1,v2


# v1,v2 = quadratic(5,10,3)

# print(v1,v2)

#参数默认值
# def add(a=0, b=0):
#   return a + b


# print(add(), add(1, 1), add(3))


#可变参数
# def adds(*numbers):
#   print(type(numbers))
#   sum = 0
#   for n in numbers:
#     sum += n
#   return sum


# print(adds(1, 2, 3, 4, 5),adds(*[1, 2, 3, 4, 5]),adds(*(1, 2, 3, 4, 5)))


#关键字参数
# def person(name,age,**others):
#   print(name,age,others)

# others = {'job':'front end...','addr':'xuzhou'}
# person('bean',30,**others)

# person('bean',30,a='1',b='2',c='3')

#命名关键字参数
# def person(name, age, *, addr):
#   print(name, age, addr)
#   pass


# others = {'addr': 'xuzhou'}
# person('bean', 30, **others)

#递归
def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n-1)


print(fact(5))
