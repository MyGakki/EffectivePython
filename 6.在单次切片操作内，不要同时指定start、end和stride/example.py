# coding=utf-8
# author='HopePower'
# time='2020/8/27 22:56'
# list[start: end: stride] 每n个元素取出来1个
a = ['a', 'b', 'c', 'd', 'e', 'f']
odds = a[::2]
evens = a[1::2]
print odds
print evens

# 使用-1作为步进，可以将字符形式存储的字符串反转过来
x = 'hello'
y = x[::-1]
print y

# 如果同时指定start, end和stride时，那么代码会变得相当费解，尤其stride为负值时
# 可以考虑想做步进，在做切割
b = a[::2]
c = b[1:-1]
print c