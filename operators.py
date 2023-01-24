a = 10
b = a
c = 10
d = a + b
print('a=10             =>', a)
print('b=a              =>', b)
print('c=10             =>', c)
print('d=a+b            =>', d)
print('a is b           =>', a is b)
print('a is c           =>', a is c)
print('a is d           =>', a is d)

print()
a = [1, 2]
b = [1, 2]
print('a=               =>', a)
print('b=               =>', b)
print('a == b           =>', a == b)
print('a.__eq__(b)      =>', a.__eq__(b))
print('a is b           =>', a is b)

print()
my_num = 0
print('my_num = 0       =>', +my_num)  # явно указываем, что my_num - это число
print('not my_num       =>', not my_num)  # отрицаем my_num

print()
my_bool = True
print('my_bool = True   =>', my_bool)
print('+my_bool         =>', +my_bool)

print()
my_car = {
    'brand': 'Toyota',
    'price': 10_000
}
print(my_car)
print("'brand' in my_car    =>", 'brand' in my_car)
print("'year' in my_car     =>", 'year' in my_car)
print("'year' not in my_car =>", 'year' not in my_car)
