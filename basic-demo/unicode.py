# -*- coding:utf-8 -*-
import sys
print(sys.getdefaultencoding())
print(sys.stdin.encoding)
print(sys.stdout.encoding)
print(sys.stderr.encoding)

utf8Bytes = '包含中文'.encode('utf-8',errors='ignore')
print(len(utf8Bytes))

utf8Str = utf8Bytes.decode('utf-8')

print(len(utf8Str))


#print('包含中文'.encode('utf-8',errors='ignore').decode('gbk',errors='ignore'))
# print(ord('A'))
# print(ord('中'))

# print(chr(65))
# print(chr(20013))

# print('\u4e2d\u6587')

#格式化字符串的2种方式
#print('hello %s %2d %.2f %x' % ('bean',5,3.1415926,15))

#print('hello {0} {1:2d} {2:.2f} {3:x}'.format('bean',5,3.1415926,15))

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('%.2f' % (r)) #想显示 %  估计不行
print('{0:.2f}%'.format(r)) #此种方式显示 % 可以