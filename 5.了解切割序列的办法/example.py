# coding=utf-8
# author='HopePower'
# time='2020/8/27 22:40'
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 使用list[start: end]来切割
print a[:]
print a[:5]
print a[:-1]
print a[4:]
print a[-3:]
print a[2:5]
print a[2:-1]
print a[-3:-1]

# 切割列表时，即便start或end索引越界也不会出现问题
first_twenty_items = a[:20]
last_twenty_items = a[-20:]
print first_twenty_items
print last_twenty_items

# 对原列表进行切割后，会产生一份全新的列表
b = a[4:]
print 'Before:', b
b[1] = 99
print 'After:', b
print 'No change:', a

# 在赋值时对左侧列表使用切割操作，会把该列表处在指定范围内的对象替换成新值,即使长度不同
print 'Before:', a
a[2: 7] = [99, 22, 14]
print 'After:', a

# 对赋值操作右侧的列表使用切片，并且起止索引都为空，会产生一个原始列表的拷贝
b = a[:]
print b

# 对赋值操作左侧的列表使用切片，并且起止索引都为空，那么系统会将右侧的新值复制一份，并用这份拷贝来替换左侧列表
b[:] = a
print b