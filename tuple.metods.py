my_nums = (10, 5, 100, 10, 5, 5)
print('my_nums = (10, 5, 100, 10)           -> ', my_nums)
print('my_nums.count(100)                   -> ', my_nums.count(100))
print('my_nums.count(5)                     -> ', my_nums.count(5))
print('my_nums.index(5)                     -> ', my_nums.index(5))

index_one = my_nums.index(5)

print('index_one = my_nums.index(5)         -> ', index_one)
index_two = my_nums.index(5, index_one + 1)
print('index_two = my_nums.index(5, index_one + 1) -> ', index_two)
index_three = my_nums.index(5, index_two + 1)
print('index_three = my_nums.index(5, two + 1) -> ', index_three)

my_list = list(my_nums)
print('my_list = list(my_nums)              -> ', my_list)
del my_list[4]
print('del my_list[4]                       -> ', my_list)
my_list.append(7)
print('my_list.append(7)                    -> ', my_list)
my_nums = tuple(my_list)
print('my_nums = tuple(my_list)             -> ', my_nums)
my_tuple_one = tuple('abcdef')
print("my_tuple = tuple('abcdef')           -> ", my_tuple_one)

my_tuple_two = tuple({'first': 1, 'second': True})
print("my_tuple = ({'first', 0}, {'second', True}) -> ", my_tuple_two)
