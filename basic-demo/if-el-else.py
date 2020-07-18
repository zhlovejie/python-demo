# -*- coding:utf-8 -*-
height = 1.75
weight = 80.5 
bmi = weight / (height * height)
if bmi > 32:
  print('严重肥胖')
elif bmi > 28 and bmi <= 32:
  print('肥胖')
elif bmi > 25 and bmi <= 28:
  print('过重')
elif bmi > 18.5 and bmi <= 25:
  print('正常')
else:
  print('过轻')