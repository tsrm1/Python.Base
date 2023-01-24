print("bool(0)      =>", bool(0))
print("bool(0.0)    =>", bool(0.0))
print("bool(0j)     =>", bool(0j))
print("bool({})     =>", bool({}))
print("bool([])     =>", bool([]))
print("bool(())     =>", bool(()))
print("bool(set())  =>", bool(set()))
print("bool(range(0))=>", bool(range(0)))
print("bool('')     =>", bool(''))


print("bool({'a': 10})      =>", bool({'a': 10}))
print("not not {'a': 10}    =>", not not {'a': 10})

print()
my_list = [1, 2]
if len(my_list) > 0:
    print(f'1. List {my_list} has elements')

if my_list:             # пустой список даёт False, не пустой список даёт True
    print(f'2. List {my_list} has elements')

print()
other_list = ['a', 'b']
print('List my_list                 =>', my_list)
print('List other_list              =>', other_list)
print('my_list or other_list        =>', my_list or other_list)

# если 1ое выражение True, 2ое выражение даже не рассматриваеться
print('len(my_list)>0 or other_list =>', len(my_list) > 0 or other_list)

print('len(my_list)<0 or other_list =>', len(my_list) < 0 or other_list)

# если 1ое выражение False, результат будет всегда 2ое выражение, даже если оно тоже False
print('len(my_list)<0 or {}         =>', len(my_list) < 0 or {})

print()
new_list = []
# если список не пустой, то он выдаст True. Второе логическое выражение даже не рассматривается (в нашем случае его просто нету) и будет вызвана функция print
my_list and print(f'List {my_list} is not empty')
# если список пустой, то он выдаст False. Второе логическое выражение даже не рассматривается (в нашем случае его просто нету) и не будет вызвана функция print
new_list and print(f'List {new_list} is not empty')
