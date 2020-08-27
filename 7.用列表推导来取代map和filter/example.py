# coding=utf-8
# author='HopePower'
# time='2020/8/27 23:07'
# 列表推导
a = [1, 2, 3]
squares = [x**2 for x in a]
print squares

# 如果使用map，那就要创建lambda函数
squares = map(lambda x: x**2, a)

# 列表推导可以过滤原始列表中的元素
even_squares = [x**2 for x in a if x % 2 == 0]
print even_squares

# 使用内置的map和fitlter会使得代码难懂
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print alt

# 字典和集也有类似的推导机制
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print rank_dict
print chile_len_set