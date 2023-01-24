from copy import deepcopy

my_motorbike = {
    'brand': 'Dukati',
    'price': 25000,
    'engine_vol': 1.2,
}

print('my_motorbike =                       -> ', my_motorbike)
print('my_motorbike =                       -> ', type(my_motorbike))
print("my_motorbike['brand'] =              -> ", my_motorbike['brand'])
print("my_motorbike['price'] =              -> ", my_motorbike['price'])
print("my_motorbike['engine_vol'] =         -> ", my_motorbike['engine_vol'])
my_motorbike['price'] = 20_000
print("my_motorbike['price'] = 20_000       -> ", my_motorbike['price'])
print("len(my_motorbike)                    -> ", len(my_motorbike))
my_motorbike['is_new'] = True
print("my_motorbike['is_new'] = True        -> ", my_motorbike)
print("len(my_motorbike)                    -> ", len(my_motorbike))
insert_dict = my_motorbike.copy()
print("insert_dict = my_motorbike.copy()    -> ", insert_dict)
my_motorbike['another_bike'] = insert_dict
print("my_motorbike['another_bike'] = insert_dict -> ", my_motorbike)
print("len(my_motorbike)                    -> ", len(my_motorbike))
del my_motorbike['another_bike']
print("del my_motorbike['another_bike']     -> ", my_motorbike)
print("len(my_motorbike)                    -> ", len(my_motorbike))
print("my_motorbike.get('model')            -> ", my_motorbike.get('model'))
print("my_motorbike.get('model', 'Unknown') -> ",
      my_motorbike.get('model', 'Unknown'))

my_list = [['first', 0], ['second', True]]
my_dict = dict(my_list)
print("my_list = [['first', 0], ['second', True]]", my_list)
print("my_dict = dict(my_list)              -> ", my_dict)

my_list = [('first', 0), ('second', True)]
my_dict = dict(my_list)
print("my_list = [['first', 0], ['second', True]]", my_list)
print("my_dict = dict(my_list)              -> ", my_dict)

print()
fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]
ziped_dict = zip(fruits, quantities)
print("fruits = ['apple', 'banana', 'lime']     -> ", fruits)
print("quantities = [100, 70, 50]               -> ", quantities)
print("ziped_dict = zip(fruits, quantities)     -> ", ziped_dict)

dict_zip = dict(ziped_dict)
print("dict_zip = dict(ziped_dict)              -> ", dict_zip)

print()
# from copy import deepcopy    # вначале файла импортировать стандартную библиотеку deepcopy
info = {
    'name': 'Roman',
    'kinder_name': []
}

print("info={'name': 'Roman', 'kinder_name': [] }           -> ",
      info)
info_shallowcopy = info.copy()  # поверхностная копия, без вложенных списков
info_deepcopy = deepcopy(info)  # глубокая копия, вместе с вложенными списками

info['kinder_name'].append('Sophiia')  # изменяем исходный объект
info_deepcopy['kinder_name'].append('Valeriia')  # изменяем глубокую копию

print("info['kinder_name'].append('Sophiia')                -> ",
      info)

print(
    "info_shallowcopy['kinder_name'].append('Valeriia')   -> ", info_shallowcopy)
print(
    "info_deepcopy['kinder_name'].append('Valeriia')      -> ", info_deepcopy)
