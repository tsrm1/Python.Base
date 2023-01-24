post_ids = {10, 25, 16, 73, 25, 16}
print('post_ids = {10, 25, 16, 73, 25, 16}  -> ', post_ids)
print('type(post_ids)                       -> ', type(post_ids))
print('len(post_ids)                        -> ', len(post_ids))

my_set = {}
print('my_set = {}                          -> ', type(my_set))
my_set = set()
print('my_set = set()                       -> ', type(my_set))

first_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}
my_set = set()
print("first_set = {'abc', 'd', 'f', 'y'}   -> ", first_set)
print("other_set = {'a', 'f', 'd'}          -> ", other_set)
print("first_set.intersection(other_set))   -> ",
      first_set.intersection(other_set))
print("other_set.intersection(first_set))   -> ",
      other_set.intersection(first_set))
print("other_set & first_set                -> ",
      other_set & first_set)

print("first_set.intersection('abcd'))      -> ",
      first_set.intersection('abcd'))
print("first_set.intersection(['a', 'b', 'c', 'd']) -> ",
      first_set.intersection(['a', 'b', 'c', 'd']))
print("first_set.intersection(('a', 'b', 'c', 'd')) -> ",
      first_set.intersection(('a', 'b', 'c', 'd')))


print("other_set.difference(first_set))     -> ",
      other_set.difference(first_set))
print("other_set - first_set                -> ",
      other_set - first_set)

print("first_set.union(other_set))          -> ",
      first_set.union(other_set))
print("other_set.union(first_set))          -> ",
      other_set.union(first_set))
print("other_set | first_set                -> ",
      other_set | first_set)

second_set = {'f', 'd'}
print("other_set.issubset(first_set))       -> ",
      other_set.issubset(first_set))
print("second_set.issubset(first_set))      -> ",
      second_set.issubset(first_set))
print("first_set.issuperset(second_set))    -> ",
      first_set.issuperset(second_set))

print("first_set.discard('d')               -> ",
      first_set.discard('d'))
print("first_set.discard('unknown')         -> ",
      first_set.discard('unknown'))
print("first_set =                          -> ",
      first_set)


print("first_set.remove('f')               -> ",
      first_set.remove('f'))

# print("first_set.remove('unknown')               -> ",
#       first_set.remove('unknown'))
print("first_set =                          -> ",
      first_set)

copied_set = first_set.copy()
print("copied_set = first_set.copy()        -> ",
      copied_set)
first_set.add('X')
copied_set.add('Y')
print("first_set.add('X')                   -> ",
      first_set)
print("copied_set.add('Y')                  -> ",
      copied_set)
print("first_set.symmetric_difference(copied_set) -> ",
      first_set.symmetric_difference(copied_set))

print("(first_set | copied_set) - (first_set & copied_set) -> ",
      (first_set | copied_set) - (first_set & copied_set))
