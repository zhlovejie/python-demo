# -*- coding:utf-8 -*-
#print(list(range(10)))

sum = 0
for idx,val in enumerate(list(range(101))):
  sum += val
  print(idx,val)
print(sum)

# sum = 0
# n = 100
# while n > 0:
#   sum += n
#   n = n - 1
# print(sum)
