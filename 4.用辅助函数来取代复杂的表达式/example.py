# coding=utf-8
# author='HopePower'
# time='2020/8/27 0:03'
my_values = {'red': ['5'], 'green': ['']}

# 使用get方法
print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

# 如果待查询的参数没有出现在字典里，或者参数的值为空白，返回默认值0

# Boolean表达式
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)

# 需要在数学表达式中使用这些参数值，要确保这些参数是整数
# 这种写法读起来困难，而且看上去很乱
red = int(my_values.get('red', [''])[0] or 0)

# 三元操作符
red = my_values.get('red', [''])[0]
red = int(red) if red[0] else 0

# 展开的if/else
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0


# 辅助函数
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


green = get_first_int(my_values, 'green')
print('Green:   %r' % green)

