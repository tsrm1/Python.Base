my_range = range(5)
print('my_range = range(5)                  -> ', my_range)
print('my_range[-1]                         -> ', my_range[-1])
print('type(my_range)                       -> ', type(my_range))
print('list(my_range)                       -> ', list(my_range))
for n in my_range:
    print(n)
my_range = range(10, 20, 3)
print('my_range = range(10, 20, 3)          -> ', my_range)
print('list(my_range)                       -> ', list(my_range))
print('my_range.start                       -> ', my_range.start)
print('my_range.stop                        -> ', my_range.stop)
print('my_range.step                        -> ', my_range.step)

list_of_num = []
for n in my_range:
    list_of_num.append(n)
    print(n)
print(list_of_num)

print('my_range.index(19)                   -> ', my_range.index(19))
print('my_range.count(19)                   -> ', my_range.count(19))
print('my_range.count(20)                   -> ', my_range.count(20))

print(dir(range))
