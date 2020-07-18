# -*- coding:utf-8 -*-
arr = list(range(1, 101))
#print(arr)

#print(arr[0:3],arr[-3:],arr[0:10:2])


str = '  hello   '


def trim(str):
  while str[:1] == ' ':
    str = str[1:]
  while str[-1:] == ' ':
    str = str[:-1]
  return str

print(trim(str),len(str),len(trim(str)))