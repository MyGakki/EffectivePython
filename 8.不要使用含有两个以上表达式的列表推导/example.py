# coding=utf-8
# author='HopePower'
# time='2020/8/27 23:17'
# 列表推导支持多重循环
matrix = [[1, 2, 3], [4, 5, 5], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print flat

squared = [[x**2 for x in row] for row in matrix]
print squared

# 超过两个表达式的列表推导是很难理解的，应该尽量避免