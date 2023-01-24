my_nums = [10, 4, 6, 6, 10, 3, 5]
print('my_nums =                            -> ', my_nums)
print('type(my_nums)                        -> ', type(my_nums))
print('my_nums.append(15)                   -> ', my_nums.append(15))
print('my_nums =                            -> ', my_nums)
print('my_nums.pop(1)                       -> ', my_nums.pop(1))
print('my_nums =                            -> ', my_nums)
print('my_nums.pop()                        -> ', my_nums.pop())
print('my_nums =                            -> ', my_nums)
print('my_nums.sort()                       -> ', my_nums.sort())
print('my_nums =                            -> ', my_nums)
print('my_nums.sort(reverse=True)           -> ', my_nums.sort(reverse=True))
print('my_nums =                            -> ', my_nums)
print('my_nums[:2]                          -> ', my_nums[:2])
print('my_nums[1:-1]                        -> ', my_nums[1:-1])
print('my_nums[-2:]                         -> ', my_nums[-2:])
print('my_nums.count(6)                     -> ', my_nums.count(6))
print('my_nums.insert(3, -2)                -> ', my_nums.insert(3, -2))
print('my_nums =                            -> ', my_nums)

copied_nums0 = my_nums
print('copied_nums0 = my_nums               -> ', copied_nums0)
print('id(my_nums)=', id(my_nums), ', id(copied_nums0)=',
      id(copied_nums0), ', ', id(my_nums) == id(copied_nums0))

copied_nums1 = my_nums.copy()
print('copied_nums1 = my_nums.copy()        -> ', copied_nums1)
print('id(my_nums)=', id(my_nums), ', id(copied_nums1)=',
      id(copied_nums1), ', ', id(my_nums) == id(copied_nums1))

copied_nums2 = list(my_nums)
print('copied_nums2 = list(my_nums)         -> ', copied_nums2)
print('id(my_nums)=', id(my_nums), ', id(copied_nums2)=',
      id(copied_nums2), ', ', id(my_nums) == id(copied_nums2))

copied_nums3 = my_nums[:]
print('copied_nums3 = my_nums[:]            -> ', copied_nums3)
print('id(my_nums)=', id(my_nums), ', id(copied_nums3)=',
      id(copied_nums3), ', ', id(my_nums) == id(copied_nums3))

copied_nums3.clear()
print('copied_nums3.clear()                 -> ', copied_nums3)

copied_nums3 = copied_nums1 + copied_nums2
print('copied_nums3 = copied_nums1 + copied_nums2 -> ', copied_nums3)

copied_nums3.extend('abcdef')
print("copied_nums3.extend('abcdef')        -> ", copied_nums3)

print('min(my_nums)                         -> ', min(my_nums))
print('max(my_nums)                         -> ', max(my_nums))
print('sum(my_nums)                         -> ', sum(my_nums))
print('len(my_nums)                         -> ', len(my_nums))
print('sum(my_nums)/len(my_nums)            -> ', sum(my_nums)/len(my_nums))


greeting = "Hello from Python"
print('greeting =                           -> ', greeting)
greeting_letters = list(greeting)
print('greeting_letters = list(greeting)    -> ', greeting_letters)

my_dict = {'a': 10, 'b': True}
print('my_dict =                            -> ', my_dict)
my_dict_keys = list(my_dict)
print('my_dict_keys = list(my_dict)         -> ', my_dict_keys)

my_enum_dict = enumerate(my_dict_keys)
print('my_enum_dict = enumerate(my_dict_keys)-> ', type(my_enum_dict))

print()
fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]
availability = [True, False, True]
text = '246'
ziped_tuple = zip(text, fruits, quantities, availability)
print("fruits = ['apple', 'banana', 'lime']     -> ", fruits)
print("quantities = [100, 70, 50]               -> ", quantities)
print("availability = [True, False, True]       -> ", availability)
print("text = '246'                             -> ", text)
print("ziped_tuple = zip(text, fruits, quantities, availability) -> ", ziped_tuple)

listed_zip = list(ziped_tuple)
print("listed_zip = list(fruit_qtys_zip)        -> ", listed_zip)
