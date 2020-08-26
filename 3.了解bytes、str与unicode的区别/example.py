# coding=utf-8
# author='HopePower'
# time='2020/8/26 23:41'

# python2中，str示例包含原始的8位值，unicode示例包含Unicode字符
import os

a = b'h\x65llo'
print type(a)
b = u'hello'
print type(b)


# 接收str或unicode，总是返回unicode
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value


print 'to_unicode', type(to_unicode('hello'))


# 接收str或unicode，总是返回str
def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value


print 'to_str', type(to_str(u'hello'))

# 在python2中，如果str只包含7位ASCII字符，那么unicode和str实例似乎就成了同一种类型
# 可以使用+操作符把这种str和unicode连接起来
print type('one' + 'two')
print type('one' + u'two')
print type(u'one' + u'two')
# 可以使用等价和不等价操作符比较两种实例
print 'one' > 'two'
print 'one' == u'two'
print u'one' < u'two'
# 在格式化字符串中，可以使用'%s'来代表unicode
print 'hello %s' % u'world'

# python3中open方法默认采用UTF-8来操作文件，需要写入Unicode。而在python2中，默认为二进制
# 该语句在Python2中可以执行，在python3中不行
with open('text.txt', 'w') as f:
    f.write(os.urandom(10))

# 以二进制wb方式打开文件，则可以兼容python2和python3
with open('text.txt', 'wb') as f:
    f.write(os.urandom(10))